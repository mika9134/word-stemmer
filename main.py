# from nltk.stem import SnowballStemmer
#
# # Text to be stemmed
# text = "Ho visto un palazzo rosso"
#
# # Create an Italian SnowballStemmer object
# italian_stemmer = SnowballStemmer("italian")
#
# # Split the text into words
# words = text.split()
#
# # Stem each word and store them in a list
# stemmed_words = []
# for word in words:
#   stemmed_words.append(italian_stemmer.stem(word))
#
# # Join the stemmed words back into a string
# stemmed_text = " ".join(stemmed_words)
#
# # Print the original and stemmed text
# print("Original Text:", text)
# print("Stemmed Text:", stemmed_text)


from nltk.stem import SnowballStemmer

# Define the path to your text file
# file_path = "~/PycharmProjects/pythonProject/venv"
file_path = "~/../venv/file.txt"


# Create an Italian SnowballStemmer object
italian_stemmer = SnowballStemmer("italian")

# Initialize an empty list to store stemmed words
stemmed_words = []

# Open the text file for reading
with open(file_path, "r") as text_file:
  # Read all lines from the file
  lines = text_file.readlines()

  # Loop through each line and process words
  for line in lines:
    # Preprocess the line (optional - remove punctuation etc.)
    # ... (add preprocessing steps here)

    # Split the line into words
    words = line.split()

    # Stem each word and add it to the list
    for word in words:
      stemmed_word = italian_stemmer.stem(word)
      stemmed_words.append(stemmed_word)

# Print the stemmed words (optional)
print(stemmed_words)

# You can further process the stemmed_words list here
