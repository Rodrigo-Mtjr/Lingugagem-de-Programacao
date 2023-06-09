'''HERANÇA SERIA NADA MAIS DO QUE USAR ATRIBUTOS OU METODOS DE UMA CLASSE A OUTRA. FAZENDO COM QUE UMA CLASSE FILHA, TENHA OS MESMOS ATRIBUTOS DO QUE
A CLASSE PAI, PODENDO APENAS DIFERENCIAR E ACRESCENTAR OUTROS ATRIBUTOS A ESSA CLASSE FILHA, SEM PRECISAR CRIAR NOVAMENTE OS MESMO ATRIBUTOS JA EXISTENTES'''

'''PARA CRIAR UMA CLASSE FILHA OU SUBCLASSE, DEVEMOS PRIMEIRO CRIAR A CLASSE PAI. EM SEGUIDA, QUANDO FOR CRIAR A CLASSE FILHA, DEVEMOS COLOCAR COMO PARAMETRO
DE ENTRADA, ENTRE PARENTES, A CLASSE DA ONDE ELA VAI HERDAR OS ATRIBUTOS E OS METODOS, E EM SEGUIDA, APENAS COLOCAR OS METODOS E ATRIBUTOS DIFERENTES, ESPECIFICOS
DAQUELA CLASSE FILHA'''

class Pessoa: #CRIANDO A CLASSE PAI
    def _init_(self): #DEFININDO OS ATRIBUTOS E METODOS COMO INIT, QUE SERA O RESPONSAVEL PELA HERANÇA EM DEMAIS CLASSES
        self.cpf = None #CRIANDO ATRIBUTO CPF
        self.nome = None #CRIANDO ATRIBUTO NOME
        self.endereco = None #CRIANDO ATRIBUTO ENDEREÇO


class Funcionario(Pessoa): #CRIANDO UMA CLASSE FILHA, CHAMADA FUNCIONARIO, COM HERANÇA DA CLASSE PESSOA, NOTE QUE ELA NAO TEM OS MESMO ATRIBUTOS QUE A CLASSE PAI
    def _init_(self): #DEFININDO OS ATRIBUTOS E METODOS COMO INIT, QUE SERA O RESPONSAVEL PELA HERANÇA EM DEMAIS CLASSES
        self.matricula = None #CRIANDO ATRIBUTOS ESPECIFICOS A ESSA CLASSE, ALEM DOS EXISITENTES NA CLASSE PAI
        self.salario = None #CRIANDO ATRIBUTOS ESPECIFICOS A ESSA CLASSE, ALEM DOS EXISITENTES NA CLASSE PAI


class Cliente(Pessoa):
    def _init_(self):
        self.codigo = None
        self.dataCadastro = None


f1 = Funcionario() #CRIANDO UM OBJETO DO TIPO FUNCIONARIO, QUE AO MESMO TEMPO ELE JA É DO TIPO PESSOA, POIS UMA HERDA ATRIBUTOS DA OUTRA
f1.nome = "Funcionário A" #PEDINDO PARA ELE ACRESCENTAR EM NOME, O VALOR FUNCIONARIA A
print(f1.nome) #PRINTANDO NA TELA O RESULTADO

c1 = Cliente() #CRIANDO UM OBJETO DO TIPO CLEINTE, QUE AO MESMO TEMPO JA É DO TIPO PESSO, POIS UMA HERDA ATRIBUTOS DA OUTRA
c1.cpf = "111.111.111-11" #PEDINDO PARA ELE ACRESCENTAR EM CPF, O VALOR 111.111.111-11
print(c1.cpf) #PRINTANDO NA TELA O RESULTADO
