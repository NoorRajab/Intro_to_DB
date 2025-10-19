-- task_5.sql
-- Script to insert a single row into the CUSTOMERS table.

-- Select the database
USE ALX_BOOK_STORE;

-- Insert the specified customer data
INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');