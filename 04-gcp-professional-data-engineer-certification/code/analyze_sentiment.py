# Imports the Google Cloud client library
from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Above mentioned was my review when I purchased this Bluetooth earphones but now since a month the earphones are not working properly. They are getting disconnected with in 5mins when connected to any device. After sale service is pathetic. I’m struggling to get these set of earphones replaced since last 15 days."
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))