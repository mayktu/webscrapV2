from bs4 import BeautifulSoup
import requests
import lxml

print ("Programa Iniciado ------>")

login = 'tela de login aki'

info = {
    'username': 'login-aqui',
    'password': 'senha-aqui'
}

## Arquivo dos links mesclados
links = open("CODIGOFONTE - RECOLHIDO COM FILTRO 3.txt","r")

## Arquivo saída  com os novos links
f = open("CODIGOFONTE - RECOLHIDO COM FILTRO 4.txt","a")

##Leitura do arquivos dos links
texto = links.readlines()

## Aqui ele mantem a sessão aberta enquanto recolhe os links de todas as paginas
with requests.Session() as session:
    post = session.post(login, data=info)
    for linha in texto :
         
        request = linha
        t = session.get(request)
        soup = BeautifulSoup(t.text, features="xml")
        lista_artigos = soup.find_all('div',class_='card-body')

        export = str(lista_artigos)
        print(export)
        
        f.write(str(export.encode('utf8')))
        print (str(linha) + 'º - In process...')
    
    ## Aqui voce busca a palavra desejada
    f.seek(0)
    if 'palavra a ser buscada aqui' in f.read():
        print ('true')
    f.close(f)