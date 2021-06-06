import subprocess

chosen_freq_number = input("Choose a frequency: 0: 433.89e6, 1: 433.847e6 2: custom\n")
freqs = [433.89e6, 433.847e6]
if chosen_freq_number == "2":
    freqs[2] = input("Choose a frequency\n")

print("recording first")
subprocess.call('python rolljam2.py first_record ' + str(freqs[int(chosen_freq_number)]), shell=True)

print("recording second")
subprocess.call('python rolljam2.py second_record ' + str(freqs[int(chosen_freq_number)]), shell=True)

print("playing first")
subprocess.call('python replay2.py first_record ' + str(freqs[int(chosen_freq_number)]), shell=True)

temp = input("click enter to run second recording")
print("playing second")
subprocess.call('python replay2.py second_record ' + str(freqs[int(chosen_freq_number)]), shell=True)
