# -*- coding: utf-8 -*-
from abc import ABC, abstractclassmethod, abstractproperty
     
        

class Cliente:
    
    def __init__(self, endereco, contas=[]):
        self.endereco = endereco
        self.contas = contas
        print('cliente inciado')


    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        print('transacao realizada')
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print('conta adicionada')
        
class Pessoa_fisica(Cliente):
    
    def __init__ (self, endereco, contas, nome, cpf, nascimento):
        super().__init__(endereco,contas)
        self.nome = nome
        self.cpf = cpf 
        self.nascimento = nascimento
        print('cpf, nome e data de nascimento')
        
##################################################
        
class Conta:
    
    def  __init__(self, numero, cliente):
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._saldo=0   
        
    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property 
    def saldo(self):
        return self._saldo
 
    @property 
    def numero(self):
        return self._numero

    @property 
    def agencia(self):
        return self._agencia
    
    @property 
    def cliente(self):
        return self._cliente

    @property 
    def historico(self):
        return self._historico 
    
    def sacar(self, valor):
        print('sacando')
    
    def depositar(self,valor):
        print('depositando')
    
    
class Conta_Corrente (Conta):
    
    def __init__(self, numero, cliente, historico=[], limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limie = limite
        self.limite_saque = limite_saque
        print('cc')

    def sacar(self, valor):
        print('algo particular da cc')
        super().sacar(valor)
    
###########################################

        
class Historico:
    
    def __init__ (self):
        print('esse historico')
        self._historico = []

    @property 
    def historico(self):
        return self._historico
          
    def adicionar_transacao(self, transacao):
        self._historico.appende(transacao)
        print('adicionando transacao')
   
####################################################    

        
class Transacao(ABC):
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    
    @abstractproperty 
    def valor(self):
        pass
        
class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        conta.sacar(self._valor)
        conta.historico.adicionar_transacao(self)
        print('sacando e registrando o saque')
    
    @property 
    def valor(self):
        return self._valor

        
class Deposito(Transacao):
    
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        conta.depositar(self._valor)
        conta.historico.adicionar_transacao(self)
        print('depositando e registrando o deposito')
    
    @property 
    def valor(self): 
        return self._valor
        
####################################################      
    
    
