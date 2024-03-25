import psycopg2
def create_tables():
    try:
        connection = psycopg2.connect(
            dbname='kursovaya_5',
            user='postgres',
            password='мдфвшьшк',
            host='localhost',
            port='5432'
        )
        cursor = connection.cursor()

        # Чтение SQL-скрипта из файла
        with open('create_tables.sql', 'r') as file:
            sql_script = file.read()

        # Выполнение SQL-скрипта для создания таблиц
        cursor.execute(sql_script)

        connection.commit()
        cursor.close()
        connection.close()
        print("Tables created successfully")
    except psycopg2.Error as e:
        print("Error creating tables.")
        print(e)

def insert_vacancies(vacancies):
    try:
        for vacancy in vacancies:
            self.cursor.execute("INSERT INTO vacancy (city, salary_from, salary_to) VALUES (%s, %s, %s)",
                                (vacancy['city'], vacancy['salary_from'], vacancy['salary_to']))
        self.connection.commit()
        print("Vacancies inserted successfully")
    except psycopg2.Error as e:
        print("Error inserting vacancies:", e)
        self.connection.rollback()

def insert_company(name, city):
    try:
        self.cursor.execute("INSERT INTO company (name, city) VALUES (%s, %s)", (name, city))
        self.connection.commit()
        print("Company inserted successfully")
    except psycopg2.Error as e:
        print("Error inserting company:", e)
        self.connection.rollback()