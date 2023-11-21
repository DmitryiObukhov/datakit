import pandas as pd

# a)
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"
df = pd.read_csv(url)

# b)
selected_columns = ["Team", "Yellow Cards", "Red Cards"]
df_selected = df[selected_columns]

# c)
num_teams = df["Team"].nunique()

# d)
df_filtered = df[df["Goals"] > 6]

print("a. Data:")
print(df.info())

print("\nb. Selected columns:")
print(df_selected.head())

print("\nc. Number of teams participating in Euro 2012:", num_teams)

print("\nd. Teams that scored more than 6 goals:")
print(df_filtered.loc[:, ["Team", "Goals"]])
