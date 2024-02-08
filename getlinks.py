import re
import heapq
import requests
import numpy as np
from GoogleNews import GoogleNews
from gensim.models import KeyedVectors
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def getLinks(query, num_links=3):
    googlenews = GoogleNews(lang="en")
    googlenews.search(query)
    return googlenews.get__links()[:num_links]

query = input("Enter query to search: ").lower()
links = getLinks(query, 3)
for l in links:
    print(l)
