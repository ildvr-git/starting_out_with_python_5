import io

SIGNS = ",.!?:;*)(][}{/\"\'"

def main():
    file_name, string = read_file()
    words_set = set("".join([x.lower() for x in string if x not in SIGNS]).split())

    # chars_lst = [x.lower() for x in string if x not in SIGNS]
    # words_str = "".join(chars_lst)
    # words_lst = words_str.split()
    # words_set = set(words_lst)
    
    rows_lst = string.lower().split("\n")
    words_dict = {}
    for search in words_set:
        counter = 0
        search_lst = []
        for row in rows_lst:
            counter += 1
            for word in row.split():
                word = "".join([ch.lower() for ch in word if ch not in SIGNS])
                if search == word:
                    search_lst.append(counter)
            words_dict[search] = search_lst

    words_dict = dict(sorted(words_dict.items()))
    
    write_data(words_dict, file_name)
    
def read_file():
    file_name = input("Введите имя файла из папки 'data', который нужно открыть >>> ")
    file = io.open(f"chapter_9\data\{file_name}.txt", mode="r", encoding="utf-8")
    string = file.read()
    file.close()
    return file_name, string

def write_data(dict, file_name):
    out_file = io.open(f"chapter_9\data\{file_name}_word_index.txt", mode="w", encoding="utf-8")
    for k in dict:
        out_file.write(k + ": ")
        for item in set(dict[k]):
            out_file.write(str(item) + " ")
        out_file.write("\n")
    out_file.close()    

if __name__ == "__main__":
    main()