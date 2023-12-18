# unpaywall-articles
The main file to run is *main.py*. It relies on these functions:
### get_unpaywall_data
For multiple queries makes a collection in MongoDB and uses Unpaywall API which, given a query, returns multiple article's metadata, including urls to actual articles in PDF format.
### download_pdfs
Attempts to download pdf in a simple way (using requests)
### find_corrupted_pdfs
Iterates through the folder containing downloaded pdfs and checks if they are corrupted using PyMuPDF. Returns a list containing paths to corrupted PDFs, which will be later deleted and taken for downloading using other method.
### manual_downloading
Pseudo-manual method for downloading PDF using Selenium: The page is physically loaded on the browser, visually checks for the download button. If download button is there, the mouse is dragged to its location and button is clicked, downloading the PDF.<br>
Includes renaming the page and turning off messages, but they may need to be adjusted according to the specifics of the browser.<br>
Coordinates where the mouse moves as well as screenshots for the download button need to be adjusted according to the dimensions of the screen.<br>
Overall this process is slow and not fault-proof, but no other working solution could be found.
