# reddit_dataset
The process in it's entirety is on *total_main*.<br>
Below the pieces of code for processing the datasets are listed in their order and explained:
### 01. ndjson_split
1. Getting the path to folder containing submissions and comments NDJSON files.
2. Creating a new folder within, called datasets-cleaned.
3. Splitting the submissions and comments NDJSON files into smaller folders containing up to 10 000 JSON elements each.
### 02. x→x_y split
Comments and submissions are separated into separate files (one file - one JSON element).
### 03. t5_remove
Removing indices from parent_id in comments, so it could be matched with submissions (parent_id elements start with indexes like "t5_" in the comments data, but doesn't start in submissions data, thus it needs to be removed for finding submission-comment pairs later)
### 04. indexing
Indexing commments: iteratively going through every JSON element of comments and retrieving their identificators for pairing with submissions. Resulting json file contains multiple dictionaries, containing identifiers and paths to these submissions.
### 05. grouping
Comments are subgrouped based on first 2 symbols of their identifiers, so that pairing could be done more efficiently.
### 06. submissions_to_pickle
Changing format (nothing too meaningful, could be avoided, just subsequent functions rely on pickle format, not json).
### 07. pairing
Finding pairs between submissions and their comments (by identifiers).
### 08. joining_submissions+comments
According to the pairing list made previously (*07. pairing*), new json file is constructed, containing multiple dictionaries, each of them containing submission text and their comments.
### 09. getting_filenames
Collecting file names without extensions.
### 10. to_MongoDB
Formating conveniently and saving all data to MongoDB.
