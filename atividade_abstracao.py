from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor):
        self.valor = valor
    @abstractmethod
    def processar_pagamento(self):
        pass

class CartaoCredito(Pagamento):
    def __init__(self,modelo):
        self.modelo = modelo
    
    
    


        


        