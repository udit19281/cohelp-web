use cohelpdb;
LOAD DATA LOCAL INFILE 'C:/Users/Dell/Desktop/NGO/web/data2/ambulance.csv' 
INTO TABLE ambulance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' 
IGNORE 1 ROWS (name, contact_number, address, link, status);

(_name,contact_number,_address,link,_status)