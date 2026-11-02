import graphviz
import os

# Mengatasi masalah PATH untuk Windows jika Graphviz diinstal secara manual
# sesuaikan dengan lokasi instalasi Graphviz
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

# 1. Inisiasi Digraph (Directed Graph)
# rankdir='LR' berarti alurnya dari Kiri ke Kanan (Left to Right)
dot = graphviz.Digraph(comment='Big Data Pipeline UTS')
dot.attr(rankdir='LR', label='Diagram Pipeline Big Data (COVID-19)', fontsize='20', labelloc='t')

# 2. Definisikan Node (Kotak-kotak)
# Kita buat node untuk setiap tahapan
dot.node('A', 'Sumber Data\nowid-covid-data.csv (98.4MB)', shape='rectangle', style='filled', color='lightblue')
dot.node('B', 'Storage (Modul 3)\nHadoop HDFS 3.2.1', shape='cylinder', style='filled', color='lightgray')
dot.node('C', 'Processing (Modul 4, 6)\nSpark 3.3.0 & Hive', shape='box', style='filled', color='orange')
dot.node('D', 'Analysis (Modul 7)\nSpark SQL & Plotly', shape='box', style='filled', color='lightgreen')

# 3. Definisikan Edge (Panah-panah)
# Kita hubungkan node-node tersebut dengan label
dot.edge('A', 'B', label='   docker cp\n   hdfs dfs -put')
dot.edge('B', 'C', label=' spark.read.csv\n .saveAsTable()')
dot.edge('C', 'D', label=' spark.sql("SELECT ...")\n fig.show()')

# 4. Render dan Simpan Gambar
# Ini akan membuat file 'pipeline_diagram.png' di folder yang sama
output_filename = 'pipeline_diagram'

try:
    # 'view=True' akan otomatis membuka gambar setelah dibuat
    dot.render(output_filename, format='png', view=True)
    print(f"Diagram '{output_filename}.png' berhasil dibuat dan ditampilkan!")
except Exception as e:
    print(f"Error: {e}")
    print("Pastikan Graphviz terinstal dan path-nya sudah benar.")