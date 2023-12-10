-- Seed data for faculty table
-- Seed data for faculty table

INSERT INTO faculty (faculty_name) VALUES ('Computing and Information Technology');
INSERT INTO faculty (faculty_name) VALUES ('Engineering');
INSERT INTO faculty (faculty_name) VALUES ('Health and Life Sciences');
INSERT INTO faculty (faculty_name) VALUES ('Humanities and Social Sciences');

-- Seed data for department table

INSERT INTO department (department_name, faculty_id) VALUES ('Computer Science', 1);
INSERT INTO department (department_name, faculty_id) VALUES ('Information Technology', 1);
INSERT INTO department (department_name, faculty_id) VALUES ('Software Engineering', 2);
INSERT INTO department (department_name, faculty_id) VALUES ('Electrical Engineering', 2);
INSERT INTO department (department_name, faculty_id) VALUES ('Mechanical Engineering', 2);
INSERT INTO department (department_name, faculty_id) VALUES ('Nursing', 3);
INSERT INTO department (department_name, faculty_id) VALUES ('Medicine', 3);

