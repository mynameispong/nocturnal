# Import Counter
from collections import Counter

# Tokenize the article: tokens
tokens = word_tokenize("I have a dream that one day down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification – one day right there in Alabama little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.I have a dream today.I have a dream that one day every valley shall be exalted, and every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed and all flesh shall see it together.This is our hope. This is the faith that I go back to the South with. With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day.This will be the day, this will be the day when all of God’s children will be able to sing with new meaning “My country ’tis of thee, sweet land of liberty, of thee I sing. Land where my father’s died, land of the Pilgrim’s pride, from every mountainside, let freedom ring!")

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [str.lower(t) for t in tokens]

# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)

# Print the 10 most common tokens
print(bow_simple.most_common(10))

#[(',', 17), ('be', 13), ('the', 12), ('of', 12), ('to', 11), ('will', 10), ('with', 9), ('and', 9), ('a', 5), ('day', 5)]

# Import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer

# Retain alphabetic words: alpha_only
alpha_only = [t for t in lower_tokens if t.isalpha()]

# Remove all stop words: no_stops ( 'be' until 'a' )
no_stops = [t for t in alpha_only if t not in english_stops]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stops]

# Create the bag-of-words: bow
bow = Counter(lemmatized)

# Print the 10 most common tokens
print(bow.most_common(10))

#[('day', 5), ('able', 5), ('together', 5), ('one', 4), ('shall', 4), ('faith', 4), ('dream', 3), ('every', 3), ('made', 3), ('land', 3)]
#MLK's most used words are quite interesting

#[(',', 33), ('and', 18), ('my', 17), ('of', 16), ('the', 11), ('to', 9), ('i', 9), ('in', 8), ('have', 7), (';', 7)]
#[('shall', 4), ('people', 3), ('god', 3), ('prince', 3), ('general', 3), ('loving', 2), ('take', 2), ('fear', 2), ('assure', 2), ('live', 2)]
#queen elizabeth's speech 
