import pymongo
import re
import spacy
import requests

client = pymongo.MongoClient("localhost",27017)

# Relação bairro/região

bairro_regiao = {
 'AARÃO REIS': 'NORTE',
 'ACABA MUNDO': 'CENTRO-SUL',
 'ACAIACA': 'NORDESTE',
 'ADEMAR MALDONADO': 'BARREIRO',
 'AEROPORTO': 'PAMPULHA',
 'ÁGUAS CLARAS': 'BARREIRO',
 'ALÍPIO DE MELO': 'PAMPULHA',
 'ALPES': 'OESTE',
 'ALTA TENSÃO': 'BARREIRO',
 'ALTA TENSÃO I': 'BARREIRO',
 'ALTO BARROCA': 'OESTE',
 'ALTO CAIÇARAS': 'NOROESTE',
 'ALTO DAS ANTENAS': 'BARREIRO',
 'ALTO DOS PINHEIROS': 'NOROESTE',
 'ALTO VERA CRUZ': 'LESTE',
 'ÁLVARO CAMARGOS': 'NOROESTE',
 'AMBROSINA': 'OESTE',
 'ANCHIETA': 'CENTRO-SUL',
 'ANDIROBA': 'NORDESTE',
 'ANTÔNIO RIBEIRO DE ABREU': 'NORDESTE',
 'APARECIDA': 'NOROESTE',
 'APARECIDA SÉTIMA SEÇÃO': 'NOROESTE',
 'ÁPIA': 'CENTRO-SUL',
 'APOLÔNIA': 'VENDA NOVA',
 'APOLONIA': 'VENDA NOVA',
 'ARAGUAIA': 'BARREIRO',
 'ÁTILA DE PAIVA': 'BARREIRO',
 'ATILA DE PAIVA': 'BARREIRO',
 'BACURAU': 'NORTE',
 'BAIRRO DAS INDÚSTRIAS I': 'BARREIRO',
 'BAIRRO NOVO DAS INDÚSTRIAS': 'BARREIRO',
 'BALEIA': 'LESTE',
 'BANDEIRANTES': 'PAMPULHA',
 'BARÃO HOMEM DE MELO I': 'OESTE',
 'BARÃO HOMEM DE MELO II': 'OESTE',
 'BARÃO HOMEM DE MELO III': 'OESTE',
 'BARÃO HOMEM DE MELO IV': 'OESTE',
 'BARREIRO': 'BARREIRO',
 'BARRO PRETO': 'CENTRO-SUL',
 'BARROCA': 'OESTE',
 'BEIJA FLOR': 'NORDESTE',
 'BEIRA-LINHA': 'NORDESTE',
 'BEIRA LINHA': 'NORDESTE',
 'BELA VITÓRIA': 'NORDESTE',
 'BELA VITORIA': 'NORDESTE',
 'BELÉM': 'LESTE',
 'BELMONTE': 'NORDESTE',
 'BELVEDERE': 'CENTRO-SUL',
 'BERNADETE': 'BARREIRO',
 'BETÂNIA': 'OESTE',
 'BIQUINHAS': 'NORTE',
 'BISPO DE MAURA': 'PAMPULHA',
 'BOA ESPERANÇA': 'NORDESTE',
 'BOA UNIÃO I': 'NORTE',
 'BOA UNIÃO II': 'NORTE',
 'BOA VIAGEM': 'CENTRO-SUL',
 'BOA VISTA': 'LESTE',
 'BOM JESUS': 'NOROESTE',
 'BONFIM': 'NOROESTE',
 'BONSUCESSO': 'BARREIRO',
 'BRASIL INDUSTRIAL': 'BARREIRO',
 'BRAÚNAS': 'PAMPULHA',
 'BURITIS': 'OESTE',
 'CACHOEIRINHA': 'NORDESTE',
 'CAETANO FURQUIM': 'LESTE',
 'CAIÇARA-ADELAIDE': 'NOROESTE',
 'CAIÇARAS': 'NOROESTE',
 'CALAFATE': 'OESTE',
 'CALIFÓRNIA': 'NOROESTE',
 'CAMARGOS': 'OESTE',
 'CAMPO ALEGRE': 'NORTE',
 'CAMPONESA': 'LESTE',
 'CAMPONESA I': 'LESTE',
'CAMPONESA II': 'LESTE',
 'CAMPONESA III': 'LESTE',
 'CAMPUS UFMG': 'PAMPULHA',
 'CANAÃ': 'VENDA NOVA',
 'CANADÁ': 'NORDESTE',
 'CANDELARIA': 'VENDA NOVA',
 'CANDELÁRIA': 'VENDA NOVA',
 'CAPITÃO EDUARDO': 'NORDESTE',
 'CARDOSO': 'BARREIRO',
 'CARLOS PRATES': 'NOROESTE',
 'CARMO': 'CENTRO-SUL',
 'CASA BRANCA': 'LESTE',
 'CASTANHEIRA': 'BARREIRO',
 'CASTELO': 'PAMPULHA',
 'CDI JATOBÁ': 'BARREIRO',
 'CDI JATOBA': 'BARREIRO',
 'CENÁCULO': 'VENDA NOVA',
 'CENTRO': 'CENTRO-SUL',
 'CÉU AZUL': 'VENDA NOVA',
 'CHÁCARA LEONINA': 'OESTE',
 'CIDADE JARDIM': 'CENTRO-SUL',
 'CIDADE JARDIM TAQUARIL': 'LESTE',
 'CIDADE NOVA': 'NORDESTE',
 'CINQÜENTENÁRIO': 'OESTE',
 'COMITECO': 'CENTRO-SUL',
 'CONCÓRDIA': 'NORDESTE',
 'CÔNEGO PINHEIRO': 'LESTE',
 'CÔNEGO PINHEIRO A': 'LESTE',
 'CONFISCO': 'PAMPULHA',
 'CONJUNTO BONSUCESSO': 'BARREIRO',
 'CONJUNTO CALIFÓRNIA I': 'NOROESTE',
 'CONJUNTO CALIFÓRNIA II': 'NOROESTE',
 'CONJUNTO CAPITÃO EDUARDO': 'NORDESTE',
 'CONJUNTO CELSO MACHADO': 'PAMPULHA',
 'CONJUNTO FLORAMAR': 'NORTE',
 'CONJUNTO JARDIM FILADÉLFIA': 'NOROESTE',
 'CONJUNTO JATOBÁ': 'BARREIRO',
 'CONJUNTO LAGOA': 'PAMPULHA',
 'CONJUNTO MINASCAIXA': 'VENDA NOVA',
 'CONJUNTO NOVO DOM BOSCO': 'NOROESTE',
 'CONJUNTO PAULO VI': 'NORDESTE',
 'CONJUNTO PROVIDÊNCIA': 'NORTE',
 'CONJUNTO SANTA MARIA': 'CENTRO-SUL',
 'CONJUNTO SÃO FRANCISCO DE ASSIS': 'PAMPULHA',
 'CONJUNTO SERRA VERDE': 'VENDA NOVA',
 'CONJUNTO TAQUARIL': 'LESTE',
 'COPACABANA': 'VENDA NOVA',
 'COQUEIROS': 'NOROESTE',
 'CORAÇÃO DE JESUS': 'CENTRO-SUL',
 'CORAÇÃO EUCARÍSTICO': 'NOROESTE',
 'CORUMBIARA': 'BARREIRO',
 'CRUZEIRO': 'CENTRO-SUL',
 'CUSTODINHA': 'OESTE',
 'DELTA': 'NOROESTE',
 'DISTRITO INDUSTRIAL DO JATOBÁ': 'BARREIRO',
 'DOM BOSCO': 'NOROESTE',
 'DOM CABRAL': 'NOROESTE',
 'DOM JOAQUIM': 'NORDESTE',
 'DOM SILVÉRIO': 'NORDESTE',
 'DONA CLARA': 'PAMPULHA',
 'ENGENHO NOGUEIRA': 'PAMPULHA',
 'ERMELINDA': 'NOROESTE',
 'ERNESTO DO NASCIMENTO': 'BARREIRO',
 'ESPERANÇA': 'BARREIRO',
 'ESPLANADA': 'LESTE',
 'ESTORIL': 'OESTE',
 'ESTRELA': 'CENTRO-SUL',
 'ESTRELA DO ORIENTE': 'OESTE',
 'ETELVINA CARNEIRO': 'NORTE',
 'EUROPA': 'VENDA NOVA',
 'EYMARD': 'NORDESTE',
 'FAZENDINHA': 'CENTRO-SUL',
 'FERNÃO DIAS': 'NORDESTE',
 'FLAMENGO': 'VENDA NOVA',
 'FLÁVIO DE OLIVEIRA': 'BARREIRO',
 'FLÁVIO MARQUES LISBOA': 'BARREIRO',
 'FLORAMAR': 'NORTE',
 'FLORESTA': 'CENTRO-SUL',
 'FREI LEOPOLDO': 'NORTE',
 'FUNCIONÁRIOS': 'CENTRO-SUL',
 'GAMELEIRA': 'OESTE',
 'GARÇAS': 'PAMPULHA',
 'GLÓRIA': 'NOROESTE',
 'GOIÂNIA': 'NORDESTE',
 'GRAJAÚ': 'OESTE',
 'GRANJA DE FREITAS': 'LESTE',
 'GRANJA WERNECK': 'NORTE',
 'GROTA': 'LESTE',
 'GROTINHA': 'NORDESTE',
 'GUANABARA': 'NORDESTE',
 'GUARANI': 'NORTE',
 'GUARATÃ': 'OESTE',
 'GUTIERREZ': 'OESTE',
 'HAVAÍ': 'OESTE',
 'HELIÓPOLIS': 'NORTE',
 'HORTO': 'LESTE',
 'HORTO FLORESTAL': 'LESTE',
 'IMBAÚBAS': 'OESTE',
 'INCONFIDÊNCIA': 'PAMPULHA',
 'INDAIÁ': 'PAMPULHA',
 'INDEPENDÊNCIA': 'BARREIRO',
 'IPÊ': 'NORDESTE',
 'IPIRANGA': 'NORDESTE',
 'ITAIPU': 'BARREIRO',
 'ITAPOÃ': 'PAMPULHA',
 'ITATIAIA': 'PAMPULHA',
 'JAQUELINE': 'NORTE',
 'JARAGUÁ': 'PAMPULHA',
 'JARDIM ALVORADA': 'PAMPULHA',
 'JARDIM AMÉRICA': 'OESTE',
 'JARDIM ATLÂNTICO': 'PAMPULHA',
 'JARDIM DO VALE': 'BARREIRO',
 'JARDIM DOS COMERCIÁRIOS': 'VENDA NOVA',
 'JARDIM FELICIDADE': 'NORTE',
 'JARDIM LEBLON': 'VENDA NOVA',
 'JARDIM MONTANHÊS': 'NOROESTE',
 'JARDIM SÃO JOSÉ': 'PAMPULHA',
 'JARDIM VITÓRIA': 'NORDESTE',
 'JARDINÓPOLIS': 'OESTE',
 'JATOBÁ': 'BARREIRO',
 'JOÃO ALFREDO': 'LESTE',
 'JOÃO PAULO II': 'BARREIRO',
 'JOÃO PINHEIRO': 'NOROESTE',
 'JONAS VEIGA': 'LESTE',
 'JULIANA': 'NORTE',
 'LAGOA': 'VENDA NOVA',
 'LAGOA DA PAMPULHA': 'PAMPULHA',
 'LAGOINHA': 'NOROESTE',
 'LAGOINHA LEBLON': 'VENDA NOVA',
 'LAJEDO': 'NORTE',
 'LARANJEIRAS': 'VENDA NOVA',
 'LEONINA': 'OESTE',
 'LETÍCIA': 'VENDA NOVA',
 'LIBERDADE': 'PAMPULHA',
 'LINDÉIA': 'BARREIRO',
 'LORENA': 'NOROESTE',
 'LOURDES': 'CENTRO-SUL',
 'LUXEMBURGO': 'CENTRO-SUL',
 'MINAS CAIXA':'VENDA NOVA',
 'MADRE GERTRUDES': 'OESTE',
 'MADRI': 'NORTE',
 'MALA E CUIA': 'CENTRO-SUL',
 'MANACÁS': 'PAMPULHA',
 'MANGABEIRAS': 'CENTRO-SUL',
 'MANGUEIRAS': 'BARREIRO',
 'MARAJÓ': 'OESTE',
 'MARAVILHA': 'OESTE',
 'MARÇOLA': 'CENTRO-SUL',
 'MARIA GORETTI': 'NORDESTE',
 'MARIA HELENA': 'VENDA NOVA',
 'MARIA TERESA': 'NORTE',
 'MARIA VIRGÍNIA': 'NORDESTE',
 'MARIANO DE ABREU': 'LESTE',
 'MARIETA I': 'BARREIRO',
 'MARIETA II': 'BARREIRO',
 'MARILÂNDIA': 'BARREIRO',
 'MARIQUINHAS': 'NORTE',
 'MARMITEIROS': 'NOROESTE',
 'MILIONÁRIOS': 'BARREIRO',
 'MINAS BRASIL': 'NOROESTE',
 'MINASCAIXA': 'VENDA NOVA',
 'MINASLÂNDIA': 'NORTE',
 'MINEIRÃO': 'BARREIRO',
 'MIRAMAR': 'BARREIRO',
 'MIRANTE': 'NORTE',
 'MIRTES': 'NORDESTE',
 'MONSENHOR MESSIAS': 'NOROESTE',
 'MONTE AZUL': 'NORTE',
 'MONTE SÃO JOSÉ': 'CENTRO-SUL',
 'MORRO DOS MACACOS': 'NORDESTE',
 'NAZARÉ': 'NORDESTE',
 'NOSSA SENHORA DA APARECIDA': 'CENTRO-SUL',
 'NOSSA SENHORA DA CONCEIÇÃO': 'CENTRO-SUL',
 'NOSSA SENHORA DE FÁTIMA': 'CENTRO-SUL',
 'NOSSA SENHORA DO ROSÁRIO': 'CENTRO-SUL',
 'NOVA CACHOEIRINHA': 'NOROESTE',
 'NOVA CINTRA': 'OESTE',
 'NOVA ESPERANÇA': 'NOROESTE',
 'NOVA FLORESTA': 'NORDESTE',
 'NOVA GAMELEIRA': 'OESTE',
 'NOVA GRANADA': 'OESTE',
 'NOVA PAMPULHA': 'PAMPULHA',
 'NOVA SUISSA': 'OESTE',
 'NOVA VISTA': 'LESTE',
 'NOVO AARÃO REIS': 'NORTE',
 'NOVO GLÓRIA': 'NOROESTE',
 'NOVO OURO PRETO': 'PAMPULHA',
 'NOVO SANTA CECÍLIA': 'BARREIRO',
 'NOVO SÃO LUCAS': 'CENTRO-SUL',
 'NOVO TUPI': 'NORTE',
 'OESTE': 'OESTE',
 'OLARIA': 'BARREIRO',
 "OLHOS D'ÁGUA": 'OESTE',
 'OURO MINAS': 'NORDESTE',
 'OURO PRETO': 'PAMPULHA',
 'PADRE EUSTÁQUIO': 'NOROESTE',
 'PALMARES': 'NORDESTE',
 'PALMEIRAS': 'OESTE',
 'PANTANAL': 'OESTE',
 'PAQUETÁ': 'PAMPULHA',
 'PARAÍSO': 'LESTE',
 'PARQUE SÃO JOSÉ': 'OESTE',
 'PARQUE SÃO PEDRO': 'VENDA NOVA',
 'PAULO VI': 'NORDESTE',
 'PEDREIRA PRADO LOPES': 'NOROESTE',
 'PETRÓPOLIS': 'BARREIRO',
 'PILAR': 'BARREIRO',
 'PINDORAMA': 'NOROESTE',
 'PINDURA SAIA': 'CENTRO-SUL',
 'PIRAJÁ': 'NORDESTE',
 'PIRATININGA': 'VENDA NOVA',
 'PIRINEUS': 'LESTE',
 'PLANALTO': 'NORTE',
 'POMPÉIA': 'LESTE',
 'PONGELUPE': 'BARREIRO',
 'POUSADA SANTO ANTÔNIO': 'NORDESTE',
 'PRADO': 'OESTE',
 'PRIMEIRO DE MAIO': 'NORTE',
 'PROVIDÊNCIA': 'NORTE',
 'RENASCENÇA': 'NORDESTE',
 'RIBEIRO DE ABREU': 'NORDESTE',
 'RIO BRANCO': 'VENDA NOVA',
 'SAGRADA FAMÍLIA': 'LESTE',
 'SALGADO FILHO': 'OESTE',
 'SANTA AMÉLIA': 'PAMPULHA',
 'SANTA BRANCA': 'PAMPULHA',
 'SANTA CECÍLIA': 'BARREIRO',
 'SANTA CRUZ': 'NORDESTE',
 'SANTA EFIGÊNIA': 'CENTRO-SUL',
 'SANTA HELENA': 'BARREIRO',
 'SANTA INÊS': 'LESTE',
 'SANTA ISABEL': 'CENTRO-SUL',
 'SANTA LÚCIA': 'CENTRO-SUL',
 'SANTA MARGARIDA': 'BARREIRO',
 'SANTA MARIA': 'OESTE',
 'SANTA RITA': 'BARREIRO',
 'SANTA RITA DE CÁSSIA': 'CENTRO-SUL',
 'SANTA ROSA': 'PAMPULHA',
 'SANTA SOFIA': 'OESTE',
 'SANTA TEREZA': 'LESTE',
 'SANTA TEREZINHA': 'PAMPULHA',
 'SANTANA DO CAFEZAL': 'CENTRO-SUL',
 'SANTO AGOSTINHO': 'CENTRO-SUL',
 'SANTO ANDRÉ': 'NOROESTE',
 'SANTO ANTÔNIO': 'CENTRO-SUL',
 'SÃO BENEDITO': 'NORDESTE',
 'SÃO BENTO': 'CENTRO-SUL',
 'SÃO BERNARDO': 'NORTE',
 'SÃO CRISTÓVÃO': 'NOROESTE',
 'SÃO DAMIÃO': 'VENDA NOVA',
 'SÃO FRANCISCO': 'PAMPULHA',
 'SÃO FRANCISCO DAS CHAGAS': 'NOROESTE',
 'SÃO GABRIEL': 'NORDESTE',
 'SÃO GERALDO': 'LESTE',
 'SÃO GONÇALO': 'NORTE',
 'SÃO JOÃO': 'BARREIRO',
 'SÃO JOÃO BATISTA': 'VENDA NOVA',
 'SÃO JORGE I': 'OESTE',
 'SÃO JORGE II': 'OESTE',
 'SÃO JORGE III': 'OESTE',
 'SÃO JOSÉ': 'PAMPULHA',
 'SÃO LUCAS': 'CENTRO-SUL',
 'SÃO LUÍZ': 'PAMPULHA',
 'SÃO LUIZ': 'PAMPULHA',
 'SÃO MARCOS': 'NORDESTE',
 'SÃO PAULO': 'NORDESTE',
 'SÃO SALVADOR': 'NOROESTE',
 'SÃO SEBASTIÃO': 'NORDESTE',
 'SÃO TOMÁZ': 'NORTE',
 'SÃO TOMAZ': 'NORTE',
 'SÃO VICENTE': 'LESTE',
 'SATÉLITE': 'NORTE',
 'SAUDADE': 'LESTE',
 'SAVASSI': 'CENTRO-SUL',
 'SENHOR DOS PASSOS': 'NOROESTE',
 'SERRA': 'CENTRO-SUL',
 'SERRA DO CURRAL': 'BARREIRO',
 'SERRA VERDE': 'VENDA NOVA',
 'SERRANO': 'PAMPULHA',
 'SILVEIRA': 'NORDESTE',
 'SION': 'CENTRO-SUL',
 'SOLAR DO BARREIRO': 'BARREIRO',
 'SOLIMÕES': 'NORTE',
 'SPORT CLUB': 'OESTE',
 'SUMARÉ': 'NOROESTE',
 'SUZANA': 'PAMPULHA',
 'TAQUARIL': 'LESTE',
 'TEIXEIRA DIAS': 'BARREIRO',
 'TIRADENTES': 'NORDESTE',
 'TIROL': 'BARREIRO',
 'TRÊS MARIAS': 'NORDESTE',
 'TREVO': 'PAMPULHA',
 'TÚNEL DE IBIRITÉ': 'BARREIRO',
 'TUPI A': 'NORTE',
 'TUPI B': 'NORTE',
 'UNIÃO': 'NORDESTE',
 'UNIDAS': 'VENDA NOVA',
 'UNIVERSO': 'VENDA NOVA',
 'URCA': 'PAMPULHA',
 'VALE DO JATOBÁ': 'BARREIRO',
 'VÁRZEA DA PALMA': 'VENDA NOVA',
 'VENDA NOVA': 'VENDA NOVA',
 'VENTOSA': 'OESTE',
 'VERA CRUZ': 'LESTE',
 'VILA AEROPORTO': 'NORTE',
 'VILA AEROPORTO JARAGUÁ': 'PAMPULHA',
 'VILA ANTENA': 'OESTE',
 'VILA ANTENA MONTANHÊS': 'PAMPULHA',
 'VILA ÁTILA DE PAIVA': 'BARREIRO',
 'VILA BANDEIRANTES': 'CENTRO-SUL',
 'VILA BARRAGEM SANTA LÚCIA': 'CENTRO-SUL',
 'VILA BATIK': 'BARREIRO',
 'VILA BETÂNIA': 'OESTE',
 'VILA BOA VISTA': 'LESTE',
 'VILA CALAFATE': 'OESTE',
 'VILA CALIFÓRNIA': 'NOROESTE',
 'VILA CANTO DO SABIÁ': 'VENDA NOVA',
 'VILA CEMIG': 'BARREIRO',
 'VILA CLÓRIS': 'NORTE',
 'VILA COPACABANA': 'VENDA NOVA',
 'VILA COPASA': 'BARREIRO',
 'VILA COQUEIRAL': 'NOROESTE',
 'VILA DA AMIZADE': 'OESTE',
 'VILA DA ÁREA': 'LESTE',
 'VILA DA LUZ': 'NORDESTE',
 'VILA DA PAZ': 'NORDESTE',
 'VILA DAS OLIVEIRAS': 'NOROESTE',
 'VILA DIAS': 'LESTE',
 'VILA DO POMBAL': 'NORDESTE',
 'VILA DOS ANJOS': 'VENDA NOVA',
 'VILA ECOLÓGICA': 'BARREIRO',
 'VILA ENGENHO NOGUEIRA': 'PAMPULHA',
 'VILA ESPLANADA': 'NORDESTE',
 'VILA FORMOSA': 'BARREIRO',
 'VILA FUMEC': 'CENTRO-SUL',
 'VILA HAVAÍ': 'OESTE',
 'VILA INDEPENDÊNCIA I': 'BARREIRO',
 'VILA INDEPENDÊNCIA II': 'BARREIRO',
 'VILA INDEPENDÊNCIA IV': 'BARREIRO',
 'VILA INESTAN': 'NORDESTE',
 'VILA IPIRANGA': 'NORDESTE',
 'VILA JARDIM ALVORADA': 'PAMPULHA',
 'VILA JARDIM LEBLON': 'VENDA NOVA',
 'VILA JARDIM MONTANHÊS': 'PAMPULHA',
 'VILA JARDIM SÃO JOSÉ': 'PAMPULHA',
 'VILA MADRE GERTRUDES I': 'OESTE',
 'VILA MADRE GERTRUDES II': 'OESTE',
 'VILA MADRE GERTRUDES III': 'OESTE',
 'VILA MADRE GERTRUDES V': 'OESTE',
 'VILA MALOCA': 'NOROESTE',
 'VILA MANGUEIRAS': 'BARREIRO',
 'VILA MANTIQUEIRA': 'VENDA NOVA',
 'VILA MARIA': 'NORDESTE',
 'VILA MINASLÂNDIA': 'NORTE',
 'VILA NOSSA SENHORA APARECIDA': 'VENDA NOVA',
 'VILA NOSSA SENHORA DO ROSÁRIO': 'LESTE',
 'VILA NOVA': 'NORTE',
 'VILA NOVA CACHOEIRINHA II': 'NOROESTE',
 'VILA NOVA CACHOEIRINHA IV': 'NORDESTE',
 'VILA NOVA DOS MILIONÁRIOS': 'BARREIRO',
 'VILA NOVA GAMELEIRA I': 'OESTE',
 'VILA NOVA GAMELEIRA II': 'OESTE',
 'VILA NOVA GAMELEIRA III': 'OESTE',
 'VILA NOVA PARAÍSO': 'OESTE',
 'VILA NOVO SÃO LUCAS': 'CENTRO-SUL',
 'VILA OESTE': 'OESTE',
 "VILA OLHOS D'ÁGUA": 'BARREIRO',
 'VILA OURO MINAS': 'NORDESTE',
 'VILA PAQUETÁ': 'PAMPULHA',
 'VILA PARAÍSO': 'LESTE',
 'VILA PARIS': 'CENTRO-SUL',
 'VILA PETRÓPOLIS': 'BARREIRO',
 'VILA PILAR': 'BARREIRO',
 'VILA PINHO': 'BARREIRO',
 'VILA PIRATININGA': 'BARREIRO',
 'VILA PIRATININGA VENDA NOVA': 'VENDA NOVA',
 'VILA PRIMEIRO DE MAIO': 'NORTE',
 'VILA PUC': 'NOROESTE',
 'VILA REAL I': 'PAMPULHA',
 'VILA REAL II': 'PAMPULHA',
 'VILA RICA': 'PAMPULHA',
 'VILA SANTA MÔNICA': 'VENDA NOVA',
 'VILA SANTA ROSA': 'PAMPULHA',
 'VILA SANTO ANTÔNIO': 'PAMPULHA',
 'VILA SANTO ANTÔNIO BARROQUINHA': 'PAMPULHA',
 'VILA SÃO DIMAS': 'NORDESTE',
 'VILA SÃO FRANCISCO': 'PAMPULHA',
 'VILA SÃO GABRIEL JACUÍ': 'NORDESTE',
 'VILA SÃO GERALDO': 'LESTE',
 'VILA SÃO JOÃO BATISTA': 'VENDA NOVA',
 'VILA SÃO PAULO': 'NORDESTE',
 'VILA SÃO RAFAEL': 'LESTE',
 'VILA SATÉLITE': 'VENDA NOVA',
 'VILA SESC': 'VENDA NOVA',
 'VILA SUMARÉ': 'NOROESTE',
 'VILA SUZANA I': 'PAMPULHA',
 'VILA SUZANA II': 'PAMPULHA',
 'VILA TIROL': 'BARREIRO',
 'VILA TRINTA E UM DE MARÇO': 'NOROESTE',
 'VILA UNIÃO': 'LESTE',
 'VILA VERA CRUZ I': 'LESTE',
 'VILA VERA CRUZ II': 'LESTE',
 'VILA VISTA ALEGRE': 'OESTE',
 'VIRGÍNIA': 'OESTE',
 'VISTA ALEGRE': 'OESTE',
 'VISTA DO SOL': 'NORDESTE',
 'VITÓRIA': 'NORDESTE',
 'VITÓRIA DA CONQUISTA': 'BARREIRO',
 'XANGRI-LÁ': 'PAMPULHA',
 'XODÓ-MARIZE': 'NORTE',
 'ZILAH SPÓSITO': 'NORTE',
 'BAIRRO DAS INDÚSTRIAS II': 'OESTE',
 'CABANA DO PAI TOMÁS': 'OESTE',
 'COLÉGIO BATISTA': 'NORDESTE',
 'DIAMANTE': 'BARREIRO',
 'GRAÇA': 'NORDESTE',
 'JARDIM GUANABARA': 'NORTE',
 'MANTIQUEIRA': 'VENDA NOVA',
 'NOVA AMÉRICA': 'VENDA NOVA',
 'PENHA': 'NORDESTE',
 'SANTA MÔNICA': 'VENDA NOVA',
 'SÃO PEDRO': 'CENTRO-SUL',
 'UNIVERSITÁRIO': 'PAMPULHA',
 'VILA DE SÁ': 'NORDESTE',
 'VILA NOVA CACHOEIRINHA I': 'NOROESTE',
 'VILA SÃO GABRIEL': 'NORDESTE'
}

