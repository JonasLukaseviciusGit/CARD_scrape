## reddit_scraper
Uses Reddit API (praw) to scrape data of past 1000 posts in a particular subreddit (as far ago as API allows)./n
API has a limited free tier. For high scale data mining, paid tier or alternative approaches should be considered.
Stores scraped data in a MongoDB database.
Requires password.py, containing authentication keys.
## reddit_dataset
Processes reddit archives of posts and comments of particular subreddit into unified database that is easy to query.
The initial datasets are found here: https://academictorrents.com/details/c398a571976c78d346c325bd75c47b82edf6124e.
The link provided contains datasets regarding top 20 000 subreddits and their contents from as far ago as 2005.
The main problems solved are:
* the submission-comment unconnectedness (submissions and comments are stored as separate datasets)
* the need to prepare datasets for convenient querying (organizing them to MongoDB to eliminate the need to load them on RAM every time)
However, the datasets still need to be loaded onto RAM for processing, thus it is crucial to make sure none of the dataset is bigger than RAM space available.
This problem could be solved with slight modifications.
Data is stored in MongoDB database, but file system is used during intermediate steps.
## scholar
A simple scraper for Google Scholar. 
Given query and other search parameters, iterates through results in multiple pages and retrieves title, author data and links to pdf contents.
Stores data in MongoDB.
## unpaywall-articles
Getting metadata, including links to their pdfs, of open access articles via Unpaywall API and downloading them.
Unpaywall is a free database containing metadata of nearly 50 mln open access articles across various domains.
However, this database does not contain actual pdfs, only links to them, thus special algorithms for their downloading were built.
* Some sites are easy to download from using simple requests.
* However, other sites identify bots and apply countermeasures. To solve it, the algorithm was built to physically load the page in the browser and auto-manually download the contents, which is both slow and inconvenient, however, no better solution was found.
* Finally, some urls link to pages that do not have standard pdf format. Given the varying format of such pages, no algorithm was built for them, they are simply skipped.
This way, only 1/3 of the pdfs on average are downloaded successfully, however, all data (including links, that could not be downloaded from) is stored in MongoDB database for fast and convenient querrying.
## pmc-articles
Downloading raw and processed contents of open access articles in PubMed Central's PMC Open Access Subset.
1. Retrieves all available articles' metadata from Unpaywall and stores them in MongoDB.
2. Then, iterates through every record (representing article) in MongoDB and downloads the article from PMC database by DOI.
However, not all articles given by Unpaywall are found within PMC dataset. Yet again, only around 1/3 of pdfs are downloaded, however, downloading is fast and convenient unlike in *unpaywall-articles*. If querying for articles was made within PMC and not Unpaywall, results may be better.
Another advantage of this way over *unpaywall-articles* is the fact that pdf can be downloaded both raw and partially processed (i.e. images separated as picture files). Moreover, dataset also provides some articles in XML format, though their downloading is not included in this code.
