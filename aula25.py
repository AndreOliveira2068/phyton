""" POO python """

class Bicicleta:
    
    def  __init__(self , cor , modelo , ano , valor):
        self.cor = cor 
        self.modelo = modelo
        self. ano = ano
        self.valor = valor
        
    def buzinar(self):
        print('bibibibibi')   
         
    def parar(self):
        print(' parando a bicicleta....')   
        print('bicicleta parada....') 
        
    def correr(self):
        print(' em movimento ...')  
        
b1= Bicicleta('cor vermelho', 'modelo', 2023, 1000)
b1.correr()
b1.parar()   
print('caracteristica da bicicleta' , b1.cor , b1.modelo, b1.ano, b1.valor)
input('digite o valor da bicicleta: ')
print(' o valor digitado é R$ 1000')
   