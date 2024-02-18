# my_file = open("names.txt")
# for name in my_file.readlines():
#     print(f"hello {name}")
# f' חיבור מחרוזות

def add_names_to_file():
    names = []
    for i in range(3):
        name = input(f"Enter name {i + 1}: ")
        names.append(name)

    with open("names.txt", "a") as file:  # Open file in append mode ('a')
        for name in names:
            file.write(name + "\n")

def print_hello_and_names():
    try:
        with open("names.txt", "r") as file:
            names = file.readlines()
            for name in names:
                print(f"Hello {name.strip()}")
    except FileNotFoundError:
        print("No names found in the file")

# Uncomment the following lines to execute the functions
# add_names_to_file()
# print_hello_and_names()
# names = open("names.txt", "w+")
# def new_names():
#     names = []
#     for i in range(3):
#         name = input("type your name:")
#         i = i + 1
#         names.append(name)




