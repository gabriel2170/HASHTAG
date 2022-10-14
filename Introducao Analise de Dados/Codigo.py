import pandas as pd

tab = pd.read_excel('Vendas.xlsx')

#Total do item

fat_total = tab["Valor Final"].sum()

print("R$ ", float(fat_total))

#Faturamento por Loja

fat_loja = tab[["ID Loja","Valor Final"]].groupby("ID Loja").sum()

print(fat_loja) 


#Faturamento por Produto

fat_prod = tab[["Produto","Valor Final"]].groupby("Produto").sum()

print(fat_prod)

#Faturamento Detalhado

fat_detalhado = tab[["ID Loja","Produto","Valor Final"]].groupby(["ID Loja", "Produto"]).sum()

print(fat_detalhado)
