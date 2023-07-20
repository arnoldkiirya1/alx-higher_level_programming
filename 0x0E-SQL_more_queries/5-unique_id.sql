-- This script creates the table 'unique_id' on the MySQL server.

-- Create the table 'unique_id' if it doesn't already exist.
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,  -- 'id' with a default value of 1 and must be unique.
  name VARCHAR(256)  -- 'name' can contain a string up to 256 characters.
);
