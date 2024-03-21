SQLite Database and Query Script

This repository contains a Python script to create an SQLite database, populate its tables, and perform a query.
Getting Started
Prerequisites

To run the script, you need to have Python installed on your system. Additionally, ensure that you have the SQLite library (sqlite3) installed.
Installation

    Clone this repository to your local machine:

    bash

git clone https://github.com/your_username/your_repository.git

Navigate to the cloned directory:

bash

    cd your_repository

Usage

    Run the Python script:

    bash

    python populate_database.py

    This script will create an SQLite database (sqlite.db), define three tables (Advisor, Student, and Advisor_Student), populate them with sample data, and perform a query to retrieve the count of students for each advisor.

    After running the script, you can find the database file (sqlite.db) populated with the data.

Script Overview

    populate_database.py: Python script to create the SQLite database, define tables, populate them with sample data, and perform a query.
    README.md: This file, providing information about the repository.

Database Schema

The SQLite database consists of three tables:

    Advisor: Stores information about advisors.
    Column	Data Type	Description
    AdvisorID	INTEGER	Unique advisor ID
    AdvisorName	TEXT	Advisor's name

    Student: Stores information about students.
    Column	Data Type	Description
    StudentID	INTEGER	Unique student ID
    StudentName	TEXT	Student's name

    Advisor_Student: Represents the relationship between advisors and students.
    Column	Data Type	Description
    AdvisorID	INTEGER	Foreign key referencing Advisor table
    StudentID	INTEGER	Foreign key referencing Student table

Query

The Python script executes the following query:

sql

SELECT a.AdvisorID, a.AdvisorName, COUNT(Advisor_Student.StudentID) AS StudentCount
FROM Advisor AS a
LEFT JOIN Advisor_Student ON a.AdvisorID = Advisor_Student.AdvisorID
GROUP BY a.AdvisorID, a.AdvisorName

This query retrieves the advisor ID, advisor name, and the count of students associated with each advisor.
License

This project is licensed under the MIT License - see the LICENSE file for details.
