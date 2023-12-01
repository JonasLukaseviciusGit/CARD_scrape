import os


def rename_latest_file(directory_path, new_name='AAA'):
    try:
        all_files = os.listdir(directory_path)
        files = [f for f in all_files if os.path.isfile(os.path.join(directory_path, f))]
        if not files:
            print(f"No files found in the directory: {directory_path}")
            return
        file_paths = [os.path.join(directory_path, f) for f in files]
        latest_file_path = max(file_paths, key=os.path.getctime)
        _, file_extension = os.path.splitext(latest_file_path)
        new_file_name = f"{new_name}{file_extension}"
        os.rename(latest_file_path, os.path.join(directory_path, new_file_name))
        print(f"The latest file '{os.path.basename(latest_file_path)}' has been renamed to '{new_file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
directory_path = r"C:\Users\HP\Desktop\CARD\google_scholar\articles"
rename_latest_file(directory_path)
