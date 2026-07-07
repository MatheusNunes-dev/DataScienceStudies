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

