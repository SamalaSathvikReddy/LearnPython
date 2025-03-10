# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 
# from chatgpt

import os

def print_directory_contents(directory):
    # Get list of files and directories in the specified directory
    contents = os.listdir(directory)
    
    # Print each item in the directory
    for item in contents:
        print(item)

# Example usage:
directory_path = '.'  # Replace with the path of the directory you want to print
print(f"Contents of directory '{directory_path}':")
print_directory_contents('/')

