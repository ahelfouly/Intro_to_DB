-- task_4.sql
USE alx_book_store;

SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE,
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'alx_book_store' 
    AND TABLE_NAME = 'Books';
