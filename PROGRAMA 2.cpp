#include<stdio.h>
#include<stdlib.h>

int main()
{
	long int i, tamanho;
	char c;
	FILE *arquivao, *arquivobase;

	printf("Programa Iniciado ------>");

	//Arquivo onde esta o primeiro recolhimento
	arquivobase = fopen("CODIGOFONTE - RECOLHIDO COM FILTRO 1.txt","r");

	//Arquivo de saída
	arquivao = fopen("CODIGOFONTE - RECOLHIDO COM FILTRO 2.txt","a+");

	//Medindo o tamanho do arquivo
	fseek(arquivobase, 0, SEEK_END);
	tamanho = ftell(arquivobase);
	fseek(arquivobase, 0, SEEK_SET);


	//Programa que ira percorrer recolhendo os links desejados
	for(i = 0; i < tamanho; i++){
		c = fgetc(arquivobase);
		printf("%c",c);
		fflush(arquivao);

		//AQUI VC EDITA DE ACORDO COM A PALAVRA A SER ENCONTRADA: <a href="
		//LEMBRE DE FECHAR OU ABRIR OS PARENTESES LA EM BAIXO
					if(c == '<'){
						i++;
						c = fgetc(arquivobase);

						if(c == 'a'){
							i++;
							c = fgetc(arquivobase);

							if(c == ' '){
							i++;
							c = fgetc(arquivobase);

							if(c == 'h'){
								i++;
								c = fgetc(arquivobase);

								if(c == 'r'){
									i++;
									c = fgetc(arquivobase);

									if(c == 'e'){
										i++;
										c = fgetc(arquivobase);

										if(c == 'f'){
											i++;
											c = fgetc(arquivobase);

											if(c == '='){
												i++;
					 							c = fgetc(arquivobase);
												 
												if(c == '"'){
													c = ' ';
													while(c != '"'){
														i++;
														c = fgetc(arquivobase);
														if(c != '"')
                                                            fputc(c,arquivao);}

												fprintf(arquivao,"\n");}}}}}}}}}}
	return 0;
}








