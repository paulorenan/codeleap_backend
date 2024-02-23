# CodeLeap BackEnd

Brief description of your project.

## Prerequisites

Before you begin, ensure you have installed:

- Python (version X.X)
- Django (version X.X)
- Django REST Framework (version X.X)

## Installation

1. Clone the repository:

```
git clone https://github.com/paulorenan/codeleap_backend.git
```


2. Navigate to the project directory:


```
cd codeleap_backend
```

3. Run database migrations:

```
python manage.py migrate
```


## Running the development server

To start the development server, run the following command:
```
python manage.py runserver
```


The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

- `GET /api/careers/`: Lists all careers.
- `POST /api/careers/`: Creates a new career.
- `GET /api/careers/<id>/`: Returns details of a specific career.
- `PATCH /api/careers/<id>/`: Updates specific fields of a career.
- `DELETE /api/careers/<id>/`: Deletes a career.






