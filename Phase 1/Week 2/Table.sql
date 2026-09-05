/* Manipulated Tables
1.Create Table: create tables
2.INSERT INTO : add columns (data) to your tables
3.ALTER TABLE : alter tables
    ADD: add columns
    RENAME : rename columns
    ALter Columns : change the datatype of a column
    Drop COLUMN : delete a columns
4.DROP Table : delete tables 
*/


CREATE TABLE  job_applied(
    job_id INT,
    application_sent_data DATE,
    custom_resume BOOLEAN,
    resume_file_name VARCHAR(225),
    cover_letter_sent BOOLEAN,
    cover_letter_file_name VARCHAR(225),
    status VARCHAR(50)
);
 
SELECT *
FROM job_applied;