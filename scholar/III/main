import requests                     # for making API requests
import passwords                    # for retrieving email address from a file
from pymongo import MongoClient     # for uploading data to MongoDB
import re                           # for cleaning title from non-alphabetic characters
import os                           # for saving files to a folder
import random                       # for generating random number in file name uniquification

# MY FUNCTIONS
from manual_downloading import manual_downloading   # for downloading files that could not be downloaded automatically
from other_functions import check_and_delete_file   # for deleting files that are too small (so most likely corrupted)
from other_functions import rename_latest_file      # for renaming the latest file (if it wasn't downloaded normally)
from other_functions import calculate_elapsed_time  # for calculating elapsed time      (final message)
from other_functions import count_files_in_folder   # for counting files in a folder    (final message)

import time                         # for retrieving current timestamp                  (final message)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client['UnpaywallArticles']
collection = db['data']

query = "pain management"
email = passwords.email
end_folder = r"C:\Users\HP\Desktop\CARD\google_scholar\articles"
isOpenAccess = True

page = 1


# Function to download PDF (simple way) and save it
# Given: url, title, folder; Returns: filepath
def download_pdf(url, title, folder):
    try:
        pdf = requests.get(url)
        file_name = title + ".pdf"
        filepath = os.path.join(folder, file_name)
        while os.path.exists(filepath):
            random_number = random.randint(100, 999)
            file_name = f"{title}_{random_number}.pdf"
            filepath = os.path.join(folder, file_name)
        with open(filepath, "wb") as pdf_file:
            pdf_file.write(pdf.content)
            return filepath
    except Exception as e:
        print(f"An error occurred: {e}")


# Function to clean title from non-alphabetic characters
# Given: raw text; Returns: cleaned text
def clean_alphabetic(text):
    pattern = re.compile(r'<.*?>')              # remove angle brackets and their contents
    result = re.sub(pattern, '', text)
    result = re.sub(r'[^a-zA-Z ]', '', result)  # remove non-alphabetic characters
    return result


time_start = time.time()    # starting point for timer

attempts_to_download = 0    # tracks attempts to download, to calculate success rate (final message)
while True:
    print(page)             # page number
    url = f"https://api.unpaywall.org/v2/search?query={query}&is_oa={isOpenAccess}&page={page}&email={passwords.email}"
    response = requests.get(url).json()['results']      # get response from API (urls to article PDFs and metadata)
    num_of_elements = len(response)                     # number of elements (articles) in response

    # if response is not empty
    if num_of_elements != 0:
        print('\033[91m' + '-' * 50 + '\033[0m')
        print('')
        count = 1
        for article in response:
            record = collection.insert_one(article)     # insert article API response to MongoDB
            record_id = record.inserted_id              # retrieving inserted record identifier for future updates

            response = article['response']
            pdf_url = response['best_oa_location']['url_for_pdf']
            if pdf_url is not None:
                title = clean_alphabetic(response['title'])
                print(f'\033[92mPage {page} Element {count}/{num_of_elements}\033[0m')
                print(pdf_url)
                print(title)
                filepath = download_pdf(pdf_url, title, end_folder)                     # download PDF the simple way
                wasDeleted = check_and_delete_file(file_path=filepath, size_threshold_kb=7)  # delete if file is corrupt

                if wasDeleted:                                                          # if file was deleted
                    index = manual_downloading(folder_path=end_folder, url=pdf_url)     # download file semi-manually
                    if index is not None:                                   # if had duplicating title and was renamed
                        title = f'{title}-{index}'                              # uniquify title with index
                    file_path = rename_latest_file(directory_path=end_folder, new_name=title)
                    if type(file_path) is list:                     # if file was renamed successfully
                        collection.update_one({"_id": record_id},
                                              {"$set": {"file_path": file_path[0]}})                # update MongoDB
                    print('Downloaded semi-manually')
                else:
                    collection.update_one({"_id": record_id}, {"$set": {"file_path": filepath}})    # update MongoDB
                    print('Downloaded automatically')

                print('')
            count += 1
            attempts_to_download += 1
    # if response is empty
    else:
        break   # end page was reached, exit the loop and print final message
    page += 1

# End message
time_end = time.time()
elapsed_time = calculate_elapsed_time(time_start, time_end)
total_files_downloaded = count_files_in_folder(end_folder)
print('\033[91m' + '-' * 50 + '\033[0m')
print(f'\033[92m PDFs downloaded successfully: {attempts_to_download}/{total_files_downloaded}\033[0m')
print('\033[92m Elapsed time: {elapsed_time}\033[0m')
