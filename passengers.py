import pandas as pd

# Kind of data handled by pandas
df = pd.DataFrame({
        "Name": ["Jenny", "Little", "Owens"],
        "Age": [23, 45, 67],
        "Favouratie_color": ["Red", "Blue", "Black"]
    })

# geting data from a specific column
name_data = df["Name"]

# getting the maxiumum nuber in  the colunm
biggest_value = df["Age"].max()

# defining data in a Dataframe using "Series"
person = pd.Series(["Tall", "beautiful", "Brave"], name="Name")

# reading and writing tabular data

