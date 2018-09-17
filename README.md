# Domain Specific Search Engine

## Requirements
The following Python packages are required:
+ nltk
+ BeautifulSoup4
+ requests
+ csv
+ numpy
+ scipy

## Documentation
For code documentation refer to: docs/build/html/index.html

## Installation and Execution
+ Install all the packages and dependencies
+ Run WebScraper.py for any topic from https://arxiv.org/ which contains links to recent
papers for that topic.(It will generate csv files containing the title, authors, abstract, date
URL and Submission date)
+ Run ScrapedData/mycsv.py to create a dictionary and generate the tf-idf matrix
and process the given query to give the documents with highest cosine similarity score.  
