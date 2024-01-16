-- Seed data for faculty table
-- Seed data for faculty table

INSERT INTO faculty (name) VALUES ('Computing and Information Technology');
INSERT INTO faculty (name) VALUES ('Engineering');
INSERT INTO faculty (name) VALUES ('Health and Life Sciences');
INSERT INTO faculty (name) VALUES ('Humanities and Social Sciences');

-- Seed data for department table

INSERT INTO department (name, faculty_id) VALUES ('Computer Science', 1);
INSERT INTO department (name, faculty_id) VALUES ('Information Technology', 1);
INSERT INTO department (name, faculty_id) VALUES ('Software Engineering', 2);
INSERT INTO department (name, faculty_id) VALUES ('Electrical Engineering', 2);
INSERT INTO department (name, faculty_id) VALUES ('Mechanical Engineering', 2);
INSERT INTO department (name, faculty_id) VALUES ('Nursing', 3);
INSERT INTO department (name, faculty_id) VALUES ('Medicine', 3);

