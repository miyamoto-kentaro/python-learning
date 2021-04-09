import os
import pathlib

# print(os.path.exists('./somefiles/test.txt'))
# print(os.path.isfile('./somefiles/test.txt'))
# print(os.path.isdir('./somefiles'))

pathlib.Path('empty.txt').touch()
