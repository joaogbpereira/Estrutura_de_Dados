# 3. Controle de Histórico de Navegação

class Pagina:
    def __init__(self, url):
        self.url = url
        self.anterior = None
        self.proximo = None

class HistoricoNavegacao:
    def __init__(self):
        self.atual = None

    def visitar_pagina(self, url):
        nova_pagina = Pagina(url)
        if self.atual:
            self.atual.proximo = nova_pagina
            nova_pagina.anterior = self.atual
        self.atual = nova_pagina
        print(f"Visitando: {self.atual.url}")

    def voltar(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            print(f"Voltando para: {self.atual.url}")
            return self.atual.url
        else:
            print("Não há página anterior.")
            return None

    def avancar(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            print(f"Avançando para: {self.atual.url}")
            return self.atual.url
        else:
            print("Não há página seguinte.")
            return None

# Exemplo de uso
historico = HistoricoNavegacao()
historico.visitar_pagina("www.exemplo.com")
historico.visitar_pagina("www.python.org")
historico.visitar_pagina("www.google.com")
historico.voltar()
historico.avancar()
historico.voltar()
historico.voltar()
historico.voltar()
historico.avancar()