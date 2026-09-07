-- Subqueries: query nested inside a larger query
--  it can be used in SELECT , FROM and WHERE Clauses.

SELECT *
FROM ( -- Query will Start here
    SELECT *
    FROM job_applied
    WHERE EXTRACT(MONTH FROM posted_date) =1
) AS january_jobs;




-- Exercise

SELECT company_id, department
FROM public.jobs
WHERE company_id IN (
    SELECT company_id
    FROM public.job_applied
    WHERE custom_resume = TRUE
    ORDER BY company_id
);
      