# Lista de bairros
bairros = ['aarão reis',
 'acaba mundo',
 'acaiaca',
 'ademar maldonado',
 'aeroporto',
 'águas claras',
 'alípio de melo',
 'alpes',
 'alta tensão',
 'alta tensão i',
 'alto barroca',
 'alto caiçaras',
 'alto das antenas',
 'alto dos pinheiros',
 'alto vera cruz',
 'álvaro camargos',
 'ambrosina',
 'anchieta',
 'andiroba',
 'antônio ribeiro de abreu',
 'aparecida',
 'aparecida sétima seção',
 'ápia',
 'apolônia',
 'apolonia',
 'araguaia',
 'átila de paiva',
 'atila de paiva',
 'bacurau',
 'bairro das indústrias i',
 'bairro novo das indústrias',
 'baleia',
 'bandeirantes',
 'barão homem de melo i',
 'barão homem de melo ii',
 'barão homem de melo iii',
 'barão homem de melo iv',
 'barreiro',
 'barro preto',
 'barroca',
 'beija flor',
 'beira-linha',
 'beira linha',
 'bela vitória',
 'bela vitoria',
 'belém',
 'belmonte',
 'belvedere',
 'bernadete',
 'betânia',
 'biquinhas',
 'bispo de maura',
 'boa esperança',
 'boa união i',
 'boa união ii',
 'boa viagem',
 'boa vista',
 'bom jesus',
 'bonfim',
 'bonsucesso',
 'brasil industrial',
 'braúnas',
 'buritis',
 'cachoeirinha',
 'caetano furquim',
 'caiçara-adelaide',
 'caiçaras',
 'calafate',
 'califórnia',
 'camargos',
 'campo alegre',
 'camponesa',
 'camponesa i',
 'camponesa ii',
 'camponesa iii',
 'campus ufmg',
 'canaã',
 'canadá',
 'candelaria',
 'candelária',
 'capitão eduardo',
 'cardoso',
 'carlos prates',
 'carmo',
 'casa branca',
 'castanheira',
 'castelo',
 'cdi jatobá',
 'cdi jatoba',
 'cenáculo',
 'centro',
 'céu azul',
 'chácara leonina',
 'cidade jardim',
 'cidade jardim taquaril',
 'cidade nova',
 'cinqüentenário',
 'comiteco',
 'concórdia',
 'cônego pinheiro',
 'cônego pinheiro a',
 'confisco',
 'conjunto bonsucesso',
 'conjunto califórnia i',
 'conjunto califórnia ii',
 'conjunto capitão eduardo',
 'conjunto celso machado',
 'conjunto floramar',
 'conjunto jardim filadélfia',
 'conjunto jatobá',
 'conjunto lagoa',
 'conjunto minascaixa',
 'conjunto novo dom bosco',
 'conjunto paulo vi',
 'conjunto providência',
 'conjunto santa maria',
 'conjunto são francisco de assis',
 'conjunto serra verde',
 'conjunto taquaril',
 'copacabana',
 'coqueiros',
 'coração de jesus',
 'coração eucarístico',
 'corumbiara',
 'cruzeiro',
 'custodinha',
 'delta',
 'distrito industrial do jatobá',
 'dom bosco',
 'dom cabral',
 'dom joaquim',
 'dom silvério',
 'dona clara',
 'engenho nogueira',
 'ermelinda',
 'ernesto do nascimento',
 'esperança',
 'esplanada',
 'estoril',
 'estrela',
 'estrela do oriente',
 'etelvina carneiro',
 'europa',
 'eymard',
 'fazendinha',
 'fernão dias',
 'flamengo',
 'flávio de oliveira',
 'flávio marques lisboa',
 'floramar',
 'floresta',
 'frei leopoldo',
 'funcionários',
 'gameleira',
 'garças',
 'glória',
 'goiânia',
 'grajaú',
 'granja de freitas',
 'granja werneck',
 'grota',
 'grotinha',
 'guanabara',
 'guarani',
 'guaratã',
 'gutierrez',
 'havaí',
 'heliópolis',
 'horto',
 'horto florestal',
 'imbaúbas',
 'inconfidência',
 'indaiá',
 'independência',
 'ipê',
 'ipiranga',
 'itaipu',
 'itapoã',
 'itatiaia',
 'jaqueline',
 'jaraguá',
 'jardim alvorada',
 'jardim américa',
 'jardim atlântico',
 'jardim do vale',
 'jardim dos comerciários',
 'jardim felicidade',
 'jardim leblon',
 'jardim montanhês',
 'jardim são josé',
 'jardim vitória',
 'jardinópolis',
 'jatobá',
 'joão alfredo',
 'joão paulo ii',
 'joão pinheiro',
 'jonas veiga',
 'juliana',
 'lagoa',
 'lagoa da pampulha',
 'lagoinha',
 'lagoinha leblon',
 'lajedo',
 'laranjeiras',
 'leonina',
 'letícia',
 'liberdade',
 'lindéia',
 'lorena',
 'lourdes',
 'luxemburgo',
 'minas caixa',
 'madre gertrudes',
 'madri',
 'mala e cuia',
 'manacás',
 'mangabeiras',
 'mangueiras',
 'marajó',
 'maravilha',
 'marçola',
 'maria goretti',
 'maria helena',
 'maria teresa',
 'maria virgínia',
 'mariano de abreu',
 'marieta i',
 'marieta ii',
 'marilândia',
 'mariquinhas',
 'marmiteiros',
 'milionários',
 'minas brasil',
 'minascaixa',
 'minaslândia',
 'mineirão',
 'miramar',
 'mirante',
 'mirtes',
 'monsenhor messias',
 'monte azul',
 'monte são josé',
 'morro dos macacos',
 'nazaré',
 'nossa senhora da aparecida',
 'nossa senhora da conceição',
 'nossa senhora de fátima',
 'nossa senhora do rosário',
 'nova cachoeirinha',
 'nova cintra',
 'nova esperança',
 'nova floresta',
 'nova gameleira',
 'nova granada',
 'nova pampulha',
 'nova suissa',
 'nova vista',
 'novo aarão reis',
 'novo glória',
 'novo ouro preto',
 'novo santa cecília',
 'novo são lucas',
 'novo tupi',
 'oeste',
 'olaria',
 "olhos d'água",
 'ouro minas',
 'ouro preto',
 'padre eustáquio',
 'palmares',
 'palmeiras',
 'pantanal',
 'paquetá',
 'paraíso',
 'parque são josé',
 'parque são pedro',
 'paulo vi',
 'pedreira prado lopes',
 'petrópolis',
 'pilar',
 'pindorama',
 'pindura saia',
 'pirajá',
 'piratininga',
 'pirineus',
 'planalto',
 'pompéia',
 'pongelupe',
 'pousada santo antônio',
 'prado',
 'primeiro de maio',
 'providência',
 'renascença',
 'ribeiro de abreu',
 'rio branco',
 'sagrada família',
 'salgado filho',
 'santa amélia',
 'santa branca',
 'santa cecília',
 'santa cruz',
 'santa efigênia',
 'santa helena',
 'santa inês',
 'santa isabel',
 'santa lúcia',
 'santa margarida',
 'santa maria',
 'santa rita',
 'santa rita de cássia',
 'santa rosa',
 'santa sofia',
 'santa tereza',
 'santa terezinha',
 'santana do cafezal',
 'santo agostinho',
 'santo andré',
 'santo antônio',
 'são benedito',
 'são bento',
 'são bernardo',
 'são cristóvão',
 'são damião',
 'são francisco',
 'são francisco das chagas',
 'são gabriel',
 'são geraldo',
 'são gonçalo',
 'são joão',
 'são joão batista',
 'são jorge i',
 'são jorge ii',
 'são jorge iii',
 'são josé',
 'são lucas',
 'são luíz',
 'são luiz',
 'são marcos',
 'são paulo',
 'são salvador',
 'são sebastião',
 'são tomáz',
 'são tomaz',
 'são vicente',
 'satélite',
 'saudade',
 'savassi',
 'senhor dos passos',
 'serra',
 'serra do curral',
 'serra verde',
 'serrano',
 'silveira',
 'sion',
 'solar do barreiro',
 'solimões',
 'sport club',
 'sumaré',
 'suzana',
 'taquaril',
 'teixeira dias',
 'tiradentes',
 'tirol',
 'três marias',
 'trevo',
 'túnel de ibirité',
 'tupi a',
 'tupi b',
 'união',
 'unidas',
 'universo',
 'urca',
 'vale do jatobá',
 'várzea da palma',
 'venda nova',
 'ventosa',
 'vera cruz',
 'vila aeroporto',
 'vila aeroporto jaraguá',
 'vila antena',
 'vila antena montanhês',
 'vila átila de paiva',
 'vila bandeirantes',
 'vila barragem santa lúcia',
 'vila batik',
 'vila betânia',
 'vila boa vista',
 'vila calafate',
 'vila califórnia',
 'vila canto do sabiá',
 'vila cemig',
 'vila clóris',
 'vila copacabana',
 'vila copasa',
 'vila coqueiral',
 'vila da amizade',
 'vila da área',
 'vila da luz',
 'vila da paz',
 'vila das oliveiras',
 'vila dias',
 'vila do pombal',
 'vila dos anjos',
 'vila ecológica',
 'vila engenho nogueira',
 'vila esplanada',
 'vila formosa',
 'vila fumec',
 'vila havaí',
 'vila independência i',
 'vila independência ii',
 'vila independência iv',
 'vila inestan',
 'vila ipiranga',
 'vila jardim alvorada',
 'vila jardim leblon',
 'vila jardim montanhês',
 'vila jardim são josé',
 'vila madre gertrudes i',
 'vila madre gertrudes ii',
 'vila madre gertrudes iii',
 'vila madre gertrudes v',
 'vila maloca',
 'vila mangueiras',
 'vila mantiqueira',
 'vila maria',
 'vila minaslândia',
 'vila nossa senhora aparecida',
 'vila nossa senhora do rosário',
 'vila nova',
 'vila nova cachoeirinha ii',
 'vila nova cachoeirinha iv',
 'vila nova dos milionários',
 'vila nova gameleira i',
 'vila nova gameleira ii',
 'vila nova gameleira iii',
 'vila nova paraíso',
 'vila novo são lucas',
 'vila oeste',
 "vila olhos d'água",
 'vila ouro minas',
 'vila paquetá',
 'vila paraíso',
 'vila paris',
 'vila petrópolis',
 'vila pilar',
 'vila pinho',
 'vila piratininga',
 'vila piratininga venda nova',
 'vila primeiro de maio',
 'vila puc',
 'vila real i',
 'vila real ii',
 'vila rica',
 'vila santa mônica',
 'vila santa rosa',
 'vila santo antônio',
 'vila santo antônio barroquinha',
 'vila são dimas',
 'vila são francisco',
 'vila são gabriel jacuí',
 'vila são geraldo',
 'vila são joão batista',
 'vila são paulo',
 'vila são rafael',
 'vila satélite',
 'vila sesc',
 'vila sumaré',
 'vila suzana i',
 'vila suzana ii',
 'vila tirol',
 'vila trinta e um de março',
 'vila união',
 'vila vera cruz i',
 'vila vera cruz ii',
 'vila vista alegre',
 'virgínia',
 'vista alegre',
 'vista do sol',
 'vitória',
 'vitória da conquista',
 'xangri-lá',
 'xodó-marize',
 'zilah spósito',
 'bairro das indústrias ii',
 'cabana do pai tomás',
 'colégio batista',
 'diamante',
 'graça',
 'jardim guanabara',
 'mantiqueira',
 'nova américa',
 'penha',
 'santa mônica',
 'são pedro',
 'universitário',
 'vila de sá',
 'vila nova cachoeirinha i',
 'vila são gabriel']


