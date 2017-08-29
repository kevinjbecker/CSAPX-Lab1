"""
================================
= CSAPX Lab 1: In-Lab Activity =
================================

date: 08/29/2017
desc: A program that creates a simplified turtle interpreter, called TinyTurtle.
auth: Kevin Becker
"""

import turtle       # forward, length, mainloop
#import sys          # argv


def main() -> None:
    input_command = input("Please enter your TinyTurtle command string: ");
    evaluate(input_command)
    turtle.mainloop()


def evaluate(cmd : str) -> None:
    while len(cmd) > 0:
        if len(cmd) == 4 or len(cmd) == 1:
            length = len(cmd)
        else:
            length = cmd.index(" ")
        temp_cmd = cmd[0:length]
        cmd_type = temp_cmd[0] # type of command (eg. 'U', 'B', 'C')
        if cmd_type == 'U':
            turtle.up()
        elif cmd_type == 'D':
            turtle.down()

        num_pixels = int(temp_cmd[1:])

        if cmd_type == 'F':
            turtle.forward(num_pixels)
        elif cmd_type == 'B':
            turtle.backward(num_pixels)
        elif cmd_type == 'L':
            turtle.left(num_pixels)
        elif cmd_type == 'R':
            turtle.right(num_pixels)
        elif cmd_type == 'C':
            turtle.circle(num_pixels)
        cmd = cmd[length+1:]


if __name__ == '__main__':
    main()
