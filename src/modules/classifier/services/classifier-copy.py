import joblib
import re
import unicodedata
from nltk.corpus import stopwords
import pymongo

# Carregar o classificador, CountVectorizer e TfidfTransformer
clf = joblib.load('src/modules/classifier/services/modelo_classificador.pkl')
cvt = joblib.load('src/modules/classifier/services/count_vectorizer.pkl')
tfi = joblib.load('src/modules/classifier/services/tfidf_transformer.pkl')

# Stopwords
stop_words = set(stopwords.words('portuguese'))
stop_words.update([
    'em','sao','ao','de','da','do','para','c','kg','un','ml','pct','und','das',
    'no','ou','pc','gr','pt','cm','vd','com','sem','gfa','jg','la','1','2','3',
    '4','5','6','7','8','9','0','a','b','c','d','e','lt','f','g','h','i','j','k',
    'l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','ate', 'eramos',
    'estao', 'estavamos', 'estiveramos','estivessemos', 'foramos', 'fossemos',
    'ha', 'hao','houveramos', 'houverao', 'houveriamos', 'houvessemos','ja',
    'nao', 'sera', 'serao', 'seriamos', 'so', 'tambem','tera', 'terao',
    'teriamos', 'tinhamos', 'tiveramos','tivessemos', 'voce', 'voces',
    "https","co","leia"
])

def remove_accents(text):
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    return text

def format_text(text):
    text = re.sub(r'https?://\S+|www\.\S+', ' ', text)            
    text = re.sub(r'[,.:;!?]+', ' ', text)                        
    text = re.sub(r'[/<>()|\+\-\$%&#\*@\'\"]+', ' ', text)        
    text = re.sub(r'[0-9]+', '', text)                            
    text = remove_accents(text)                                   
    text = re.sub(r'\s+', ' ', text).strip().lower()              

    return text

def classifica_crime(text, clf, cvt, tfi):
    print('text1:', text)
    text = format_text(text)
    print('text2:', text)

    X_cvt = cvt.transform([text])
    X_tfi = tfi.transform(X_cvt)

    print('X_tfi:', X_tfi.toarray())
    classe = clf.predict(X_tfi)[0]
    print('classe:', classe)
    return classe

def salva_e_classifica(data, mongo_db, mongo_db_coll, clf, cvt, tfi, **mongo_conn_kw):
    client = pymongo.MongoClient(**mongo_conn_kw)
    db = client[mongo_db]
    coll = db[mongo_db_coll]
    
    for item in data:
        if any(item.get(key) for key in ['body', 'title', 'description']):
            texto = f"{item.get('title', '')} {item.get('description', '')} {item.get('body', '')}"
            resul = classifica_crime(texto, clf, cvt, tfi)

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
            print('Sem dados válidos para classificar:', item)

def salva_Tweets_classificados_crime(clf, cvt, tfi):
    client = pymongo.MongoClient()
    db = client["bh-safezone"]
    mycol = db["whatsapps"]
    data = mycol.find({"classified": {"$ne": 0}})  # Pega só os não classificados

    t = data.clone()
    tt = data.clone()
    c = len(list(t))
    
    if c >= 1:
        salva_e_classifica(tt, "bh-safezone", "whatsapps", clf, cvt, tfi)


salva_Tweets_classificados_crime(clf, cvt, tfi)