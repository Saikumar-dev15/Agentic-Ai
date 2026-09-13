WITH top_paying_jobs AS(
    SELECT
        ja.job_id,
        ja.job_title,
        ja.industry,
        ja.salary_inr,
        ja.company_name AS name
    FROM 
       public.job_applied AS ja

    LEFT JOIN public.jobs AS j ON ja.job_id = j.job_id
    WHERE 
        ja.job_title = 'Junior Data Analyst' AND
        ja.city = 'Bengaluru' AND
        ja.salary_inr IS NOT NULL
    ORDER BY 
        ja.salary_inr DESC
)

SELECT *
FROM top_paying_jobs
INNER JOIN job_skills ON top_paying_jobs.job_id = job_skills.job_id
INNER JOIN  skills ON  job_skills.skill_id = skills.skill_id;

