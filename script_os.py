import os.path

CURRENT_FILE = (os.path.abspath(__file__))  # /Users/goncharov/QAGURU/homework7/script_os.py
CURRENT_DIR = os.path.dirname(CURRENT_FILE)  # /Users/goncharov/QAGURU/homework7

TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)  # /Users/goncharov/QAGURU/homework7/tmp
