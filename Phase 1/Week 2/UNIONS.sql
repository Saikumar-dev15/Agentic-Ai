SELECT
     company_name,
     job_title,
     job_id,
     country
FROM january_jobs

UNION

SELECT
    job_title,
    company_name,
    job_id,
    country
FROM february_jobs;


