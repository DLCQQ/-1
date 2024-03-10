def create_grades_dict(surname, subject):
    students = {
        'Иванов': {
            'Математика': [5, 4, 3, 5, 5],
            'Физика': [4, 4, 3, 5, 4],
            'Информатика': [5, 5, 5, 4, 3],
            'Литература': [3, 4, 4, 3, 5]
        },
        'Петров': {
            'Математика': [4, 5, 3, 4, 4],
            'Физика': [5, 4, 4, 5, 5],
            'Информатика': [4, 3, 5, 5, 4],
            'Литература': [3, 4, 4, 4, 5]
        },
        'Сидоров': {
            'Математика': [3, 4, 5, 3, 4],
            'Физика': [5, 5, 4, 5, 4],
            'Информатика': [4, 5, 5, 4, 3],
            'Литература': [4, 3, 4, 5, 5]
        }
    }

    student = None
    for key, value in students.items():
        if key == surname:
            student = value
            break

    if student is None:
        return "Ученик с такой фамилией не найден"

    if subject not in student:
        return "У ученика нет такого предмета"

    choice = int(input("Выберите действие (1 - вывод всех оценок по предмету, 2 - вывод среднего балла): "))

    if choice == 1:
        return student[subject]
    elif choice == 2:
        avg_grade = sum(student[subject]) / len(student[subject])
        return f"Средний балл по предмету '{subject}': {avg_grade}"
    else:
        return "Некорректный выбор"

surname = input("Введите фамилию ученика: ")
subject = input("Введите название предмета: ")
result = create_grades_dict(surname, subject)
print(result)
