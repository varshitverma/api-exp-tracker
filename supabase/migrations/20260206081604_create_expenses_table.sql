-- Create Expenses table..
CREATE TABLE IF NOT EXISTS expenses (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    date TIMESTAMP NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- indexing
CREATE INDEX IF NOT EXISTS idx_expenses_date ON expenses(date);
CREATE INDEX IF NOT EXISTS idx_expenses_category ON expenses(category);
