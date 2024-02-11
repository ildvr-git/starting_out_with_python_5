from ex9_3_1 import read_file
from ex9_4 import get_set


def main():
    print("В строке ниже введите имя первого файла")
    set_1 = get_set(read_file())
    print("В строке ниже введите имя второго файла")
    set_2 = get_set(read_file())

    print()

    print_result("находятся и в том, и в другом файле", (set_1 | set_2))
    print_result("находятся одновременно в обоих файлах", (set_1 & set_2))
    print_result("находятся в файле 1, но не входят в файл 2", (set_1 - set_2))
    print_result("находятся в файле 2, но не входят в файл 1", (set_2 - set_1))
    print_result("находятся либо в 1, либо во 2, но не в обоих сразу", (set_1 ^ set_2))
    
def print_result(text, action):
    print(f"Список слов, которые {text}:")
    lst = list(action)
    for item in lst[0:len(lst)-1]:
        print(item, end=", ")
    print(lst[len(lst)-1], end=".\n")
    print()
    
if __name__ == "__main__":
    main()