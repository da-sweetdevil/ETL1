import pandas as pd

df = pd.read_excel("c:/Back2Work/data/orders_cities.xlsx")

# print(df)
# print(df.head()) # 1st 5 rows
# print(df.columns) # table header (index)
# print(set(df.columns)) # as entries
# print(df.info()) # countings and datatypes

num_rows = df.shape[0]
# num_columns = df.shape[1]
# num_rowss = len(df) # same
# num_columnss = len(df.columns)

# print("Number of Columns:", num_columns)
# print("Number of Rows:", num_rows)
# print("Number of Columns:", num_columnss)
# print("Number of Rows:", num_rowss)

total_cost = df["cost"].sum()
# fourth_col = df.iloc[:, 3] # selects 4th column
# total_cost = fourth_col.sum()

total_city = df.groupby("city", as_index=False)["cost"].sum() # as_index=False DataFrame outcome
# totals_df = total_city.reset_index() # get a DataFrame w headers (redundant after as_index=False)
total_city.columns = ["City", "Total Costs"] # Rename DF columns

# Print in a friendly defined format:
# for city, cost in total_city.items(): # .items() turns the grouping into pairs > for key, value in unpacks each pair into 2 variables for use inside the loop
#     print(f"Total for {city}: {cost}")

# print(f"Number of Orders: {num_rows})
# print(f"Total Cost: {total_cost} €)
# print(f"Total per City: {total_city})
# print(totals_df)

total_city.to_csv("C:/Back2Work/outcome.csv", index=False) # auto-overwrites the existing file (lose old data)
# totals_df.to_csv("C:/Back2Work/outcome.csv", index=False) # index=False removes row numbers added by DataFrame
# total_city.to_csv("C:/Back2Work/outcome.csv", index=False, header=["City", "Total Costs"]) # Specify column names !!must be DataFrame!!
# total_city.to_csv("C:/Back2Work/outcome.csv", mode="a", header=False) # header=False removes column names (True by default) for mode="a" to only add the table data
print("All Done!")