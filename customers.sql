LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/customers_updated.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;