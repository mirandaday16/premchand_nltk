import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from nltk.probability import FreqDist

y_font = {'fontname': 'Devanagari Sangam MN'}
plt.yticks(**y_font)

nltk.corpus.indian.words('hindi.pos')


# Setting up corpus text
corpus_root = '.'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
string_text = wordlists.raw('Premchand.txt')
tokens = [w for w in word_tokenize(string_text)]
w_tokens = [w for w in tokens]
text = nltk.Text(w_tokens)


# Vocabulary counting
print("Total words in corpus: ", len(text))
print("Total unique vocabulary words: ", len(set(text)))


# Looking at collocations
print("Number of collocations: ", len(text.collocation_list()))
for w in text.collocation_list():
    print(w)
print("Collocations are almost all multi-word verb constructions,"
      "two-part names, or names/titles followed by honorifics")


# Looking at frequently distributed words
f_dist = FreqDist(text)
f_dist_list = f_dist.most_common(1000)
for w in f_dist_list:
    if len(w[0]) > 6:
        print(w[0], "occurs", w[1], "times.")

# Dispersion plot of most frequent content words:
text.dispersion_plot(["विश्वास", "प्रसन्न", "बुढ़िया", "स्वीकार", "मुश्किल", "बिरादरी", "मुस्कराकर",
                      "नेत्रों", "व्यवहार", "आश्चर्य", "स्वार्थ", "विपत्ति", "परीक्षा", "सहानुभूति",
                      "मुहल्ले", "सैकड़ों", "दारोग़ा", "प्रस्ताव"])


# Dispersion plot for some terms referring to girls/women:
text.dispersion_plot(["महिला", "औरत", "बीवी", "पत्नी", "बेटी", "बच्ची", "लड़की", "दादी", "नानी", "बुढ़िया", "विधवा",
                      "रानी", "वेश्या", "बेचारी"])


# Dispersion plot for words related to social topics:
text.dispersion_plot(["गाँव", "किसान", "गाय", "भ्रष्ट", "राजनीति", "जात", "हिंदू",
                      "मुसलमान", "इस्लाम", "धर्म", "धार्मिक", "अधिकार",
                      "न्याय", "अन्याय", "अमेरिका"])


# Dispersion plot for some place names:
text.dispersion_plot(["दिल्ली", "हैदराबाद", "कलकत्ता", "लखनऊ", "कानपुर",
                      "बनारस"])
