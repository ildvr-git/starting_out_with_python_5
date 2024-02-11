import random


class Question:
    def __init__(self, question_text, var_1,
                 var_2, var_3, var_4, right_num):
        self.__question = question_text
        self.__var_1 = var_1
        self.__var_2 = var_2
        self.__var_3 = var_3
        self.__var_4 = var_4
        self.__right_num = right_num

    def set_question(self, question):
        self.__question = question

    def set_var_1(self, var_1):
        self.__var_1 = var_1
        
    def set_var_2(self, var_2):
        self.__var_2 = var_2

    def set_var_3(self, var_3):
        self.__var_3 = var_3

    def set_var_4(self, var_4):
        self.__var_4 = var_4

    def set_right_num(self, right_num):
        self.__right_num = right_num

    def get_question(self):
        return self.__question
    
    def get_var_1(self):
        return self.__var_1
    
    def get_var_2(self):
        return self.__var_2
    
    def get_var_3(self):
        return self.__var_3
    
    def get_var_4(self):
        return self.__var_4
        
    def get_right_num(self) -> int:
        return self.__right_num
    
    def __str__(self) -> str:
        pass


q1_text = "Столица Армении"
q1_v1 = "Ереван"
q1_v2 = "Тбилиси"
q1_v3 = "Кутаиси"
q1_v4 = "Баку"
q1_right = 1

q2_text = "Кто владеет Амазон"
q2_v1 = "Безос"
q2_v2 = "Маск" 
q2_v3 = "Гейтс"
q2_v4 = "Путин"
q2_right = 1

q3_text = "Ответ на вопрос"
q3_v1 = "Нет ответа"
q3_v2 = "7" 
q3_v3 = "42"
q3_v4 = "Путин"
q3_right = 3

q4_text = "Столица Мадагаскара"
q4_v1 = "Анкара"
q4_v2 = "Антананариву"
q4_v3 = "Онтарио"
q4_v4 = "Ангола"
q4_right = 2

q5_text = "Кто был первым президентом Совествкого Союза"
q5_v1 = "Ельцин"
q5_v2 = "Ленин" 
q5_v3 = "Горбачёв"
q5_v4 = "Андропов"
q5_right = 3

q6_text = "Кто является дедом Кайло Рена"
q6_v1 = "Энакин Скайуокер"
q6_v2 = "Хан Соло" 
q6_v3 = "Обиван Киноби"
q6_v4 = "Путин"
q6_right = 1

q7_text = "Столица Грузии"
q7_v1 = "Ереван"
q7_v2 = "Тбилиси"
q7_v3 = "Кутаиси"
q7_v4 = "Баку"
q7_right = 2

q8_text = "Кто владеет The Boring Company"
q8_v1 = "Безос"
q8_v2 = "Маск" 
q8_v3 = "Гейтс"
q8_v4 = "Путин"
q8_right = 2

q9_text = "9 - 2"
q9_v1 = "Нет ответа"
q9_v2 = "7" 
q9_v3 = "42"
q9_v4 = "Путин"
q9_right = 2

q10_text = "Столица Азербайджана"
q10_v1 = "Ереван"
q10_v2 = "Тбилиси"
q10_v3 = "Кутаиси"
q10_v4 = "Баку"
q10_right = 4


def main():
    q1 = Question(q1_text, q1_v1, q1_v2, q1_v3, q1_v4, q1_right)
    q2 = Question(q2_text, q2_v1, q2_v2, q2_v3, q2_v4, q2_right)
    q3 = Question(q3_text, q3_v1, q3_v2, q3_v3, q3_v4, q3_right)
    q4 = Question(q4_text, q4_v1, q4_v2, q4_v3, q4_v4, q4_right)
    q5 = Question(q5_text, q5_v1, q5_v2, q5_v3, q5_v4, q5_right)
    q6 = Question(q6_text, q6_v1, q6_v2, q6_v3, q6_v4, q6_right)
    q7 = Question(q7_text, q7_v1, q7_v2, q7_v3, q7_v4, q7_right)
    q8 = Question(q8_text, q8_v1, q8_v2, q8_v3, q8_v4, q8_right)
    q9 = Question(q9_text, q9_v1, q9_v2, q9_v3, q9_v4, q9_right)
    q10 = Question(q10_text, q10_v1, q10_v2, q10_v3, q10_v4, q10_right)

    question_list = {1: q1, 2: q2, 3: q3, 4: q4, 5: q5,
                     6: q6, 7: q7, 8: q8, 9: q9, 10: q10}

    # Раунд для игрока 1:
    print("~~~Раунд для игрока №1~~~")
    question_list, p1_counter = round(question_list)
    
    # Раунд для игрока 2
    print("~~~Раунд для игрока №2~~~")
    question_list, p2_counter = round(question_list)
    
    print(f"Игрок 1 набрал {p1_counter} очков!")
    print(f"Игрок 2 набрал {p2_counter} очков!")
   
    if p1_counter > p2_counter:
        print("Игрок 1 победил!") 
    elif p1_counter < p2_counter:
        print("Игрок 2 победил!")
    else:
        print("Ничья!")


def round(dct: dict):
    counter = 0

    for i in range(5):
        # q_num = random(len(dct))
        round_question = random.choice(list(dct.items()))
        value = round_question[1]
        del dct[round_question[0]]
                
        print(f"Раунд {i + 1}.")
        
        print("Вопрос: ", end=" ")
        print(value.get_question(), end="?\n")
        
        print("Варианты ответа:")
        print(f"1. {value.get_var_1()}")
        print(f"2. {value.get_var_2()}")
        print(f"3. {value.get_var_3()}")
        print(f"4. {value.get_var_4()}")
        print()
        
        print("Введите номер ответа: ")
        answer = input(">>> ")

        print()

        if int(answer) == value.get_right_num():
            counter += 1

    return dct, counter


if __name__ == "__main__":
    main()
