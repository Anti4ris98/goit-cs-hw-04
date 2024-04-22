import os
import time
from multiprocessing import Pool, Manager, cpu_count

def search_word_in_file(args):
    filename, word, results_dict = args
    print(f"Обробляється файл: {filename}")  # Додано логування
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if word in content:
                results_dict[filename] = word
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

    manager = Manager()
    results_dict = manager.dict()  # Створюємо словник для результатів у менеджері

    pool_size = cpu_count()  # Кількість процесів відповідає кількості ядер процесора

    # Створюємо пул процесів
    with Pool(pool_size) as pool:
        pool.map(search_word_in_file, [(file_path, word_to_search, results_dict) for file_path in file_paths])

    # Виводимо результати
    print("Результати пошуку:")
    for filename, word in results_dict.items():
        print(f"Слово '{word}' знайдено в файлі '{filename}'")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"Час виконання: {end_time - start_time} секунд")