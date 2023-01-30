import json
import jmespath
f=open(r'H:\automation_scripts\aaascraping_sites\all_non_adult_listings.json', encoding="utf8")
data=json.load(f)
search_data="data[0:].domainName"
search_data="data[*].domainName"
search_data="data[?domainName.anysubfolder=='name_u_want_to_search'].domainName"
all_domain=(jmespath.search(search_data,data))
for i in all_domain:
    print(i.lower())