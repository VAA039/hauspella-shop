# HAUSPELLA Shop

<p align="center">
  <img src="https://img.shields.io/badge/HAUSPELLA-Shop-2D7FF9?style=for-the-badge" alt="HAUSPELLA Shop">
</p>

<p align="center">
  <strong>Modern e-commerce platform built with Django</strong><br>
  Part of the <strong>HAUSPELLA ERP</strong> ecosystem.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django)
![Status](https://img.shields.io/badge/Status-In_Development-orange)
![Database](https://img.shields.io/badge/Database-SQLite-blue)
![Platform](https://img.shields.io/badge/Platform-Web-success)

</p>

---

# About

**HAUSPELLA Shop** is an e-commerce application built with **Python** and **Django**.

The project is part of the **HAUSPELLA ERP** ecosystem and is designed to become a complete online store with integrated product management, order processing and marketplace support.

The current version focuses on building a flexible and scalable product catalog architecture.

---

# Features

## Product Catalog

- Product categories
- Product management
- Product pricing
- Product statuses

## Product Media

- Multiple product images
- PDF documents
- Multiple videos for every product
- Multiple publishing platforms for each video

Supported video platforms:

- VK Video
- Rutube
- Dzen Video
- Platforma
- Odnoklassniki Video
- Kinescope
- Wibes
- Rambler
- Coub
- Twitch

## Administration

- Django Admin
- Inline editing
- Automatic file cleanup
- PDF validation
- Ordered media collections

---

# Project Architecture

```text
HAUSPELLA Shop

├── Catalog
│   ├── Categories
│   ├── Products
│   ├── Images
│   ├── Documents
│   └── Videos
│       └── Video Sources
│
├── Cart
│
├── Orders
│
└── Pages
```

---

# Project Structure

```text
apps/
├── catalog/
│   ├── admin.py
│   ├── migrations/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── views.py
│
├── cart/
│
├── orders/
│
├── pages/
│
└── core/
```

---

# Technology Stack

- Python 3.13
- Django 5.2
- SQLite
- HTML5
- CSS3

Future versions will include:

- PostgreSQL
- Redis
- Celery
- Docker

---

# Installation

Clone repository

```bash
git clone https://github.com/VAA039/hauspella-shop.git
cd hauspella-shop
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Apply migrations

```bash
python manage.py migrate
```

Create administrator

```bash
python manage.py createsuperuser
```

Run development server

```bash
python manage.py runserver
```

Open in browser

```
http://127.0.0.1:8000/
```

Admin panel

```
http://127.0.0.1:8000/admin/
```

---

# Development Roadmap

## Version 1.0

- [x] Product catalog
- [x] Categories
- [x] Product images
- [x] Product documents
- [x] Product videos
- [x] Multiple video platforms
- [x] Django administration panel

## Version 1.1

- [ ] Shopping cart
- [ ] Checkout
- [ ] Order management
- [ ] Email notifications

## Version 1.2

- [ ] User accounts
- [ ] Wishlist
- [ ] Product search
- [ ] Product filtering

## Version 2.0

- [ ] Payment gateway
- [ ] Marketplace synchronization
- [ ] HAUSPELLA ERP integration
- [ ] Analytics dashboard

---

# Project Goals

The long-term goal is to create a complete ecosystem for marketplace sellers and online businesses, including:

- Product Management
- Inventory Management
- CRM
- ERP
- Marketplace Integration
- Order Management
- Financial Analytics

---

# Screenshots

### Main Page

> Screenshot will be added later.

### Product Page

> Screenshot will be added later.

### Django Administration

> Screenshot will be added later.

---

# License

This project is currently under active development.

All rights reserved.

---

# Author

**Alexander Volkov**

Python & Django Developer

GitHub: https://github.com/VAA039

---

<p align="center">

Made with ❤️ using Django

</p>