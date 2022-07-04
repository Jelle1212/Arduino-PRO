#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import json
import argparse

#subprocess.run(f"arduino-cli compile -b arduino:samd:arduino_zero_native --libraries ./libraries -e")

class Compiler:
    """
    This is the compiler class, where the different settings and functionalities are stored
    """
    def __init__(self, board, port, baudrate, programmer):
        self.board = board
        self.port = port
        self.baudrate = baudrate
        self.programmer = programmer

    def print_settings(self):
        """
        Print the settings of the JSON file in the vscode folder
        """
        print("Board: " + self.board)
        print("Port: " + self.port)
        print("Baudrate: " + self.baudrate)
        print("Programmer: " + self.programmer) 

    def build(self):
        """
        Build the project with its corresponding settings
        """
        command = "arduino-cli compile -b " + self.board + " --libraries ./libraries -e"
        subprocess.run(f"{command}")

    def upload(self):
        """
        Upload the HEX to the board

        $ arduino-cli board details -b arduino:samd:arduino_zero_native --list-programmers
        
        Id        Programmer name
        edbg      Atmel EDBG
        atmel_ice Atmel-ICE
        sam_ice   Atmel SAM-ICE
        jlink     Segger J-Link
        """

        if self.programmer == "none":
            command = "arduino-cli upload -b " + self.board + " -p " + self.port
        else:
            command = "arduino-cli upload -b " + self.board + " -P " + self.programmer

        subprocess.run(f"{command}")

    def burn_bootloader(self):
        """
        Burn the corresponding bootloader to the board
        """
        command = "arduino-cli burn-bootloader -b " + self.board + " -P " + self.programmer
        subprocess.run(f"{command}")

    def clean(self):
        """
        Clean the project
        """
        command = "arduino-cli compile --clean -b " + self.board + " --libraries ./libraries -e"
        subprocess.run(f"{command}")
    
    def monitor(self):
        """
        Open the Serial Monitor of the board
        """
        command = "arduino-cli monitor -p " + self.port + " -c baudrate=" + self.baudrate
        subprocess.run(f"{command}")

        




def get_apro_settings():
    """
    Find the settings for the compiler in the apro_settings.json file which lies in the .vscode folder

    Example of an apro_settins.json:
    {
    "board" : "arduino:samd:arduino_zero_native",
    "port"  : "COM7",
    "baudrate" : "115200"
    }
    """
    path = os.getcwd() + "/.vscode/apro_settings.json"
    with open(path, "r") as file:
        settings = json.load(file)
        board = settings['board']
        port = settings['port']
        baud = settings['baudrate']
        programmer = settings['programmer']
    
    return board, port, baud, programmer

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Python Arduino-CLI script for embedded development in Visual Studio Code")
    parse.add_argument("-b", "--build", action="store_true", help="Build the Arduino project")
    parse.add_argument("-u", "--upload", action="store_true", help="Upload the compiled Arduino project")
    parse.add_argument("-c", "--clean", action="store_true", help="Clean the Arduino project")
    parse.add_argument("-m", "--monitor", action="store_true", help="Open the Serial Monitor")
    parse.add_argument("-l", "--burn", action="store_true", help="Burn bootloader")

    #Excute parse_args()

    args = parse.parse_args()
    board, port, baud, programmer = get_apro_settings()
    arduino = Compiler(board=board, port=port, baudrate=baud, programmer=programmer)

    if args.build:
        print("Building...")
        arduino.print_settings()
        arduino.build()
    elif args.upload:
        print("Uploading...")
        arduino.print_settings()
        arduino.build()
        arduino.upload()
    elif args.clean:
        print("Cleaning...")
        arduino.print_settings()
        arduino.clean()
    elif args.monitor:
        print("Monitoring...")
        arduino.monitor()
    elif args.burn:
        print("Burning...")
        arduino.burn_bootloader()
    else:
        print("Nothing to do here...")