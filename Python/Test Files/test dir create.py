import os

directory = input("Enter Folder Name: ")

parent_dir = r"C:\Users\shavi\OneDrive\Desktop"

path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '%s' created" %directory)
