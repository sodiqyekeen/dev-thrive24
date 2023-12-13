
DROP TABLE IF EXISTS transact;

PRAGMA foreign_keys = ON;


-- Transaction table
CREATE TABLE transact(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_reference VARCHAR(225),
    status_payment VARCHAR(10) UNIQUE NOT NULL,
    progress_level VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
