import tkinter


class MyGui:
    
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.top_fr = tkinter.Frame()
        self.bot_fr = tkinter.Frame()

        self.value = tkinter.StringVar()
        self.info_label = tkinter.Label(self.top_fr,
                                        textvariable=self.value)
        
        self.info_label.pack()
        self.top_fr.pack()
        
        self.action_button = tkinter.Button(self.bot_fr,
                                            text="Показать инфо",
                                            command=self.show_info)
        self.exit_button = tkinter.Button(self.bot_fr,
                                          text="Выйти",
                                          command=self.main_window.destroy)
        
        self.action_button.pack(side="left")
        self.exit_button.pack(side="left")
        
        self.bot_fr.pack()
        
        tkinter.mainloop()
        
    def show_info(self):
        self.value.set(
            "162390, Россия. Вологодская обл.," +
            "\n г. Великий Устюг," +
            "\n Почта Деда Мороза"
        )
        
            
if __name__ == "__main__":
    my = MyGui()
        