WITH skills_demand AS (
    SELECT 
        skills.skill_name,
        skills.skill_id,
        COUNT(job_skills.job_id) AS demand_count
    FROM job_applied
    INNER JOIN job_skills 
        ON job_applied.job_id = job_skills.job_id
    INNER JOIN skills 
        ON job_skills.skill_id = skills.skill_id
    WHERE 
        job_title = 'Data Analyst'
        AND salary_inr IS NOT NULL
    GROUP BY 
        skills.skill_name,
        skills.skill_id
),

average_salary AS (
    SELECT 
        skills.skill_name,
        skills.skill_id,
        ROUND(AVG(salary_inr)) AS avg_salary
    FROM job_applied
    INNER JOIN job_skills 
        ON job_applied.job_id = job_skills.job_id
    INNER JOIN skills 
        ON job_skills.skill_id = skills.skill_id
    WHERE 
        job_title = 'Data Analyst'
        AND salary_inr IS NOT NULL
    GROUP BY 
        skills.skill_name,
        skills.skill_id
)

SELECT 
    skills_demand.skill_id,
    skills_demand.skill_name,
    skills_demand.demand_count,
    average_salary.avg_salary
FROM skills_demand
INNER JOIN average_salary 
    ON skills_demand.skill_id = average_salary.skill_id
ORDER BY 
    skills_demand.demand_count DESC,
    avg_salary DESC;