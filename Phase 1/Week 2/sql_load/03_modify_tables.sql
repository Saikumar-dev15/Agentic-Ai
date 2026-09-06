COPY public.job_applied (application_id,company_name,industry,city,country,employee_count,job_id,job_title,department,salary_inr,posted_date,closing_date,work_mode,job_status,application_sent_date,custom_resume,resume_file_name,cover_letter_sent,cover_letter_file_name,status,last_updated
)
FROM 'C:/postgres/CSV Files/job_applied.csv'
DELIMITER ','
CSV HEADER;


COPY public.skills (skill_id,skill_name,skill_type)
FROM 'C:/postgres/CSV Files/skills.csv'
DELIMITER ','
CSV HEADER;


COPY public.job_skills (job_id,skill_id)
FROM 'C:/postgres/CSV Files/job_skills.csv'
DELIMITER ','
CSV HEADER;


COPY public.interviews (interview_id,application_id,interview_date,interview_type,interview_status,feedback
)
FROM 'C:/postgres/CSV Files/interviews.csv'
DELIMITER ','
CSV HEADER;