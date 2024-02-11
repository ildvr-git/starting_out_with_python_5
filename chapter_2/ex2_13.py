ridgge_lenght = float(input("Введите длину гряды в метрах >>> "))
support_space = float(input("Введите величину пространства, занимаемого одной" + 
              " одной концевой опорой в метрах >>> "))
vine_spaings = float(input("Введите расстояние между виноградными лозами в метрах >>> "))

vine_qty = (ridgge_lenght - (2*support_space)) / vine_spaings
print("Количество виноградных лоз, которые" +
      " поместятся на гряде - {} шт.".format(int(vine_qty)))