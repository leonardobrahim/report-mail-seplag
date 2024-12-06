import pandas as pd

# Simula os dados (substituir com a leitura do arquivo real, como CSV ou Excel)
data = {
    "UGC_Sigla_Ação": ["Ação 1", "Ação 2", "Ação 3", "Ação 4"],
    "Dotação Autorizada": [100000, 150000, 200000, 250000],
    "Liquidado": [50000, 120000, 180000, 200000],
    "Ano": [2024, 2024, 2023, 2024],
}

# Cria o DataFrame
df = pd.DataFrame(data)

# Filtra os dados por Ano = 2024
filtered_df = df[df["Ano"] == 2024].copy()

# Calcula o % Liquidado
filtered_df["% Liquidado"] = (filtered_df["Liquidado"] / filtered_df["Dotação Autorizada"]) * 100

# Remove a coluna 'Ano', se não for necessária na tabela final
filtered_df = filtered_df.drop(columns=["Ano"])

# Gera a tabela HTML
# Remova qualquer linha que tente inserir títulos antes da tabela
html_table = filtered_df.to_html(
    index=False,
    border=1,
    justify="center",
    classes="styled-table",
    table_id="execucao-orcamentaria",
)

# Adicione manualmente ao HTML somente o que é necessário
html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 20px;
        }}
        .styled-table {{
            margin: 0 auto;
            border-collapse: collapse;
            width: 80%;
        }}
        .styled-table th, .styled-table td {{
            border: 1px solid #dddddd;
            padding: 8px;
            text-align: center;
        }}
        .styled-table th {{
            background-color: #f4f4f4;
        }}
    </style>
</head>
<body>
    <!-- Título opcional -->
    {html_table}
</body>
</html>
"""

# Salva o HTML em um arquivo
with open("execucao_orcamentaria_2024.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML gerado com sucesso!")
