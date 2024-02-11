from classes import employees


def main():

    supervisor = employees.ShiftSupervisor("Gayorgyi Semenovich", 123,
                                           5000, 5432)
    
    print(supervisor)
    

if __name__ == "__main__":
    main()