# 🏗 Machine Learning Model Development
Two sections of models were built. NLP for article summarization and Forecasting to predict geopolitical data.
## NLP
A Natural Language Processing system was built that takes the URL of articles as input and summarizes them into a single paragraph. This pipeline is connected to our web scraping algorithm, meaning a user can enter a search term (e.g. Canadian Election), obtain a list of political articles, and the NLP system summarizes the top 2 write-ups. The architecture of the summarization model consists of data extraction, finding sentence similarity, prioritizing terms, building a similarity matrix, and outputting the final string. The tech stack for this system includes `Python`, `Nltk`, `NetworkX`, `BeautifulSoup`, and `Newspaper`.
## Forecasting
A Data Forecasting system was built that allows users to visualize geopolitical information and predict future metrics. Currently, the data consists of Canada and Australia comparing GDP, Costs of Imported Goods, and Populations, however, the pipeline works with any measurement and nation-state. The tech stack for this system includes `Python`, `Pandas`, `Scikit-Learn`, and `Plotly`.
## Deployement
All the models were shipped to the [ML-App](https://github.com/Diplomatica-HTN/ML-App) Repository to be used on the interactive application.
