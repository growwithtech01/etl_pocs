# 🚀 Vespa Cluster Setup (Docker Compose)

This project runs a **production-structured Vespa cluster locally** using separate containers for config, content, query, feed, slobrok, and admin.

---

# 🏗 Architecture

```
vespa-network (bridge)

config    → cluster brain (deployment happens here)
content   → indexing & storage
query     → search endpoint (port 8080)
feed      → document API (port 8081)
slobrok   → service registry
admin     → cluster supervision
```

---

# 📁 Project Structure

```
vespa-cluster/
│
├── docker-compose.yml
└── application/
    ├── services.xml
    ├── hosts.xml
    └── schemas/
        └── doc.sd
```

---

# ▶️ Start Cluster

Start all Vespa services:

```bash
docker compose up -d
```

Wait 60 seconds for cluster initialization.

Check containers:

```bash
docker ps
```

---

# 📦 Deploy Application

Download Vespa CLI (one time):

```bash
curl -L https://github.com/vespa-engine/vespa/releases/latest/download/vespa-cli_linux_amd64.tar.gz | tar -xz
```

Deploy application package:

```bash
./vespa deploy --wait 300 http://localhost:19071 application
```

Expected output:

```
Success: Deployed application
```

---

# 📥 Feed Document

Insert a document into Vespa:

```bash
curl -X POST http://localhost:8081/document/v1/doc/docid/1 \
  -H "Content-Type: application/json" \
  -d '{
        "fields": {
          "title": "Hello Vespa",
          "body": "This is a test document"
        }
      }'
```

---

# 🔎 Query Document

Search indexed documents:

```bash
curl "http://localhost:8080/search/?query=vespa"
```

Expected: document returned in JSON.

---

# 🧪 Health Checks

Config server:

```
http://localhost:19071/state/v1/health
```

Query node:

```
http://localhost:8080/state/v1/health
```

Feed node:

```
http://localhost:8081/state/v1/health
```

---

# 💾 Persistent Storage

Docker volumes used:

```
vespa-config-data
vespa-content-data
```

Data persists across container restarts.

---

# 🔄 Stop Cluster

```bash
docker compose down
```

Remove volumes (optional reset):

```bash
docker compose down -v
```

---

# 🧠 How It Works

1. Config server stores application
2. All nodes fetch configuration automatically
3. Content node creates index
4. Feed node accepts documents
5. Query node serves search requests

---

# 🌐 Endpoints Summary

| Service | URL                                                                    |
| ------- | ---------------------------------------------------------------------- |
| Query   | [http://localhost:8080/search](http://localhost:8080/search)           |
| Feed    | [http://localhost:8081/document/v1](http://localhost:8081/document/v1) |
| Config  | [http://localhost:19071](http://localhost:19071)                       |
| Health  | /state/v1/health                                                       |

---

# ✅ Result

You now have a:

* Production-structured Vespa cluster
* Separate query and feed endpoints
* Persistent storage
* Clean deployment workflow
* Fully functional local search cluster


