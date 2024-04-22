import os
import threading
import time
import queue  # Імпортуємо модуль черги

def search_word_in_file(filename, word, results_queue):
    print(f"Обробляється файл: {filename}")  # Додано логування
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if word in content:
                results_queue.put((filename, word))
                print(f"Знайдено '{word}' у файлі {filename}")  # Додано логування
            else:
                print(f"У файлі {filename} слово не знайдено")  # Додано логування
    except Exception as e:
        print(f"Error occurred while processing {filename}: {e}")

def main():
    folder_path = "files"  # шлях до папки з файлами
    word_to_search = "numpy"  # слово, яке шукаємо

    file_list = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in file_list]

    results_queue = queue.Queue()  # Створюємо чергу для результатів
    threads = []
    for file_path in file_paths:
        thread = threading.Thread(target=search_word_in_file, args=(file_path, word_to_search, results_queue))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    results = {}  # Словник для зберігання результатів
    while not results_queue.empty():
        filename, word = results_queue.get()
        results[filename] = word

    # Виводимо результати
    print("Результати пошуку:")
    for filename, word in results.items():
        print(f"Слово '{word}' знайдено в файлі '{filename}'")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Час виконання: {end_time - start_time} секунд")