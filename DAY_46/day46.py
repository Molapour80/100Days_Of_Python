# -*- coding: utf-8 -*-
# کتابخانه‌های مورد نیاز
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd

### ---------- بخش ۱: ساخت گراف و رسم ساده ---------- ###
# ساخت گراف
G = nx.Graph()
G.add_nodes_from(["Ali", "Reza", "Sara", "Maryam", "Amir", "Neda"])
G.add_edges_from([
    ("Ali", "Reza"),
    ("Ali", "Sara"),
    ("Reza", "Maryam"),
    ("Maryam", "Amir"),
    ("Sara", "Amir"),
    ("Reza", "Amir"),
    ("Neda", "Maryam")
])

# رسم با matplotlib
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    edge_color='gray',
    font_size=12,
    font_weight='bold',
    alpha=0.9
)
plt.title("Social Network Graph (Static)", fontsize=15)
plt.savefig("social_network.png")  # ذخیره تصویر
plt.show()

### ---------- بخش ۲: رسم تعاملی با Pyvis ---------- ###
net = Network(notebook=True, height="700px", width="100%", bgcolor="#222222", font_color="white")
net.from_nx(G)

# تنظیمات ظاهری
net.set_options("""
{
  "physics": {
    "barnesHut": {
      "gravitationalConstant": -80000,
      "centralGravity": 0.3,
      "springLength": 250
    },
    "minVelocity": 0.75
  }
}
""")

net.show("social_network_interactive.html")  # ذخیره به صورت HTML

### ---------- بخش ۳: تحلیل شبکه ---------- ###
# محاسبه معیارهای مهم
print("\nتحلیل شبکه:")
print("- درجه گره‌ها:", dict(G.degree()))
print("- بین‌مرکزیت:", nx.betweenness_centrality(G))
print("- نزدیکی مرکزیت:", nx.closeness_centrality(G))

# ذخیره داده‌های تحلیل در DataFrame
metrics = {
    "Node": list(G.nodes()),
    "Degree": dict(G.degree()).values(),
    "Betweenness": nx.betweenness_centrality(G).values(),
    "Closeness": nx.closeness_centrality(G).values()
}
df_metrics = pd.DataFrame(metrics)
print("\nجدول معیارهای شبکه:")
print(df_metrics)