def encontra_Regiao(bairro):
    regiao = bairro_regiao[bairro.upper()]
    
    return regiao

def regioes():
    
    reg =     [["CENTRO-SUL","Região Centro-Sul","Região Centro-Sul de Belo Horizonte","Região Centro Sul", "Regiao Centro-Sul da capital","Região Centro-Sul de BH","Centro-Sul","Centro Sul"],
               ["LESTE","Região Leste","Região Leste de Belo Horizonte","Leste","Região Leste da capital","Região Leste de BH"],
               ["NORDESTE","Região Nordeste","Região Nordeste de Belo Horizonte","Região Nordeste da Capital","Região Nordeste de BH"],
               ["NORTE","Região Norte","Região Norte de Belo Horizonte","Região Norte da Capital","Região Norte de BH"],
               ["VENDA NOVA","Venda Nova","Região Venda Nova de Belo Horizonte","Região Venda Nova da Capital","Região Venda Nova de BH"],
               ["PAMPULHA","Regiao da Pampulha","Região da Pampulha de Belo Horizonte","Região da Pampulha de BH","Pampulha"],
               ["NOROESTE","Região Noroeste","Região Noroeste de Belo Horizonte","Região Noroeste da Capital","Região Noroeste de BH"],
               ["OESTE","Região Oeste","Região Oeste de Belo Horizonte","Região Oeste da Capital","Região Oeste de BH"],
               ["BARREIRO","Região do Barreiro","Região do Barreiro de Belo Horizonte","Região do Barreiro da Capital","Região do Barreiro de BH","Barreiro","Região Barreiro"]]
    
    return reg;


