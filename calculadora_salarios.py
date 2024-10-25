class funcionario:
    def __init__(self, nome, tipo, salario_base):
        self.nome = nome
        self.tipo = tipo  
        self.salario_base = salario_base

    def calcular_salario(self):
        if self.tipo == "Estagi�rio":
            return self.salario_base * 0.8 
        elif self.tipo == "CLT":
            return self.salario_base
        elif self.tipo == "PJ":
            return self.salario_base * 1.2
        else:
            raise ValueError("Tipo de funcion�rio inv�lido!")

    def imprimir_detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo de Contrato: {self.tipo}")
        print(f"Sal�rio: {self.calcular_salario()}")


# Exemplo de uso
funcionarios = [
    funcionario("Lucas", "Estagi�rio", 1500),
    funcionario("Marcos", "CLT", 2500),
    funcionario("Ana", "PJ", 4000)
]

for funcionario in funcionarios:
    funcionario.imprimir_detalhes()
