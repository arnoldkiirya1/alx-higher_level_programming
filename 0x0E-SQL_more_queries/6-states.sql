-- Create the database 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the 'hbtn_0d_usa' database for further operations.
USE hbtn_0d_usa;

-- Create the table 'states' if it doesn't already exist.
CREATE TABLE IF NOT EXISTS states (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- 'id' is an auto-generated primary key.
  name VARCHAR(256) NOT NULL  -- 'name' can't be NULL and can contain a string up to 256 characters.
);
