# Objectives

# The Python function print() must be used at least three times


# whoami
# ip a
# lshw -short
# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.
# Instead of os.system() function, utilize the subprocess module instead. Refer to python.org for how this can be achieved.



# This will not run on windows needs to be mac or linux due to os being bash

import subprocess
import os

computer = "whoami"
ipa = "ifconfig"
lshw = "lshw -short"

print("Who am I?")
os.system(computer)
print("What is my network configuration?")
subprocess.run(ipa)
print("What is my type of hardware?")
os.system(lshw)
