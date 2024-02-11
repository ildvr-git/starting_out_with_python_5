import my_classes as c

def main():
    my_car = c.Car("LADA", 1972)

    for i in range(5):
        my_car.accelerate()
        print(f"После ускорения скорость составляет {my_car.get_speed()}")
            
    for i in range(5):
        my_car.brake()
        print(f"После торможения скорость составляет {my_car.get_speed()}")

if __name__ == "__main__":
    main()