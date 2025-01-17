import pandas as pd

mpg_df = pd.read_csv("./resources/mpg.csv")
mpg_df["horsepower"].unique()
mpg_df = mpg_df.loc[mpg_df["horsepower"] != "?"]
mpg_df.set_index("car name", inplace = True)

mpg_df["horsepower"] = pd.to_numeric(mpg_df["horsepower"])
mpg_df.plot(kind = "scatter", x = "horsepower", y = "mpg", grid = True, figsize = (8,8), title = "MPG vs Horsepower")