# Expense Tracker - Setup Guide

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/varshitverma/api-exp-tracker.git
cd backend
```

### 2. Generate & Collect API Keys (IMPORTANT - Do This First!)

Before proceeding with setup, you need to generate two API keys:

#### A. Supabase API Keys

1. Go to [Supabase](https://supabase.com)
2. Create a new project or use existing one
3. Go to **Settings** → **API**
4. Copy these values:
   - **Project URL** - This is your `SUPABASE_URL`
   - **Service Role Secret** - This is your `SUPABASE_KEY`

#### B. ExchangeRate API Key

1. Go to [ExchangeRate-API](https://www.exchangerate-api.com)
2. Sign up for a free account
3. Copy your **API Key**
4. This will be part of your `EXCHANGE_RATE_API_URL`

### 3. Create a `.env` file

Create a `.env` file in the backend directory and add your API keys:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_secret_key
EXCHANGE_RATE_API_URL=https://v6.exchangerate-api.com/v6/YOUR_EXCHANGERATE_API_KEY/latest
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Supabase Setup & Database Migrations

#### Login to Supabase

```bash
npx supabase login
# Please login with your Supabase account
```

#### Link your Supabase Project

```bash
npx supabase link
# Select the project you created on Supabase for this app
```

#### Create Migration (if not already created)

```bash
npx supabase migration new create_expenses_table
```

#### Push Migrations to Database

```bash
npx supabase db push
# This will push the migration to your Supabase project and create the expenses table in your database
```

#### Apply Migrations

```bash
npx supabase migration up
```

#### Reset Database (Optional - use if you need to start fresh)

```bash
npx supabase db reset --linked
# This will reset your database and run all migrations again
# Use this if you want to start fresh with the database in case of any issues
# Then run all commands above again to set up the database
```

### 6. Start the Server

```bash
python -m uvicorn main:app --reload
```

Server runs on: `http://127.0.0.1:8000`

### 7. Access API Documentation

Once the server is running, you can view interactive API documentation:

- **Swagger UI (Interactive):** [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)
  - Best for testing endpoints directly
  - Try out requests and see responses
