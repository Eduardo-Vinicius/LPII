# Linguagem de Programação II
# AC05 ADS2D - Banco
#
# Alunos: aluno1.sobrenome@aluno.faculdadeimpacta.com.br
#         aluno2.sobrenome@aluno.faculdadeimpacta.com.br
from typing import Union, List, Dict

Number = Union[int, float]


class Cliente():
    """
    Classe Cliente do Banco.

    possui os atributos: nome, telefone e email, todos privados
    caso o email não seja um email válido gera um ValueError,
    caso o telefone não seja um número gera um TypeError
    """

    def __init__(self, nome: str, telefone: int, email: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email

    def get_nome(self) -> str:
        """Acessor do atributo Nome."""
        return self._nome

    def get_telefone(self) -> int:
        """Acessor do atributo Telefone."""
        return self._telefone

    def set_telefone(self, novo_telefone: int) -> None:
        """
        Mutador do atributo telefone, caso não receba um número,
        gera um TypeError
        """
        try:
            if type(novo_telefone) is not int:
                raise TypeError
        except TypeError:
            print('Número de telefone inválido, informe um número válido!')
        else:
            self._telefone = novo_telefone

    def get_email(self) -> str:
        """Acessor do atributo Email."""

        return self._email

    def set_email(self, novo_email: str) -> None:
        """
        Mutador do atributo Email, caso não receba um email válido
        gera um ValueError.
        """
        try:
            if '@' not in novo_email:
                raise ValueError
        except ValueError:
            print('E-mail inválido, gentileza informar um e-mail válido.')
        else:
            self._email = novo_email


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    * abre_contas: abre uma nova conta, atribuindo o numero da conta em ordem
    crescente.
    * lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna que armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """

    def __init__(self, nome: str):
        self._nome = nome
        self.contas = []
        self.contador = 0

    def get_nome(self) -> str:
        """Acessor do Atributo Nome."""
        return self._nome

    def abre_conta(self, clientes: List[Cliente], saldo_ini: Number) -> None:
        """
        Método para abertura de nova conta, recebe os clientes
    e o saldo inicial.
        Caso o saldo inicial seja menor que 0 devolve um ValueError
        """

        try:
            if saldo_ini < 0:
                raise ValueError
        except ValueError:
            print('Saldo inicial não pode ser menor que 0.')
        else:
            self.contador += 1
            count = Conta(clientes, self.contador, saldo_ini)
            self.contas.append(count)

    def lista_contas(self) -> List['Conta']:
        """Retorna a lista com todas as contas do banco."""
        return self.contas


class Conta():
    """
    Classe Conta.
    * Todas as operações (saque e deposito, e saldo inicial) devem aparecer
    no extrato como tuplas, exemplo ('saque', 100), ('deposito'), 200) etc.
    * Caso o saldo inicial seja menor que zero deve lançar um ValueError
    * A criação da conta deve aparecer no extrato com o valor
    do saldo_inicial, exemplo: ('saldo_inicial', 1000)
    DICA: Crie uma variável interna privada para guardar as
    operaões feitas na conta
    """

    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        self.cliente = clientes
        self.numero_conta = numero_conta
        self._saldo = saldo_inicial
        self.lista = [('saldo_inicial', saldo_inicial)]

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        return self.cliente

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        return self._saldo

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        return self.numero_conta

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        Caso o valor do saque seja maior que o saldo da conta,
        deve retornar um ValueError, e não efetuar o saque
        '''
        try:
            if valor > self._saldo:
                raise ValueError
        except ValueError:
            print('Saldo indisponível.')
        else:
            self._saldo -= valor
            self.lista.append(('saque', valor))

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        try:
            if valor < 0:
                raise ValueError
        except ValueError:
            print('Deposito não pode ser menor do que 0.')
        else:
            self._saldo += valor
            self.lista.append(tuple(('deposito', valor)))

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações (Tuplas) executadas na Conta
        '''

        return self.lista
