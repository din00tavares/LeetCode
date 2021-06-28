import wordcloud
from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    uninteresting_words = {"the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"\
    "ebook","for","in","on","up","dr","mr","oh"}
    
    # LEARNER CODE START HERE
    frequencies = {}
    text = file_contents.split()
    for word in text:
        if not word.isalpha():
            word = ''.join([l for l in word if l.isalpha()])
        if word.lower() not in uninteresting_words:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
    #wordcloud
    cloud = wordcloud.WordCloud(background_color='white',width=1920, height=1080)
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# file_contents = open('word_cloud/dracula.txt',encoding='utf-8').read()
file_contents = BeautifulSoup(requests.get('https://www.python.org').content).text
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.savefig('word_cloud/python.png')
plt.show()