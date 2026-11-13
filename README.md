# Sistema Bancário Orientado a Objetos em Python

Este projeto implementa um modelo bancário utilizando conceitos avançados de **Programação Orientada a Objetos (POO)** em Python, incluindo Abstração, Encapsulamento, Herança, Polimorfismo e Métodos Especiais (Dunder).

====

## 1. Diagrama de Classes (Mermaid)

```mermaid
classDiagram
    class Conta {
        <<Abstract>>
        #str _numero
        #str _titular
        #float _saldo
        +numero: str
        +titular: str
        +saldo: float
        +depositar(valor: float)
        +sacar(valor: float)* bool
        +aplicar_rendimento_ou_tarifa()*
        +__str__() str
        +__repr__() str
        +__eq__(outro) bool
        +__lt__(outro) bool
    }

    class ContaCorrente {
        -float _limite_cheque_especial
        +limite_cheque_especial: float
        +sacar(valor: float) bool
        +aplicar_rendimento_ou_tarifa()
    }

    class ContaPoupanca {
        -float _taxa_rendimento
        +taxa_rendimento: float
        +sacar(valor: float) bool
        +aplicar_rendimento_ou_tarifa()
    }

    class ContaInvestimento {
        -float _taxa_saque
        +taxa_saque: float
        +sacar(valor: float) bool
        +aplicar_rendimento_ou_tarifa()
    }

    Conta <|-- ContaCorrente
    Conta <|-- ContaPoupanca
    Conta <|-- ContaInvestimento
