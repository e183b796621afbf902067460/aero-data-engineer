# Aero Data Engineer
Depends on: [framework](https://github.com/e183b796621afbf902067460/aero-data-engineer/tree/master/etl/framework).

---

Microservices written on FastAPI helps to automate Data Vault management. ETL written on Dagster helps to schedule our tasks.

# Configuration

First of all to configure the whole project correctly need to do next steps:

- Clone current repository:
```
https://github.com/e183b796621afbf902067460/aero-data-engineer.git
```

- Get into the project folder:
```
cd aero-data-engineer/
```

- Check environment variables in [.env](https://github.com/e183b796621afbf902067460/aero-data-engineer/blob/master/etl/.env) whether to change default values.

# Docker

- Run docker compose (`sudo`):
```
docker-compose up -d --build
```

- Check each container's ID and copy them:
```
docker ps
```

- Create Clickhouse schema:
```
docker exec -it <clickhouse-service ID> python3 app/orm/scripts/create.py
```

- Setup alembic for PostgreSQL schema:
```
sudo docker exec -it <postgres-service ID> bash -c 'cd app/orm; alembic upgrade head'
```

- And add additional data to Data Vault:
```
sudo docker exec -it <postgres-service ID> python3 app/views/__init__.py
```

---

After need to go to [launchpad](http://localhost:3000/locations/definitions.py%3Apit_users/jobs/pit_users/playground) for pit_users's DAG and click-on Launch Run on the lower right corner. 


So, after DAG's ran need to do next steps to see where our data are stored:
```
sudo docker exec -it <clickhouse ID> clickhouse-client
```

Set needed database:
```
use clickhouse;
```

And make basic query:
```
select * from pit_users;
```

# Exit
- To stop all running containers:
```
docker stop $(docker ps -a -q)
```
- And remove it all:
```
docker rm $(docker ps -a -q)
```

# Description
First of all need to say about [framework](https://github.com/e183b796621afbf902067460/aero-data-engineer/tree/master/etl/framework) — that's the kernel of whole ETL in this project and element of scalability. Framework and [Data Vault](https://github.com/e183b796621afbf902067460/aero-data-engineer/tree/master/microservices/postgres/app/orm) schema are strongly coupling, because if there is wrong naming nothing won't work. [tap](https://github.com/e183b796621afbf902067460/aero-data-engineer/blob/master/etl/framework/fabrics/pit_users/fabrics.py#L26) — [tap](https://github.com/e183b796621afbf902067460/aero-data-engineer/blob/master/microservices/postgres/app/views/__init__.py#L12). 

So, after we have extracted needed configuration from Data Vault we push it to the DF's task and MapReduce them. For instance, if we decided to add one more source with another endpoint and different JSON response, but it's still data about users, only what we should to do is to create a new handler, overload do() method to the right way and add it to right fabric. 

Otherwise, if we decided to parse another endpoints, for example it could be addresses/, just create a new fabric and write a new DAG for this fabric in the same way as previous one.
