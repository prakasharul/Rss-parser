import feedparser
import json
import dateparser

class RssParser():
    def parseurl(self, url):
        '''
        parse a rss xml url feed to json
        '''
        self.parsed_url = feedparser.parse(url)
        return self.parsed_url
    
    def parsemultipleurl(self, urls):
        '''
        parse multiple rss xml feed url to json
        '''
        self.parsedurls = []
        for url in urls:
            self.parsedurls.append(self.parseurl(url))
        return self.parsedurls
    def parsepublishdate(self, date):
        parseddate = dateparser.parse(date)
        return parseddate.strftime('%m/%d/%Y %I:%M:%S %p')
        
    def feedformat(self, entry):
        '''
        feed format what are the field shout present in the feed
        '''
        feed = {}
        feed['title']  = entry.get('title')
        feed['summary']= entry.get('summary')
        feed['link'] = entry.get('link')
        feed['published']=self.parsepublishdate(entry.get('published'))
        feed['thumnail']=entry.get('storyimage')
        return feed.copy()
            
    def formatedfeed(self, urls):
        '''
        format parsed url to pecific format
        '''
        formatted_feeds = []
        feed = {}
        for url in urls:
            for entry in url.entries:
                feed = self.feedformat(entry)
                formatted_feeds.append(feed)
        return formatted_feeds
    
    def sortfeeds(self, formattedfeeds):
        '''
        sort parsed feeds by date time
        '''
        sortedfeeds = sorted(formattedfeeds, key=lambda t: t['published'], reverse=True)
        return sortedfeeds
        
