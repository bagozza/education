import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline().strip()
            all_data.append(line)
            if not line:
                break


files = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.now()

for f in files:
    print(f)
    read_info(f)

end = datetime.now()
t_line_function = end - start
print(f'{t_line_function} # Линейный вызов')

if __name__ == '__main__':
    start = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end = datetime.now()
    time_of_multiprocessing = end - start
    print(f'{time_of_multiprocessing} # Многопроцессный')