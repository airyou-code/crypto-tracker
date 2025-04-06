# Crypto Tracker API

This is a test project for managing cryptocurrencies, built using Django, PostgreSQL, ~~Celery, Redis, and RabbitMQ~~. The project also utilizes my custom Bitget API Python library available at [bitget-api-python](https://github.com/airyou-code/bitget-api-python).

## Overview

Crypto Tracker API provides a set of endpoints for creating, retrieving, updating, and deleting cryptocurrency records. A custom endpoint is available to refresh metadata for all stored cryptocurrencies,
~~and a Celery task periodically updates the information for the specified currencies in the system.~~

## Technologies Used

- **Django** – The web framework used to build the API.
- **PostgreSQL** – Database for persistent data storage.
- ~~**Celery** – Asynchronous task queue used for background processes.~~
- ~~**Redis** – Message broker for Celery.~~
- ~~**RabbitMQ** – Alternative message broker used in some configurations.~~
- **bitget-api-python** – Custom Bitget API Python library, available at [https://github.com/airyou-code/bitget-api-python](https://github.com/airyou-code/bitget-api-python).

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
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   Create a `.env` file with the necessary settings for Django, PostgreSQL, Redis, and RabbitMQ.

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
