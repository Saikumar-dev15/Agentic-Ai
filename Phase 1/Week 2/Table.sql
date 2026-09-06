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
 
INSERT INTO job_applied(
    job_id,
    application_sent_data,
    custom_resume,
    resume_file_name,
    cover_letter_sent,
    cover_letter_file_name,
    status)

VALUES  (1,
        '2026-09-05',
        true,
        'resume_01.pdf',
        true,
        'cover_letter_01.pdf',
        'submitted'),
        (2,
        '2026-09-06',
        false,
        'resume_02.pdf',
        false,
        NULL,
        'interview scheduled'),
        (3,
        '2026-09-07',
        true,
        'resume_03.pdf',
        true,
        'cover_letter_03.pdf',
        'ghosted'),
        (4,
        '2026-09-07',
        true,
        'resume_04.pdf',
        false,
        NULL,
        'submitted'),
        (5,
        '2026-09-08',
        false,
        'resume_05.pdf',
        true,
        'cover_letter_05.pdf',
        'rejected');

ALTER TABLE job_applied
ADD contact VARCHAR(50);

UPDATE job_applied 
SET contact = 'Sai Kumar'
WHERE job_id = 1;

UPDATE job_applied 
SET contact = 'Vaishnavi'
WHERE job_id = 2;

UPDATE job_applied 
SET contact = 'Jaideep'
WHERE job_id = 3;

UPDATE job_applied 
SET contact = 'Shiva'
WHERE job_id = 4;

UPDATE job_applied 
SET contact = 'Gowtham'
WHERE job_id = 5;


ALTER TABLE job_applied
RENAME COLUMN contact TO contact_name

ALTER TABLE job_applied
ALTER COLUMN contact_name TYPE TEXT;

ALTER TABLE job_applied
Drop COLUMN contact_name;

DROP TABLE job_applied;

SELECT *
FROM job_applied;