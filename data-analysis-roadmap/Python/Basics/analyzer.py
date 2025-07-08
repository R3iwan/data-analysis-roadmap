text = input("Введите текст для анализа:\n")

# 1. Считаем символы
char_count = len(text)
print(f"Общее количество символов: {char_count}")

# 2. Считаем слова
# .split() создает список из слов
word_list = text.split()
word_count = len(word_list)
print(f"Количество слов: {word_count}")

# 3. Считаем предложения
# .count() считает, сколько раз символ встречается в строке
sentence_count = text.count('.') + text.count('!') + text.count('?')
# Проверка на случай, если текст не пустой, но знаков препинания нет
if sentence_count == 0 and char_count > 0:
    sentence_count = 1
print(f"Количество предложений: {sentence_count}")