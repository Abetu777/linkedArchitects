from pyvis.network import Network
import pandas as pd

df = pd.read_csv('mapArchitects.csv', index_col=0)

net = Network(notebook=True)

for i in df.index:
    net.add_node(i)

for i in df.index:
    for j in df.columns:
        if df.loc[i][j] != 0:
            net.add_edge(i, j, value=int(2*df.loc[i][j]))

net.show_buttons()
net.show('aa.html')



