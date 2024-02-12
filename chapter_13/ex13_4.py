import tkinter


class MyGUI():
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.descr_frame = tkinter.Frame()
        self.input_frame = tkinter.Frame()
        self.output_frame = tkinter.Frame()
        self.buttons_frame = tkinter.Frame()

        self.descr_label = tkinter.Label(self.descr_frame,
                                         text="Эта программа конвертирует показания " +
                                              "\nтемпературы по шкале Цельсия в " +
                                              "\nтемпературу по шкале Фаренгейта.")
        self.descr_label.pack()
        self.descr_frame.pack()

        self.input_promt = tkinter.Label(self.input_frame,
                                         text="Введите показатель температуры" +
                                              "\nв градусах Цельсия: ")
        self.value = tkinter.StringVar()
        self.input_field = tkinter.Entry(self.input_frame)

        self.input_promt.pack(side="left")
        self.input_field.pack(side="left")
        self.input_frame.pack()

        self.output_descr = tkinter.Label(self.output_frame,
                                          text="Введённая температура по шкале Фаренгейта: ")
        self.output_field = tkinter.Label(self.output_frame,
                                          textvariable=self.value)

        self.output_descr.pack(side="left")
        self.output_field.pack(side="left")
        self.output_frame.pack()

        self.action_button = tkinter.Button(self.buttons_frame,
                                            text="Конвертировать",
                                            command=self.convert)
        self.exit_button = tkinter.Button(self.buttons_frame,
                                          text="Выход",
                                          command=self.main_window.destroy)

        self.action_button.pack(side="left")
        self.exit_button.pack(side="left")
        self.buttons_frame.pack()

        tkinter.mainloop()

    def convert(self):
        temper_c = self.input_field.get()
        temper_f = (9*float(temper_c))/5+32
        self.value.set(temper_f)

if __name__ == "__main__":
    my_gui = MyGUI()
