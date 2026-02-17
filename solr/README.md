# 🚀 SolrCloud Setup with Docker Compose

This guide explains how to reset SolrCloud, upload ZooKeeper config, create a collection, and enable the `/select` handler.

---

# 📦 Prerequisites

* Docker installed
* Docker Compose installed
* Ports `8983`, `2181` available
* Containers: `solr1`, `solr2`, `zookeeper`

---

# 🔄 Step 1: Reset Existing SolrCloud Environment

Stop and remove containers:

```bash
docker compose down
```

Remove existing data directories:

```bash
rm -rf solr1-data solr2-data zk-data
```

---

# ▶️ Step 2: Start SolrCloud Cluster

Start containers in detached mode:

```bash
docker compose up -d
```

Verify containers are running:

```bash
docker ps
```

---

# ⚙️ Step 3: Upload Config to ZooKeeper

Upload the configset named `catalog`:

```bash
docker exec -it solr1 solr zk upconfig \
  -n catalog \
  -d /opt/solr/server/solr/configsets/catalog/conf \
  -z zookeeper:2181
```

Alternative single-line command:

```bash
docker exec -it solr1 solr zk upconfig -n catalog -d /opt/solr/server/solr/configsets/catalog/conf -z zookeeper:2181
```

---

# 📚 Step 4: Create Collection

Create collection named `catalog`:

```bash
curl "http://localhost:8983/solr/admin/collections?action=CREATE\
&name=catalog\
&numShards=1\
&replicationFactor=2\
&collection.configName=catalog"
```

Expected result:

```json
{
  "success": "...",
  "status": 0
}
```

---

# 🔍 Step 5: Enable `/select` Handler (Optional - Legacy Support)

By default, SolrCloud uses `/query`. To enable `/select`:

## Edit solrconfig.xml

Add this inside `<config>`:

```xml
<requestHandler name="/select" class="solr.SearchHandler"/>
```

---

## Restart Solr Nodes

```bash
docker restart solr1 solr2
```

---

## Test Query Using `/select`

```bash
curl "http://localhost:8983/solr/catalog/select?q=*:*&wt=json"
```

---

# 🧪 Test Cluster Health

Check collections:

```bash
curl "http://localhost:8983/solr/admin/collections?action=LIST"
```

Check cluster status:

```bash
curl "http://localhost:8983/solr/admin/collections?action=CLUSTERSTATUS"
```

---

# 📂 Directory Structure Example

```
project-root/
│
├── docker-compose.yml
├── solr1-data/
├── solr2-data/
├── zk-data/
└── README.md
```

---

# ✅ Summary

| Step | Action                      |
| ---- | --------------------------- |
| 1    | docker compose down         |
| 2    | remove data directories     |
| 3    | docker compose up -d        |
| 4    | upload zk config            |
| 5    | create collection           |
| 6    | enable `/select` (optional) |

---

# 🎯 Access URLs

Solr Admin UI:

```
http://localhost:8983/solr
```

ZooKeeper:

```
zookeeper:2181
```
