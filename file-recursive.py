import os
import sys

walk_dir = sys.argv[1]
for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        print(file_path)
