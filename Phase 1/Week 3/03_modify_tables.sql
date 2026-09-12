-- 1. Load jobs first
COPY public.jobs (
    job_id,
    company_id,
    job_title,
    department,
    salary_inr,
    posted_date,
    closing_date,
    work_mode,
    job_status
)
FROM 'C:/postgres/CSV Files/jobs.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);


-- 2. Load skills
COPY public.skills (
    skill_id,
    skill_name,
    skill_type
)
FROM 'C:/postgres/CSV Files/skills.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);


-- 3. Load job applications
COPY public.job_applied (
    application_id,
    company_name,
    industry,
    city,
    country,
    employee_count,
    job_id,
    job_title,
    department,
    salary_inr,
    posted_date,
    closing_date,
    work_mode,
    job_status,
    application_sent_date,
    custom_resume,
    resume_file_name,
    cover_letter_sent,
    cover_letter_file_name,
    status,
    last_updated
)
FROM 'C:/postgres/CSV Files/job_applied.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);


-- 4. Load job skills
COPY public.job_skills (
    job_id,
    skill_id
)
FROM 'C:/postgres/CSV Files/job_skills.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);


-- 5. Load interviews
COPY public.interviews (
    interview_id,
    application_id,
    interview_date,
    interview_type,
    interview_status,
    feedback
)
FROM 'C:/postgres/CSV Files/interviews.csv'
WITH (
    FORMAT CSV,
    HEADER TRUE,
    DELIMITER ','
);