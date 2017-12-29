import urllib.request, urllib.error, urllib.parse,http.cookiejar
import re

def checkDomain(domain):
  site='http://www.checkdomain.com/cgi-bin/checkdomain.pl?domain=' + domain
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
  req = urllib.request.Request(site, headers=hdr)
  response = urllib.request.urlopen(req)
  data = response.read()
  pat = re.compile("has already been registered by the organization below")
  if pat.search(data.decode('utf-8')) is None:
    print("Domain %s : Available" %(domain))
  else:
    print("Domain %s : Not Available" %(domain))


fo = open("domains.txt",'r', encoding="UTF-8")
av = open('availables.txt', 'w', encoding="UTF-8")
domains = fo.readlines()
fo.close()

for domain in domains:
  domain = domain.strip()
  av.write(str(checkDomain(domain)) + '\n')

       