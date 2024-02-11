import io
CODES = {"A":"!", "a":"@", "B":"#", "b":"$", "C":"%", "c":"(", "D":"^", \
        "d":")", "E":"&", "e":"-", "F":"*", "f":"=", "G":"_", "g":"+", \
        "H":"<", "h":">", "I":",", "i":".", "J":"/", "j":"?", "K":":", \
        "k":"{", "L":"}", "l":"[", "M":"]", "m":"1", "N":"2", "n":"3", \
        "O":"4", "o":"5", "P":"6", "p":"7", "Q":"8", "q":"9", "R":"0", \
        "r":"|", "S":";", "s":"Q", "T":"W", "t":"E", "U":"R", "u":"T", \
        "V":"Y", "v":"u", "W":"U", "w":"i", "X":"z", "x":"Z", "Y":"M", \
        "y":"G", "Z":"g", "z":"J", " ":"Ю"}

def main():
    read_string = read_file()
    transformed_string = transform(read_string, CODES)    
    write_to_file(transformed_string)  
  
def read_file():
    file_name = input("Введите имя файла из папки 'data', который нужно открыть >>> ")
    file = io.open(f"chapter_9\data\{file_name}.txt", mode="r", encoding="utf-8")
    string = file.read()
    file.close()
    return string
    

def transform(string, codes):
    # new_lst = []
    # for c in string:
    #     new_c = codes.get(c, "H")
    #     new_lst.append(new_c)
    # new_string = "".join(new_lst)
    # # print(new_string)
    # return new_string
    return "".join([codes.get(c, "!!!ОШИБКА!!!") for c in string])

def write_to_file(string):
    file_name = input("Введите имя файла в папке 'data', в который будет записана строка >>> ")
    file = io.open(f"chapter_9\data\{file_name}.txt", mode="w", encoding="utf-8")
    file.write(string)
    file.close()

if __name__ == "__main__":
    main()