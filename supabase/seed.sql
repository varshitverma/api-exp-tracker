INSERT INTO expenses (amount, category, description, date, payment_method)
VALUES
(1200.50, 'Food', 'Swiggy dinner order', '2026-01-05 19:30:00', 'UPI'),
(450.00, 'Transport', 'Uber ride to office', '2026-01-06 09:15:00', 'Credit Card'),
(2999.99, 'Shopping', 'Amazon headphones purchase', '2026-01-07 21:45:00', 'Debit Card'),
(800.00, 'Entertainment', 'Movie tickets - IMAX', '2026-01-08 18:00:00', 'UPI'),
(15000.00, 'Rent', 'January house rent', '2026-01-01 10:00:00', 'Bank Transfer'),
(350.75, 'Food', 'Cafe coffee & snacks', '2026-01-09 17:20:00', 'Cash'),
(2200.00, 'Utilities', 'Electricity bill', '2026-01-10 12:30:00', 'UPI'),
(999.00, 'Subscriptions', 'Spotify yearly subscription', '2026-01-11 14:00:00', 'Credit Card'),
(540.00, 'Transport', 'Petrol refill', '2026-01-12 08:40:00', 'Cash'),
(4200.00, 'Shopping', 'Zara clothing purchase', '2026-01-13 16:15:00', 'Debit Card'),
(650.00, 'Food', 'Dominos pizza night', '2026-01-14 20:10:00', 'UPI'),
(12000.00, 'EMI', 'Laptop EMI installment', '2026-01-15 11:00:00', 'Credit Card'),
(1800.00, 'Health', 'Doctor consultation & medicines', '2026-01-16 13:25:00', 'UPI'),
(750.00, 'Entertainment', 'Steam game purchase', '2026-01-17 22:45:00', 'Debit Card'),
(300.00, 'Miscellaneous', 'Stationery items', '2026-01-18 15:30:00', 'Cash');
-- These are sample seed data for the EXPENSES table. You can modify or add more entries as needed.
-- to pre populate the expenses table with this data, simply run this SQL script against your Supabase database.
