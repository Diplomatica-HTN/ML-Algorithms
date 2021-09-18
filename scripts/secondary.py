from newspaper import Article

url = 'https://www.cbc.ca/news/politics/vote-counting-elections-canada-2021-1.6179742'
article = Article(url)

article.download()

article.parse()

print('****', article.title, '****')

article.nlp()
print('\nSUMMARY\n', article.summary)
print('\nKEYWORDS\n', article.keywords)