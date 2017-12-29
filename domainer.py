tlds = open('tld2.txt').read().splitlines()[1:]
words = open('100k.txt', encoding='UTF-8').read().splitlines()
domains = open('domains.txt', 'w',encoding='UTF-8')
matches = []

for domain in tlds:
	for word in words:

		length = len(word)  - len(domain)

		if (len(domain) >= len(word)) or (word[0] == '#'):
			exit

		elif domain.lower() == word[length:]:

			match = word[0:length] + '.' + domain.lower()

			matches.append(match)
			domains.write(match + '\n')

print(matches)

