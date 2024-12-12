# Django REST API with Enhanced Security

This project provides a Django-based REST API with enhanced security measures including token-based authentication and validation. It allows users to perform CRUD operations on `Todo` items and convert images to PDFs securely.

## Features

- **Token Authentication**: Ensures only authenticated users can access the API.
- **CRUD Operations**:
  - Fetch `Todo` items (`GET`)
  - Add new `Todo` items (`POST`)
  - Update existing `Todo` items (`PUT`)
  - Delete `Todo` items (`DELETE`)
- **File Conversion**: Convert uploaded images to PDF files.
- **Validation**: Data validation for all endpoints with appropriate error handling.

## Requirements

- Python 3.6+
- Django 3.2+
- Django REST Framework (DRF)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

## Endpoints and Usage

### 1. Fetch Data (GET `/api/showdata`)
Fetches all `Todo` items or items for a specific `uid`.

#### Headers:
- `Authorization: Token <your_token>`

#### Example Request:
```bash
curl -X GET http://127.0.0.1:8000/api/showdata -H "Authorization: Token <your_token>"
```

### 2. Add Data (POST `/api/adddata`)
Adds a new `Todo` item.

#### Headers:
- `Authorization: Token <your_token>`
- `Content-Type: application/json`

#### Example Request:
```bash
curl -X POST http://127.0.0.1:8000/api/adddata \
     -H "Authorization: Token <your_token>" \
     -H "Content-Type: application/json" \
     -d '{"uid": "123", "task": "Buy groceries"}'
```

### 3. Update Data (PUT `/api/updatedata`)
Updates an existing `Todo` item by `uid`.

#### Headers:
- `Authorization: Token <your_token>`
- `Content-Type: application/json`

#### Example Request:
```bash
curl -X PUT http://127.0.0.1:8000/api/updatedata \
     -H "Authorization: Token <your_token>" \
     -H "Content-Type: application/json" \
     -d '{"uid": "123", "task": "Buy fruits"}'
```

### 4. Delete Data (DELETE `/api/deldata`)
Deletes a `Todo` item by `uid`.

#### Headers:
- `Authorization: Token <your_token>`

#### Example Request:
```bash
curl -X DELETE http://127.0.0.1:8000/api/deldata?uid=123 \
     -H "Authorization: Token <your_token>"
```

### 5. Convert Image to PDF (POST `/api/convert_image_to_pdf`)
Uploads an image and converts it to a PDF file.

#### Headers:
- `Authorization: Token <your_token>`

#### Example Request:
```bash
curl -X POST http://127.0.0.1:8000/api/convert_image_to_pdf \
     -H "Authorization: Token <your_token>" \
     -F "image=@/path/to/image.jpg"
```

## Security

- **Authentication**: All endpoints require a valid token in the `Authorization` header.
- **Data Validation**: Requests are validated, and invalid data is rejected with appropriate error messages.

## Testing

Run tests to ensure the API functions correctly:
```bash
python manage.py test
```

## Notes

- Replace `<your_token>` with a valid token obtained from the `Token` authentication system.
- Ensure all API requests are sent over HTTPS in a production environment.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for suggestions and improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

