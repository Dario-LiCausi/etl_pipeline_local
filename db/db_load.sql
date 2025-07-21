


CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Drink VARCHAR(100),
    Qty INT,
    Price FLOAT,
    Branch VARCHAR(100),
    Payment_Type VARCHAR(50),
    Date_Time DATETIME
);