#import required modules
import pandas as pd
import numpy as np

#create new data frame for sales transactions
salesDF = pd.read_csv("D:\ACC470\salesFINAL.csv")

#display transaction count for sales
print(str("The total sales transactions are ") + str(salesDF.shape[0]))

#display sum of sales transactions
total = salesDF["SalesDollars"].sum()
total = round(total)
print(str("The total sales dollars is ") + str(total))

#create new data frame for purchases transactions
purchasesDF = pd.read_csv("D:\ACC470\PurchasesFINAL.csv")

#display transaction count for purchases
print(str("The total purchases transactions are ") + str(purchasesDF.shape[0]))

#display sum of purchases transactions
total = purchasesDF["Dollars"].sum()
total = round(total)
print(str("The total purchases dollars is ") + str(total))

#create new data frame for beginning inventory transactions
beginvDF = pd.read_csv("D:\ACC470\BegInvFINAL.csv")

#display transaction count for beginning inventory
print(str("The total beginning inventory transactions are ") + str(beginvDF.shape[0]))

#create new data frame for purchase price data
purpriceDF = pd.read_csv("2016PurchasePrices.csv")
purpriceDF = purpriceDF[["Brand","PurchasePrice"]]

#merge purchase price dataframe with beginning inventory data frame on Brand
begpurbrandDF = pd.merge(purpriceDF, beginvDF, on = "Brand")

#add calculated field to purbrandDF called extended cost
begpurbrandDF["ExtCost"] = begpurbrandDF["PurchasePrice"] * begpurbrandDF["onHand"]

#sum the calculated field in the beginning inventory data frame by sales dollars
total = begpurbrandDF["ExtCost"].sum()
total = round(total)
print(str("The total extended cost is ") + str(total))

#create new data frame for ending inventory transactions
endinvDF = pd.read_csv("D:\ACC470\EndInvFINAL.csv")

#display transaction count forending inventory
print(str("The total ending inventory transactions are ") + str(endinvDF.shape[0]))

#merge purchase price dataframe with ending inventory data frame on Brand
endpurbrandDF = pd.merge(purpriceDF, endinvDF, on = "Brand")

#add calculated field to purbrandDF called extended cost
endpurbrandDF["ExtCost"] = endpurbrandDF["PurchasePrice"] * endpurbrandDF["onHand"]

#sum the calculated field in the ending inventory data frame by sales dollars
total = endpurbrandDF["ExtCost"].sum()
total = round(total)
print(str("The total extended cost is ") + str(total))