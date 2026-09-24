USE assignment2;

CREATE TABLE Clinic
	(clinicNo 	INT			NOT NULL,
    name		VARCHAR(255),
    address		VARCHAR(255),
    phoneNumber	VARCHAR(255),
PRIMARY KEY (clinicNo));

CREATE TABLE Staff
	(staffNo	INT			NOT NULL,
	firstName	VARCHAR(255),
    lastName	VARCHAR(255),
    address		VARCHAR(255),
    DOB			DATE,
    salary		DECIMAL(10,2),
    position	VARCHAR(255),
    clinicNo	INT,
PRIMARY KEY (staffNo),
FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo));

CREATE TABLE Owner
	(ownerNo 	INT			NOT NULL,
    firstName	VARCHAR(255),
    lastName	VARCHAR(255),
    address		VARCHAR(255),
    phoneNumber	VARCHAR(255),
PRIMARY KEY (ownerNo));

CREATE TABLE Horse
	(horseID 	INT			NOT NULL,
    name		VARCHAR(255),
    DOB			DATE,
    colour		VARCHAR(255),
    ownerNo		INT,
    clinicNo	INT,
PRIMARY KEY (horseID),
FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo));

CREATE TABLE Treatment
	(treatNo	INT			NOT NULL,
    treatmentName	VARCHAR(255),
    description		TEXT,
    cost			DECIMAL(10, 2),
PRIMARY KEY (treatNo));

CREATE TABLE Consultation
	(consulNo	INT			NOT NULL,
	date		DATE,
    dignosis	TEXT,
    notes		TEXT,
    horseID		INT,
    staffNo		INT,
PRIMARY KEY (consulNo),
FOREIGN KEY (horseID) REFERENCES Horse(horseID),
FOREIGN KEY (staffNo) REFERENCES Staff(staffNo));

CREATE TABLE Consultation_Treatment
	(consulNo 	INT 	NOT NULL,
    treatNo		INT		NOT NULL,
PRIMARY KEY (consulNo, treatNo),
FOREIGN KEY (consulNo) REFERENCES Consultation(consulNo),
FOREIGN KEY (treatNo) REFERENCES Treatment(treatNo));

CREATE TABLE Treatment_Horse
	(treatNo	INT		NOT NULL,
    horseID		INT		NOT NULL,
PRIMARY KEY (treatNo, horseID),
FOREIGN KEY (treatNo) REFERENCES Treatment(treatNo),
FOREIGN KEY (horseID) REFERENCES Horse(horseID));

COMMIT;