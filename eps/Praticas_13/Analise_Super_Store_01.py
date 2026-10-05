# %%
import pandas as pd

df = pd.read_csv("../../data/Superstore.csv", encoding="latin1")

pd.set_option("display.max_columns", None)
df.head()
# %%
# 1, 2. 9994 rows and 21 columns
df.shape


# %%
# 3. 
df.dtypes

# %%
# 4. 0 nulls value
df.info()

# %%
# 6

customer_count = df["Customer ID"].nunique()
customer_count
# %%

#6. 
products_count = df["Product ID"].nunique()
products_count

#%%
# 7. The most expensive product
df["Product Price"] = df["Sales"] / df["Quantity"]
df = df.sort_values(by=["Product Price"], ascending=False)
df.head(1)

# %%

# 8. The cheapest product

df = df.sort_values(by=["Product Price"], ascending=True)
df.head(1)

# %%
# 9. Qual e o valor medio dads vendas? 

mean_sales = df["Sales"].mean()
mean_sales 

# %%

# 10. 

df = df.sort_values(by=["Product Price"], ascending=False)
df["Product Name"].head(10)

# %%
# 11. Sales > 500

filter = df["Sales"] > 500
df[filter]

# %%

# 12 Customer that have more than 1 Order ID

group = df.groupby(by = ["Customer ID"])["Order ID"].nunique()
filter = group > 1
customers = group[filter].index.to_list()
customers

# %%

# 14. Mostre apenas vendas realizadas em 2013.

df["Order Date"] = pd.to_datetime(dayfirst = True, arg = df["Order Date"])
filter = df["Order Date"].dt.year == 2013

df[filter]



# %% 

# 15. Quais pedidos foram feitos em janeiro?

filter = df["Order Date"].dt.month == 1

df[filter]["Order ID"]



# %%

# 16. Order with discount

filter = df["Discount"] > 0.01

df[filter]


# %%

# 17. Customer from Los Ageles



filter = df["City"] == "Los Angeles"

df[filter]


# %%

# 18.


filter = (df["Sales"] >= 100) & ( df["Sales"] <= 300 ) 

df[filter].shape[0]

# %%

# 19. Get the order from AP-10720	

filter = df["Customer ID"] == "AP-10720"

df[filter]
 
# %%

# 20. 

filter = df["Category"] == "Office Supplies"

df[filter]


# %%

# 21. How many order each customer has?

df.groupby(by = ["Customer ID"])["Order ID"].nunique()

# %%


# 22. How much each customer spent?

df.groupby(by = ["Customer ID"])["Sales"].sum()

# %%

# 23. It s not the best way to do

df_mean_ticket =  df.groupby(by = ["Customer ID"]).agg({"Order ID" : ["nunique"],
                                      "Sales" : ["sum"]})

df_mean_ticket.columns = ["NumberOfOrders", "SumSales"]

df_mean_ticket["mean_ticket"] = df_mean_ticket["SumSales"] / df_mean_ticket["NumberOfOrders"]

df_mean_ticket.head()


# %%

# 24. Revenue by Category


df.groupby(by = ["Category"])["Sales"].sum()


# %%

# 25. Best seller product

df["Product Name"].value_counts().sort_values(ascending= False).head(1)


# %%

# 26. The city with most orders

df.groupby(by = ["City"])["Order ID"].count().sort_values(ascending= False).head(1)

# %%
# 27

df.groupby(by = ["State"])["Sales"].sum().sort_values(ascending=False).head(1)

# %%

# 29. Mean Monthly Revenue

df.groupby(by = df["Order Date"].dt.month)["Sales"].mean()

# %%

# 30

df.groupby(by = ["Category"])["Sales"].mean().sort_values(ascending=False)



