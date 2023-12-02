''' tests bluetooth message from smartphone'''
from piRover_bluetooth import *

bluetooth_init()

while True:

    command_id, command_value = get_command()
    print(command_id, command_value)