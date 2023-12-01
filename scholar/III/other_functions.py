import os


def check_and_delete_file(file_path, size_threshold_kb=7):
    try:
        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)

        # Convert file size to kilobytes
        size_kb = file_size / 1024

        # Delete the file if it's smaller than or equal to the threshold
        if size_kb > size_threshold_kb:
            return False
        else:
            os.remove(file_path)
            return True
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


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
        file_path = os.path.join(directory_path, new_file_name)
        os.rename(latest_file_path, file_path)
        return [file_path]
    except Exception as e:
        print(f"An error occurred: {e}")


def calculate_elapsed_time(timestamp_a, timestamp_b):
    # Calculate the time difference in seconds
    time_difference = timestamp_b - timestamp_a

    # Calculate hours, minutes, and seconds
    hours, remainder = divmod(time_difference, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 0:
        return f"{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds"
    elif minutes > 0:
        return f"{int(minutes)} minutes, {int(seconds)} seconds"
    else:
        return f"{int(seconds)} seconds"


def count_files_in_folder(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        # Filter out subdirectories, leaving only files
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        # Count the number of files
        num_files = len(files)

        return num_files
    except OSError as e:
        print(f"Error: {e}")
        return None
