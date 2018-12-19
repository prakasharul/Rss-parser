# Rss-parser
parse XML Rss feed to json with pretty formatted and sorted feeds 

### dependency 

```sh
pip install -r requirement.txt
```

### usage

```python
from rssparser import RssParser

rssparser = RssParser()

#parse a rss xml url feed to json
rssparser.parseurl('rss-url')

#parse multiple rss xml feed url to json
rssparser.parsemultipleurl('rss-url-list')

#format parsed url to pecific format
rssparser.formatedfeed('parsed-feed-url')

#sort formatted feeds by date time
rssparser.sortfeeds('formatted-feeds')
```
##### Sample Output

```json
{
"link":"https://www.ndtv.com/india-news/rafale-verdict-not-a-setback-still-an-issue-in-peoples-court-jyotiraditya-scindia-1962568",
"published":"12/14/2018 12:52:44 PM",
"summary":"The Supreme Court order giving the government a clean chit on the Rafale deal is not a setback as the issue is still live in the people court and the Congress will continue to raise it in...",
"thumnail":"https://c.ndtvimg.com/2018-12/abig59ak_jyotiraditya-scindia-parliament_120x90_14_December_18.jpg",
"title":"Rafale Jet Deal Still An Issue In People's Court: Jyotiraditya Scindia"
}
```



