-- It define a temporary result set that you can reference.
-- Can reference within a SELECT, INSERT , UPDATE, or DELETE Statement
-- Define  with  WITH.

WITH january_jobs AS (--CTE definition starts here
    SELECT *
    FROM job_applied
    WHERE EXTRACT(MONTH FROM posted_date) =1
) -- CTE definition ends here

SELECT * 
FROM january_jobs;


-- Exercise
