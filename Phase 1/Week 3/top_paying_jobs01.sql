SELECT
    ja.job_id,
    ja.job_title,
    ja.city,
    ja.industry,
    ja.work_mode,
    ja.salary_inr,
    ja.application_sent_date,
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


