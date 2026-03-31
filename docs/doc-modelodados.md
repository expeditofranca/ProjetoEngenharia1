# Modelo de Dados (Entidade-Relacionamento)

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