# pmc-articles
### unpaywall_mongodb
First, database is created and the list of queries is specified.<br>
Then, iterating through every query in the list:
1. A collection in a database is created
2. Using Unpaywall API, all results of the query are retrieved. Resulting articles' metadata is stored in MongoDB.

### pmcids_mongodb
Iterating through every record previously generated and now stored in MongoDB, DOI is taken and turned into pmcId (special identifier for PubMed Central database)<br>
This conversion is achieved PMC's DOI to pmcId converter: https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/. Conversions are done in bulk, not one by one, thus eliminating the need for multiple requests. However, not all DOIs can be converted to pmcIds as not all articles on Unpaywall are present within PMC.<br>
Resulting pmcIds are saved along with their respective records in MongoDB.

### add_tgz_pdf_links_to_mongodb
Uses *get_tgz_and_pdf* function, which given the pmcId, returns urls to pdf and tgz (folder containing processed pdf files).

### downloading_folders
Uses *download_tar* function to download .tar.gz files, extract them, save in a specified folder and save the link to it in MongoDB.
