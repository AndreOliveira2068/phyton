
  
"""input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída.""" 


C = int(input()) 
for i in range(C): 
    valor = int(input())
    if valor <= 8000:
        print("Inseto!")
    else:
        print("Maior que 8000!")