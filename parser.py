import feedparser as fp
data = fp.parse('https://infobus.francobus.ca/rss/Transportation-en-CA.xml')

for entry in data.entries:
    if 'Gabriel-Dumont' in entry.summary_detail.value:
        print('{}: {}'.format(entry.title[6:11], entry.title[39:]))
