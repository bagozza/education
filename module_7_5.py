from os import walk
from os.path import getmtime, getsize, dirname
from pathlib import Path


def main():
    base_path = input('Введите путь для поиска файлов: ')
    base_path = Path(base_path)
    if not base_path.is_dir():
        print('Указанный путь не является папкой')
    for path, _, files in walk(base_path):
        path = Path(path)
        for file in files:
            path_file = path / file
            file_time = getmtime(path_file)
            file_size = getsize(path_file)
            file_root = dirname(path_file)
            print(
                f'Обнаружен файл: {file}, Путь: {path_file}, Размер: {file_size} байт, Время изменения: {file_time}, Родительская директория: {file_root}'
            )


if __name__ == "__main__":
    main()
