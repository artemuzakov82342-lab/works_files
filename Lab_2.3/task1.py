def count_lines_and_words():
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        line_count = len(lines)
        word_count = 0

        for line in lines:
            words = line.split()
            word_count += len(words)

        with open('statistics.txt', 'w', encoding='utf-8') as file:
            file.write(f"Количество строк: {line_count}\n")
            file.write(f"Количество слов: {word_count}\n")

        print(f"Результат записан в statistics.txt")

    except FileNotFoundError:
        print("Файл input.txt не найден.")


count_lines_and_words()