<h1> Apt-Get-Home: Home finder</h1>

<p>Extracting all features from description and property tax records from popular real estate website to fully feature the home from the home link user enters. Then recommending user top two  properties, currently active on the market, that matches the majority of the features based on the features of the home the user entered.</p>

<h2> The Problem & Solution:</h2>

### The Problem:
Anyone looking to buy a home has a hard time putting all the features they desire into any website to search for homes and explaining to their agent. That discourages a lot of consumers to continue their search if they don't find what they are looking for after a couple of searches. Also, the websites display all the properties on the market and don't go far enough to understand their consumers' needs.

### My Solution:
My model will take features from the home link or address they put in and will give the user only 2 properties that are active on the market and matches the most features of that home. 

## Creating Model:

### Data:
All the data is scraped from popular real estate website to get real time results.

### Features:

The model takes all the information from the link user provides. Currently, it works on the following features:

1. Zip code (primary search parameter)
2. City (used if no results are found in the same zip code)
3. Home size (in Sqft)
4. Lot size (if it is a single family house)
5. HOA fees (if any)
6. Year built
7. Bedroom count
8. Bathroom count
9. Price
    * Use current value of the home from the estimate provided by the real estate website
    * If no estimate provided, use last sold price
    * If the home is still active or pending, use the listing price

### Model Selection:
Currently, it runs on an empirical model of the predefined cost of each feature. The scientific model is in work which will determine the value for each feature based on user rating to the results. 

## Future Work:
* Use **NLP** to match different features and not limit just based on the basic stats. The model currently starts the search based on the parameters specified with no forgiveness. Add some flexibility to the parameters to have search generate results and not fail, just because it can't find within the same zip code or city. 

* Get access to a real estate data API to get real-time data and not have to worry about scrapping data. 

* Implement pricing feature for any home to get estimated pricing and time it would take for the home to sell based on the specific features of the home. The value of the features in homes will be used based on the area since people living in different parts of the country give positive value to some features that someone from another part of the country will give a negative value.

* This solves the problem of homeowners and buyers looking for the valuation of their current or next home. Currently, they could be confused by all the websites giving different prices. The websites don't explain how they come up with the value and which properties and features they use.

* Also, it will give users options of choosing which features their property has to calculate the precise home value and the amount of time it will take to sell. 

* Add agent rating also to determine which agent would get them the best value for their money.


## Usage
Clone this repository with the command

```
git clone git@github.com:Data-is-life/apt-get-home.git
```

All codes are located in **src** folder. The main file is called **app.py**. If you'd like to run in the Jupyter notebook, run **Main_prog.ipynb** from the **src** folder. 

The repository has the following structure. 

```
├── Data
│   ├── features_review.ods
│   └── url_ranges.ods
├── img
│   ├── Experience.png
│   ├── From_Bay_Area.png
│   ├── From_Denver.png
│   ├── From_Las_Vegas.png
│   ├── From_Pheonix.png
│   ├── From_Portland.png
│   ├── From_Seattle.png
│   ├── From_Utah.png
│   ├── Logo.png
│   ├── RE Companies.png
│   ├── RE Websites.png
│   ├── to_Bay_Area.png
│   ├── to_Denver.png
│   ├── to_Las_Vegas.png
│   ├── to_Pheonix.png
│   ├── to_Portland.png
│   ├── to_Seattle.png
│   └── To_Utah.png
├── Presentation
│   └── Apt-Get-Home - Mohit Gangwani.pdf
├── README.md
└── src
    ├── app.py
    ├── FUNCTIONS.pyc
    ├── GET_RESULTS.py
    ├── GET_SEARCH_URL.py
    ├── header_list.py
    ├── INITIAL_SCRAPPER_FUNCTIONS.py
    ├── LIST_DF_FUNCTIONS.py
    ├── Main_prog.ipynb
    ├── PARSER_FUNCTIONS.py
    ├── proxies_list.py
    ├── Not in use
    │   ├── app.ipynb
    │   ├── old_commands.py
    │   ├── old_parser.py
    │   ├── old_scraper.ipynb
    │   ├── proxie_check.py
    │   ├── unused_commands.py
    │   └── url_gen.py
    ├── proxies_list.pyc
    ├── __pycache__
    │   ├── FUNCTIONS.cpython-36.pyc
    │   ├── GET_RESULTS.cpython-36.pyc
    │   ├── GET_SEARCH_URL.cpython-36.pyc
    │   ├── header_list.cpython-36.pyc
    │   ├── INITIAL_SCRAPPER_FUNCTIONS.cpython-36.pyc
    │   ├── LIST_DF_FUNCTIONS.cpython-36.pyc
    │   ├── MAIN_FUNCTIONS.cpython-36.pyc
    │   ├── moduletest.pyc
    │   ├── PARSER_FUNCTIONS.cpython-36.pyc
    │   ├── proxie_check.cpython-36.pyc
    │   ├── proxies_list.cpython-36.pyc
    │   ├── SCRAPPER_FUNCTIONS.cpython-36.pyc
    │   └── SEARCH_URL_GEN.cpython-36.pyc
    └── Tester_file.ipynb
```

## Resources used:

<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" width="300"></br>
<img src="https://www.redfin.com/blog/wp-content/uploads/sites/5/2015/01/redfinlogo_blogpreview2.jpg" width="300"></br>
<img src="https://i.imgur.com/fkPSojf.png" width="300"></br>
<img src="https://pandas.pydata.org/_static/pandas_logo.png" width="300"></br>
<img src="https://bids.berkeley.edu/sites/default/files/styles/400x225/public/projects/numpy_project_page.jpg?itok=flrdydei" width="300"></br>
<img src="https://tettra.co/culture-codes/wp-content/logos/github.png" width="300"></br>
<img src="https://funthon.files.wordpress.com/2017/05/bs.png?w=1200" width="300">