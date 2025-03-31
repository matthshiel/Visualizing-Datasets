import json
import matplotlib.pyplot as plt
import pandas as pd


with open('nobelprize.json', 'r', encoding='utf8') as file:
    data = json.load(file)

prizes = [prize['category'] for prize in data['prizes']]
prize_counts = {category: prizes.count(category) for category in set(prizes)}

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(prize_counts.values(), labels=prize_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Nobel Prizes by Category")
plt.show()

import pandas as pd

file_path = "SYB67_130_202411_Exchange Rates.csv"
data = pd.read_csv(file_path, header=None)

columns = [
    "Country Code", "Country", "Year", "Indicator", "Currency", "Currency Description",
    "Exchange Rate", "Empty Column", "Source"
]
data.columns = columns

bahrain_data = data[(data["Country"] == "Bahrain") & (data["Indicator"].str.contains("period average"))].copy()
british_pound_data = data[(data["Country"] == "British Indian Ocean Terr.") & (data["Indicator"].str.contains("period average"))].copy()

bahrain_data["Exchange Rate"] = pd.to_numeric(bahrain_data["Exchange Rate"], errors="coerce")
british_pound_data["Exchange Rate"] = pd.to_numeric(british_pound_data["Exchange Rate"], errors="coerce")

bahrain_data["Year"] = pd.to_numeric(bahrain_data["Year"], errors="coerce")
british_pound_data["Year"] = pd.to_numeric(british_pound_data["Year"], errors="coerce")
bahrain_data = bahrain_data.sort_values("Year")
british_pound_data = british_pound_data.sort_values("Year")



plt.figure(figsize=(10, 6))
plt.plot(bahrain_data["Year"], bahrain_data["Exchange Rate"], label="Bahrain (BHD/USD)", marker="o")
plt.plot(british_pound_data["Year"], british_pound_data["Exchange Rate"], label="British Pound (GBP/USD)", marker="o")


plt.xlabel("Year")
plt.ylabel("Exchange Rate to USD")
plt.title("Bahrain and British Pound vs. USD")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



