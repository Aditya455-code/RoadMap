import pandas as pd

data = {
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Clothing", "Electronics"],
    "Sales": [1000, 1500, 2000, 1200, 800, 1700]
}

df = pd.DataFrame(data)

pivot=pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Category",
    aggfunc=sum
)
pivot=pivot.fillna(0)
print(pivot)