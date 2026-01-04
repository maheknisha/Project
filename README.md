E-Commerce Backend API (Python & MySQL)
This project implements a backend system using Python (Flask) and MySQL.
It focuses on database design, RESTful APIs, pagination, filtering, error handling, and SQL queries.

#Technologies Used
Python
Flask
MySQL
REST API

# Database Design
The database contains the following tables:
1. Users
Stores user information,Email is unique
2. Products
Stores product details,Includes stock management
3. Orders
Stores order details,Linked to users
4. Order_Items
Stores products within each order, Links orders and products

# Relationships
One user → many orders,One order → many order items,One product → many order items

# API Development 
CRUD APIs are implemented for:Users,Products,Orders

# Features
Create, Read, Update, Delete operations, Stock updates when orders are placed
# Join-based queries for order summaries

# Pagination & Filtering
Endpoint
GET /orders?status=PAID&page=1&limit=10

# Description

Filters orders by status

Supports pagination using page and limit parameters

# Error Handling
The API handles:
Duplicate email entries
Invalid stock values
Missing required fields
Foreign key constraint violations
Appropriate error messages are returned in JSON format.

# SQL Queries
Top 5 users with highest total spending
Uses joins and aggregation
List all out-of-stock products, Fetches products with stock = 0, Fetch all orders with item count and total amount,Uses joins, COUNT(), and SUM()

# Setup Instructions
Install required libraries:
--pip install flask flask-mysqldb
Create a MySQL database and tables.
Update database credentials in app.py.
Run the application:
--python app.py

Submission Note
Section 1 (Python & DSA) solutions are included in the code files and comments.
This README focuses on Section 2 – Database & API tasks as per instructions.

Section 1 (Python & DSA) solutions are included in the code files and comments.
This README focuses on Section 2 – Database & API tasks as per instructions.
