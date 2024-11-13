#!/usr/bin/env python

from psycopg_pool import ConnectionPool


postgres_pool = ConnectionPool("host=localhost dbname=postgres user=postgres password=postgres")
conn = postgres_pool.getconn()
conn.autocommit = False
conn.execute(query="ALTER ROLE postgres WITH LOGIN")
conn.commit()
