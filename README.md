# Crypto Tracker API

This is a test project for managing cryptocurrencies, built using Django, PostgreSQL, ~~Celery, Redis, and RabbitMQ~~. The project also utilizes my custom Bitget API Python library available at [bitget-api-python](https://github.com/airyou-code/bitget-api-python).

## Overview

Crypto Tracker API provides a set of endpoints for creating, retrieving, updating, and deleting cryptocurrency records. A custom endpoint is available to refresh metadata for all stored cryptocurrencies,
~~and a Celery task periodically updates the information for the specified currencies in the system.~~

## Technologies Used

- **Django** – The web framework used to build the API.
- **PostgreSQL** – Database.
- ~~**Celery** – Asynchronous task queue used for background processes.~~
- ~~**Redis** – Message broker for Celery.~~
- ~~**RabbitMQ** – Alternative message broker used in some configurations.~~
- **bitget-api-python** – My Custom Bitget API Python library, available at [https://github.com/airyou-code/bitget-api-python](https://github.com/airyou-code/bitget-api-python).

## Try the Application

1. **Registration & Login:**  
   Visit [https://cryptotracker.prompthub.study/](https://cryptotracker.prompthub.study/) to register a new account and log in.

2. **Test the API via Swagger:**  
   After logging in, you can try the API using Swagger at [https://cryptotracker.prompthub.study/api/v1/](https://cryptotracker.prompthub.study/api/v1/).

3. **Admin Interface:**  
   To view and manage cryptocurrency data, access the admin interface at [https://cryptotracker.prompthub.study/admin/cryptotracker/cryptocurrency/](https://cryptotracker.prompthub.study/admin/cryptotracker/cryptocurrency/).


## Endpoints Overview

The API conforms to the OpenAPI 3.0.3 specification. Below is a brief description of the main endpoints:

### `/api/v1/cryptocurrencies/`

- **GET**  
  Returns a list of all cryptocurrencies.  
  *Description*: Provides CRUD operations for cryptocurrencies.  
  *Example*: An array of cryptocurrency objects.

- **POST**  
  Creates a new cryptocurrency record.  
  *Description*: Records are created and enriched using data from the Bitget API library.

### `/api/v1/cryptocurrencies/{symbol}/`

- **GET**  
  Retrieves detailed information of a cryptocurrency identified by its symbol.

- **PUT / PATCH**  
  Updates an existing cryptocurrency record (fully or partially).  
  *Description*: Allows updating cryptocurrency data, including refreshing metadata.

- **DELETE**  
  Deletes a cryptocurrency record.

### `/api/v1/cryptocurrencies/refresh/`

- **POST**  
  Custom endpoint for refreshing the metadata of all cryptocurrencies.  
  *Description*: Triggers an update process (which is integrated with Celery) to refresh all stored currency data.

## ~~Background Tasks~~

~~A Celery task is set up to periodically update the metadata of the cryptocurrencies stored in the system, ensuring that the information remains current.~~

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/airyou-code/crypto-tracker.git
   cd your-repo-name
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file with the necessary settings for Django, PostgreSQL
   ```bash
   # .env.example
   ALLOWED_HOSTS="*"
   CSRF_TRUSTED_ORIGINS="https://cryptotracker.prompthub.study"
   CORS_ORIGIN_WHITELIST="https://cryptotracker.prompthub.study"
   CORS_ALLOWED_ORIGINS="https://cryptotracker.prompthub.study"
   BITGET_API_KEY=
   BITGET_API_SECRET=
   BITGET_API_PASSPHRASE=

   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_DB=
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   DATABASE_URL=postgresql://user:pass@db:5432/db_name
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Server:**
   ```bash
   python manage.py runserver
   ```

~~6. **Start the Celery Worker:**~~
   ```bash
   celery -A your_project_name worker -l info
   ```

~~7. **Start Celery Beat (if using scheduled tasks):**~~
   ```bash
   celery -A your_project_name beat -l info
   ```

## License

This project is open source and available under the [MIT License](LICENSE).
