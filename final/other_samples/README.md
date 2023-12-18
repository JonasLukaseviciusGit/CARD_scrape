## other_samples
Contains unfinished, yet working pieces of code:<br>
### quora
Script for scraping Quora (doesn't have an API).
1. Given the query, the browser is loaded in headless mode using Selenium.
2. Results in the page are loaded dynamically, so scrolling is done every with delays (interval length randomized within limits specified).
3. After the specified number of scrolls, the results (urls to posts) are saved in a json file.<br>

The htmls are scraped using regex, thus contain various meaningless urls (that do not link to posts). This could be avoided by parsing the html content non-textually or parsing it as it is, but cleaning afterwards.
### science_direct
An example of how to use ScienceDirect API to retrieve article contents in XML format given article's PII identifier.
