SELECT skill_name,
    ROUND(AVG(salary_inr)) AS avg_salary
FROM job_applied
INNER JOIN job_skills ON job_applied.job_id = job_skills.job_id
INNER JOIN  skills ON  job_skills.skill_id = skills.skill_id
WHERE 
    job_title = 'Data Analyst'
    AND salary_inr IS NOT NULL
GROUP BY 
    skill_name
ORDER BY
    avg_salary
