def combine_files():
    files = ['file1.txt', 'file2.txt', 'file3.txt']

    try:
        with open('combined.txt', 'w', encoding='utf-8') as combined_file:
            for i, file_name in enumerate(files, 1):
                try:
                    with open(file_name, 'r', encoding='utf-8') as current_file:
                        content = current_file.read().strip()

                    combined_file.write(f"== Содержимое {file_name} ==\n")
                    combined_file.write(content)

                    if i < len(files):
                        combined_file.write("\n\n")

                    print(f"Файл {file_name} успешно добавлен в combined.txt")

                except FileNotFoundError:
                    print(f"Файл {file_name} не найден. Пропускаем.")

        print("\nОбъединение завершено. Результат в combined.txt")

    except Exception as e:
        print(f"Ошибка при создании combined.txt: {e}")

combine_files()