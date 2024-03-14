from db_manager import DBManager

def main():
    # Создаем экземпляр класса DBManager
    db_manager = DBManager(
        dbname='kursovaya_5',
        user='postgres',
        password='мдфвшьшк',
        host='localhost',
        port='5432'
    )

    # Подключаемся к базе данных
    db_manager.connect()

    # Интерактивно получаем информацию от пользователя
    city = input("Введите город: ")
    min_salary, max_salary = map(int, input("Введите минимальную и максимальную зарплату через пробел: ").split())
    company_name = input("Введите название компании: ")

    # Получаем и выводим список вакансий в соответствии с введенными параметрами
    vacancies = db_manager.get_vacancies(city, min_salary, max_salary, company_name)
    print("\nVacancies:")
    if vacancies:
        for vacancy in vacancies:
            print(vacancy)
    else:
        print("No vacancies found.")

    # Отключаемся от базы данных
    db_manager.disconnect()

if __name__ == '__main__':
    main()
