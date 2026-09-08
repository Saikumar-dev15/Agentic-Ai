-- ============================================================
-- INNER JOIN Examples using tables from 02_create_tables.sql
-- Tables: jobs, skills, job_skills, job_applied, interviews
-- ============================================================


-- Example 1: Get each job title along with the skills required
-- (jobs -> job_skills -> skills)
SELECT
    jobs.job_id,
    jobs.job_title,
    skills.skill_name,
    skills.skill_type
FROM jobs
INNER JOIN job_skills
    ON jobs.job_id = job_skills.job_id
INNER JOIN skills
    ON job_skills.skill_id = skills.skill_id;


-- Example 2: Get job applications with their job details
-- (job_applied -> jobs)
SELECT
    job_applied.application_id,
    job_applied.company_name,
    job_applied.status,
    jobs.job_title,
    jobs.salary_inr,
    jobs.work_mode
FROM job_applied
INNER JOIN jobs
    ON job_applied.job_id = jobs.job_id;


-- Example 3: Get interviews along with the application and job info
-- (interviews -> job_applied -> jobs)
SELECT
    interviews.interview_id,
    interviews.interview_date,
    interviews.interview_type,
    interviews.interview_status,
    job_applied.company_name,
    job_applied.cover_letter_sent,
    jobs.job_title,
    COUNT(*) AS skill_count
FROM interviews
INNER JOIN job_applied
    ON interviews.application_id = job_applied.application_id
INNER JOIN jobs
    ON job_applied.job_id = jobs.job_id
WHERE 
     job_applied.cover_letter_sent = TRUE
GROUP BY
    interviews.interview_id,
    interviews.interview_date,
    interviews.interview_type,
    interviews.interview_status,
    job_applied.company_name,
    job_applied.cover_letter_sent,
    jobs.job_title;



WITH remote_job_skills AS (
    SELECT
        js.skill_id,
        COUNT(*) AS skill_count
    FROM job_skills AS js
    INNER JOIN jobs AS j
        ON js.job_id = j.job_id
    GROUP BY js.skill_id
)

SELECT
    rjs.skill_id,
    s.skill_name,
    rjs.skill_count
FROM remote_job_skills AS rjs
INNER JOIN skills AS s
    ON rjs.skill_id = s.skill_id;