from ex9_3_1 import read_file
from ex9_4 import get_set

def main():
    string = read_file()
    words_lst = delete_signs(string.split())
    words_set = get_set(string)

    words_dict = {}
    for search in words_set:
        counter = 0
        for word in words_lst:
            if search == word:
                counter += 1
        words_dict[search] = counter
    
    for key in words_dict:
        print(key, words_dict[key])

def delete_signs(lst):
    new_lst = []
    for word in lst:
        if word[-1:-4:-1] == "!!!":
             word = word[0:len(word) - 3]

        if word[-1] in ["!", ".", ",", ":", ";", ")", "?"]:
            word = word[0:len(word) - 1]
            
        if word[0] == "(":
            word = word[1:]
        
        new_lst.append(word.lower())
    return new_lst
    
if __name__ == "__main__":
    main()

