# Apt-Get-Home: Home finder #

Extracting all features from description and property tax records from popular real estate website to fully feature the home from the home link user enters. Then recommending user top two  properties, currently active on the market, that matches majority of the features based on the features of the home the user entered.

## The Problem & Solution: ##

### The Problem:
Anyone looking to buy a home has a hard time putting all the features they desire into any website to search for homes and explaining to their agent. That discourages a lot of consumers to continue their search if they don't find what they are looking for after a couple of searches. Also, the websites display all the properties on the market and don't go far enough to understand their consumers needs.

### My Solution:
My model will take features from the home link or address they put in and will give the user only 2 properties that are active on the market and matches the most features of that home. 

### Creating Model:

#### Data:
All the data is scrapped from popular real estate website to get real time results.

#### Features:

The model takes all the information from the link user provides. Currently it works on the following features:

1. Zip code (primary search parameter)
2. City (used if no results are found in the same zip code)
3. Home size (in Sq ft)
4. Lot size (if it is a single family house)
5. HOA fees (if any)
6. Year built
7. Bedroom count
8. Bathroom count
9. Price
    * Use current value of the home from the estimate provided by the real estate website
    * If no estimate provided, use last sold price
    * If the home is still active or pending, use the listing price

#### Model Selection:
Currently it runs on a imperical model of predifined cost of each feature. Scientific model is in work which will determine value for each feature based on user rating to the results. 

### Future Work:
* Use **NLP** to match different features and not limit just based on the basic stats. The model currently start search based on the parameters specified with no forgiveness. Add some flexibility to the parameters to have search generate results and not fail, just because it can't find within the same zip code or city. 

* Get access to a real estate data API to get realtime data and not have to worry about scrapping data. 

* Implement pricing feature for any home to get estimated pricing and time it would take for home to sell based on the specific features of the home. The value of the features in homes will be used based on the area, since people living in different parts of the country give positive value to some features that someone from another part of the country will give negative value.

* This solves the problem of homeowners and buyers looking for the valuation of their current or next home. Currently they could be confused by all the websites giving different prices. The websites don't explain how they come up with the value and which properties and features they use.

* Also, it will give users options of choosing which features their property has to calculate precise home value and the amount of time it will take to sell. 

* Add agent rating also to determine which agent would get them the best value for their money.