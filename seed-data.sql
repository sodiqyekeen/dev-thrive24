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

-- Seed data for tutors table

INSERT INTO tutors (first_name, last_name, skills, experience, availability, email, hourly_rate) 
VALUES ('Leo', "Smart", "python data-science", "5 years experience working with chatgpt", "MON WED FRI", "leosmart@skill.com", "$5");

INSERT INTO tutors (first_name, last_name, skills, experience, availability, email, hourly_rate) 
VALUES ('Bob', "Smith", "web development", "3 years experience working with cousera", "MON TUE FRI", "bsmith@skill.com", "$3");

INSERT INTO tutors (first_name, last_name, skills, experience, availability, email, hourly_rate) 
VALUES ('Rapheal', "Wood", "front-end engineer", "7 years experience working with facebook", "WED FRI SAT", "rwood@skill.com", "$6");

INSERT INTO tutors (first_name, last_name, skills, experience, availability, email, hourly_rate) 
VALUES ('Marley', "White", "database administrator", "10 years experience working with US government", "FRI SAT SUN", "mwhite@skill.com", "$10");

INSERT INTO tutors (first_name, last_name, skills, experience, availability, email, hourly_rate) 
VALUES ('Chris', "Awolola", "cyber security", "4 years experience working with GT bank", "MON TUE WED", "cawolola@gmail.com", "$5");



