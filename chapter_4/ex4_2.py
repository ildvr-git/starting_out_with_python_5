CALORIES_PER_MIN = 4.2
for n in range(10, 31, 5):
    print("За {} минут сожжётся".format(n) +
          "{: .1f} калорий".format(CALORIES_PER_MIN*n))