import nltk
nltk.corpus.indian.words('hindi.pos')
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import WhitespaceTokenizer
# from matplotlib import rcParams
# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['Hind']

corpus_root = '/Users/mirandadayadkins/Desktop/Corpi'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

string_text = wordlists.raw('Premchand.txt')

tokens = WhitespaceTokenizer().tokenize(wordlists.raw('Premchand.txt'))

w_tokens = [w for w in tokens if w.isalpha()]

print(sorted(set(w_tokens))[:30])

text = nltk.Text(w_tokens)

text.dispersion_plot(["अऋण"])

