import subprocess

while True:
        chosen_number = input("\nChoose: 0: run jamming and recording, 1: run replay, 2: quit\n")
        if chosen_number == 0:
            subprocess.call('python rolljam2.py', shell=True)
        elif chosen_number == 1:
            subprocess.call('python replay2.py', shell=True)
        elif chosen_number == 2:
            break
