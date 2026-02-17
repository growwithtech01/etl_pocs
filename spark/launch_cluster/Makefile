SPARK_CONTAINER=spark-master
SPARK_HOME=/opt/spark
WORK_DIR=/opt/spark/work
JOB_DIR=$(WORK_DIR)/jobs

APP ?= employees_job.py
MASTER ?= spark://spark-master:7077

run:
	docker exec -it $(SPARK_CONTAINER) \
	$(SPARK_HOME)/bin/spark-submit \
	--master $(MASTER) \
	$(JOB_DIR)/$(APP)

ps:
	docker ps

logs:
	docker logs $(SPARK_CONTAINER)
