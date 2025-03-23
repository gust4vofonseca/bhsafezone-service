from sklearn.metrics import confusion_matrix,f1_score
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
import numpy as np
import sklearn as skl
import random
from scipy import stats
import math
from sklearn.model_selection import GridSearchCV
import pymongo
import re
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

# Evita baixar os pacotes se já estiverem disponíveis
nltk.data.path.append('/home/gustavo/nltk_data')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


df = pd.read_csv('src/modules/classifier/services/tweetsNoticiaCrime.csv')

df['novo_texto'] = df['Tweet'].copy()

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

# Criação da função CountVectorizer
cvt = CountVectorizer(strip_accents='ascii', lowercase=True, stop_words=stop_words)

X_cvt = cvt.fit_transform(df['novo_texto'])
#print("Vocabulary: ", cvt.vocabulary_)
#print(X_cvt.toarray())

# Criação da função TfidfTransformer
tfi = TfidfTransformer(use_idf=True)

X_tfi = tfi.fit_transform(X_cvt)

# A entrada será a transformação de vetores com a normalização tf-idf
entrada = X_tfi.toarray()
# A saida será as classes 1 para crime 0 para não
saida = df['Classe']

#Lista de random_states
random_list = []
melhores_param = []
melhores_scores = []


for i in range(5):
    # Gera um número inteiro aleatório entre 0 e 100
    numero_aleatorio = random.randint(0, 100)
    print(numero_aleatorio)
    
    # Separando 20% dos dados para teste
    X_train, X_test, y_train, y_test = train_test_split(entrada, saida, test_size=0.2,random_state=numero_aleatorio)
    
    # Separando 20% dos dados para teste novamente
    # add o numero aleatorio
    random_list.append(numero_aleatorio)
    X2_train, X2_test, y2_train, y2_test = train_test_split(X_train, y_train, test_size=0.2,random_state=numero_aleatorio)
    
    # Define modelo
    clf = MultinomialNB()

    # Define os parametros
    param_grid = {
        'alpha': [0.1, 0.01, 0.001, 0.0001],
        'fit_prior': [True, False],
        'class_prior': [(0.2, 0.8), (0.5, 0.5), (0.8, 0.2)]
    }
    # Define os 10 folds
    grid = GridSearchCV(clf, param_grid, refit = True, verbose = 3, cv=10, scoring='f1')

    # fitting the model for grid search
    grid.fit(X2_train, y2_train)
    
    # printa melhor parametro
    print('\n',grid.best_params_)

    # printa o modelo
    print('\n',grid.best_estimator_)
    
    # adiciona o melhor parametro
    melhores_param.append(grid.best_params_)
    
    print(f"\nMelhor acurácia encontrada: {grid.best_score_:.4f}")
    
    # adiciona a melhor acuracia
    melhores_scores.append(grid.best_score_)
    
print("Lista de random states", random_list)
print("\nLista demelhores parametros", melhores_param)
print("\nLista de melhores resultados", melhores_scores)


# media das acuracias
media = np.mean(melhores_scores)

# desvio padrão das acuracias
desvio_padrao = np.std(melhores_scores)

# Nível de confiança desejado
n_conf = 0.95


print("media =",media)
print("\ndesvio padrão =",desvio_padrao)

tam_amostra = len(melhores_scores)

# Intervalo de confiança

inter_inf = media - (2.131 * desvio_padrao) / math.sqrt(tam_amostra)
inter_sup = media + (2.131 * desvio_padrao) / math.sqrt(tam_amostra)

print("\nIntervalo de confiança = ", inter_inf, '-', inter_sup)

print("\nIntervalo inferior =", inter_inf)

print("\nIntervalo de superior =", inter_sup)

# Acuracia melhores parametros

# Define modelo
clf = MultinomialNB(alpha= 0.1, class_prior= (0.2, 0.8), fit_prior=True)

# Treinamento do modelo
clf.fit(X_train, y_train)

# Realizando a predição
resultado = clf.predict(X_test)

# Avaliando o modelo
print('Acurácia: {:.2f}'.format(metrics.accuracy_score(y_test, resultado)))

# Criar a matriz de confusão
cm = confusion_matrix(y_test, resultado)

# Exibir a matriz de confusão em uma plotagem
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=['Classe 0', 'Classe 1'], yticklabels=['Classe 0', 'Classe 1'])


# Adicionar as informações de TP, FP, FN e TN
plt.text(0.5, 0.3, f'TN = {cm[0, 0]}', fontsize=12, ha='center', va='center')
plt.text(0.5, 1.3, f'FN = {cm[1, 0]}', fontsize=12, ha='center', va='center')

plt.text(1.5, 0.3, f'FP = {cm[0, 1]}', fontsize=12, ha='center', va='center')
plt.text(1.5, 1.3, f'TP = {cm[1, 1]}', fontsize=12, ha='center', va='center', color ='white')


plt.xlabel('Verdadeiros')
plt.ylabel('Previstos')

plt.savefig('matriz_de_confusao.png')
# plt.show()

f1 = f1_score(y_test, resultado)

# Exibir a pontuação F1
print('Pontuação F1:', f1)

def classifica_crime(text,clf):
    novo_cvt = cvt.transform(pd.Series(text))
    novo_tfi = tfi.transform(novo_cvt).toarray() 
    classe = clf.predict(novo_tfi)[0]
    return classe


def salva_e_classifica(data, mongo_db, mongo_db_coll, clf, **mongo_conn_kw):
    client = pymongo.MongoClient(**mongo_conn_kw)

    db = client[mongo_db]
    coll = db[mongo_db_coll]
    
    for item in data:
        if any(item.get(key) for key in ['body', 'title', 'description']):
            resul = classifica_crime(f"{item.get('title', '')} {item.get('description', '')} {item.get('body', '')} ", clf)
            
            if resul == 1:
                coll.update_one(
                    {'_id': item['_id']},  
                    {'$set': {'is_crime': 1, 'classified': 1, 'found_location': 0}} 
                )
            else:
                coll.update_one(
                    {'_id': item['_id']},  
                    {'$set': {'is_crime': 0, 'classified': 1, 'found_location': 0}} 
                )
        else:
            print(item)



def salva_Tweets_classificados_crime(clf):
    db = client["bh-safezone"]
    
    mycol = db["whatsapps"]
    data = mycol.find({"classified": 0})
    
    t = data.clone()
    tt = data.clone()
    c = len(list(t))
    if(c >= 1):
        salva_e_classifica(tt,"bh-safezone", "whatsapps", clf)
            
client = pymongo.MongoClient("localhost",27017)

salva_Tweets_classificados_crime(clf)