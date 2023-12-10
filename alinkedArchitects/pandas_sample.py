import pandas as pd

data = (
    [i for i in range(1, 5)],  
    [i for i in range(5, 9)],  
    [i for i in range(9, 13)],  
    [i for i in range(13, 17)],
)

index = ["a","b", "c", "d"]
columns = ["A", "B", "C", "D"]

df = pd.DataFrame(data, index=index, columns=columns)

# print(df.loc["a"]["A"])

for i in df.index:
    for j in df.columns:
        print(i, j, df.loc[i][j])
