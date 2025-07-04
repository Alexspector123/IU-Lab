use db1;
CREATE TABLE Student(
	StudentID varchar(50) PRIMARY KEY,
    StudentName varchar(50),
    Dob date,
    Major varchar(30)
);

CREATE TABLE Course(
	CourseID varchar(50) PRIMARY KEY,
    CourseName varchar(50)
);

CREATE TABLE Lecturer(
	LecturerID varchar(50) PRIMARY KEY,
    LecturerName varchar(50),
    DepartmentID varchar(50)
);
ALTER TABLE Lecturer
ADD FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID);

CREATE TABLE Department(
	DepartmentID varchar(50) PRIMARY KEY,
    DepartmentName varchar(50)
);

CREATE TABLE Register(
    StudentID varchar(50),
    CourseID varchar(50)
);
ALTER TABLE Register
ADD FOREIGN KEY (StudentID) REFERENCES Student(StudentID);
ALTER TABLE Register
ADD FOREIGN KEY (CourseID) REFERENCES Course(CourseID);

CREATE TABLE Teach(
    LecturerID varchar(50),
    CourseID varchar(50)
);
ALTER TABLE Teach
ADD FOREIGN KEY (LecturerID) REFERENCES Lecturer(LecturerID);
ALTER TABLE Teach
ADD FOREIGN KEY (CourseID) REFERENCES Course(CourseID);
    