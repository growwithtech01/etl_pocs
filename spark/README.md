# 🚀 Apache Spark Cluster Setup (Docker Compose)

This project runs a **Spark standalone cluster** with:

* 1 Spark Master
* 2 Spark Workers
* Shared Docker network (`vespa-network`)
* Persistent work directory

Uses the **official Apache Spark image (`apache/spark:3.5.0`)**.

---

# 🏗 Architecture

```
vespa-network (external Docker network)

spark-master    → Cluster manager (UI: 8088, Port: 7077)
spark-worker-1  → Worker node
spark-worker-2  → Worker node
```

---

# 📁 Project Structure

```
spark-cluster/
│
├── docker-compose.yml
└── spark-work/
```

---

# ▶️ Start Spark Cluster

Start containers:

```bash
docker compose up -d
```

Verify running containers:

```bash
docker ps
```

---

# 🌐 Access Spark UI

Open browser:

```
http://localhost:8088
```

You should see:

* Spark Master running
* 2 Workers connected

---

# 🧪 Test Spark Shell

Enter Spark shell:

```bash
docker exec -it spark-master /opt/spark/bin/spark-shell
```

Run test:

```scala
sc.parallelize(1 to 5).map(_ * 10).collect()
```

Expected output:

```
Array(10, 20, 30, 40, 50)
```

Exit shell:

```scala
exit
```

---

# ⚙️ Cluster Details

| Component       | Port     | Purpose           |
| --------------- | -------- | ----------------- |
| Spark Master UI | 8088     | Web dashboard     |
| Spark Master    | 7077     | Worker connection |
| Worker nodes    | internal | Execute jobs      |

---

# 🔄 Stop Cluster

Stop containers:

```bash
docker compose down
```

---

# 💾 Persistent Storage

Directory used:

```
./spark-work
```

Stores Spark logs and job data.

---

# ✅ Why apache/spark Image

Bitnami Spark images are no longer publicly available.

Official Apache image:

```
apache/spark:3.5.0
```

Benefits:

* Official
* Reliable
* Production safe
* Always maintained

---

# 🧠 How It Works

1. Master starts cluster
2. Workers connect to master
3. Jobs submitted to master
4. Workers execute tasks
5. Results returned

---

# 🌐 Master URL (for spark-submit)

```
spark://spark-master:7077
```

---

# ✅ Result

You now have a working:

* Spark standalone cluster
* 1 Master + 2 Workers
* Docker-based setup
* Ready for Spark jobs

