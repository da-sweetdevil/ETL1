## ETL1 - Logistics Order Analysis ##
> A Python script that extracts data from an Excel file and calculates total cost per city..

### "analyze_orders.py" Script that ->
   - Reads an EXCEL file with delivery data (order_ID, client, city, cost)
   - Loads the file with Pandas
   - Prints: Number of orders - Total cost - Cost per city
   - Frames the **Cost per City** outcome
   - Exports DataFrame to a new CSV

   ## How to Run
   python src/analyze_orders.py data/orders_cities.xlsx

   ## Output
   output/totals_by_city.csv

   ## Requirements
   - pandas
   - pathlib
   - openpyxl


### Push to GitHub ->
   - Commit script + data + README file + .gitignore file
   - Push to a new repository "ETL1"


### ====================== ###
|      Made By @ Y M E N     |
### ====================== ###