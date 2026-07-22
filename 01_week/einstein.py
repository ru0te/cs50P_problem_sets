def calculate_energy():
    mass = int(input("Enter mass: "))
    light_speed = 300000000
    return mass * (light_speed * light_speed)


def main():
    result = calculate_energy()
    print(f"E: {result}")


if __name__ == "__main__":
    main()
