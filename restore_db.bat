psql -U postgres -c "drop database d64qjg45ounupa;"
psql -U postgres -c "create database d64qjg45ounupa;"
psql -U postgres -c "grant all privileges on database d64qjg45ounupa to oeczildqfxopfl;"
pg_restore -U postgres -d d64qjg45ounupa -1 8c32ccda-1247-4b82-b85e-bfb39d41ab77
