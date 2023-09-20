# Importing Libraries
import os
from pathlib import Path
from filecmp import cmp
from tkinter import Tk
from tkinter.filedialog import askdirectory


# list of all documents
# DATA_DIR = Path('C:\Users\saurabh\Documents')
DATA_DIR = Path("D:\c_exercises")
# files = sorted(os.listdir(DATA_DIR))

# DATA_DIR= askdirectory(title="select a folder")
# print(path)
# full_path=os.path.join(path,file_x)
files = sorted(os.listdir(DATA_DIR))
print(files)

# List having the classes of documents
# with the same content
duplicateFiles = []

# comparison of the documents
for file_x in files:

	if_dupl = False

	for class_ in duplicateFiles:
		# Comparing files having same content using cmp()
		# class_[0] represents a class having same content
		if_dupl = cmp(
			DATA_DIR / file_x,
			DATA_DIR / class_[0],
			shallow=False
		)
		if if_dupl:
			class_.append(file_x)
			break

	if not if_dupl:
		duplicateFiles.append([file_x])

# Print results
print(duplicateFiles)







# # Importing Libraries
# import os
# from pathlib import Path
# from filecmp import cmp


# # list of all documents
# DATA_DIR = Path(r"C:/Users/saurabh/Documents")
# files = sorted(os.listdir(DATA_DIR))

# # List having the classes of documents
# # with the same content
# duplicateFiles = []

# # comparison of the documents
# for file_x in files:

# 	if_dupl = False

# 	for class_ in duplicateFiles:
# 		# Comparing files having same content using cmp()
# 		# class_[0] represents a class having same content
# 		if_dupl = cmp(
# 			DATA_DIR / file_x,
# 			DATA_DIR / class_[0],
# 			shallow=False
# 		)
# 		if if_dupl:
# 			class_.append(file_x)
# 			break

# 	if not if_dupl:
# 		duplicateFiles.append([file_x])

# # Print results
# print(duplicateFiles)