def avenidas(loc):
    try:
        url = f'http://geocoder.pbh.gov.br/geocoder/v2/address?logradouro={loc.replace(" ", "%20")}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        print(f"URL solicitada: {url}")  # Debug: Printar a URL solicitada

        if r.status_code == 200:
            try:
                avenida = r.json()
                print(f"Resposta JSON: {avenida}")  # Debug: Printar a resposta JSON
                if 'endereco' in avenida and len(avenida['endereco']) > 0:
                    bairro = avenida['endereco'][0].get('bairropopular', 'Desconhecido')
                    regiao = avenida['endereco'][0].get('nomeregional', 'Desconhecido')

                    return [bairro, regiao]
                else:
                    print("Endereço não encontrado")
                    return "Endereço não encontrado"
            except ValueError as e:
                print(f"Erro ao decodificar JSON: {e}")
                print(f"Resposta do servidor: {r.text}")  # Debug: Printar a resposta bruta do servidor
                return "Erro ao decodificar JSON"
        else:
            print(f"Erro na solicitação HTTP: {r.status_code}")
            return "Erro na solicitação HTTP"
    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")
        return "Erro ao fazer a solicitação HTTP"


def viadutos(loc):
    try:
        # Adicionar cabeçalho User-Agent para simular uma requisição de navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Construir a URL com o logradouro
        url = f'http://geocoder.pbh.gov.br/geocoder/v2/address?logradouro={loc}'
        
        # Fazer a requisição para a API
        r = requests.get(url, headers=headers)
        
        # Verificar se a resposta foi bem-sucedida
        if r.status_code == 200:
            try:
                # Tentar decodificar a resposta JSON
                viaduto = r.json()

                # Verificar se há dados de 'endereco' e se a lista não está vazia
                if 'endereco' in viaduto and len(viaduto['endereco']) > 0:
                    for end in viaduto['endereco']:
                        # Verificar se o tipo de logradouro é 'VIADUTO'
                        if end.get('tipologradouro') == 'VIADUTO':
                            regiao = end.get('nomeregional', 'Desconhecida')
                            bairro = end.get('bairropopular', 'Desconhecida')
                            return [bairro, regiao]
                # Caso não encontre o viaduto ou os dados
                return ['Desconhecido', 'Desconhecida', "Não_BH"]

            except ValueError as e:
                # Erro ao decodificar JSON
                print(f"Erro ao decodificar JSON: {e}")
                return ['Desconhecido', 'Desconhecida', "Não_BH"]
        
        elif r.status_code == 403:
            # Lidar com o erro 403 (Proibido)
            print(f"Erro 403: Acesso proibido. Verifique as permissões ou limites da API.")
            return ['Desconhecido', 'Desconhecida', "Não_BH"]
        
        else:
            # Se a resposta não for 200 ou 403, exibir erro
            print(f"Erro na solicitação HTTP: {r.status_code}")
            return ['Desconhecido', 'Desconhecida', "Não_BH"]

    except requests.RequestException as e:
        # Exceções relacionadas à requisição HTTP
        print(f"Erro ao fazer a solicitação HTTP: {e}")
        return ['Desconhecido', 'Desconhecida', "Não_BH"]


