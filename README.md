# 💱 Currency Converter API

# Backend API project built with FastAPI.

A simple currency conversion API built with **FastAPI**.
This service allows users to convert currencies from one currency to another and manage stored exchange rates using a JSON file as a temporary storage space.

---

#  Project Overview

This project is a **Backend API service** for currency conversion.

Users can:

* Convert an amount from one currency to another
* Add new currencies
* Store the exchange rates in a JSON file and use them for conversion.

The project is built using **FastAPI** because of its high performance and ease of building APIs.

---

#  Technologies Used

* Python
* FastAPI
* Uvicorn
* Docker
* JSON file storage

---

#  Project Structure

```
currency-api/
│
├── app.py
│
├── routes/
│   └── currency_routes.py
│
├── services/
│   └── converter.py
│
├── models/
│   └── schemas.py
│
├── data/
│   └── rates.json
|
├── Dockerfile
└── README.md
```

---

#  Running the Project Locally

## 1. Install Requirements

```bash
pip install fastapi uvicorn
```

## 2. Run the Server

```bash
uvicorn app:app --reload
```

After starting the server, open:

```
http://localhost:8000/docs

or

http://127.0.0.1:8000/docs
```

This will display the **FastAPI Swagger UI**, which allows you to test the API directly from the browser.

---

#  API Usage

## Convert Currency

Endpoint

```
GET /currency/convert
```

Parameters

| Parameter     | Example |
| ------------- | ------- |
| from_currency | USD     |
| to_currency   | EUR     |
| amount        | 100     |

Example request

```
/currency/convert?from_currency=USD&to_currency=EUR&amount=100
```

---

## Add a New Currency

Endpoint

```
POST /currency/add
```

Example request body

```json
{
  "currency": "SAR",
  "rate": 3.75
}
```

---


---

#  Running the Project with Docker

## 1. Build the Image

```bash
docker build -t currency-api .

or

docker buildx build --load -t currency-api .
```

## 2. Run the Container

```bash
docker run -p 8000:8000 currency-api```

Then open in your browser:

```
http://127.0.0.1:8000/docs


##  Using Environmental variables

```bash
docker run --env-file .env -p 9000:9000 currency-api

Then open in your browser:

http://localhost:9000/docs
```

---

#  Notes

* Exchange rates are stored in the `data/rates.json` file.
* The file can be edited to add or modify currency rates and use them.
* The project can be extended in the future by using a database and  Update existing currency rates
* Delete currencies.


---


