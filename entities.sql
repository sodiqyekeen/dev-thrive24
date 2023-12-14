
-- DROP TABLE IF EXISTS tutors;
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS user;

PRAGMA foreign_keys = ON;

-- Faculty table
CREATE TABLE faculty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    faculty_name VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Department table
CREATE TABLE department (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name VARCHAR(255) UNIQUE NOT NULL,
    faculty_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES faculty(id) ON DELETE CASCADE
);

-- Users table
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matric_no VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    department_id INT NOT NULL,
    level INT NOT NULL,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES department(id) ON DELETE SET NULL
);

-- PRAGMA foreign_keys = ON;


-- -- tutors table
-- CREATE TABLE tutors (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     first_name VARCHAR(255) NOT NULL,
--     last_name VARCHAR(255) NOT NULL,
--     skills VARCHAR(255) UNIQUE NOT NULL,
--     experience VARCHAR(255) NOT NULL,
--     availability VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL,
--     hourly_rate VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
--     -- FOREIGN KEY (department_id) REFERENCES department(id) ON DELETE SET NULL
-- );