def ruas(loc):
    try:
        url = f'http://geocoder.pbh.gov.br/geocoder/v2/address?logradouro={loc}'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            try:
                rua = r.json()
                if 'endereco' in rua and len(rua['endereco']) > 0:
                    bairro = rua['endereco'][0].get('bairropopular', 'Desconhecido')
                    regiao = rua['endereco'][0].get('nomeregional', 'Desconhecido')

                    return [bairro, regiao]
                else:
                    return ['Desconhecido', 'Desconhecida', "Não_BH"]
            except ValueError as e:
                print(f"Erro ao decodificar JSON: {e}")
                return ['Desconhecido', 'Desconhecida', "Não_BH"]
        else:
            print(f"Erro na solicitação HTTP: {r.status_code}")
            return ['Desconhecido', 'Desconhecida', "Não_BH"]
    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")
        return ['Desconhecido', 'Desconhecida', "Não_BH"]



def save_to_mongo_crime(termo, tt, db_name, perfil):
    # Função exemplo para salvar no MongoDB
    client = pymongo.MongoClient("localhost", 27017)
    db = client[db_name]
    collection = db[perfil]
    document = {"termo": termo, "tt": tt}
    collection.insert_one(document)


def pracas(loc):
    try:
        # Adicionando o cabeçalho User-Agent para simular uma requisição de navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        url = f'http://geocoder.pbh.gov.br/geocoder/v2/address?logradouro={loc}'
        r = requests.get(url, headers=headers)
        print(f"URL solicitada 2: {url}")  # Debug: Printar a URL solicitada

        if r.status_code == 200:
            try:
                praca = r.json()
                print(f"Resposta JSON: {praca}")  # Debug: Printar a resposta JSON
                if 'endereco' in praca and len(praca['endereco']) > 0:
                    bairro = praca['endereco'][0].get('bairropopular', 'Desconhecido')
                    regiao = praca['endereco'][0].get('nomeregional', 'Desconhecido')

                    return [bairro, regiao]
                else:
                    print("Endereço não encontrado")
                    return "Endereço não encontrado"
            except ValueError as e:
                print(f"Erro ao decodificar JSON: {e}")
                print(f"Resposta do servidor: {r.text}")  # Debug: Printar a resposta bruta do servidor
                return "Erro ao decodificar JSON"
        else:
            print(f"Erro na solicitação HTTP: {r.status_code}")
            return "Erro na solicitação HTTP"
    except requests.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP: {e}")
        return "Erro ao fazer a solicitação HTTP"


