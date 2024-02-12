import tkinter


class MyGUI:

    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_fr = tkinter.Frame(self.main_window)
        self.bot_fr = tkinter.Frame(self.main_window)

        self.sinister_button = tkinter.Button(self.top_fr,
                                       text = "Sinister",
                                       command=self.show_translation_sinister)
        self.medium_button = tkinter.Button(self.top_fr,
                                       text = "Medium",
                                       command=self.show_translation_medium)
        self.dexter_button = tkinter.Button(self.top_fr,
                                       text = "Dexter",
                                       command=self.show_translation_dexter)
        
        self.sinister_button.pack(side="left")
        self.medium_button.pack(side="left")
        self.dexter_button.pack(side="left")

        self.descr_label = tkinter.Label(self.bot_fr,
                                         text="Перевод: ")
        
        self.value = tkinter.StringVar()

        self.translation_label = tkinter.Label(self.bot_fr,
                                               textvariable=self.value)
        
        self.descr_label.pack(side="left")
        self.translation_label.pack(side="left")

        self.top_fr.pack()
        self.bot_fr.pack()

        tkinter.mainloop()

    def show_translation_sinister(self):
        # pass
        # if word == "sinister":
        #     self.value.set("Левый") 
        # elif word == "medium":
        #     self.translation.set("Средний")
        # else:
        self.value.set("Левый")
        

    def show_translation_medium(self):
        
        self.value.set("Средний")


    def show_translation_dexter(self):
        
        self.value.set("Правый")


if __name__ == "__main__":
    my_gui = MyGUI()