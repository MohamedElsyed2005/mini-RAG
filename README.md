# mini-RAG

# FastAPI Application

A simple FastAPI application with a versioned API router and environment-based application configuration.

## Project Structure

```text
.
├── main.py
├── routes/
│   └── base.py
├── .env
└── README.md
````

### `main.py`

The main entry point of the application.

It:

* Loads environment variables from `.env`.
* Creates the FastAPI application.
* Registers the API routes from `routes/base.py`.

### `routes/base.py`

Contains the base API router.

The router is available under the `/api/v1` prefix and provides a welcome endpoint:

```text
GET /api/v1/
```

The endpoint returns the application name and version from the environment variables.

## Environment Variables

Create a `.env` file in the project root:

```env
APP_NAME=My FastAPI App
APP_VERSION=1.0.0
```

## Installation

Install the required dependencies:

```bash
pip install fastapi uvicorn python-dotenv
```

## Run the Application

Start the development server with:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://localhost:8000
```

Open the API endpoint:

```text
http://localhost:8000/api/v1/
```

## Example Response

```json
{
    "app_name": "My FastAPI App",
    "app_version": "1.0.0"
}
```

## API Documentation

FastAPI automatically provides interactive API documentation:

```text
http://localhost:8000/docs
```

and alternative documentation:

```text
http://localhost:8000/redoc
```
