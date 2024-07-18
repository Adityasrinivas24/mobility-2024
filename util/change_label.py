# import os

# # Define the mapping from old class IDs to new class IDs
# class_mapping = {
#     0: 4,  
#     1: 6,  
#     2: 3,  
#     3: 2,  
#     4: 1,  
#     5: 0, 
#     6: 5, 
# }

# # Path to the directory containing the label files
# labels_dir = '../datasets/LCV'

# # Function to process each annotation file
# def process_annotation_file(file_path):
#     new_lines = []
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         for line in lines:
#             parts = line.strip().split()
#             class_id = int(parts[0])
#             if class_id == 7:
#                 # Skip Tractor class
#                 continue
#             new_class_id = class_mapping.get(class_id, -1)
#             if new_class_id == -1:
#                 # Skip if no valid mapping is found
#                 continue
#             new_line = ' '.join([str(new_class_id)] + parts[1:])
#             new_lines.append(new_line)
    
#     # Write the modified lines back to the file
#     with open(file_path, 'w') as file:
#         for line in new_lines:
#             file.write(f"{line}\n")

# # Process all label files in the directory
# for filename in os.listdir(labels_dir):
#     if filename.endswith('.txt'):
#         file_path = os.path.join(labels_dir, filename)
#         process_annotation_file(file_path)

# print("Annotation files have been processed and updated.")

import os

# Define the directory containing the YOLO annotation files
annotation_dir = '../datasets/Truck'

# Define the mapping of class IDs
class_id_mapping = {
    0: 3,
    1: 1,
    2: 2,
    3: 6,  # Placeholder for 3, assuming no specific mapping
    4: 0,
    5: 4,
    6: 5,
}
def update_class_id(class_id):
    return class_id_mapping.get(class_id, class_id)

def modify_annotation_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Modify the class IDs
    modified_lines = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) > 0:
            class_id = int(parts[0])
            new_class_id = update_class_id(class_id)
            parts[0] = str(new_class_id)
            modified_lines.append(' '.join(parts))
    
    # Write the modified contents back to the file
    with open(file_path, 'w') as file:
        file.write('\n'.join(modified_lines) + '\n')

def main():
    # Iterate through all files in the annotation directory
    for filename in os.listdir(annotation_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(annotation_dir, filename)
            modify_annotation_file(file_path)
            print(f"Modified file: {file_path}")

if __name__ == "__main__":
    main()
