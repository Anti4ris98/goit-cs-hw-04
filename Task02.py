import os
import time
from multiprocessing import Pool, Manager, cpu_count

def search_words_in_file(args):
    filename, words, results_dict = args
    print(f"Обробляється файл: {filename}")  # Додано логування
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            found_words = [word for word in words if word in content]
            if found_words:
                results_dict[filename] = found_words
                print(f"Знайдено {', '.join(found_words)} у файлі {filename}")  # Додано логування
            else:
                print(f"У файлі {filename} слова не знайдено")  # Додано логування
    except Exception as e:
        print(f"Error occurred while processing {filename}: {e}")

def main():
    folder_path = "files"  # шлях до папки з файлами
    words_to_search = ["numpy", "networkx"]  # слова, які шукаємо

    file_list = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in file_list]

    manager = Manager()
    results_dict = manager.dict()  # Створюємо словник для результатів у менеджері

    pool_size = cpu_count()  # Кількість процесів відповідає кількості ядер процесора

    # Створюємо пул процесів
    with Pool(pool_size) as pool:
        pool.map(search_words_in_file, [(file_path, words_to_search, results_dict) for file_path in file_paths])

    # Виводимо результати
    print("Результати пошуку:")
    for filename, found_words in results_dict.items():
        print(f"Слова {', '.join(found_words)} знайдено в файлі '{filename}'")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Час виконання: {end_time - start_time} секунд")