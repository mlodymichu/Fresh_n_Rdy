# ProjectZesolovvy

## Database

To setup postgres db create .env file:
```
POSTGRES_DB = 'freshready'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
PGADMIN_EMAIL: 'admin@example.com'
PGADMIN_PASSWORD: 'admin'
```
And run `docker compose up -d`


## Backend

To setup backend create .env file or add to it:
```
SECRET_KEY='SUPER_SECRET_KEY'
DATABASE_URL='postgresql://username:password@your-db-url:5432/db-name'
```
