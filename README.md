<h1> Apt-Get-Home: Home finder</h1>

Apt-Get-Home is a smart home-finder tool that extracts features from property listings and tax records, then recommends the top two active properties that best match the home a user enters.

---
### The Problem & Solution:

**The Problem:**
Searching for homes online can be frustrating:
- Websites don’t fully capture buyer preferences.
- Users struggle to translate “what they want” into search filters.
- Agents get incomplete information, leading to wasted effort.

**The Solution:**

Apt-Get-Home analyzes the features of a given home (via link or address) and returns two active market listings that match the majority of its features.

---
### How It Works:

**Data:**
Scraped from a popular real estate site to provide real-time results.

**Features Considered:**

* Zip code (primary)
* City (fallback if no zip results)
* Home size (sqft)
* Lot size (for single-family)
* HOA fees
* Year built
* Bedrooms & bathrooms
* Price (estimate, last sold, or listing price)

**Model:**
* Current: empirical scoring based on predefined feature weights.
* Future: data-driven scoring informed by user ratings & feedback.
---
### Future Work:
* Use **NLP** to capture more nuanced property features.
* Add flexibility in searches (not fail if no exact zip/city match).
* Integrate with a real estate API (instead of scraping).
* Build pricing & time-to-sell prediction models.
* Let users adjust property features for more accurate valuation.
* Include agent ratings to connect buyers with the best agents.
---
### Usage

Clone the repo:
```
git clone git@github.com:Data-is-life/apt-get-home.git
cd apt-get-home/src
```
Run the App
```
python app.py
```
Or explore in Jupyter:
```
jupyter notebook Main_prog.ipynb
```

---
### 📂 Repository Structure

```
├── Data/                # Raw data & lookup files
├── img/                 # Visualizations & logos
├── Presentation/        # Project presentation slides
├── src/                 # Main codebase
│   ├── app.py           # Main app script
│   ├── Main_prog.ipynb  # Jupyter notebook version
│   ├── ...              # Helper scripts
└── README.md
```
---
### 📚 Built With
* Python 🐍
* Pandas
* NumPy
* BeautifulSoup
* Redfin (data source)
--
### 📜 License
MIT License © 2019 Mohit Gangwani