def salva_tweet_local(bairro,regiao,data, mongo_db, mongo_db_coll, **mongo_conn_kw):

    client = pymongo.MongoClient(**mongo_conn_kw)

    db = client[mongo_db]

    coll = db[mongo_db_coll]
    
    data['regiao'] = regiao.upper()
    data['bairro'] = bairro.lower()
    coll.update_one(
    {'_id': data['_id']},  
    {'$set': {'is_crime': 1, 
              'found_location': 1, 
              'region': regiao.lower(), 
              'bairro': bairro.lower(),
              'integrated': 0
              }} 
    )

def encontra_local_link(txt,bairros,nlp):
    doc = nlp(txt)        
    print(doc)
    for ent in doc.ents:
        
        if(ent.label_ == 'LOC'):
            
            loc = str(ent).lower()
            
            if loc in bairros:
                regiao = encontra_Regiao(loc)
                bairro = loc
                return [bairro,regiao];
            
            elif("avenida" in loc):
                avenida = avenidas(loc[8:])
                return avenida;
            
            elif("rua" in loc):
                rua = ruas(loc[4:])
                return rua;
            
            elif("praça" in loc):
                praca = pracas(loc[6:])
                print(praca)
                return praca;
            
            elif("viaduto" in loc):
                viaduto = viadutos(loc[8:])
                return viaduto;
            
    regi = regioes()
    for regiao in regi:
        for x in regiao:
            if x.lower() in txt.lower():
                return ["Desconhecido",regiao[0],regiao[0]]; 
    
    
    if "metropolitana" in txt.lower():
        return ["Desconhecido","Região Metropolitana","Região_Metropolitana"];
    
    elif "belo horizonte" in txt.lower():
        return ["Desconhecido","Desconhecida","Geral"];
        
    elif "BH" in txt:
        return ["Desconhecido","Desconhecida","Geral"];
    
    elif "#BH" in txt:
        return ["Desconhecido","Desconhecida","Geral"];
        
    elif "capital" in txt.lower():
        return ["Desconhecido","Desconhecida","Geral"];
        
    return ["Desconhecido","Desconhecido","Não_BH"];


