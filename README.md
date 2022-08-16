# Arduino-PRO
Python script to create a professional Arduino coding environment for Visual Studio Code

Installation

1. Download the Arduino CLI extension and paste the .exe file in the installation folder of Arduino (I.E. C:\Program Files (x86)\Arduino).
2. Download the python APRO file and also paste it in the installation folder of Arduino.
3. Open Visual Studio Code and install VsCode Action Buttons extension.
4. Open the extension setting of the VsCode Action Buttons and edit the settings.json file, which can also be seen in https://www.youtube.com/watch?v=5IuZ-E8Tmhg&t=524s&ab_channel=YuriR at 8:35.
5. Copy and paste the following json in the settings.json file
{
    "actionButtons": {

        "defaultColor": "white",
        "reloadButton": "Reload",
        "commands": [
            {
                "name" : "Clean",
                "color" : "white",
                "command" : "apro.py -c"
            },
            {
                "name" : "Build",
                "color": "white",
                "command": "apro.py -b"
            },
            {
                "name" : "Run",
                "color" : "white",
                "command" : "apro.py -u"
            },
            {
                "name" : "Serial Port",
                "color" : "white",
                "command" : "apro.py -m"
            },
            {
                "name" : "Burn",
                "color" : "white",
                "command" : "apro.py -l"
            }
        ]
    },
    "terminal.integrated.defaultProfile.windows": "Git Bash", //Change default terminal 
}

6. For a vscode project example see tme_vuurtoren project.
