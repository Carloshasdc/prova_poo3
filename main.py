class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= self._saldo:
                self._saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor de saque deve ser positivo.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self._saldo:.2f}")

# Exemplo de uso da classe:
conta = ContaBancaria("João Silva", 1000)
conta.exibir_saldo()  # Exibe o saldo inicial
conta.depositar(500)  # Adiciona 500 ao saldo
conta.sacar(200)      # Retira 200 do saldo
conta.exibir_saldo()  # Exibe o saldo final
