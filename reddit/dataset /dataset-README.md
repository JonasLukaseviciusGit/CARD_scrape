# Documentation of the reddit/dataset subfolder contents
---
This subfolder contains the scripts that have been used to process dataset from here:
  https://academictorrents.com/details/c398a571976c78d346c325bd75c47b82edf6124e

File and folder paths in scripts are my personal, replace them with yours accordingly.

---
### ndjson-iterate
The dataset originally is in ndjson format. This script allows iterative printing of its content.

### ndjson→json-files_split
Splits ndjson file to multiple json files (each containing 10 000 dictionaries). Resulting json files are more standard to work with and can be loaded quickly.

### json_pretty-print
Template script for printing json dictionary in an easy-to-read manner,

### formating-single
Creates a folder.
Then it iterates through every dictionary in json file and for every dictionary does the following:
  1. Creates a dictionary containing every key and value as it is, only without "selftext".
  2. Applies the meaningful_print function for "selftext" value, with that value being passed as data:
  3. Creates .txt file for that text content generated in step 2 and saves it in the folder.
  4. Adds that path to the dictionary by key "path".
  5. Repeats this cycle for every dictionary in the json file.

### formating-multiple
Same as formating-multiple, but processes multiple json files (that have been created by ndjson→json-files_split)

### indexing-comments
From every comments file (separated into json files with formating-multiple) and every dictionary (comment) in it makes a list<br>
Example:<br>
$~~~~~~~~~~~~~~~$[file, index, link_id, parent_id]<br>
$~~~~~~~~~~~~~~~$[002, 5462, rw4weef468, h5r1yj89we]<br>
A total list of all such list is saved in a .pkl (pickle) file.<br>
The aim of this procedure is to prepare a list to be used in later search for relations between posts and comments.

### indexing-submissions
Same as indexing-comments, but for submissions. Takes [file, index, id].

### pairing
Takes resulting lists of indexing-comments and indexing-submissions.
Then looks for relations between submissions and comments:
1. Takes id of the submission.
2. Compares that id with every id, link_id and parent_id in every comment and looks for identical.
3. Repeats steps 1-2 for every submission (there are over 1.2 M of them).

To check for all relations in this way it would take roughly a week with my computer speed. The algorithm could be sped up by deploying multiprocessing (1), removing paired elements (2) and some other ways.<br>
However, 1000 submissions have been checked yet no pairings made.
