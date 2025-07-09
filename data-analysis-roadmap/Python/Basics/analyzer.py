text = input("Введите текст для анализа:\n")

# --- Старая функциональность ---
char_count = len(text)
print(f"Общее количество символов: {char_count}")

word_list = text.split()
total_word_count = len(word_list) 
print(f"Общее количество слов: {total_word_count}")

sentence_count = text.count('.') + text.count('!') + text.count('?')
if sentence_count == 0 and char_count > 0:
    sentence_count = 1
print(f"Количество предложений: {sentence_count}")

# --- Новая функциональность ---
unique_words = []
for word in word_list:
    cleaned_word = word.lower().strip(".,!?:;")
    if cleaned_word not in unique_words and cleaned_word != '':
        unique_words.append(cleaned_word)

unique_words.sort()

print("-" * 20)
print(f"Количество уникальных слов: {len(unique_words)}")
print(f"Уникальные слова: {unique_words}")