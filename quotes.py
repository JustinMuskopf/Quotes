import random, json; 
print random.choice(json.load(open('quotes.json'))["quotes"])["quote"].encode('utf-8');
