import os
import pandas as pd

caminho_excel = r"valores_gerais.xlsx"
df = pd.read_excel(caminho_excel)

df_filtrado = df.query('Ano == [2023, 2024]')

df_filtrado = (
    df_filtrado.groupby(['Ano', 'UGC_Sigla_Ação'])[['Dotação Autorizada', 'Liquidado']]
    .sum()
    .reset_index()
    .sort_values(['UGC_Sigla_Ação','Ano'])
)
df_filtrado['Liquidado %'] = df_filtrado['Liquidado'] / df_filtrado['Dotação Autorizada']


df_filtrado['Liquidado'] = df_filtrado['Liquidado'].map('R$ {:,.2f}'.format)
df_filtrado['Dotação Autorizada'] = df_filtrado['Dotação Autorizada'].map('R$ {:,.2f}'.format)


df_filtrado['Liquidado %'] = df_filtrado['Liquidado %'].map('{:,.2%}'.format)



colunas_desejadas = ['Ano','UGC','Dotação Autorizada', 'Liquidado','Liquidado %']

df_filtrado.columns = colunas_desejadas

df_html = df_filtrado.to_html(float_format="{:.2f}".format)


