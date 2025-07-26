import pandas as pd

df_0 = pd.read_csv('data/daily_sales_data_0.csv')
df_1 = pd.read_csv('data/daily_sales_data_1.csv')
df_2 = pd.read_csv('data/daily_sales_data_2.csv')

columns = ["Sales", "Date", "Region"]
rows = []


def process_data(df):
    for i in range(len(df)):
        if df["product"][i] == "pink morsel":
            row = [("$"+str((float(df["price"][i].replace("$","").replace(".",""))/100*int(df["quantity"][i])))), df["date"][i], df["region"][i]]
        rows.append(row)

process_data(df_0)
process_data(df_1)
process_data(df_2)

df = pd.DataFrame(rows, columns=columns)
df.to_csv('data/pink_morsel_sales.csv', index=False)