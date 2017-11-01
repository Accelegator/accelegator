""" Routes commands to the REPL """


def route_commands(command, arg1, arg2, arg3):

    if command == "list":
        call = 1

    if command == "show":
        if arg2 == "":
            call = 2
        else:
            call = 3

    if command == "search":
        if arg2 == "":
            call = 4
        else:
            call = 5

    if command == "write":

        if arg1 == "list":
            call = 6

        elif arg1 == "show":
            if arg3 == "":
                call = 7
            else:
                call = 8

        elif arg1 == "search":
            if arg3 == "":
                call = 9
            else:
                call = 10

    if command == "help":
        if arg1 == "":
            call = 11
        else:
            call = 12

    return call
