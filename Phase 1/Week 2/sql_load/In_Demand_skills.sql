SELECT skill_name,
    COUNT (job_skills.job_id) AS demand_count
FROM job_applied
INNER JOIN job_skills ON job_applied.job_id = job_skills.job_id
INNER JOIN  skills ON  job_skills.skill_id = skills.skill_id
WHERE 
    job_title = 'Data Analyst'
GROUP BY 
    skill_name
ORDER BY
    demand_count DESC;