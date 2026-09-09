SELECT
     company_name,
     job_title,
     job_id,
     country
FROM january_jobs

UNION ALL

SELECT
    job_title,
    company_name,
    job_id,
    country
FROM february_jobs

UNION ALL

SELECT
    job_title,
    company_name,
    job_id,
    country
FROM march_jobs;


SELECT *
FROM january_jobs; 

-- Exercise 
/*
Find the job postings from the first quarter that have a salary greater than $60K
- Combine job posting tables from the first quater of 2026 (Jan - Mar) 
- Gets job postings with an average yearly salary > $60,000
*/

SELECT 
     quarter1_job_postings.job_title,
     quarter1_job_postings.country,
     quarter1_job_postings.posted_date::DATE,
     quarter1_job_postings.job_status,
     quarter1_job_postings.salary_inr
FROM (
     SELECT *
     FROM january_jobs
     UNION ALL
     SELECT *
     FROM february_jobs
     UNION ALL
     SELECT *
     FROM march_jobs
) AS quarter1_job_postings
WHERE 
     quarter1_job_postings.salary_inr > 60000 AND
     quarter1_job_postings.job_title = 'Data Analyst'
ORDER BY
     quarter1_job_postings.salary_inr




