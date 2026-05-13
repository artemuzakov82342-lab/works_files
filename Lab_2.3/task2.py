def search_word_in_text():
    try:
        search_word = input("Введите слово для поиска: ").strip()

        with open('text.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        found = False
        count = 0
        line_numbers = []

        for i, line in enumerate(lines, start=1):
            words = line.split()
            if search_word in words:
                found = True
                count += words.count(search_word)
                line_numbers.append(i)

        print(f"Слово найдено: {'Да' if found else 'Нет'}")
        if found:
            print(f"Количество вхождений: {count}")
            print(f"Номера строк: {line_numbers}")

        with open('search_results.txt', 'w', encoding='utf-8') as file:
            file.write(f"Слово для поиска: {search_word}\n")
            file.write(f"Найдено: {'Да' if found else 'Нет'}\n")
            if found:
                file.write(f"Количество вхождений: {count}\n")
                file.write(f"Номера строк: {line_numbers}\n")

        print("Результаты записаны в search_results.txt")

    except FileNotFoundError:
        print("Файл text.txt не найден.")

search_word_in_text()