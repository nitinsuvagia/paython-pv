import os

def write_files_to_pv(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create a few files
    for i in range(1, 4):
        file_path = os.path.join(directory, f"file_{i}.txt")
        with open(file_path, "w") as file:
            file.write(f"This is the content of file {i}\n")
        print(f"Written {file_path}")

if __name__ == "__main__":
    pv_directory = "/mnt/pv-data"
    write_files_to_pv(pv_directory)
