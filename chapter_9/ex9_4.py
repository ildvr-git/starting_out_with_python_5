""" Эта программа открывает заданный текстовый файл
и затем показывает список всех уникальных слов в файле. """
import ex9_3_1 as ext

def main():
    read_string = ext.read_file()
    new_set = get_set(read_string)
    lst = list(new_set)
    lst.sort()
    for w in lst:
        print(w)

def get_set(string):
    raw_set = set(string.split())
    new_set = delete_signs(raw_set)
    return new_set

# def delete_signs(in_set):
#     new_set = set()
#     for word in in_set:
#         if word[-1:-4:-1] == "!!!":
#              word = word[0:len(word) - 3]

#         if word[-1] in ["!", ".", ",", ":", ";", ")", "?"]:
#             word = word[0:len(word) - 1]
            
#         if word[0] == "(":
#             word = word[1:]
        
#         new_set.add(word.lower())
#     return new_set

def delete_signs(in_set):
    new_set = set()
    signs = ",.!?:;*)(][}{/\"\'"
    for word in in_set:
        for char in word:
            if char in signs:
                word = word.replace(char, "")
        new_set.add(word.lower())
    return new_set

    
if __name__ == "__main__":
    main()