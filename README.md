# covid19-bigdata-pipeline

Tugas UTS mata kuliah Big Data (IFB-451). Pipeline batch untuk dataset COVID-19
(Our World in Data, ~98 MB) di atas Hadoop HDFS + Spark, dijalankan dengan
Docker Compose. Analisis dilakukan dari JupyterLab.

## Stack

- Hadoop HDFS 3.2.1 (namenode + datanode, image bde2020)
- Spark 3.3.0 (master + worker) + Hive
- JupyterLab (jupyter/pyspark-notebook)
- Docker Compose

## Menjalankan

```bash
docker compose up -d

# upload dataset ke HDFS
docker cp owid-covid-data.csv namenode:/tmp/
docker exec -it namenode hdfs dfs -put /tmp/owid-covid-data.csv /data/
```

Akses:

- JupyterLab: http://localhost:8888
- HDFS NameNode UI: http://localhost:9870
- Spark Master UI: http://localhost:8081

Alurnya: CSV masuk ke HDFS (`hdfs dfs -put`), dibaca dari notebook dengan
`spark.read.csv`, disimpan sebagai tabel Hive (`.saveAsTable()`), lalu dianalisis
dengan Spark SQL dan divisualisasikan pakai Plotly.

## File

- `docker-compose.yml` — definisi cluster
- `arsi.py` — generate diagram pipeline (butuh Graphviz terinstall)
- `notebooks/` — notebook analisis
- `owid-covid-data.csv` — dataset (tidak ikut di repo, download dari Our World in Data)
