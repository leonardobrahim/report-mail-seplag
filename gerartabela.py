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


