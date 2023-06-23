import csv
import json

# Открываем CSV-файл
with open('test_csv.csv', 'r') as file:

    csv_reader = csv.reader(file)

    # Проходим по каждой строке CSV-файла
    for row in csv_reader:

        answer = {
            row[0]: {
                "oid": row[2],
                "description": row[-1]
            }
        }

        with open('test_data_json.json', 'r+') as json_file:
            # Загружаем содержимое JSON-файла
            json_data = json.load(json_file)

            # Обновляем данные в JSON-файле
            json_data.update(answer)

            # Устанавливаем указатель файла в начало
            json_file.seek(0)

            # Записываем обновленные данные в JSON-файл
            json.dump(json_data, json_file, indent=4)

            # Очищаем содержимое файла после конца записи
            json_file.truncate()
