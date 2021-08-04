from pathlib import Path

# Absolute path
# c:\Program Files\Microsoft
# /usr/local/bin
# Relative path

# path = Path("ecommerce")
# print(path.exists()) # Check if the directory exists
#
# path = Path("emails")
# print(path.mkdir())  # Create the directory
#
# path = Path("ecommerce")
# print(path.rmdir())  # Remove the directory

path = Path()
# print(path.glob("*"))  # Searches in all files and directories
# print(path.glob("*.*")) # Searches in all files
# print(path.glob("*.py"))  # Searches only in .py files

for file in path.glob("*.py"):
    print(file)