import os

def validate_annotations(labels_dir, num_classes):
    for subdir, _, files in os.walk(labels_dir):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(subdir, filename)
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        parts = line.strip().split()
                        class_id = int(parts[0])
                        if class_id >= num_classes:
                            print(f"Invalid class ID {class_id} in file {file_path}")

# Validate the annotations
validate_annotations('../datasets/new-classes/labels/train',8)  # Assuming 8 classes
validate_annotations('../datasets/new-classes/labels/val',8)
validate_annotations('../datasets/new-classes/labels/test',8)