def encontra_texto_link(link):
    from bs4 import BeautifulSoup
    from requests.adapters import HTTPAdapter
    from requests.packages.urllib3.util.retry import Retry

    retry_strategy = Retry(
      total=20,
      backoff_factor=1
    )
    
    
    adapter = HTTPAdapter(max_retries=retry_strategy)
    http = requests.Session()
    http.mount("https://", adapter)
    http.mount("http://", adapter)

    
    texto = ''
    
    html = http.get(link).content
    soup = BeautifulSoup(html, 'html.parser')
    
    if('www.itatiaia.com' in link):
        #titulo
        texto += str(soup.find_all('h1'))
        #materia"
        texto += str(soup.find_all(class_='c_article_content svelte-e5q6qs'))
        
    elif('www.band.uol.com' in link):
        #titulo
        texto += str(soup.find_all('title'))
        #materia"
        texto += str(soup.find_all(class_='text'))
        
    elif('hoje.vc' in link):
        #titulo
        texto += str(soup.find_all('h1'))
        #materia"
        texto += str(soup.find_all(class_='styled__Paragraph-sc-fdx3oi-6 eValfS'))
            
    elif('www.otempo.com' in link):
        #titulo
        texto += str(soup.find_all('h1'))
        #materia"
        texto += str(soup.find_all(id='text-content'))
                  
    elif('www.r7.com' in link):
        #titulo
        texto += str(soup.find_all(class_='toolkit-title'))
        #materia"
        texto += str(soup.find_all('p'))
                  
    elif('noticias.r7.com' in link):
        #titulo
        texto += str(soup.find_all(class_='toolkit-title'))
        #materia"
        texto += str(soup.find_all('p'))
                  
    elif('r7.com' in link):
        #titulo
        texto += str(soup.find_all(class_='toolkit-title'))
        #materia"
        texto += str(soup.find_all('p'))

    print("Texto:", texto)
        
    cleantext = BeautifulSoup(texto, "lxml").text
    
    caracteres = ["/","<",">","(",")","|",'[',']','*']
    
    for c in caracteres:
        cleantext = cleantext.replace(c, ' ')
    
    return cleantext

