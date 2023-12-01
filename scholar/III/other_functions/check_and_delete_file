import os

def check_and_delete_file(file_path, size_threshold_kb=7):
    try:
        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)

        # Convert file size to kilobytes
        size_kb = file_size / 1024

        if size_kb > size_threshold_kb:
            print(f"The file '{file_path}' is larger than {size_threshold_kb}kB.")
        else:
            # Delete the file if it's smaller than or equal to the threshold
            os.remove(file_path)
            print(f"The file '{file_path}' has been deleted because it is smaller than {size_threshold_kb}kB.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = r"C:\Users\HP\Desktop\CARD\google_scholar\articles-copy\Book Review Pain Management.pdf"
check_and_delete_file(file_path)
