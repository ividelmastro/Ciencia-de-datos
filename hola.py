print("hola")
print("quiero ver si funciona git")


import pandas as pd

df = pd.read_csv("archive/circuits.csv")
print(df.head().to_string())