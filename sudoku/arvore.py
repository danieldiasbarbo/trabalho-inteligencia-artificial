class Nodo:
    def __init__(self, objeto, nivel):
        self.nivel = nivel
        self.objeto = objeto
        self.filhos = objeto.get_filhos()
