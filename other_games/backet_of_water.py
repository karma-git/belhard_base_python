from prettytable import PrettyTable
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


table = PrettyTable()

table.field_names = ["\\", "backet A (3l)", "backet B (5l)"]
table.add_row(["fill up the backet\n", "1", "2"])
table.add_row(["empty the backet\n", "3", "4"])
table.add_row(["pour water", "from A to B\n5", "from B to A\n6"])
table.add_row(['\nadd', '\ntype _quit_ for quit', '\ntype _clear_ for \nclear count table'])

table_2 = PrettyTable()
table_2.field_names = ["backet A, Liters", "backet B, Liters", "iteration"]

a, b = 0, 0
i = 0

while True:
    clear()
    print(table)
    print(table_2)
    #    c = int(input("Select an operation: "))
    if b == 4:
        print(f"congratz, the riddle has been passed\nThe backet B has {b} Litres in {i} => iterations")  # vivesti tablicy
        break
    else:
        c = input("select an operation: ")
        if c.isdigit() and int(c) in range(1, 7):
            c = int(c)
        elif c == 'quit' or c == 'clear':
            c = str(c)
        else:
            continue

    i += 1
    if c == 1:  # """Press 1 for pick up the backet A"""
        if a == 0:
            a += 3
        elif a != 0 and a != 3:
            a = 3
        elif a == 3:
            table_2.add_row([a, b, i])
            continue
        table_2.add_row([a, b, i])

    elif c == 2:  # """Press 2 for pick up the backet B"""
        if b == 0:
            b += 5
        elif b == 5:
            table_2.add_row([a, b, i])
            continue
        elif b != 0 and b != 5:
            b = 5
        table_2.add_row([a, b, i])

    elif c == 3:  # """Press 3 for empty the backet A"""
        a = 0
        table_2.add_row([a, b, i])

    elif c == 4:  # """Press 4 for empty the backet B"""
        b = 0
        table_2.add_row([a, b, i])

    elif c == 5:  # """Press 5 for pour a water from backet A to backet B"""
        if b + a > 5:
            a -= 5 - b
            a = abs(a)
            b += 3 - a
        else:
            b += a
            a = 0
        table_2.add_row([a, b, i])

    elif c == 6:  # """Press 6 for pour a water from backet B to backet A"""
        if a + b > 3:
            b -= 3 - a
            b = abs(b)
            a += 5 - b
        else:
            a += b
            b = 0
        table_2.add_row([a, b, i])

    elif c == 'quit':
        print(f"bye, we looking forward for your returning!")
        quit()
    elif c == 'clear':
        clear()
        table_2 = PrettyTable()
        table_2.field_names = ["backet A, Liters", "backet B, Liters", "iteration"]
        table_2.add_row([a, b, i])
        continue
