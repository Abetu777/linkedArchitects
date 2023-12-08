from pyvis.network import Network
import pandas as pd

df = pd.read_csv('mapArchitects.csv', index_col=0)


net = Network(notebook=True)
net.add_nodes(df.index)

# df = arch

net.show_buttons(filter_='physics')
net.show('aa.html')