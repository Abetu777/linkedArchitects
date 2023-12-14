from pyvis.network import Network
import pandas as pd

net = Network(notebook=True)

net.add_node('aaa')

net.show_buttons()
net.show('sample.html')