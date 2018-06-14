#import sys, json
#import random

#quote = random.choice(json.load(open('quotes.json'))["quotes"])
#print quote.encode('utf8')
import random, json; print random.choice(json.load(open('quotes.json'))["quotes"]);
