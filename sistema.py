from computador import Computador

class SistemaComputadores:
    def __init__(self):
        self.computadores = []  # lista de PCs

    def adicionar_computador(self, computador: Computador):
        self.computadores.append(computador)

    def listar_computadores(self):
        if not self.computadores:
            print("Nenhum computador cadastrado.")
            return

        print("\nLista de Computadores:")
        for i, pc in enumerate(self.computadores, start=1):
            print(f"{i}. {pc.resumo()}")

    def mostrar_todos_detalhes(self):
        if not self.computadores:
            print("Nenhum computador cadastrado.")
            return

        for pc in self.computadores:
            pc.mostrar_configuracao()