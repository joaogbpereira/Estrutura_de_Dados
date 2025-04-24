class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        """
        Args:
            nome (str): O nome da pessoa.
            idade (int): A idade da pessoa.
            peso (float): O peso da pessoa.
            altura (float): A altura da pessoa em centímetros.
        """
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        for _ in range(anos):
            if self.idade < 21:
                self.altura += 0.5  # aumento de 0.5 cm por ano (em vez de 0.05, que é muito pouco)
            self.idade += 1

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros


# Criando uma instância
pessoa1 = Pessoa("Alice", 18, 60.0, 160.0)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}kg, Altura: {pessoa1.altura}cm")

# Aplicando mudanças
pessoa1.envelhecer(3)
pessoa1.engordar(2.5)
pessoa1.emagrecer(1.0)
pessoa1.crescer(1.0)

# Imprimindo após mudanças
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}kg, Altura: {pessoa1.altura}cm")
