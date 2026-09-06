CREATE TABLE public.job_applied(
    application_id INT PRIMARY KEY,
    job_id INT,
    company_name TEXT,
    industry TEXT,
    city TEXT , 
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
    last_updated DATE
);



CREATE TABLE public.skills(
    skill_id INT PRIMARY KEY,
    skill_name TEXT,
    skill_type TEXT
);


CREATE TABLE public.job_skills(
    job_id INT,
    skill_id INT,
    PRIMARY KEY (job_id, skill_id),
    FOREIGN KEY (skill_id) REFERENCES public.skills(skill_id)
);


CREATE TABLE public.interviews(
    interview_id INT PRIMARY KEY,
    application_id INT ,
    interview_date DATE,
    interview_type TEXT,
    interview_status TEXT,
    feedback TEXT,
    FOREIGN KEY (application_id)
        REFERENCES public.job_applied(application_id)
);

ALTER TABLE public.interviews OWNER to postgres;
ALTER TABLE public.job_applied OWNER to postgres;
ALTER TABLE public.skills OWNER to postgres;
ALTER TABLE public.job_skills OWNER to postgres;


CREATE INDEX idx_interviews_application_id ON public.interviews(application_id);
CREATE INDEX idx_job_skills_skill_id ON public.job_skills(skill_id);


SELECT *
FROM public.job_applied;
