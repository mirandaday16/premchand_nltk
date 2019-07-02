import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WhitespaceTokenizer
import matplotlib.pyplot as plt

y_font = {'fontname': 'Devanagari Sangam MN'}
plt.yticks(**y_font)

nltk.corpus.indian.words('hindi.pos')


corpus_root = '.'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

string_text = wordlists.raw('Premchand.txt')

tokens = WhitespaceTokenizer().tokenize(wordlists.raw('Premchand.txt'))
w_tokens = [w for w in tokens]
text = nltk.Text(w_tokens)

print("Total words in corpus: ", len(text))
print("Total unique vocabulary words: ", len(set(text)))
# print(set(text))

print("Number of collocations: ", len(text.collocation_list()))
for w in text.collocation_list():
    print(w)

# text.dispersion_plot(["महिला", "औरत"])

text.dispersion_plot(["गाँव", "किसान", "गाय"])

