import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if (filename.endswith(".py") or filename.endswith(".js")) and filename[0].isdigit():
            new_name = f"problem_{filename}"
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")


if __name__ == "__main__":
    # Replace 'your_directory_path' with the path to your directory
    your_directory_path = 'leetcode/'  # e.g., './leetcode'
    rename_files(your_directory_path)
