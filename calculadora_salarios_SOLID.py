class Funcionario:
    def __init__(self, nome, salario_base, calculadora_salario):
        self.nome = nome
        self.salario_base = salario_base
        self.calculadora_salario = calculadora_salario

    def calcular_salario(self):
        return self.calculadora_salario.calcular(self.salario_base)

    def tipo_contrato(self):
        return self.calculadora_salario.tipo


class CalculadoraSalarioEstagiario:
    tipo = "Estagiário"

    def calcular(self, salario_base):
        return salario_base * 0.8


class CalculadoraSalarioCLT:
    tipo = "CLT"

    def calcular(self, salario_base):
        return salario_base


class CalculadoraSalarioPJ:
    tipo = "PJ"

    def calcular(self, salario_base):
        return salario_base * 1.2


class ImpressorDetalhes:
    @staticmethod
    def imprimir_detalhes(funcionario):
        print(f"Nome: {funcionario.nome}")
        print(f"Tipo de Contrato: {funcionario.tipo_contrato()}")
        print(f"Salário: {funcionario.calcular_salario()}")
        
funcionarios = [
    Funcionario("Lucas", 1500, CalculadoraSalarioEstagiario()),
    Funcionario("Marcos", 2500, CalculadoraSalarioCLT()),
    Funcionario("Ana", 4000, CalculadoraSalarioPJ())
]

for funcionario in funcionarios:
    ImpressorDetalhes.imprimir_detalhes(funcionario)
