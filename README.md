

---

# Spam API

## Project Description

**Spam API** is a web application that allows users to register, log in, manage contacts, mark spam, and search for users and contacts. This application uses Django for the backend and offers a set of RESTful APIs for interacting with the data.

---

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [API Documentation](#api-documentation)
   - [Register API](#register-api)
   - [Login API](#login-api)
   - [Contact List API](#contact-list-api)
   - [Mark Spam API](#mark-spam-api)
   - [Search By Name API](#search-by-name-api)
   - [Search By Phone API](#search-by-phone-api)
   - [Generate Random Data API](#generate-random-data-api)
3. [License](#license)
4. [Contributing](#contributing)
5. [Contact Information](#contact-information)

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/project-name.git
   cd project-name
   ```

2. **Set Up Virtual Environment**

   **On Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

---

## API Documentation

### Register API

- **Endpoint:** `/api/register/`
- **Method:** `POST`
- **Description:** Registers a new user by providing their details.
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "phone_number": "123-456-7890",
    "email": "john.doe@example.com",
    "password": "securepassword123"
  }
  ```
- **Response:**
  - **Success (201 Created):**
    ```json
    {
      "name": "John Doe",
      "phone_number": "123-456-7890",
      "email": "john.doe@example.com",
      "password": "securepassword123"
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "error": "Error message describing what went wrong"
    }
    ```

### Login API

- **Endpoint:** `/api/login/`
- **Method:** `POST`
- **Description:** Logs in a user and returns an authentication token.
- **Request Body:**
  ```json
  {
    "phone_number": "123-456-7890",
    "password": "securepassword123"
  }
  ```
- **Response:**
  - **Success (200 OK):**
    ```json
    {
      "token": "your_authentication_token_here"
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "error": "Invalid credentials"
    }
    ```
- **Headers:**
  - **Authorization:** Not required for login.

### Contact List API

- **Endpoint:** `/api/contacts/`
- **Method:** `GET`
- **Description:** Retrieves the list of contacts for the authenticated user.
- **Headers:**
  - **Authorization:** `Bearer <token>`
- **Response:**
  - **Success (200 OK):**
    ```json
    [
      {
        "name": "Jane Smith",
        "phone_number": "234-567-8901"
      },
      ...
    ]
    ```

### Mark Spam API

- **Endpoint:** `/api/spam/`
- **Method:** `POST`
- **Description:** Marks a phone number as spam for the authenticated user.
- **Request Body:**
  ```json
  {
    "phone_number": "234-567-8901"
  }
  ```
- **Headers:**
  - **Authorization:** `Bearer <token>`
- **Response:**
  - **Success (201 Created):**
    ```json
    {
      "message": "Spam marked successfully"
    }
    ```
  - **Conflict (200 OK):** (if already marked)
    ```json
    {
      "message": "Spam already marked"
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "error": "Phone number is required"
    }
    ```

### Search By Name API

- **Endpoint:** `/api/search-by-name/<query>/`
- **Method:** `GET`
- **Description:** Searches for users and contacts by name, prioritizing those whose names start with the search query.
- **Request Parameters:**
  - `query` (string): The search query string.
- **Headers:**
  - **Authorization:** `Bearer <token>`
- **Response:**
  - **Success (200 OK):**
    ```json
    [
      {
        "name": "John Doe",
        "phone_number": "123-456-7890",
        "is_spam": true
      },
      ...
    ]
    ```

### Search By Phone API

- **Endpoint:** `/api/search-by-phone/<number>/`
- **Method:** `GET`
- **Description:** Searches for users and contacts by phone number.
- **Request Parameters:**
  - `number` (string): The phone number to search for.
- **Headers:**
  - **Authorization:** `Bearer <token>`
- **Response:**
  - **Success (200 OK):**
    ```json
    [
      {
        "name": "John Doe",
        "phone_number": "123-456-7890",
        "is_spam": true
      },
      ...
    ]
    ```

### Generate Random Data API

- **Endpoint:** `/api/generate-random-data/`
- **Method:** `POST`
- **Description:** Generates and inserts random data into the `User`, `Contact`, and `Spam` tables.
- **Request Body:**
  ```json
  {
    "user_count": 5,
    "contact_per_user": 10,
    "spam_per_user": 5
  }
  ```
- **Headers:**
  - **Authorization:** `Bearer <token>` (for authenticated users, to ensure access)
- **Response:**
  - **Success (201 Created):**
    ```json
    {
      "message": "Random data generated successfully."
    }
    ```
  - **Error (400 Bad Request):**
    ```json
    {
      "error": "Error message describing what went wrong"
    }
    ```

---





- **Name:** Tarrun Krishna
- **Email:**tarrunkrishna387@gmail.com

---
