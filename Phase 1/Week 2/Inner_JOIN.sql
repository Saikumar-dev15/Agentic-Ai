SELECT
    job_skills.skill_id
FROM skills AS job_skills
INNER JOIN jobs AS job_applied
    ON job_applied.skill_id = job_skills.skill_id;