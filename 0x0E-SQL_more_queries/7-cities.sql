-- Create the database 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the 'hbtn_0d_usa' database for further operations.
USE hbtn_0d_usa;

-- Create the table 'cities' if it doesn't already exist.
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT PRIMARY KEY,  -- 'id' is an auto-generated primary key.
  state_id INT NOT NULL,  -- 'state_id' can't be NULL.
  name VARCHAR(256) NOT NULL,  -- 'name' can't be NULL and can contain a string up to 256 characters.
  FOREIGN KEY (state_id) REFERENCES states(id)  -- 'state_id' is a FOREIGN KEY referencing 'id' of the states table.
);
