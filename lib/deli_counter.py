katz_deli = []

def line(deli_line):
    if len(deli_line) <= 0:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently:"
        for index, person in enumerate(deli_line):
            current_line += f" {index + 1}. {person}"
        print(current_line)

def take_a_number(deli_line, new_person):
    deli_line.append(new_person)
    print(f"Welcome, {new_person}. You are number {len(deli_line)} in line.")

def now_serving(deli_line):
    if len(deli_line) > 0:
        print(f"Currently serving {deli_line[0]}.")
        deli_line.pop(0)

    else:
        print("There is nobody waiting to be served!")