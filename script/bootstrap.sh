#!/bin/bash
set -e

psql -h localhost -v ON_ERROR_STOP=1 --username "flask" --dbname "flask" <<-EOSQL
   CREATE TABLE IF NOT EXISTS hello (id serial, value text);
EOSQL