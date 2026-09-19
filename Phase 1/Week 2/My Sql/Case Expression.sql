/*
CASE - begins the expressions
WHEN - specifies the conditions to look at
THEN - what to do when the conditions is TRUE
ELSE - Optional
END - concludes the case expression.
*/

SELECT 
--     job_title,
--     city,
     COUNT(job_id) AS number_of_jobs,
     CASE 
         WHEN city = 'Anywhere' THEN 'Remote'
         WHEN city = 'Hyderabad' THEN 'Local'
         ELSE 'Onsite'
     END AS city_category
FROM job_applied
WHERE job_title = 'Data Analyst'
GROUP BY city_category;
