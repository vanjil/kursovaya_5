import psycopg2


class DBManager:
    """Класс для работы с базой данных PostgreSQL."""

    def __init__(self, connection_params):
        self.connection_params = connection_params
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.connection_params)
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except psycopg2.Error as e:
            print("Unable to connect to the database:", e)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    def create_table_and_insert_data(self, vacancies):
        """Создает таблицу и вставляет данные о вакансиях."""
        try:
            # Создание таблицы
            create_table_query = """
            CREATE TABLE IF NOT EXISTS vacancies (
                id SERIAL PRIMARY KEY,
                company_name VARCHAR,
                vacancy_name VARCHAR,
                salary VARCHAR,
                vacancy_url VARCHAR
            );
            """
            self.cursor.execute(create_table_query)

            # Вставка данных
            for vacancy in vacancies:
                company_name = vacancy.get('employer', {}).get('name', 'Unknown')
                vacancy_name = vacancy.get('name', 'Unnamed Vacancy')
                salary_info = vacancy.get('salary')
                if salary_info:
                    salary = salary_info.get('from', 'Salary not specified')
                else:
                    salary = 'Salary not specified'
                vacancy_url = vacancy.get('alternate_url', '')
                insert_query = """
                INSERT INTO vacancies (company_name, vacancy_name, salary, vacancy_url)
                VALUES (%s, %s, %s, %s);
                """
                self.cursor.execute(insert_query, (company_name, vacancy_name, salary, vacancy_url))

            self.connection.commit()
            print("Data inserted successfully")
        except psycopg2.Error as e:
            print("Error inserting data:", e)

    def get_companies_and_vacancies_count(self):
        """Получает из базы данных список всех компаний и количество вакансий у каждой компании."""
        try:
            query = """
            SELECT company_name, COUNT(*) AS vacancy_count FROM vacancies GROUP BY company_name;
            """
            self.cursor.execute(query)
            companies_and_vacancies = self.cursor.fetchall()
            print("Companies and their vacancies count:")
            for company_info in companies_and_vacancies:
                print(company_info)
        except psycopg2.Error as e:
            print("Error fetching data:", e)

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        try:
            query = """
            SELECT ROUND(AVG(salary::NUMERIC)) FROM vacancies WHERE salary != 'Salary not specified';
            """
            self.cursor.execute(query)
            avg_salary = self.cursor.fetchone()[0]
            print(f"Average salary: {avg_salary}")
        except psycopg2.Error as e:
            print("Error fetching data:", e)

    def get_all_vacancies(self):
        """Получает из базы данных список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию."""
        try:
            query = """
            SELECT company_name, vacancy_name, salary, vacancy_url FROM vacancies;
            """
            self.cursor.execute(query)
            vacancies = self.cursor.fetchall()
            print("All Vacancies:")
            for vacancy in vacancies:
                print(vacancy)
        except psycopg2.Error as e:
            print("Error fetching data:", e)

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        try:
            query = """
            SELECT * FROM vacancies WHERE salary != 'Salary not specified' AND salary::NUMERIC > (
                SELECT AVG(salary::NUMERIC) FROM vacancies WHERE salary != 'Salary not specified'
            );
            """
            self.cursor.execute(query)
            vacancies = self.cursor.fetchall()
            print("Vacancies with salary higher than average:")
            for vacancy in vacancies:
                print(vacancy)
        except psycopg2.Error as e:
            print("Error fetching data:", e)

    def get_vacancies_with_keyword(self, keyword: str):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова."""
        try:
            query = """
            SELECT * FROM vacancies WHERE vacancy_name ILIKE %s;
            """
            self.cursor.execute(query, ('%' + keyword + '%',))
            vacancies = self.cursor.fetchall()
            print(f"Vacancies with keyword '{keyword}':")
            for vacancy in vacancies:
                print(vacancy)
        except psycopg2.Error as e:
            print("Error fetching data:", e)
