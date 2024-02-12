import tkinter


class MyGui:

    def __init__(self) -> None:
        
        self.main_window = tkinter.Tk()

        self.rate_frame = tkinter.Frame(self.main_window)
        self.rate_desc_label = tkinter.Label(self.rate_frame,
                                             text="Выберите категорию тарифа: ")
        self.radio_var = tkinter.IntVar()
        self.rb1 = tkinter.Radiobutton(self.rate_frame,
                                       text="Дневное время (с 6:00 до 17:59)",
                                       variable=self.radio_var,
                                       value=12)
        self.rb2 = tkinter.Radiobutton(self.rate_frame,
                                       text="Вечернее время (с 18:00 до 23:59)",
                                       variable=self.radio_var,
                                       value=10)
        self.rb3 = tkinter.Radiobutton(self.rate_frame,
                                       text="Непиковый период (с полуночи до 5:59)",
                                       variable=self.radio_var,
                                       value=5)
        
        self.rate_desc_label.pack(side="top")
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rate_frame.pack()

        self.entry_frame = tkinter.Frame(self.main_window)
        self.entry_descr = tkinter.Label(self.entry_frame,
                                         text="Введите кол-во минут: ")
        self.entry_field = tkinter.Entry(self.entry_frame,
                                         width=10)
        self.entry_descr.pack(side="left")
        self.entry_field.pack(side="left")
        self.entry_frame.pack()

        self.res_frame = tkinter.Frame(self.main_window)
        self.res_descr = tkinter.Label(self.res_frame,
                                       text="Стоимость вызова составит: ")
        self.result = tkinter.StringVar()
        self.res_field = tkinter.Label(self.res_frame,
                                       textvariable=self.result)
        self.res_descr.pack()
        self.res_field.pack()
        self.res_frame.pack()
                
        self.but_frame = tkinter.Frame(self.main_window)
        self.action_but = tkinter.Button(self.but_frame,
                                         text="Расчитать",
                                         command=self.action)
        self.exit_but = tkinter.Button(self.but_frame,
                                       text="Выйти",
                                       command=self.main_window.destroy)
        self.action_but.pack(side="left")
        self.exit_but.pack(side="left")
        self.but_frame.pack()
        
        tkinter.mainloop()

    def action(self):
        rate = self.radio_var.get()
        minutes = self.entry_field.get()
        result = rate*int(minutes)
        self.result.set(str(result))


if __name__ == "__main__":
    my = MyGui()


        
        
        
        