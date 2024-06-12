import os.path
import shutil

CURRENT_FILE = (os.path.abspath(__file__))  # /Users/goncharov/QAGURU/homework7/script_os.py
CURRENT_DIR = os.path.dirname(CURRENT_FILE)  # /Users/goncharov/QAGURU/homework7

TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
print(TMP_DIR)  # /Users/goncharov/QAGURU/homework7/tmp

if not os.path.exists('tmp2'):
    os.mkdir('tmp2')
    print('Создал tmp2')
else:
    print('Не создал, уже есть.')

shutil.rmtree(os.path.join(CURRENT_DIR, 'tmp2'))