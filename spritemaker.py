import os
from PIL import Image

# Find all PNG files in the current directory
png_files = [file for file in os.listdir(".") if file.lower().endswith(".png")]

# Sort the PNG files alphanumerically by filename
png_files.sort()

# Check the number of files
if len(png_files) < 2:
    print("There are not enough PNG files to create a sprite sheet.")
    exit()

if len(png_files) > 256:
    print("The number of images exceeds the limit (256).")
    exit()

# Check if all files have the same dimensions
first_image = Image.open(png_files[0])
width, height = first_image.size

for file in png_files[1:]:
    image = Image.open(file)
    if image.size != (width, height):
        print("Not all PNG files have the same dimensions.")
        exit()


# Prompt user for the base name
base_name = input("Enter the base name for the output file: ")
base_name = base_name.replace(" ", "_")

# Create the sprite sheet
sprite_sheet_height = height * len(png_files)
sprite_sheet = Image.new("RGBA", (width, sprite_sheet_height), (0, 0, 0, 0))

y_offset = 0  # Update the initial offset

for file in png_files:
    image = Image.open(file)
    sprite_sheet.paste(image, (0, y_offset))
    y_offset += height # Set the y_offset to 1 for the remaining images

# Create the "output" directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save the sprite sheet
output_file = f"{base_name}_{width}px_x_{height}px_{len(png_files)}frames.png"
output_path = os.path.join(output_dir, output_file)
sprite_sheet.save(output_path)


# Create the accompanying text file
text_file = f"{base_name}_{width}px_x_{height}px_{len(png_files)}frames.txt"
text_path = os.path.join(output_dir, text_file)
with open(text_path, "w") as file:
    file.write("Has Alpha Channel: yes\n")
    file.write(f"Number of Animations: {len(png_files)}\n")
    file.write("Horizontal Animation: no\n")
    file.write("Vertical Resizable: no\n")
    file.write("Horizontal Resizable: no\n")
    file.write("Fixed Top: 0\n")
    file.write("Fixed Bottom: 0\n")
    file.write("Fixed Left: 0\n")
    file.write("Fixed Right: 0\n") # Add a single blank line at the end

print(f"Sprite sheet saved as {output_file}.")
print(f"Accompanying text file saved as {text_file}.")

