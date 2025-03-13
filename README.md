# Fresh & Ready

## Database

To setup postgres, pgadmin & keycloak, create .env file:
```
POSTGRES_DB_NAME_FNR = 'fnr'
POSTGRES_DB_NAME_KC = 'keycloak'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'password'
PGADMIN_EMAIL = 'admin@example.com'
PGADMIN_PASSWORD = 'password'
KC_ADMIN = 'admin'
KC_ADMIN_PASSWORD ='password' 
```
And run `docker compose up -d`


## Backend

To setup backend create .env file or add to it:
```
SECRET_KEY='SUPER_SECRET_KEY'
DATABASE_URL='postgresql://username:password@your-db-url:5432/db-name'
```
