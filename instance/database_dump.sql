PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE data_base (
	id INTEGER NOT NULL, 
	"userName" VARCHAR(200) NOT NULL, 
	email VARCHAR(254) NOT NULL, 
	"phoneNumber" VARCHAR(15) NOT NULL, 
	address VARCHAR(500) NOT NULL, 
	"permanentAddress" VARCHAR(500), 
	gender VARCHAR(10), 
	password VARCHAR(32) NOT NULL, 
	eca JSON, 
	"educationDetails" VARCHAR(2000), 
	"fatherName" VARCHAR(225) NOT NULL, 
	"motherName" VARCHAR(225) NOT NULL, 
	"fullName" VARCHAR(225) NOT NULL, 
	country VARCHAR(225), 
	PRIMARY KEY (id), 
	UNIQUE ("userName"), 
	UNIQUE (email)
);
INSERT INTO data_base VALUES(1,'09430656311','saketthakur4797@gmail.com','09430656311','Gaur enclave-2, Flat No. G-6 shalimar garden, sector 2 Ghaziabad, UTTAR PRADESH 201005 India','shalimar garden, sector 2','male','sha256$ZQdY32DxCkKFlxXi$06d7f8ff781ad0f59f6ab1cc5430d4244804731ba92cd8c66cfbe800574c8cf7','"Gaur enclave-2, Flat No. G-6 shalimar garden, sector 2 Ghaziabad, UTTAR PRADESH 201005 India"','kaksufhlaweufhaoweuifhawoeufh;aofhafh','asdlfkjaslfihawolfinawleifjaweofij;oiji','asdlfkjaslfihawolfinawleifjaweofij;oiji','Appario Retail Private Ltd','India');
COMMIT;
