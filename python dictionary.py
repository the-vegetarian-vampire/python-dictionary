import csv

with open("cats.csv", "r") as file:  # this opens the file; file being cats for example
    reader = csv.DictReader(file)  # this tells python to read the file
    counts = {}  # this is an empty dictionary (keys with values) can also be: counts = dict()
        for row in reader:  # this goes through file's row in dictionary
            cats = row["cats"]  # cats is now a variable
            counts[cats] += 1  # iterates(loops) over cats and adds one
        else:
            counts[cats] = 1

for cats in sorted(counts): #  iterates over counts in key of dictionary and sorts alphabetically
    print(f"{cats}: {counts[cats]}") 