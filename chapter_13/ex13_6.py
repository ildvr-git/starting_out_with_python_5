import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_fr = tkinter.Frame()
        self.mid_fr = tkinter.Frame()
        self.bot_fr = tkinter.Frame()

        self.desc_label = tkinter.Label(self.top_fr,
                                        text="Выберите услуги: ")
        
        self.chb1_var = tkinter.IntVar()
        self.chb2_var = tkinter.IntVar()
        self.chb3_var = tkinter.IntVar()
        self.chb4_var = tkinter.IntVar()
        self.chb5_var = tkinter.IntVar()
        self.chb6_var = tkinter.IntVar()
        self.chb7_var = tkinter.IntVar()
        
        # self.chb1_var.set(1)
        # self.chb2_var.set(2)
        # self.chb3_var.set(0)
        # self.chb4_var.set(0)
        # self.chb5_var.set(0)
        # self.chb6_var.set(0)
        # self.chb7_var.set(0)

        self.chb1 = tkinter.Checkbutton(self.mid_fr,
                                        text="Замена масла",
                                        variable=self.chb1_var)
        self.chb2 = tkinter.Checkbutton(self.mid_fr,
                                        text="смазочные работы",
                                        variable=self.chb2_var)
        self.chb3 = tkinter.Checkbutton(self.mid_fr,
                                        text="промывка радиатора",
                                        variable=self.chb3_var)
        self.chb4 = tkinter.Checkbutton(self.mid_fr,
                                        text="замена жидкости в трансмиссии",
                                        variable=self.chb4_var)
        self.chb5 = tkinter.Checkbutton(self.mid_fr,
                                        text="осмотр",
                                        variable=self.chb5_var)
        self.chb6 = tkinter.Checkbutton(self.mid_fr,
                                        text="замена глушителя выхлопа",
                                        variable=self.chb6_var)
        self.chb7 = tkinter.Checkbutton(self.mid_fr,
                                        text="перестановка шин",
                                        variable=self.chb7_var)
        
        self.chb1.pack(side="top")
        self.chb2.pack(side="top")
        self.chb3.pack(side="top")
        self.chb4.pack(side="top")
        self.chb5.pack(side="top")
        self.chb6.pack(side="top")
        self.chb7.pack(side="top")

        self.action_but = tkinter.Button(self.bot_fr,
                                         text="Показать стоимость",
                                         command=self.action)
        self.exit_but = tkinter.Button(self.bot_fr,
                                       text="Выйти",
                                       command=self.main_window.destroy)
        
        self.action_but.pack(side="left")
        self.exit_but.pack(side="right")
        
        self.result = tkinter.StringVar()
        self.result_label = tkinter.Label(self.bot_fr,
                                          textvariable=self.result)
        
        self.result_label.pack(side="bottom")

        self.top_fr.pack()
        self.bot_fr.pack()
        self.mid_fr.pack()
        
        tkinter.mainloop()

    def action(self):
        result = 0

        if self.chb1_var.get() == 1:
             result += 500
        if self.chb2_var.get() == 1:
             result += 300
        if self.chb3_var.get() == 1:
             result += 700
        if self.chb4_var.get() == 1:
             result += 1000
        if self.chb5_var.get() == 1:
             result += 800
        if self.chb6_var.get() == 1:
             result += 1300
        if self.chb7_var.get() == 1:
             result += 900

        self.result.set(result)
        
         
if __name__ == "__main__":
    my_gui = MyGUI()
