# Small FastAPI Backend

This project is a minimal backend built using **FastAPI**. It contains two JSON endpoints and can be accessed through both a web browser and `curl`.

## Features

* Two GET endpoints that return JSON responses.
* Can be tested using a web browser.
* Can be tested using `curl`.
* Built with FastAPI.

## Project Structure

```text
.
├── main.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Server

Start the FastAPI server with:

```bash
uvicorn main:app --reload
```

The server will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### 1. Home Endpoint

**Request**

```http
GET /
```

Open in your browser:

```text
http://127.0.0.1:8000/
```

Or test using:

```bash
curl.exe http://127.0.0.1:8000/
```

**Sample Response**

```json
{
  "message": "Welcome to my first backend!",
  "status": "Server is running successfully"
}
```

---

### 2. Student Endpoint

**Request**

```http
GET /student
```

Open in your browser:

```text
http://127.0.0.1:8000/student
```

Or test using:

```bash
curl.exe http://127.0.0.1:8000/student
```

**Sample Response**

```json
{
  "name": "Muhammad Ahmad",
  "university": "COMSATS University Islamabad",
  "program": "BS Electronics and Computing",
  "semester": 4
}
```

## Interactive API Documentation

FastAPI automatically generates API documentation. Once the server is running, open:

```text
http://127.0.0.1:8000/docs
```

## Technologies Used

* Python
* FastAPI
* Uvicorn

## Author

Muhammad Ahmed
