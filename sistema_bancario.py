from abc import ABC, abstractmethod
import re

class Conta(ABC):
    """Classe base abstrata para todas as contas bancárias."""
    
    def __init__(self, numero: str, titular: str, saldo_inicial: float = 0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial  # Utiliza o setter para validação

    @property
    def numero(self) -> str:
        return self._numero

    @numero.setter
    def numero(self, valor: str):
        if not re.match(r"^\d{4,6}-\d$", str(valor).strip()):
            raise ValueError(f"Número de conta '{valor}' inválido. Formato esperado: XXXXX-X")
        self._numero = valor.strip()

    @property
    def titular(self) -> str:
        return self._titular

    @titular.setter
    def titular(self, valor: str):
        if not valor or len(valor.strip()) < 3:
            raise ValueError("O nome do titular deve ter pelo menos 3 caracteres.")
        self._titular = valor.strip()

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = float(valor)

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._saldo += valor

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        """Método abstrato para saque. Cada conta possui sua regra de taxa/limite."""
        pass

    @abstractmethod
    def aplicar_rendimento_ou_tarifa(self) -> None:
        """Método abstrato para processamento periódico de tarifas ou rendimentos."""
        pass

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] Conta: {self.numero} | Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(numero='{self.numero}', titular='{self.titular}', saldo={self.saldo})"

    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Conta):
            return False
        return self.numero == outro.numero

    def __lt__(self, outro: object) -> bool:
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.saldo < outro.saldo

class ContaCorrente(Conta):
    """Representa uma conta corrente com limite de cheque especial e tarifa mensal."""
    
    def __init__(self, numero: str, titular: str, saldo_inicial: float = 0.0, limite_cheque_especial: float = 500.0):
        self._limite_cheque_especial = 0.0
        super().__init__(numero, titular, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    @property
    def limite_cheque_especial(self) -> float:
        return self._limite_cheque_especial

    @limite_cheque_especial.setter
    def limite_cheque_especial(self, valor: float):
        if valor < 0:
            raise ValueError("O limite do cheque especial não pode ser negativo.")
        self._limite_cheque_especial = float(valor)

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        
        saldo_disponivel = self.saldo + self.limite_cheque_especial
        if valor > saldo_disponivel:
            raise ValueError(f"Saldo insuficiente. Saldo + Limite disponível: R$ {saldo_disponivel:.2f}")
        
        self._saldo -= valor
        return True

    def aplicar_rendimento_ou_tarifa(self) -> None:
        tarifa = 20.0
        if self.saldo + self.limite_cheque_especial >= tarifa:
            self._saldo -= tarifa
            print(f"Tarifa mensal de R$ {tarifa:.2f} descontada da {self.numero}.")
        else:
            raise ValueError("Saldo e limite insuficientes para pagamento da tarifa mensal.")


class ContaPoupanca(Conta):
    """Representa uma conta poupança com taxa de rendimento mensal."""
    
    def __init__(self, numero: str, titular: str, saldo_inicial: float = 0.0, taxa_rendimento: float = 0.005):
        super().__init__(numero, titular, saldo_inicial)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self) -> float:
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor: float):
        if not (0 <= valor <= 0.1):
            raise ValueError("A taxa de rendimento deve estar entre 0% e 10% (0.0 a 0.1).")
        self._taxa_rendimento = float(valor)

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError(f"Saldo insuficiente na Poupança. Saldo atual: R$ {self.saldo:.2f}")
        
        self._saldo -= valor
        return True

    def aplicar_rendimento_ou_tarifa(self) -> None:
        rendimento = self.saldo * self.taxa_rendimento
        self._saldo += rendimento
        print(f"Rendimento de R$ {rendimento:.2f} creditado na {self.numero}.")


