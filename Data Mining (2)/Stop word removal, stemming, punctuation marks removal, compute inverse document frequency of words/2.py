import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import nltk
nltk.download('punkt')


#==============================Sample text document=============================#
document='''
Natural language processing (NLP) is a component of artificial 
intelligence (AI) that allows computer programs to understand human language 
as it's written and spoken. NLP has been around for over 50 years  
and has roots in linguistics.
'''
#==========================Step A : Stop Word Removal===========================#
nltk.download('stopwords')
stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize(document)
filtered_words=[word for word in word_tokens if word.lower() not in stop_words]
#==========================Step B : Stemming====================================#
stemmer=PorterStemmer()
stemmed_words=[stemmer.stem(word) for word in filtered_words]
#====Step C: Removal of Punctuation Marks====#
filtered_word_with_no_punc=[word for word in stemmed_words if word not in string.punctuation]
#==============Step D : Compute Inverse Document Frequency(IDF)=================#
corpus=[document]   #List of all documents(in this case just one)
vectorizer=TfidfVectorizer()
x=vectorizer.fit_transform(corpus)
idf=vectorizer.idf_
word_idf=dict(zip(vectorizer.get_feature_names_out(),idf))
#============================Print Results======================================#
print("Original Document : \n")
print(document)
print(f"\nA)After stopword removal : \n")
print(filtered_words)
print(f"\nB)After Stemming : \n")
print(stemmed_words)
print(f"\nC)After Removal of Punctuation Marks : \n")
print(filtered_word_with_no_punc)
print(f"\nD)Inverse Document Frequency(IDF) of words : \n")
print(word_idf)

