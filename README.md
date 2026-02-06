# Expense Tracker - Setup Guide

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/varshitverma/api-exp-tracker.git
cd backend / folder_name
```

### 2. Create a `.env` file

Copy and fill in your Supabase credentials:

```env
SUPABASE_URL=your_supabase_url // This is Project URL in Supabase project
SUPABASE_SECRET_KEY=your_supabase_secret_key // This is Secret  Key
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Supabase Setup & Database Migrations

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

### 5. Start the Server

```bash
python -m uvicorn main:app --reload
```

Server runs on: `http://127.0.0.1:8000`

### 6. Update Requirements

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
