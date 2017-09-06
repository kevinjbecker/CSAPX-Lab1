# -*- coding: utf-8 -*-
"""
=============================
| CSAPX Lab 1: TinyTurtyle  |
=============================

date: 09/03/2017
description: A program that creates a simplified turtle interpreter, called TinyTurtle.
author: Kevin Becker
"""

import turtle  # forward, length, mainloop
import sys     # argv


def main() -> None:
    """
    The main function prompts user to enter a command, then simplifies it, and executes it

    :return: None
    """

    # Get the side length from either the command line (if present), or by
    # prompting the user
    if len(sys.argv) == 2:
        input_command = int(sys.argv[1])
    else:
        input_command = input('Welcome to TinyTurtle.\nPlease enter your TinyTurtle command: ')


    simplified_cmds = simplify_cmds(input_command)
    print('Expanded program: ' + simplified_cmds + '\nEvaluating...')
    evaluate(simplified_cmds)
    turtle.mainloop()
    print('Turtle display window has closed, TinyTurtle system will now stop.')


def evaluate(cmd: str) -> None:
    """
    This function evaluates the input TT commands

    :param cmd: the string of basic TT commands to be run

    :return: None
    """

    while len(cmd) > 0:
        if len(cmd) == 4 or len(cmd) == 1:
            cmd_length = len(cmd)
        else:
            cmd_length = cmd.index(" ")
        current_cmd = cmd[0:cmd_length]
        cmd_type = current_cmd[0]  # type of command (eg. 'U', 'B', 'C')

        # runs the commands that don't require a number here (up/down)
        if(cmd_type in ['U','D']):
            if cmd_type == 'U':
                turtle.up()
                cmd_run = 'up'
            elif cmd_type == 'D':
                turtle.down()
                cmd_run = 'down'
            print(cmd_run+'()')
        else:
            # if it gets to this section, the command requires a pixel number (it's not an up or down command)
            num_pixels = int(current_cmd[1:])
            if cmd_type == 'F':
                turtle.forward(num_pixels)
                cmd_run = 'forward'
            elif cmd_type == 'B':
                turtle.backward(num_pixels)
                cmd_run = 'backward'
            elif cmd_type == 'L':
                turtle.left(num_pixels)
                cmd_run = 'left'
            elif cmd_type == 'R':
                turtle.right(num_pixels)
                cmd_run = 'right'
            elif cmd_type == 'C':
                turtle.circle(num_pixels)
                cmd_run = 'circle'
            #prints what command was just run and any associated numbers
            print(cmd_run+'({})'.format(num_pixels))
        # removes the just executed command from the string so it doesn't execute it again
        cmd = cmd[cmd_length + 1:]
    print('System has completed evaluating commands. Waiting for user action...')


def simplify_cmds(cmd_string: str)->str:
    """
    This function simplifies any enhanced TT commands to their simple TT command form
    (Ex. Removes and iterates or polygons

    :param cmd_string: the string of all TT commands to be run

    :return: String
    """

    simplified_cmds = ''
    basic_commands = ['F','B','L','R','C','U','D']
    while len(cmd_string) > 0:
        if cmd_string[0] in basic_commands: # checks if the next command to be tested is a basic or enhanced TT command
            if len(cmd_string) == 4 or len(cmd_string) == 1:
                cmd_length = len(cmd_string)
            else:
                cmd_length = cmd_string.index(' ')
            simplified_cmds += cmd_string[0:cmd_length+1]
            cmd_string = cmd_string[cmd_length+1:] # removes the recently added command from the original string
        elif cmd_string[0] == 'I': # iterate case; these next lines get into the enhanced TT
            """first_at_sign = cmd_string.index('@') # this line checks for nested iterates
            total_iterates = cmd_string[0:first_at_sign].count('I')
            index_of_last_at_sign = 0 # this is needed for expanding iterates in the event there are nested iterates
            for _ in range(0,total_iterates):
                index_of_last_at_sign = cmd_string[index_of_last_at_sign:].index('@')"""
            simplified_cmds += expand_iterate(cmd_string[0:cmd_string.index('@')])# index_of_last_at_sign] , total_iterates) # expands the iterate; the cmd_string.index('<space>@') gives expand_iterate
                                                                                         # only the iteration times and commands to loop
            cmd_string = cmd_string[cmd_string.index('@')+1:]
        elif cmd_string[0] == 'P':
            simplified_cmds += expand_polygon(cmd_string[0:7]) # since a polygon command is always 7 characters in length, we can just slice from 0 to 7 index and it will work
            cmd_string = cmd_string[7:]
    return simplified_cmds


def expand_iterate(iterate_cmd: str)->str: # , total_iterates: int)->str:
    """
    This function expands any iterate TT commands to their simple TT command form
    (Ex. "I3 F100 R120 @" becomes "F100 R120 F100 R120 F100 R120")
    NOTE: I attempted to do the extra credit, however after I thought I completed it,
    I found a case that did not work: "I3 I3 F100 R120 @ I4 F250 R090 @ @" where there are nested iterates,
    just not one in the other. Had I realized this sooner, I would have changed it to work but alas, no extra credit for me

    :param iterate_cmd: the string of the Iterate TT command to be run

    :return: String
    """

    simplified_iterate_cmd = ''
    # index_of_last_i = 0 # this is used to get the inner most I
    #for _ in range(0,total_iterates):
        # index_of_last_at_sign = cmd_string[index_of_last_at_sign:].index('@')
    number_of_iterations = int(iterate_cmd[1])
    iteration_cmd = iterate_cmd[3:] # 3 starts commands; we can assume the end of the string is the end of the commands to iterate since we're only given that when the method is called
    for _ in range(0, number_of_iterations):
        simplified_iterate_cmd += iteration_cmd
    # while simplified_iterate_cmd.index('I') != -1:
        # print('There are nested iterates, attempting to resolve...')
    return simplified_iterate_cmd


def expand_polygon(polygon_cmd: str)->str:
    """
    This function expands any polygon TT commands to their simple TT command form
    (Ex. "P3 100" becomes "F100 L120 F100 L120 F100 L120")

    :param polygon_cmd: the string of all TT commands to be run

    :return: String
    """

    number_of_sides = int(polygon_cmd[1])
    angle_size = int(180 - (((number_of_sides - 2) * 180) / number_of_sides))
    side_length = int(polygon_cmd[3:])
    return expand_iterate('I' + str(number_of_sides) + ' F' + str(side_length) + ' L' + str(angle_size) + ' ') # no '@' is needed since the expand_iterate requires the @ sign to be removed


# only run this program if it is not being imported by another main module
if __name__ == '__main__':
    main()
