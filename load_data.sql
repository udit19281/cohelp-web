use cohelpdb;

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/NGO/web/data2/ambulance.csv' 
INTO TABLE ambulance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' 
IGNORE 1 ROWS (name, contact_number, address, link, status,contact_person);

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/NGO/web/data2/foodSupport.csv' 
INTO TABLE FoodSupport FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' 
IGNORE 1 ROWS (name, contact_number, address, contact_person, status);

LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/NGO/web/data2/bloodPlasma.csv' 
INTO TABLE BloodPlasma FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' 
IGNORE 1 ROWS (name, contact_number, address, contact_person, medical_conditions, availibility_status, link);