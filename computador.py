class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_threads, cpu_base_clock, cpu_turbo_clock, ram_tipo, ram_capacidade, ram_frequencia):

        self.modelo = modelo
        self.gpu_nome = gpu_nome
        self.gpu_memoria = gpu_memoria
        self.cpu_nome = cpu_nome
        self.cpu_threads = cpu_threads
        self.cpu_base_clock = cpu_base_clock
        self.cpu_turbo_clock = cpu_turbo_clock
        self.ram_tipo = ram_tipo
        self.ram_capacidade = ram_capacidade
        self.ram_frequencia = ram_frequencia

    def resumo(self):
        return f"{self.modelo} | {self.cpu_nome} | {self.gpu_nome} | {self.ram_capacidade}GB RAM"

    def mostrar_configuracao(self):
        print(f"\nModelo: {self.modelo}")
        print(f"CPU: {self.cpu_nome} ({self.cpu_threads} threads)")
        print(f"Clock: {self.cpu_base_clock}GHz - {self.cpu_turbo_clock}GHz")
        print(f"GPU: {self.gpu_nome} ({self.gpu_memoria}GB)")
        print(f"RAM: {self.ram_capacidade}GB {self.ram_tipo} {self.ram_frequencia}MHz")