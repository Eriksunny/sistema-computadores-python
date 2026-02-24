from computador import Computador
from sistema import SistemaComputadores

# Criando o sistema
sistema = SistemaComputadores()

# PC 1 (PC do Lucas)
pc1 = Computador(
    "H310M",
    "AMD RX 550",
    4,
    "Intel Core i5 9400F",
    6,
    2.9,
    4.1,
    "DDR4",
    16,
    2666
)

# PC 2 (PC do Adrian)
pc2 = Computador(
    "B550M Gaming",
    "RTX 3050",
    8,
    "Ryzen 7 5700G",
    16,
    3.8,
    4.6,
    "DDR4",
    16,
    3200
)
# PC 3 (PC do Yago)
pc3 = Computador(
    "B450M",
    "GTX 1660 Super",
    6,
    "Ryzen 5 2600X",
    12,
    3.6,
    4.2,
    "DDR4",
    16,
    3000
)

# Adicionando ao sistema
sistema.adicionar_computador(pc1)
sistema.adicionar_computador(pc2)
sistema.adicionar_computador(pc3)

# Listar PCs (resumo)
sistema.listar_computadores()

# Mostrar detalhes completos
print("\nDetalhes completos:")
sistema.mostrar_todos_detalhes()


