from pyvis.network import Network
import pandas as pd

df = pd.read_csv('mapArchitects.csv', index_col=0)


net = Network(notebook=True)

for i in df.index:
    net.add_node(i)

# Add edges
for i in list(df.index):
    for j in list(df.columns):
        net.add_edge(i, j)
        

net.show_buttons()
net.show('linkedArchitects.html')



