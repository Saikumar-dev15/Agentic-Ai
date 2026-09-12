-- January
CREATE TABLE january_jobs AS
SELECT *
FROM job_applied
WHERE EXTRACT(MONTH FROM posted_date) = 1;


-- February
CREATE TABLE february_jobs AS
SELECT *
FROM job_applied
WHERE EXTRACT(MONTH FROM posted_date) = 2;


-- March
CREATE TABLE march_jobs AS
SELECT *
FROM job_applied
WHERE EXTRACT(MONTH FROM posted_date) = 3;

SELECT posted_date
FROM january_jobs;
