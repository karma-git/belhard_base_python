#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wppr_calculator
from prettytable import PrettyTable


def regular_obj_exceptions(*args):
    """
    :param args: The method take and print an error if found it
    :return: args or none
    """
    try:
        for i in args:
            i = float(i)
            if i <= 0:
                print(f"{i} less then 0!")
                break
        else:
            return args
    except ValueError:
        print(f"{i} must be decimal")


def add_wpps_args():
    """
    The method to take args for WallPaper
    :return: params
    """
    roll_weight = input("Roll width in cm: ")
    roll_length = input("Roll length in m: ")
    if regular_obj_exceptions(roll_weight, roll_length):
        return float(roll_weight), float(roll_length)
    else:
        print("something goes wrong")


def add_room_args():
    """
    The method to take args for Room
    :return: params
    """
    x = input("Room length in m: ")
    y = input("Room length in m: ")
    z = input("Room height in m: ")
    if regular_obj_exceptions(x, y, z):
        return float(x), float(y), float(z)
    else:
        print("something goes wrong")


def main():
    wpps_args = add_wpps_args()
    wpps = wppr_calculator.WallPapers(wpps_args[0] / 100, wpps_args[1])  # arg[0] cm - to m
    room_args = add_room_args()
    room = wppr_calculator.Room(room_args[0], room_args[1], room_args[2])

    def add_excess_obj():
        """
        The method asks user to input a room / excess object params and put them in instance Room
        :return none
        """
        # while True:
        #     handler = input("Do you need exclude from room square an object? Y / N: ")
        #     if handler == 'N':
        #         break
        #     elif handler == 'Y':
        try:
            length = float(input("Please enter an object length, m: "))
            weight = float(input("Please enter an object weight, m: "))
            if length > 0 and weight > 0:
                description = input("Please enter an object description: ")
                room.add_excess_object(length, weight, description)
                # continue
            else:
                print(f"len & weight. Must be higher than 0!")
        except ValueError:
            print(f"incorrect value for len / weight")
            # else:
            #     print(f" {handler} Can not be recognized as known command, try again or press N")

    def print_objects():
        """
        The method prints all object from Room.excess_obj_list
        Plus their params via cls NamedObject property_dictionary method
        :return:
        """
        objects_list = room.excess_sqr_list
        table = PrettyTable()
        table.field_names = ["description", "length", "width", "square"]
        for element in objects_list:
            elem_dict = element.property_dictionary()
            table.add_row([elem_dict['description'], elem_dict['length'],
                           elem_dict['width'], elem_dict['square']])
        else:
            return table

    def del_object_from_ex_lst():
        """
        The method deletes an object from Room.excess_obj_list by description
        :return: "{The object} has been deleted" or "There are no {object}"
        """
        search = input("Input an object name(description) :")
        search_list = room.excess_sqr_list
        for i in search_list:
            if i.property_dictionary()['description'] == search:
                room.excess_sqr_list.remove(i)
                print(f"an object {search} has been deleted")
                break
        else:
            print(f"There are no {search} object")
        # if search in room.excess_sqr_list:
        #     room.excess_sqr_list.remove(search)
        #     # return f"an object {search} has been deleted"
        #     print("an object {search} has been deleted")
        # else:
        #     print(f"There are no {search} object")
        #     # return f"There are no {search} object"

    def clear_ex_list():
        """
        The method
        """
        room.excess_sqr_list.clear()
        print(f"List has been cleared.")
        # return f"List has been cleared."

    def stats_print():
        """
        The method print room / excess stats
        :return: none
        """
        total_sqr = room.sqr()
        wp_sqr = room.wallpapers_sqr()
        print(f"Total square of the room - {total_sqr}"
              f"\nSquare for hang wallpapers {wp_sqr}")

    def rolls_count():
        """
        The method take args from user and put them in instance WallPaper
        :return:
        """
        wp_count = room.roll_count()
        print(f"Needs {wp_count} rolls of the wallpaper")

    #TODO: Ask an user to work with excess objects or print results:
    print(f"Do you want to interact with an object/s "
          f"\nwhich needs to be excluded from the final square?\n"
          f"If so -> press Y\n"
          f"Else: -> N (You will take params for hang wallppprs)\n")
    # interact = input("Press: Y or N: ")
    while True:
        interact = input("Press: Y or N: ")
        if interact == 'Y':
            print(f"Interact options:\n"
                  f"add - to add an excess object\n"
                  f"show - to show which objects already exists\n"
                  f"remove - to remove an object by name(description)\n"
                  f"clear - to delete all objects which exists")
            action = input("Select an action: ")
            if action == "add":
                add_excess_obj()
            elif action == "show":
                print(print_objects())
            elif action == "remove":
                del_object_from_ex_lst()
            elif action == "clear":
                clear_ex_list()
            else:
                print(f"{action} is unknown command.\n"
                      f"Please try again.")
        elif interact == 'N':
            break
        else:
            print(f"{interact} cannot be recognized as known command.\n"
                  f"Please try again.")
    stats_print()
    rolls_count()
    ###WINDOOR # ACTIONS#
#    add_excess_obj()
#     if room.excess_sqr_list:  # temp
#         print_objects()


main()
