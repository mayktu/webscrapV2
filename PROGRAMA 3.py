
## Arquivo onde esta os links filtrados no programa 2
f = open("CODIGOFONTE - RECOLHIDO COM FILTRO 2.txt",'r')

## Arquivo saída com os links mesclados
mesclados = open("CODIGOFONTE - RECOLHIDO COM FILTRO 3.txt",'a')

## Frase a ser mesclada
vetor = ["frase a ser mesclada aqui"]

## Leitura do arquivo com links filtrados
texto = f.readlines()

for linha in texto :

    url=vetor[0] + linha

    mesclados.write(str(url))
    
f.close()
mesclados.close()
