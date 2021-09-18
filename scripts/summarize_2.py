from newspaper import Article

# import nltk
# nltk.download('punkt')

url = 'https://www.cbc.ca/news/politics/vote-counting-elections-canada-2021-1.6179742'
article = Article(url)

article.download()

article.parse()

# print(article.authors)
# print(article.publish_date)
print('****', article.title, '****')
# print(article.text)

article.nlp()
print('\nSUMMARY\n', article.summary)
print('\nKEYWORDS\n', article.keywords)


# print(article.movies)