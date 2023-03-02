import os
import shutil

from_dir = "C:/Users/ilina/Downloads"
to_dir = "C:/Users/ilina/Downloads/sample"

listoffiles=os.listdir(from_dir)
print(listoffiles)

for file_name in listoffiles:
    name, extension = os.path.splitext(file_name)
