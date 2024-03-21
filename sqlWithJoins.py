import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE Advisor( 
    AdvisorID INTEGER NOT NULL PRIMARY KEY, 
    AdvisorName TEXT NOT NULL
);

CREATE TABLE Student( 
    StudentID INTEGER NOT NULL PRIMARY KEY, 
    StudentName TEXT NOT NULL
);

CREATE TABLE Advisor_Student(
    AdvisorID INTEGER,
    StudentID INTEGER,
    FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
    FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
    PRIMARY KEY(AdvisorID, StudentID)
);
''')

tables = [
    [
        (1, "John Paul"),
        (2, "Anthony Roy"),
        (3, "Raj Shetty"),
        (4, "Sam Reeds"),
        (5, "Arthur Clintwood")
    ],
    [
        (501, "Geek1"),
        (502, "Geek2"),
        (503, "Geek3"),
        (504, "Geek4"),
        (505, "Geek5"),
        (506, "Geek6"),
        (507, "Geek7"),
        (508, "Geek8"),
        (509, "Geek9"),
        (510, "Geek10")
    ],
    [
        (1, 501),
        (3, 501),
        (5, 501),
        (4, 502),
        (5, 502),
        (3, 503),
        (2, 504),
        (4, 505),
        (2, 506),
        (2, 507),
        (3, 508),
        (2, 510),
        (4, 510)
    ]
]

queries = ["""INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES (?, ?)""",
           """INSERT INTO Student(StudentID, StudentName) VALUES (?, ?)""",
           """INSERT INTO Advisor_Student(AdvisorID, StudentID) VALUES (?, ?);"""
           ]

for index in range(len(queries)):
    cursor.executemany(queries[index], tables[index])

conn.commit()

cursor.execute('''
    SELECT a.AdvisorID, a.AdvisorName, COUNT(Advisor_Student.StudentID) AS StudentCount
    FROM Advisor AS a
    LEFT JOIN Advisor_Student ON a.AdvisorID = Advisor_Student.AdvisorID
    GROUP BY a.AdvisorID, a.AdvisorName
''')

rows = cursor.fetchall()

for row in rows:
    print("ID:", row[0], "Advisor:", row[1], "- Students:", row[2])

conn.close()
