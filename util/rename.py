import os

def rename_files_in_directory(directory, prefix):
    files = os.listdir(directory)
    files.sort()  # Sort files to ensure consistent numbering
    count = 1
    
    for filename in files:
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        # Construct the new file name
        new_filename = f"{prefix} ({count}){file_extension}"
        # Get the full paths for the current and new file names
        src = os.path.join(directory, filename)
        dst = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(src, dst)
        count += 1

# Define the directory and the prefix
directory = 'lcv-annotations'
prefix = 'Datacluster LCV'

# Call the function to rename files
rename_files_in_directory(directory, prefix)

print("Files have been renamed.")
