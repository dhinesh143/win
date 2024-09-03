import os

# Base directories for validation
VALID_IMAGE_DIR = r'E:\aiml\waste-detection-main\sorted\valid\images'
VALID_LABEL_DIR = r'E:\aiml\waste-detection-main\sorted\valid\labels'

# List of class names matching the YOLO label indices
class_names = [
    'battery', 'can', 'cardboard_bowl', 'cardboard_box', 'chemical_plastic_bottle',
    'chemical_plastic_gallon', 'chemical_spray_can', 'light_bulb', 'paint_bucket',
    'plastic_bag', 'plastic_bottle', 'plastic_bottle_cap', 'plastic_box',
    'plastic_cultery', 'plastic_cup', 'plastic_cup_lid', 'reuseable_paper',
    'scrap_paper', 'scrap_plastic', 'snack_bag', 'stick', 'straw'
]

# Function to generate labels
def generate_labels(image_dir, label_dir):
    for class_index, class_name in enumerate(class_names):
        class_image_dir = os.path.join(image_dir, class_name)
        class_label_dir = os.path.join(label_dir, class_name)
        
        # Create the class-specific label directory if it does not exist
        os.makedirs(class_label_dir, exist_ok=True)
        
        if not os.path.exists(class_image_dir):
            print(f"Class folder {class_image_dir} not found, skipping.")
            continue

        for image_filename in os.listdir(class_image_dir):
            if image_filename.endswith('.jpg') or image_filename.endswith('.png'):
                # Generate the label filename corresponding to the image
                label_filename = image_filename.replace('.jpg', '.txt').replace('.png', '.txt')
                label_file_path = os.path.join(class_label_dir, label_filename)
                
                # YOLO format: class_index x_center y_center width height (normalized)
                # Here we assume the object occupies the full image
                yolo_label = f"{class_index} 0.5 0.5 1.0 1.0\n"
                
                # Write the label file
                with open(label_file_path, 'w', encoding='utf-8') as label_file:
                    label_file.write(yolo_label)
                
                print(f"Generated label for {image_filename} in {class_name}.")

# Generate labels for the validation set only
generate_labels(VALID_IMAGE_DIR, VALID_LABEL_DIR)

print("Label generation complete for the validation set.")