- **ReDoc (Beautiful Docs):** [http://127.0.0.1:8000/api/redoc](http://127.0.0.1:8000/api/redoc)
  - Clean, organized documentation
  - Great for reading API specifications

- **OpenAPI Schema (JSON):** [http://127.0.0.1:8000/api/openapi.json](http://127.0.0.1:8000/api/openapi.json)
  - Raw OpenAPI specification
  - For programmatic use & third-party tools

### 8. Update Requirements

After installing new packages, update requirements file:

```bash
pip freeze > requirements.txt
```

---

## API Endpoints

### Add Expense

**POST** `/expenses`

```json
{
  "amount": 50.0,
  "category": "food",
  "description": "lunch",
  "date": "2026-02-04T12:00:00",
  "payment_method": "card"
}
```

### Get All Expenses

**GET** `/expenses`

### Get Specific Expense

**GET** `/expenses/{id}`

### Update Expense

**PUT** `/expenses/{id}`

```json
{
  "amount": 75.0,
  "category": "food",
  "description": "dinner",
  "date": "2026-02-04T12:00:00",
  "payment_method": "card"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Expense updated",
  "data": {
    "id": 1,
    "amount": 75.0,
    "category": "food",
    "description": "dinner",
    "date": "2026-02-04T12:00:00",
    "payment_method": "card"
  }
}
```

### Convert Expenses to Another Currency

**GET** `/expenses/convert/{target_currency}`

Converts all user expenses from INR to a target currency using real-time exchange rates.

**Example Response:**

```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "amount": 100,
      "original_amount": 100,
      "original_currency": "INR",
      "converted_amount": 1.11,
      "target_currency": "USD",
      "category": "food",
      "description": "lunch"
    }
  ],
  "total_in_target_currency": 111.5,
  "exchange_rate": 0.0111,
  "target_currency": "USD",
  "base_currency": "INR"
}
```

### Delete Expense

**DELETE** `/expenses/{id}`

Deletes an expense by ID.

**Response:**
```json
{
  "success": true,
  "message": "Expense deleted"
}
```

---

## 3rd Party APIs

### Exchange Rate API

**Purpose:** Convert user expenses to different currencies when traveling.

**Provider:** [ExchangeRate-API](https://www.exchangerate-api.com)

**Setup:** API key is configured in `.env` file (see Step 3 above)

**Feature Description:**
When a user selects a country/currency from the UI:

1. Backend receives the target currency code (e.g., `USD`, `EUR`, `GBP`)
2. Backend calls the Exchange Rate API to fetch current exchange rates from INR
3. All existing expenses are converted to the selected currency
4. User sees individual expenses and total expenses in the selected currency
5. This is helpful when traveling to another country to track spending in local currency

**Supported Currencies:** 160+ currencies including USD, EUR, GBP, JPY, INR, AED, and more.

---

## Database Schema

| Column         | Type        | Notes                        |
| -------------- | ----------- | ---------------------------- |
| id             | BIGINT      | Primary Key (auto-generated) |
| amount         | FLOAT       | Expense amount               |
| category       | VARCHAR(50) | Category name                |
| description    | TEXT        | Optional description         |
| date           | TIMESTAMP   | When expense occurred        |
| payment_method | VARCHAR(50) | cash, card, digital wallet   |
| created_at     | TIMESTAMP   | Auto-set on creation         |
| updated_at     | TIMESTAMP   | Auto-set on creation         |

--

## Folder Structure

```
backend/
├── app/
│   ├── model/
│   │   └── expense_model.py
│   └── routes/
│       ├── get_routes.py
│       └── post_routes.py
├── migrations/
│   └── 001_create_expenses_table.sql
├── main.py
├── setup_db.py
├── requirements.txt
└── .env
```

---

## 📦 Deployment Guide (EC2 + Nginx + FastAPI)

This guide covers deploying your Expense Tracker backend to AWS EC2 with Nginx reverse proxy.

### 🚀 1️⃣ EC2 Server Setup (Ubuntu)

#### Step 1: Launch EC2 Instance

- **OS:** Ubuntu 22.04
- **Instance type:** t3.small (recommended minimum 2GB RAM)

**Open Security Group Ports:**
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)

#### Step 2: Connect via SSH

```bash
ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP
```

#### Step 3: Update Server

```bash
sudo apt update && sudo apt upgrade -y
```

### 🐍 2️⃣ Backend Deployment (FastAPI + Gunicorn)

#### Step 1: Clone Repository

```bash
cd ~
git clone https://github.com/your-repo/backend.git
cd backend
```

#### Step 2: Install Python & Dependencies

```bash
# Install Python and venv
sudo apt install python3 python3-venv python3-pip -y

# Create virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install gunicorn

# Deactivate when done
deactivate
```

#### Step 3: Create `.env` File

```bash
nano .env
```

Add your API keys:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_secret_key
EXCHANGE_RATE_API_URL=https://v6.exchangerate-api.com/v6/YOUR_API_KEY/latest
```

Save with `Ctrl+X` → `Y` → `Enter`

#### Step 4: Create systemd Service

```bash
sudo nano /etc/systemd/system/fastapi.service
```

Paste the following:

```ini
[Unit]
Description=FastAPI App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/backend
ExecStart=/home/ubuntu/backend/env/bin/gunicorn \
          -k uvicorn.workers.UvicornWorker \
          main:app \
          --bind 127.0.0.1:8000 \
          --workers 2
Restart=always

[Install]
WantedBy=multi-user.target
```

Save with `Ctrl+X` → `Y` → `Enter`

#### Step 5: Enable & Start Backend Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable fastapi
sudo systemctl start fastapi

# Check status
sudo systemctl status fastapi
```

### 🌐 3️⃣ Install & Configure Nginx

#### Step 1: Install Nginx

```bash
sudo apt install nginx -y
```

#### Step 2: Configure Nginx

```bash
sudo nano /etc/nginx/sites-available/default
```

Replace with:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location / {
        root /var/www/html;
        index index.html;
        try_files $uri /index.html;
    }
}
```

#### Step 3: Test & Restart Nginx

```bash
# Test configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx

# Enable on startup
sudo systemctl enable nginx
```

### 🔒 4️⃣ SSL Certificate (HTTPS with Let's Encrypt)

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Generate certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Auto-renewal enabled by default
```

### ✅ Verification

- **API:** `http://yourdomain.com/api/v1/expenses`
- **Docs:** `http://yourdomain.com/api/docs`
- **Check logs:** `sudo journalctl -u fastapi -f`
