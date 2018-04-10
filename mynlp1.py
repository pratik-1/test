from nltk import FreqDist, bigrams, trigrams, ngrams
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt
import numpy as np

stopwords = stopwords.words('english')
mywords = ['one','two', 'three', 'much', 'every','therefore']
stopwords.extend(mywords)

tokenized = []

with open('divOfLabor', 'r') as lines:
    lines = lines.read()
    lines = lines.lower()
    # print(lines)
    tokenizer = RegexpTokenizer('\w+')
    tokens = tokenizer.tokenize(lines)
    # print(tokens)
    filtered_words = [w for w in tokens if not w in stopwords]
    # print('filteredwords:  ', filtered_words)
    tokenized.append(filtered_words)

#
# def plot(ngram, imagefile):
#     index = []
#     values = []
#     for i in ngram:
#         index.append(i[0])
#         values.append(i[1])
#     fig = plt.figure()
#     index1 = np.arange(len(index))
#     plt.bar(index1, values)
#     plt.xlabel('Words')
#     plt.ylabel('Occurences')
#     plt.title('Scores by group and gender')
#     plt.xticks(index)
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

# frequency of occurence
common = FreqDist(tokenized[0]).most_common(50)
print('common:        ', common)
# FreqDist(tokenized[0]).plot(20, cumulative=False)
# plot(common, 'monogram.png')

# frequency of bigrams
bigram_words = FreqDist(bigrams(tokenized[0])).most_common(50)
print('bigram_words:  ', bigram_words)

# frequency of trigrams
trigram_words = FreqDist(trigrams(tokenized[0])).most_common(50)
print('trigram_words: ', trigram_words)
FreqDist(trigrams(tokenized[0])).plot(20, cumulative=False)











