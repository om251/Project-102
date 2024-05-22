import os
import shutil

from_dir = "/Users/ompatel/Downloads"
to_dir = "/Users/ompatel/Documents/Python/PRO-C102- AUTOMATE FILE SEGREGATION/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, ext = os.path.splitext(i)
    print(name, ext)
    if ext == "":
        continue
    if ext == ".pdf" or ext == ".doc" or ext == ".docx" or ext == ".txt":
        path1 = os.path.join(from_dir, i)  # Use os.path.join for creating paths
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(to_dir, "Document_Files", name)  # Append the extension to the file name
   
        if os.path.exists(path2):
            print("Moving" + name + "to" + "......")
            shutil.move(path1, path3)

        else:
            os.makedirs(path2)
            print("Moving" + name + "to" + "......")
            shutil.move(path1, path3)