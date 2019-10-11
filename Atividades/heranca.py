class Funcionario:
    
    def __init__(self, hora_trabalho, qtd_hrs_trab):
        self.salario_hora = hora_trabalho
        self.hrs_trab = qtd_hrs_trab

    def calcula_salario(self):
        return (self.salario_hora * self.hrs_trab)

    def dar_aumento(self):
        salario = self.salario_hora * self.hrs_trab
        aumento = salario * 6 / 100
        return salario + aumento


class Programador(Funcionario):
    # def __init__(self, sal_horas, qtd_horas, linguagem_preferida):
    #    super().__init__(sal_horas, qtd_horas)
    #    self.linguagem = linguagem_preferida

    def __init__(self, qtd_horas: float, valor_hora: float, linguagem):
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas
        self.linguagem = linguagem
    


class Estagiario(Funcionario):
    
    def calcula_salario(self):
        return self.salario_hora * self.hrs_trab + 150 + 350



        

if __name__ == '__main__':
    f = Funcionario(23, 24)
    print(f.calcula_salario())
    print(f.dar_aumento())
    
    p = Programador(2, 2, 'Python')
    print(p.calcula_salario())
    print(p.linguagem)
    

    e = Estagiario(100, 23)
    print(e.calcula_salario())
    print(e.dar_aumento())
    