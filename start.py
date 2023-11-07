import subprocess
import os
subprocess.call(["pip", "install", "-r", "assets/requirements.txt"])
from utils import inputs
os.system('cls' if os.name == 'nt' else 'clear')
print(r'''
  /$$$$$$  /$$$$$$ /$$      /$$ /$$
 /$$__  $$|_  $$_/| $$$    /$$$|__/
| $$  \ $$  | $$  | $$$$  /$$$$ /$$
| $$$$$$$$  | $$  | $$ $$/$$ $$| $$
| $$__  $$  | $$  | $$  $$$| $$| $$
| $$  | $$  | $$  | $$\  $ | $$| $$
| $$  | $$ /$$$$$$| $$ \/  | $$| $$
|__/  |__/|______/|__/     |__/|__/
''')
print('\033[1;35m[Control] ->','\033[1;34m[F1] Aimbot: Always On/Hold Mode')
print('\033[1;35m          ->','\033[1;34m[Mouse4] Hold Mode: Press/Release')
print('\033[1;35m          ->','\033[1;34m[0] Exit')
print('\033[1;33m\n[Tips] Press F1 to set mode\n')
inputs.aimbot(ENABLE_AIMBOT=True)
