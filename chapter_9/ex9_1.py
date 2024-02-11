def main():
    rooms = {"CS101":"3004", "CS102":"4501", "CS103":"6755", "NT110":"1244", "CM241":"1411"}
    teachers = {"CS101":"Haynes", "CS102":"Alvarado", "CS103":"Rich", "NT110":"Burke", "CM241":"Lee"}
    time = {"CS101":"8:00 a.m.", "CS102":"9:00 a.m.", "CS103":"10:00 a.m.", "NT110":"11:00 a.m.", "CM241":"1:00 p.m."}

    search = input("Enter a course number >>> ")
    while search not in rooms.keys():
        search = input("Course number not found! Enter a course number again >>> ")
    
    print(f"{search} course:")
    header = "Room\tCourse time\tTeacher"
    print(header)
    print("`"*(len(header) + 7))
    print(f"{rooms[search]}\t{time[search]}\t{teachers[search]}")

if __name__ == "__main__":
    main()
    

