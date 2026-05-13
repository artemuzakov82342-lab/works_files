def sort_words():
    try:
        with open('words.txt', 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]

        sorted_alpha = sorted(words)  # По алфавиту
        sorted_length = sorted(words, key=len)  # По длине
        sorted_reverse = sorted(words, reverse=True)  # Обратный алфавитный

        with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted_alpha))

        with open('sorted_by_length.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted_length))

        with open('sorted_reverse.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted_reverse))

        print("Сортировка завершена!")
        print("Созданы файлы:")
        print("- sorted_alphabetically.txt")
        print("- sorted_by_length.txt")
        print("- sorted_reverse.txt")

    except FileNotFoundError:
        print("Ошибка: words.txt не найден")

sort_words()