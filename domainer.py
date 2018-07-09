import argparse, urllib.request

parser = argparse.ArgumentParser(description='Find possible domains that use the tld in the name')
parser.add_argument('--tld','-t', default=None,type=argparse.FileType('r'), help='list of top level domains (tlds), default iana.org list if left empty')
parser.add_argument('--words','-w', required=True, type=argparse.FileType('r'), help='list of words to search')
parser.add_argument('--domains', '-d', default='domains.txt', type=argparse.FileType('w'), help="file to output to, defaults to domains.txt")

args = parser.parse_args()



if args.tld == None:
	tlds = urllib.request.urlopen('http://data.iana.org/TLD/tlds-alpha-by-domain.txt').read().decode('UTF-8').splitlines()[1:]
else:
	tlds = args.tld.read().splitlines()	

words = args.words.read().splitlines()
domains = args.domains

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


print('Done! Check', args.domains.name)
