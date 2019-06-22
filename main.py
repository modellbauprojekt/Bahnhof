#! /usr/bin/env python3
"""
main.py
This is executed on 
boot of the RPi Zero W

Dependencies:

bluetooth.py:
    Wrapper around the socket module,
    providing the
    bluetooth.Connection class
    with one important function:
    bluetooth.Connection.send() 
"""
import bluetooth

"""
config.py:
    Configuration file,
    providing many config-variables,
    that might differ, depending on what
    Station this is.
"""
import config


"""
Functions:

main(): 
    Main function executing other functions
"""


"""
main:
    Arguments:
        argv : Arguments on the Commandline
    Returns:
        Number, used to return to the OS.
        If you return 0, there is no Error,
        else there is.

Comment:
    Program exits, if the function exits.
"""
def main(argv):
    connection = bluetooth.Connection (
        server = bluetooth.server_address(),
        port = 3
    )
    connection.send(bytes("REQ:{Config.}:1", "UTF-8"))

if __name__ == '__main__':
    exit(main(sys.argv))
