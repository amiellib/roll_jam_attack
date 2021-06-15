import subprocess

chosen_freq_number = input("Choose a frequency: 0: 433.89e6, 1: 433.847e6 2: 433.862e6 3:custom\n")
freqs = [433.89e6, 433.847e6, 433.862e6]
if chosen_freq_number == "3":
    freqs[2] = input("Choose a frequency\n")

print("recording first")
subprocess.call('python jam_save_corrected.py first_record ' + str(freqs[int(chosen_freq_number)]), shell=True)

print("recording second")
subprocess.call('python jam_save_corrected.py second_record ' + str(freqs[int(chosen_freq_number)]), shell=True)

print("playing first")
subprocess.call('python replay.py first_record ' + str(freqs[int(chosen_freq_number)]), shell=True)

temp = input("click enter to run second recording")
print("playing second")
subprocess.call('python replay.py second_record ' + str(freqs[int(chosen_freq_number)]), shell=True)
