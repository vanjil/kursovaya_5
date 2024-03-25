import requests

employer_ids = [1373, 15478, 3529, 1740, 15478, 39305, 907345, 23427, 1878711, 575665]

def get_vacancies_from_employers(employer_ids):
    all_vacancies = []
    for employer_id in employer_ids:
        # Формируем запрос к API HH для получения данных о вакансиях по ID компании
        url = f"https://api.hh.ru/vacancies?employer_id={employer_id}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            vacancies = data.get('items', [])
            all_vacancies.extend(vacancies)
        else:
            print(f"Failed to fetch vacancies for employer ID {employer_id}. Status code: {response.status_code}")
    return all_vacancies