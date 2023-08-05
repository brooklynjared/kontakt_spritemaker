import os
import sys


def main():

    path = input("Path to image files: ").strip()

    if os.path.isdir(path):
        print("Path: ", path)

        try:
            png_files = [file for file in os.listdir(path) if file.lower().endswith(".png")]
            for file in png_files:
                base_name, extention = file.split(".")
                generate_txt_file(base_name, path)
        except:
            sys.exit("An error occurred.")
    else:
        sys.exit("Input was not a valid path. Did it end with a slash?")


    return

def generate_txt_file(base_name, path, alpha="yes", animations=0):
    txt_file = f"{base_name}.txt"
    txt_path = os.path.join(path, txt_file)
    with open(txt_path, "w") as file:
        file.write(f"Has Alpha Channel: {alpha}\n")
        file.write(f"Number of Animations: {str(animations)}\n")
        file.write("Horizontal Animation: no\n")
        file.write("Vertical Resizable: no\n")
        file.write("Horizontal Resizable: no\n")
        file.write("Fixed Top: 0\n")
        file.write("Fixed Bottom: 0\n")
        file.write("Fixed Left: 0\n")
        file.write("Fixed Right: 0\n") # Add a single blank line at the end
    return



if __name__ == "__main__":
    main()