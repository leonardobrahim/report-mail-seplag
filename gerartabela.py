import os
import pandas as pd


#caminho do arquivo csv
caminho_excel = "valores_gerais.xlsx"
df = pd.read_excel(caminho_excel)

df_filtrado = df.query('Ano == 2024')
df_filtrado = df_filtrado.groupby('UGC_Sigla_Ação')[['Dotação Autorizada', 'Liquidado']].sum().reset_index()


df_filtrado['Liquidado'] = df_filtrado['Liquidado'].astype(float)
df_filtrado['Dotação Autorizada'] = df_filtrado['Dotação Autorizada'].astype(float)



df_filtrado['Liquidado %'] = df_filtrado['Liquidado'] / df_filtrado['Dotação Autorizada']
df_filtrado['Liquidado'] = df_filtrado['Liquidado'].map('R$ {:,.2f}'.format)
df_filtrado['Dotação Autorizada'] = df_filtrado['Dotação Autorizada'].map('R$ {:,.2f}'.format)

df_filtrado['Liquidado %'] = df_filtrado['Liquidado %'].map('{:,.2%}'.format)


colunas_desejadas = ['UGC_Sigla_Ação','Dotação Autorizada', 'Liquidado','Liquidado %']

df_filtrado = df_filtrado[colunas_desejadas]

df_html = df_filtrado[colunas_desejadas].to_html(float_format="{:.2f}".format)


