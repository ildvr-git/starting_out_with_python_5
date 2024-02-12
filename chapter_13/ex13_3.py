import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.submid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        self.gallons_promt = tkinter.Label(self.top_frame,
                                           text="Введите количество галлонов: ")
        self.gallons_input = tkinter.Entry(self.top_frame)

        self.miles_promt = tkinter.Label(self.mid_frame,
                                         text="Введите количество миль: ")
        self.miles_input = tkinter.Entry(self.mid_frame)

        self.result_descr = tkinter.Label(self.submid_frame,
                                         text="MPG: ")
        
        self.value = tkinter.StringVar()
        self.result_text = tkinter.Label(self.submid_frame,
                                         textvariable=self.value)
        
        self.action_button = tkinter.Button(self.bottom_frame,
                                            text="Посчитать MPG",
                                            command=self.get_result)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Выйти",
                                          command=self.main_window.destroy)
        
        self.action_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.result_descr.pack(side="left")
        self.result_text.pack(side="left")

        self.gallons_promt.pack(side="left")
        self.gallons_input.pack(side="left")
        
        self.miles_promt.pack(side="left")
        self.miles_input.pack(side="left")

        self.top_frame.pack()
        self.mid_frame.pack()
        self.submid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def get_result(self):
        gallons = float(self.gallons_input.get())
        miles = float(self.miles_input.get())
        result = miles/gallons
        self.value.set(result)

if __name__ == "__main__":
    my_gui = MyGUI()
