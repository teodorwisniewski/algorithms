import os
import sys

def rename_files_in_subfolders(root_directory):
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for filename in filenames:
            if filename.endswith(".py") and filename[0].isdigit():
                new_name = f"problem_{filename}"
                old_file = os.path.join(dirpath, filename)
                new_file = os.path.join(dirpath, new_name)
                os.rename(old_file, new_file)
                print(f"Renamed '{old_file}' to '{new_file}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_script.py [root_directory]")
        sys.exit(1)

    root_directory = sys.argv[1]

    # Check if the provided directory path exists
    if not os.path.isdir(root_directory):
        print(f"The directory '{root_directory}' does not exist.")
        sys.exit(1)

    rename_files_in_subfolders(root_directory)
