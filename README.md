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