def encontra_local(item,bairros,nlp):
    
    txt = f"{item.get('title', '')} {item.get('description', '')} {item.get('body', '')} "
    
    doc = nlp(txt)
    
    for ent in doc.ents:
        if(ent.label_ == 'LOC'):
            loc = str(ent).lower()

            if loc in bairros:
                regiao = encontra_Regiao(loc)
                bairro = loc
                return [bairro,regiao];
            
            elif("avenida" in loc):
                avenida = avenidas(loc[8:])
                return avenida;
            
            elif("rua" in loc):
                rua = ruas(loc[4:])
                return rua;
            
            elif("praça" in loc):
                praca = pracas(loc[6:])
                return praca;
            
            elif("viaduto" in loc):
                viaduto = viadutos(loc[8:])
                return viaduto;
        
    
    if(len(item['links']) > 0):
        link = item['links'][0]['link']
        textoLink = encontra_texto_link(link)
        resul = encontra_local_link(textoLink,bairros,nlp)
        return resul
    
    regi = regioes()
    for regiao in regi:
        for x in regiao:
            if x.lower() in txt.lower():
                return ["Desconhecido",regiao[0],regiao[0]]; 
    
    
    if "metropolitana" in txt.lower():
        return ["Desconhecido","Região Metropolitana","Região_Metropolitana"];
    
    elif "belo horizonte" in txt.lower():
        return ["Desconhecido","Desconhecida","Geral"];
        
    elif "BH" in txt:
        return ["Desconhecido","Desconhecida","Geral"];
    
    elif "#BH" in txt:
        return ["Desconhecido","Desconhecida","Geral"];
        
    elif "capital" in txt.lower():
        return ["Desconhecido","Desconhecida","Geral"];
   
    return ["Desconhecido","Desconhecido","Não_BH"];


def filtra_local(bairros):
    import pymongo
    import re
    import spacy
    bairros2 = []
    
    for bairro in bairros:
        bairros2.append(bairro.lower())
    
    nlp = spacy.load('pt_core_news_lg')
    
    client = pymongo.MongoClient("localhost", 27017)

    db = client["bh-safezone"]
    
    mycol = db["whatsapps"]
    data = mycol.find({"is_crime": 1, "found_location": 0})
    t = data.clone()
    
    for item in data:
        lista = encontra_local(item,bairros2,nlp)
        
        print("Lista:", lista)

        if(len(lista)<3):
            salva_tweet_local(lista[0],lista[1],item,"bh-safezone","whatsapps")
        else:
            salva_tweet_local(lista[0],lista[1],item,"bh-safezone","whatsapps")



filtra_local(bairros)