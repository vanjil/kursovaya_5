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

def fill_tables():
    try:
        connection = psycopg2.connect(
            dbname='kursovaya_5',
            user='postgres',
            password='мдфвшьшк',
            host='localhost',
            port='5432'
        )
        cursor = connection.cursor()

        # Данные для заполнения таблиц
        companies = [
            ('Company A', 'City A'),
            ('Company B', 'City B'),
            ('Company C', 'City C')
        ]

        vacancies = [
            ('City A', 50000, 70000),
            ('City B', 60000, 80000),
            ('City C', 70000, 90000)
        ]

        # Вставка данных в таблицы
        for company in companies:
            cursor.execute("INSERT INTO company (name, city) VALUES (%s, %s)", company)

        for vacancy in vacancies:
            cursor.execute("INSERT INTO vacancy (city, salary_from, salary_to) VALUES (%s, %s, %s)", vacancy)

        connection.commit()
        cursor.close()
        connection.close()
        print("Tables filled with data successfully")
    except psycopg2.Error as e:
        print("Error filling tables with data.")
        print(e)

if __name__ == '__main__':
    create_tables()
    fill_tables()
