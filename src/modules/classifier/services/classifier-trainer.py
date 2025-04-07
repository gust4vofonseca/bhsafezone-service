import pandas as pd
import numpy as np
import random
import math
import re
import unicodedata
import nltk
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score


nltk.download('stopwords')

# Stopwords personalizadas
stop_words = set(stopwords.words('portuguese'))
stop_words.update(['https', 'co', 'leia'])

# Pré-processamento
def remove_accents(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))

def clean_text(text):
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    text = re.sub(r'[,.:;!?/<>()[\]{}|\\+\-=%&#@\"\'\*]', ' ', text)
    text = re.sub(r'\d+', '', text)
    text = remove_accents(text)
    text = text.lower()
    words = [w for w in text.split() if w not in stop_words]
    return ' '.join(words)

# Carrega os dados
df = pd.read_csv('src/modules/classifier/services/tweetsNoticiaCrime.csv')

# Copia texto e limpa
df['novo_texto'] = df['Tweet'].astype(str).apply(clean_text)

nao_crime = df[df['Classe'] == 0]

amostras = nao_crime.sample(n=279, random_state=42, replace = True)

df = df[df['Classe'] != 0]

df = pd.concat([df, amostras])

# Remove pontuação

df['novo_texto'] = df['novo_texto'].str.replace('[,.:;!?]+', ' ', regex=True).copy()

# Remove caracteres especiais
df['novo_texto'] = df['novo_texto'].str.replace ('[/<>()|\+\-\$%&#@\'\"]+', ' ', regex=True).copy()

# remove Numeros
df['novo_texto'] = df['novo_texto'].str.replace('[0-9]+', '', regex=True)

#StopWords
stop_words = ['em','sao','ao','de','da','do','para','c','kg','un','ml',
              'pct','und','das','no','ou','pc','gr','pt','cm','vd','com',
              'sem','gfa','jg','la','1','2','3','4','5','6','7','8','9',
              '0','a','b','c','d','e','lt','f','g','h','i','j','k','l',
              'm','n','o','p','q','r','s','t','u','v','x','w','y','z',
              'ate', 'eramos', 'estao', 'estavamos', 'estiveramos',
              'estivessemos', 'foramos', 'fossemos', 'ha', 'hao',
              'houveramos', 'houverao', 'houveriamos', 'houvessemos',
              'ja', 'nao', 'sera', 'serao', 'seriamos', 'so', 'tambem',
              'tera', 'terao', 'teriamos', 'tinhamos', 'tiveramos',
              'tivessemos', 'voce', 'voces',"https","co","leia"]

for word in stopwords.words('portuguese'):
    stop_words.append(word)
    
# Balanceamento simples
nao_crime = df[df['Classe'] == 0].sample(n=279, random_state=42, replace=True)
df = pd.concat([df[df['Classe'] != 0], nao_crime])

# Criação da função CountVectorizer
cvt = CountVectorizer(strip_accents='ascii', lowercase=True, stop_words=stop_words)
X_cvt = cvt.fit_transform(df['novo_texto'])
tfi = TfidfTransformer()
X_tfi = tfi.fit_transform(X_cvt)
entrada = X_tfi.toarray()
saida = df['Classe']

# Testes com múltiplos random_state
random_list = []
melhores_param = []
melhores_scores = []

for _ in range(5):
    seed = random.randint(0, 100)
    random_list.append(seed)

    X_train, _, y_train, _ = train_test_split(entrada, saida, test_size=0.2, random_state=seed)

    clf = MultinomialNB()
    param_grid = {
        'alpha': [0.1, 0.01, 0.001],
        'fit_prior': [True, False],
        'class_prior': [(0.5, 0.5), (0.2, 0.8)]
    }

    grid = GridSearchCV(clf, param_grid, cv=10, scoring='f1', verbose=0)
    grid.fit(X_train, y_train)

    melhores_param.append(grid.best_params_)
    melhores_scores.append(grid.best_score_)

    print(f"Seed: {seed} | Best Params: {grid.best_params_} | F1 Score: {grid.best_score_:.4f}")

# Resultados finais
media = np.mean(melhores_scores)
std = np.std(melhores_scores)
conf_int = 2.131 * std / math.sqrt(len(melhores_scores))

print("\nResumo Final:")
print("Seeds testadas:", random_list)
print("Melhores parâmetros:", melhores_param)
print(f"Média F1: {media:.4f}")
print(f"Intervalo de confiança (95%): [{media - conf_int:.4f}, {media + conf_int:.4f}]")

# Após o melhor treinamento
melhor_index = np.argmax(melhores_scores)
melhor_seed = random_list[melhor_index]

# Refaz o melhor modelo com a melhor seed
X_train, _, y_train, _ = train_test_split(entrada, saida, test_size=0.2, random_state=melhor_seed)

clf_final = MultinomialNB(**melhores_param[melhor_index])
clf_final.fit(X_train, y_train)

# Salva os modelos
joblib.dump(clf_final, 'src/modules/classifier/services/modelo_classificador.pkl')
joblib.dump(cvt, 'src/modules/classifier/services/count_vectorizer.pkl')
joblib.dump(tfi, 'src/modules/classifier/services/tfidf_transformer.pkl')

print("Modelos salvos com sucesso.")
