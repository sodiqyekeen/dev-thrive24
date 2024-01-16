
DROP TABLE IF EXISTS faculty;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS transact;
DROP TABLE IF EXISTS rating;

-- Faculty table
CREATE TABLE faculty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Department table
CREATE TABLE department (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    faculty_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (faculty_id) REFERENCES faculty(id) ON DELETE CASCADE
);

CREATE TABLE student (
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

-- Transaction table
CREATE TABLE transact(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_reference VARCHAR(225),
    payment_status VARCHAR(10) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rating (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tutor_id VARCHAR(255) NOT NULL,
    user_id VARCHAR(255) NOT NULL,
    rating VARCHAR(255) NOT NULL,
    review VARCHAR(255) NOT NULL
);

CREATE TABLE skills(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Skill_Name VARCHAR(255) NOT NULL, 
    Description VARCHAR(255) NOT NULL
);

CREATE TABLE Skill_Exchange(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student1_ID NOT NULL,
    student2_ID NOT NULL,
    skill_ID NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    Status VARCHAR(255) NOT NULL,
    FOREIGN KEY (student1_ID) REFERENCES student(id) ON DELETE SET NULL,
    FOREIGN KEY (student2_Id) REFERENCES student(id) ON DELETE SET NULL,
    FOREIGN KEY (skill_ID) REFERENCES skills(id) ON DELETE SET NULL
);


CREATE TABLE User_Skill (
   id iINTEGER PRIMARY KEY AUTOINCREMENT,
   Proficiency_level VARCHAR(250),
   student_ID NOT NULL,
   Skill_ID NOT NULL,
   FOREIGN KEY (student_ID) REFERENCES student(id) ON DELETE SET NULL,
   FOREIGN KEY (Skill_ID) REFERENCES kills(id) ON DELETE SET NULL,
);