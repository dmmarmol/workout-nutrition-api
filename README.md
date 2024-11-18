# Container

Initiate docker containers
```sh
make start
```

### Connect pgAdmin to PostgreSQL:
- Open [http://localhost:6001](http://localhost:6001)
- Login using the values from `/.env` `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`
- After logging in, you’ll need to create a new connection to your PostgreSQL container.
- In pgAdmin, click on Servers → Add new Server.
- In the General tab, give it a name (e.g., Nutrition DB).
- Under the Connection tab:
- Host: `nutrition-api-db` (This is the service name of your PostgreSQL container, which acts like a hostname within the custom Docker network).
- Port: 5432 (default PostgreSQL port).
- Maintenance database: postgres (default database).
- Username: The value of ${DB_USER} from your .env file.
- Password: The value of ${DB_PASSWORD} from your .env file.
- Optional: check "Save Password?"
