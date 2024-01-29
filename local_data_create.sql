CREATE DATABASE local_patient WITH OWNER = 'test_user';
-- Create a new user
--CREATE USER test_user WITH ENCRYPTED PASSWORD 'psql123';

-- Grant privileges to the new user
GRANT ALL PRIVILEGES ON DATABASE local_patient TO test_user;

\c local_patient;

SET role test_user;

CREATE TABLE clinics (
	id serial4 NOT NULL,
	"name" text NOT NULL,
	address text NOT NULL,
	email text NULL,
	"phoneNumber" text NULL,
	"isActive" bool NOT NULL DEFAULT true,
	"createdAt" timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updatedAt" timestamp(3) NOT NULL,
	CONSTRAINT clinics_pkey PRIMARY KEY (id)
);
CREATE UNIQUE INDEX clinics_name_address_key ON public.clinics USING btree (name, address);

CREATE TABLE patients (
	id serial4 NOT NULL,
	"externalId" text NULL,
	"firstName" text NOT NULL,
	"lastName" text NOT NULL,
	"dateOfBirth" date NULL,
	verified bool NOT NULL DEFAULT false,
	notes text NULL,
	"isActive" bool NOT NULL DEFAULT true,
	anticoagulation bool NOT NULL DEFAULT false,
	"anticoagulationDate" timestamp(3) NULL,
	"pacingDependent" bool NOT NULL DEFAULT false,
	address text NULL,
	mobile text NULL,
	landline text NULL,
	email text NULL,
	"gpName" text NULL,
	"gpAddress" text NULL,
	"gpPhone" text NULL,
	"gpEmail" text NULL,
	"otherNotes" text NULL,
	"nextTm" timestamp(3) NULL,
	"tmSchedule" text NULL,
	"createdAt" timestamp(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"updatedAt" timestamp(3) NOT NULL,
	"clinicId" int4 NULL,
	"statusComment" text NULL,
	"lockedAt" timestamp(3) NULL,
	"lockedByEmail" text NULL,
	"lockedByName" text NULL,
	CONSTRAINT patients_pkey PRIMARY KEY (id),
	CONSTRAINT "patients_clinicId_fkey" FOREIGN KEY ("clinicId") REFERENCES clinics(id) ON DELETE SET NULL ON UPDATE CASCADE,
);

INSERT INTO clinics(id, name, address, email, phoneNumber, isActive)
            values (1,'Apollo', 'New Delhi', 'test123@gmail.com', '1234567890', true);
INSERT INTO clinics(id, name, address, email, phoneNumber, isActive)
            values (2,'Max', 'Noida', 'test456@gmail.com', '0123456789', true);

INSERT INTO patients(id, firstName, lastName, isActive,address, mobile, email, clinicId)
            values (1,'John', 'Wick', true, 'New Delhi','1111111111', 'test123456@gmail.com', 1);
INSERT INTO patients(id, firstName, lastName, isActive, address, mobile, email, clinicId)
            values (2,'Barry', 'Allen', true, 'Noida','2222222222', 'test12345678@gmail.com', 2);

COMMIT;