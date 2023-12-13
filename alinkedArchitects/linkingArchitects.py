from pyvis.network import Network
import pandas as pd

df = pd.read_csv('mapArchitects2.csv', index_col=0)

df = df.head(10)

net = Network(notebook=True)

for i in df.columns:
    net.add_node(i)

# Add edges
for i in list(df.index):
    for j in list(df.columns):
        if df.loc[i][j] == 0:
            pass
        else:
            net.add_edge(i, j, width=int(df.loc[i][j]))


net.show_buttons()
net.show('linkedArchitects.html')