class ContaInvestimento(Conta):
    """Representa uma conta de investimentos com rendimento e taxa sobre saques."""
    
    def __init__(self, numero: str, titular: str, saldo_inicial: float = 0.0, taxa_saque: float = 0.015):
        super().__init__(numero, titular, saldo_inicial)
        self.taxa_saque = taxa_saque

    @property
    def taxa_saque(self) -> float:
        return self._taxa_saque

    @taxa_saque.setter
    def taxa_saque(self, valor: float):
        if not (0 <= valor <= 0.05):
            raise ValueError("A taxa de saque deve estar entre 0% e 5% (0.0 a 0.05).")
        self._taxa_saque = float(valor)

    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        
        valor_com_taxa = valor * (1 + self.taxa_saque)
        if valor_com_taxa > self.saldo:
            raise ValueError(f"Saldo insuficiente para valor + taxa de saque (Total: R$ {valor_com_taxa:.2f}).")
        
        self._saldo -= valor_com_taxa
        return True

    def aplicar_rendimento_ou_tarifa(self) -> None:
        rendimento = self.saldo * 0.012
        self._saldo += rendimento
        print(f"Rendimento de investimento R$ {rendimento:.2f} creditado na {self.numero}.")

if __name__ == "__main__":
    print("--- 1. CRIAÇÃO DE INSTÂNCIAS (10 OBJETOS) ---")
    contas = []
    
    try:
        contas = [
            ContaCorrente("1001-1", "Yuri Santos", 1500.0, 1000.0),
            ContaCorrente("1002-2", "Luís Soeiro", 800.0, 500.0),
            ContaCorrente("1003-3", "Marcio Freire", 2500.0, 2000.0),
            ContaCorrente("1004-4", "Marcus Cunha", 100.0, 300.0),
            ContaPoupanca("2001-1", "Sarah Pessoa", 5000.0, 0.006),
            ContaPoupanca("2002-2", "Ana Lima", 1200.0, 0.005),
            ContaPoupanca("2003-3", "Carlos Eduardo", 3000.0, 0.005),
            ContaInvestimento("3001-1", "Beatriz Rocha", 10000.0, 0.01),
            ContaInvestimento("3002-2", "Daniel Mendes", 15000.0, 0.02),
            ContaInvestimento("3003-3", "Elena Rostova", 7500.0, 0.015),
        ]
        print(f"Sucesso: {len(contas)} contas instanciadas com sucesso.\n")
    except ValueError as e:
        print(f"Erro ao instanciar conta: {e}")

    print("--- 2. DEMONSTRAÇÃO DE POLIMORFISMO (OPERAÇÃO EM LOTE) ---")
    print("Aplicando rendimentos/tarifas e realizando saques de R$ 200,00 em todas as contas:")
    for conta in contas:
        try:
            print(f"\nEstado Inicial: {conta}")
            conta.aplicar_rendimento_ou_tarifa()
            conta.sacar(200.0)
            print(f"Pós-Saque     : {conta}")
        except ValueError as e:
            print(f"Falha na operação para {conta.numero}: {e}")

    print("\n--- 3. MÉTODOS ESPECIALES (DUNDER) ---")
    print("Representação amigável (__str__):", str(contas[0]))
    print("Representação técnica   (__repr__):", repr(contas[0]))
    print("Igualdade (__eq__)      :", contas[0] == contas[1])
    
    contas_ordenadas = sorted(contas)
    print(f"\nConta com menor saldo: {contas_ordenadas[0]}")
    print(f"Conta com maior saldo: {contas_ordenadas[-1]}")

    print("\n--- 4. TRATAMENTO DE EXCEÇÕES (ESTADOS INVÁLIDOS) ---")
    
    # Teste 1:
    try:
        c_invalida = ContaCorrente("9999-9", "Teste Erro", saldo_inicial=-500.0)
    except ValueError as e:
        print(f"[EXCEÇÃO CAPTURADA] Saldo Negativo: {e}")

    # Teste 2:
    try:
        c_invalida = ContaPoupanca("123", "Teste Numero")
    except ValueError as e:
        print(f"[EXCEÇÃO CAPTURADA] Número Inválido: {e}")

    # Teste 3:
    try:
        contas[0].sacar(50000.0)
    except ValueError as e:
        print(f"[EXCEÇÃO CAPTURADA] Saque Excedido: {e}")