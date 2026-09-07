-- Remove existing tables
DROP TABLE IF EXISTS public.interviews;
DROP TABLE IF EXISTS public.job_skills;
DROP TABLE IF EXISTS public.job_applied;
DROP TABLE IF EXISTS public.skills;
DROP TABLE IF EXISTS public.jobs;


-- 1. Jobs table
CREATE TABLE public.jobs (
    job_id INT PRIMARY KEY,
    company_id INT,
    job_title VARCHAR(50),
    department TEXT,
    salary_inr NUMERIC,
    posted_date DATE,
    closing_date DATE,
    work_mode TEXT,
    job_status TEXT
);


-- 2. Skills table
CREATE TABLE public.skills (
    skill_id INT PRIMARY KEY,
    skill_name TEXT,
    skill_type TEXT
);


-- 3. Job Applied table
CREATE TABLE public.job_applied (
    application_id INT PRIMARY KEY,
    job_id INT,
    company_name TEXT,
    industry TEXT,
    city TEXT,
    country TEXT,
    employee_count INT,
    job_title TEXT,
    department TEXT,
    salary_inr NUMERIC,
    posted_date DATE,
    closing_date DATE,
    work_mode TEXT,
    job_status TEXT,
    application_sent_date DATE,
    custom_resume BOOLEAN,
    resume_file_name TEXT,
    cover_letter_sent BOOLEAN,
    cover_letter_file_name TEXT,
    status TEXT,
    last_updated DATE,

    CONSTRAINT fk_job_applied_job
        FOREIGN KEY (job_id)
        REFERENCES public.jobs(job_id)
);


-- 4. Job Skills table
CREATE TABLE public.job_skills (
    job_id INT,
    skill_id INT,

    CONSTRAINT pk_job_skills
        PRIMARY KEY (job_id, skill_id),

    CONSTRAINT fk_job_skills_job
        FOREIGN KEY (job_id)
        REFERENCES public.jobs(job_id),

    CONSTRAINT fk_job_skills_skill
        FOREIGN KEY (skill_id)
        REFERENCES public.skills(skill_id)
);


-- 5. Interviews table
CREATE TABLE public.interviews (
    interview_id INT PRIMARY KEY,
    application_id INT,
    interview_date DATE,
    interview_type TEXT,
    interview_status TEXT,
    feedback TEXT,

    CONSTRAINT fk_interview_application
        FOREIGN KEY (application_id)
        REFERENCES public.job_applied(application_id)
);


-- 6. Indexes
CREATE INDEX idx_interviews_application_id
    ON public.interviews(application_id);

CREATE INDEX idx_job_skills_skill_id
    ON public.job_skills(skill_id);

SELECT *
--      job_title AS title,
--      job_status AS Status,
--      posted_date AS date,
--    COUNT(job_id) AS jobs_posted_count,
--    EXTRACT (MONTH FROM posted_date) AS date_month
--    EXTRACT (YEAR FROM posted_date) AS date_year
FROM 
    public.jobs;
/*WHERE
     job_title = 'Data Analyst'
GROUP BY
    date_month
ORDER BY 
       jobs_posted_count  DESC;
*/