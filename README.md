# Posição da Execução Orçamentária por UO 2024

Este projeto é uma aplicação para gerar relatórios de execução orçamentária com base em dados de um arquivo Excel e enviá-los por e-mail com formatação personalizada em HTML.

## Funcionalidades

- **Processamento de Dados**:
  - Filtragem dos dados para o ano de 2024.
  - Agrupamento por `UGC_Sigla_Ação` com cálculo da soma de valores de `Dotação Autorizada` e `Liquidado`.
  - Geração de percentual de execução (`Liquidado %`) com formatação monetária e percentual.

- **Geração de Relatório**:
  - Conversão dos dados filtrados em uma tabela HTML formatada.

- **Envio por E-mail**:
  - Configuração de servidor SMTP com variáveis de ambiente.
  - Envio de e-mails com tabela HTML integrada e imagens personalizadas (cabeçalho e rodapé).

## Requisitos

- **Python**: >= 3.8
- **Bibliotecas**:
  - `pandas`
  - `dotenv`
  - `smtplib`
  - `email`
  - `openpyxl` (para leitura de arquivos Excel)
- **Arquivos Necessários**:
  - Arquivo Excel com dados orçamentários (`valores_gerais.xlsx`).
  - Imagens para cabeçalho e rodapé (`header.png` e `footer.png`).

## Estrutura do Projeto

