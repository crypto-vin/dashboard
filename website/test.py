#strip text

from textblob import Sentence


full_msg = 'Vin Nairobi2020 0712897106'

def strip_msg(msg):
    words = full_msg.split()
    print(words)

strip_msg(full_msg)
