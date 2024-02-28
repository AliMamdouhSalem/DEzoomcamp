jupyter nvconvert --to=script *name*

jupyter notebook

pgcli -h localhost -p 5432 -u root -d ny_taxi

docker run -it   -e POSTGRES_USER="root"   -e POSTGRES_PASSWORD="root"   -e POSTGRES_DB="ny_taxi"   -v "/workspaces/DEzoomcamp/docker-sql/nytaxi_postgres:/var/lib/postgresql/data" -p 5432:5432 --network=pg-network --name pg-database   postgres:13

docker run -it \
   -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
   -e PGADMIN_DEFAULT_PASSWORD="root" \
   -p 8080:80 \
   --network=pg-network \
   --name pgadmin-2 \
   dpage/pgadmin4

   wget *url*

   docker build -t taxi_ingest:v001 .

    URL= "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

   docker run -it --network=pg-network taxi_ingest:v001 --user=root --password=root --host=pg-database --port=5432 --db=ny_taxi --table_name=yellow_taxi_trips --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz" 


terraform fmt

terraform init

terraform plan

terraform apply 

terraform destroy

