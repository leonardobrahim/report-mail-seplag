import pandas as pd

caminho_excel = "valores_gerais.xlsx"
df = pd.read_excel(caminho_excel)

df_filtrado = df.query('Ano == 2024')
df_filtrado = df_filtrado.groupby('UGC_Sigla_Ação')[['Dotação Autorizada', 'Liquidado']].sum().reset_index()

df_filtrado['Liquidado'] = df_filtrado['Liquidado'].astype(float)
df_filtrado['Dotação Autorizada'] = df_filtrado['Dotação Autorizada'].astype(float)

df_filtrado['Liquidado %'] = (df_filtrado['Liquidado'] / df_filtrado['Dotação Autorizada']) * 100

df_filtrado['Liquidado'] = df_filtrado['Liquidado'].map('R$ {:,.2f}'.format)
df_filtrado['Dotação Autorizada'] = df_filtrado['Dotação Autorizada'].map('R$ {:,.2f}'.format)
df_filtrado['Liquidado %'] = df_filtrado['Liquidado %'].map('{:,.2f}%'.format)

colunas_desejadas = ['UGC_Sigla_Ação', 'Dotação Autorizada', 'Liquidado', 'Liquidado %']
df_filtrado = df_filtrado[colunas_desejadas]

html_table = df_filtrado.to_html(
    index=False,
    border=1,
    justify="center",
    classes="styled-table",
    table_id="execucao-orcamentaria",
)

df_html = f"""
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
            width: 90%;
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
    {html_table}
</body>
</html>
"""
