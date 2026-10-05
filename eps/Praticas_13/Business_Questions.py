# %%

import pandas as pd

df = pd.read_csv("../../data/Superstore.csv", encoding="latin1")

df.head()
 
# %%

# 1. Quais são os 10 melhores clientes em faturamento?

df.groupby(by = ["Customer ID" , "Customer Name"])["Sales"].sum().sort_values(ascending=False).head(10)

# %%

# 2. Quais são os 10 produtos responsáveis pela maior parte da receita?

df.groupby(by = ["Product ID", "Product Name"])["Sales"].sum().sort_values(ascending=False).head(10)

# %%

# Qual categoria está crescendo mais ao longo dos meses?
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["OrderYearMonth"] = df["Order Date"].dt.to_period("M")

categories = df.groupby(by = ["OrderYearMonth", "Category"])["Sales"].sum()

# %% 

# pct_change represens the increasing month by month
# when we use mean represents the mean incresing monthly


new_df = categories.reset_index()

pivot = new_df.pivot_table(index = ["OrderYearMonth"], columns=["Category"], values= ["Sales"])

growth = pivot.pct_change()

# 1. crescimento médio mensal
avg_growth = growth.mean().sort_values(ascending=False)

# 2. crescimento total (início → fim)
total_growth = (pivot.iloc[-1] / pivot.iloc[0]) - 1

# 3. último crescimento mensal
last_month_growth = growth.iloc[-1]

# %%

# Clientes com risco de chunr 
# Clientes que nao compraram no periodo de 2014-09-30 para frente
last_date = df["Order Date"].max() - pd.Timedelta(days= 180)
last_order = df.groupby(by = ["Customer ID"])["Order Date"].max().reset_index()


filter = last_order["Order Date"] < last_date
last_order[filter]

# %%

# RFM
# Recency → dias desde a última compra
# Frequency → número de pedidos
# Monetary → total gasto

today = df["Order Date"].max()
rfm = df.groupby(by = ["Customer ID"]).agg({"Sales" : "sum",
                                      "Order ID" : "count",
                                      "Order Date" : "max"}).reset_index()


rfm.columns = ["Customer ID","Monetary", "Frequency", "Recency"]
rfm["Recency"] = abs(rfm["Recency"] - today)
rfm


# %%

# 46. Qual foi o melhor mês da história para cada categoria?

result = df.groupby(by = ["Category", "OrderYearMonth"])["Sales"].sum().reset_index()

best_month = result.loc[result.groupby("Category")["Sales"].idxmax()]

best_month

# %%

# Existe sazonalidade nas vendas?
first = df.groupby(by = ["OrderYearMonth"]).agg({"Sales": "sum",
                                                    "Order ID" : "count"}).reset_index()

first.groupby(by = df["OrderYearMonth"].dt.month).agg({"Sales": "mean",
                                                       "Order ID" : "mean"})


"""
Desafio avançado (nível de entrevista)

52. Crie uma análise de retenção de clientes

Sem pesquisar uma solução pronta, responda:

Quantos clientes fizeram a primeira compra em cada mês?
Desses clientes, quantos voltaram a comprar no mês seguinte?
E após 2 meses?
E após 3 meses?
"""










