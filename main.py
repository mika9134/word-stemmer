from nltk.stem import SnowballStemmer

# Text to be stemmed
text = "Ho visto un palazzo rosso"

# Create an Italian SnowballStemmer object
italian_stemmer = SnowballStemmer("italian")

# Split the text into words
words = text.split()

# Stem each word and store them in a list
stemmed_words = []
for word in words:
  stemmed_words.append(italian_stemmer.stem(word))

# Join the stemmed words back into a string
stemmed_text = " ".join(stemmed_words)

# Print the original and stemmed text
print("Original Text:", text)
print("Stemmed Text:", stemmed_text)
