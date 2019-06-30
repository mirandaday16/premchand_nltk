import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize

nltk.corpus.indian.words('hindi.pos')


corpus_root = '/Users/mirandadayadkins/Desktop/Premchand/Premchand'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

string_text = wordlists.raw('Premchand.txt')

tokens = WhitespaceTokenizer().tokenize(wordlists.raw('Premchand.txt'))
tokens = wordpunct_tokenize(wordlists.raw('Premchand.txt'))

w_tokens = [w for w in tokens if w.isalpha()]

# print(sorted(set(w_tokens))[:30])

text = nltk.Text(w_tokens)

print(len(text))
print(len(set(text)))
# print(set(text))

print(len(text.collocation_list()))
print(text.collocation_list())

# text.dispersion_plot(["प्रेम", "प्यार"])

