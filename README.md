
# Either modify/run bash.py to print a quote to console, or execute this command:
python -c "import random, json; print(random.choice(json.load(open('quotes.json'))['quotes']));"

# For extra fun, ensure cowsay is installed and run:
python -c "import random, json; print(random.choice(json.load(open('quotes.json'))['quotes']))" | cowsay -n

