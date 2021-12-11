from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

from . import pars
from textblob import Word

doc = u'Дорожный знак "Пешеходный переход" демонтирован вместе с опорой после ДТП.'
text_ru = TextBlob(doc)

print(text_ru.translate(to='en'))
