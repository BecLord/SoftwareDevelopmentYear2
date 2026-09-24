USE assignment2;

INSERT INTO Clinic VALUES(1, 'The Kingdom Clinic', 'Market St, Kenmare, County Kerry', '123456789');
INSERT INTO Clinic VALUES(2, 'The Rebel Clinic', 'Tramore Road, County Cork', '987654321');

INSERT INTO Staff VALUES(1, 'Mary', 'Lynch', '12 Green St, Kildare, County Kerry', '1998-05-14', 50000, 'Vet, Manager', 1);
INSERT INTO Staff VALUES(2, 'John', 'Brown', '4 Blossom Tree Lane, Tralee, County Kerry', '1990-03-22', 40000, 'Vet', 1);
INSERT INTO Staff VALUES(3, 'Lilly', 'White', '12 Douglas Road, County Cork', '1983-07-30', 45000, 'Vet, Manager', 2);

INSERT INTO Owner VALUES(1, 'Mark', 'Collins', '1 Light Street, County Kerry', '0876543210');
INSERT INTO Owner VALUES(2, 'Deidre', 'Long', '2 Patricks Street, Cork', '0865432109');

INSERT INTO Horse VALUES(1, 'Sherlock', '2019-02-12', 'Black', 1, 1);
INSERT INTO Horse VALUES(2, 'Snow', '2017-06-25', 'White', 2, 2);

INSERT INTO Treatment VALUES(1, 'Vaccination', 'A vaccine', 100.00);
INSERT INTO Treatment VALUES(2, 'Hoof Care', 'hoof care and trimming', 75.00);
INSERT INTO Treatment VALUES(3, 'Dental Check', 'Examination and care of the horse’s teeth', 120.00);

INSERT INTO Consultation VALUES(1, '2024-11-01', 'Mild fever', 'Requires observation and treatment', 1, 1);
INSERT INTO Consultation VALUES(2, '2024-11-02', 'Leg injury', 'Requires bandaging and rest', 2, 2);

INSERT INTO Consultation_Treatment VALUES(1, 1);
INSERT INTO Consultation_Treatment VALUES(1, 2);
INSERT INTO Consultation_Treatment VALUES(2, 3);

INSERT INTO Treatment_Horse VALUES(1, 1);
INSERT INTO Treatment_Horse VALUES(2, 1);
INSERT INTO Treatment_Horse VALUES(3, 2);

COMMIT;
