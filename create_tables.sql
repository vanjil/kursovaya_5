CREATE TABLE IF NOT EXISTS company (
    id SERIAL PRIMARY KEY,
    name TEXT,
    city TEXT
);

CREATE TABLE IF NOT EXISTS vacancy (
    id SERIAL PRIMARY KEY,
    city TEXT,
    salary_from INTEGER,
    salary_to INTEGER
);
ALTER TABLE vacancy
ADD COLUMN company_id INTEGER;
