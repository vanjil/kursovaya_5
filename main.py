from db_manager import DBManager
from hh_vacancies import get_vacancies_from_employers


def main():
    # Параметры подключения к базе данных
    connection_params = {
        'dbname': 'kursovaya_5',
        'user': 'postgres',
        'password': 'мдфвшьшк',
        'host': 'localhost',
        'port': '5432'
    }

    # Создаем экземпляр класса DBManager
    db_manager = DBManager(connection_params)

    # Подключаемся к базе данных
    db_manager.connect()

    # Создаем таблицу и наполняем ее данными
    employer_ids = [1373, 15478, 3529, 1740, 15478, 39305, 907345, 23427, 1878711, 575665]
    vacancies = get_vacancies_from_employers(employer_ids)
    db_manager.create_table_and_insert_data(vacancies)

    # Предлагаем пользователю выбрать действие
    while True:
        print("Хотите получить из базы:\n"
              "1. Все компании и их вакансии\n"
              "2. Все вакансии\n"
              "3. Среднюю зарплату по вакансиям\n"
              "4. Вакансии с зарплатой выше средней\n"
              "5. Вакансии по ключевому слову\n"
              "0. Завершить программу\n")

        choice = input("Ваш выбор: ")

        if choice == "1":
            db_manager.get_companies_and_vacancies_count()
        elif choice == "2":
            db_manager.get_all_vacancies()
        elif choice == "3":
            db_manager.get_avg_salary()
        elif choice == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif choice == "5":
            keyword = input("Введите ключевое слово: ")
            db_manager.get_vacancies_with_keyword(keyword)
        elif choice == "0":
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

    # Отключаемся от базы данных
    db_manager.disconnect()


if __name__ == "__main__":
    main()
