# Во входных данных из книги есть косяк, в строке 91 (относится к 1993 году)
# было значение World Series Not Played in 1994, хотя в этот год победителем была
# Toronto Blue Jays => произошло смещение. В новой версии файла в папке data добавил в строку
# 91 Toronto Blue Jays и сместил всё, что ниже, на одну строку вниз.

import io

def main():
    file = io.open(f"chapter_9\data\WorldSeriesWinners.txt", mode="r", encoding="utf-8")
    lst = [x.rstrip("\n") for x in file.readlines()]
    winners_set = set([x for x in lst if "Not Played" not in x])
    file.close()

    win_counters = count_wins(winners_set, lst)
    years = get_years(lst)
    
    user_year = input("Enter a year >>> ")
    while not user_year.isdigit() or int(user_year) < 1903 or int(user_year) > 2009:
        user_year = input("Wrong input! Year must be betwenn 1903 and 2009! Enter a year again >>> ")
    
    try:
        print(f"Team that won World Series that year is {years[user_year]}!\n" + \
              f"Number of times that team has won the World Series is {win_counters[years[user_year]]}.")
    except KeyError:
        print(years[user_year])

def count_wins(in_set, lst):
    dict = {}
    for i in in_set:
        counter = 0
        for j in lst:
            if i == j:
                counter += 1
        dict[i] = counter
    return dict
    
def get_years(lst):
    dict = {}
    year = 1903
    for item in lst:
        dict[str(year)] = item
        year += 1
    return dict

if __name__ == "__main__":
    main()
    
