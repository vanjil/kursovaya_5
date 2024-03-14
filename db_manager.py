import psycopg2

class DBManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database")
        except psycopg2.Error as e:
            print("Unable to connect to the database:", e)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")

    def get_vacancies(self, city, min_salary, max_salary, company_name):
        try:
            query = """
            SELECT * FROM vacancy 
            WHERE city ILIKE %s 
            AND salary_from >= %s 
            AND salary_to <= %s
            AND company_id IN (SELECT id FROM company WHERE name ILIKE %s)
            """
            self.cursor.execute(query, (f'%{city}%', min_salary, max_salary, f'%{company_name}%'))
            vacancies = self.cursor.fetchall()
            return vacancies
        except psycopg2.Error as e:
            print("Error fetching vacancies:", e)
            return None
