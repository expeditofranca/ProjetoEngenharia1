# Modelo Conceitual

```mermaid
classDiagram
    class Cliente {
        +String cpf
        +String nome
        +String telefone
        +String rua
        +String numero
        +String bairro
        +String profissao
        +Float renda
    }

    class Pagamento {
        +int cod_pagamento
        +Float valor
        +Date data
        +String status
    }

    class Divida {
        +int cod_divida
        +int num_nota
        +Float valor
        +Date data
        +String status
        +String cpf_f
    }

    class Compra {
        +int cod_compra
        +String status
        +Boolean fiado
        +Date data
        +Float valor
    }

    Cliente "1" -- "0..*" Pagamento : efetua
    Cliente "1" -- "1" Divida : tem
    Cliente "1" -- "0..*" Compra : realiza
    Compra "0..*" -- "1" Divida : gera
    Pagamento "0..*" -- "1" Divida : liquida
```

# Modelo de Dados (Entidade-Relacionamento)

```mermaid
erDiagram
    CLIENTE ||--o{ PAGAMENTO : "efetua"
    CLIENTE ||--|| DIVIDA : "tem"
    CLIENTE ||--o{ COMPRA : "realiza"
    DIVIDA ||--o{ PAGAMENTO : "liquida"
    COMPRA }o--|| DIVIDA : "gera"

    CLIENTE {
        string nome PK
        string cpf
        string telefone
        string endereco_rua
        string endereco_numero
        string endereco_bairro
        string profissao
        float renda
    }

    PAGAMENTO {
        int cod_pagamento PK
        float valor
        date data
        string status
    }

    COMPRA {
        int cod_compra PK
        string status
        boolean fiado
        date data
        float valor
    }

    DIVIDA {
        string cpf_f PK
        int cod_divida
        int num_nota
        float valor
        date data
        string status
    }
```