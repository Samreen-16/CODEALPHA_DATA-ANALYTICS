from textblob import TextBlob 
texts = ["I love this!", "This is bad.", "It's okay."] 
for text in texts: 
    blob = TextBlob(text) 
    polarity = blob.sentiment.polarity 
    print(f"{text} => {sentiment}") 
