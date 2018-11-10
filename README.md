# Domain Specific Search Engine

## Group Members
+ Shivam Bhagat 2015B5A70460H
+ Abhinav Kumar 2015B5A70674H
+ Yashdeep Thorat 2015B5A70675H

## Requirements
The following Python packages are required:
+ nltk
+ BeautifulSoup4
+ requests
+ csv
+ numpy
+ scipy

## Documentation
+ For code documentation refer to: docs/build/html/index.html
+ Refer to DesignDocumentation.pdf for design documentation.

## Installation and Execution
+ Install all the packages and dependencies
+ Run WebScraper.py for any topic from https://arxiv.org/ which contains links to recent
papers for that topic.(It will generate csv files containing the title, authors, abstract, date
URL and Submission date)
+ Run ScrapedData/IndexData.py to create a dictionary and generate the tf-idf matrix
and process the given query to give the documents with highest cosine similarity score.  
+ Run ScrapedData/gui.py to run the application on the local server and open the specified link in the browser.
