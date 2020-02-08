from bs4 import BeautifulSoup
import requests
import lxml

print ("Programa Iniciado ------>")

login = 'tela de login aki'

info = {
    'username': 'login-aqui',
    'password': 'senha-aqui'
}

f = open("CODIGOFONTE - RECOLHIDO COM FILTRO 1.txt","a")

vetor = ["pagina a ser navegada atras dos links"]

## Aqui ele mantem a sessão aberta enquanto recolhe os links de todas as paginas
with requests.Session() as session:
    post = session.post(login, data=info)
    for i in range(122,1086,1):
         
        request = vetor[0] + str(i)
        t = session.get(request)
        soup = BeautifulSoup(t.text, features="xml")
        lista_artigos = soup.find_all('p',class_='p-1 font-weight-bold')

        export = str(lista_artigos)
        print(export)
        
        f.write(str(export.encode('utf8')))
        print (str(i) + 'º - In process...')
    f.close(f)