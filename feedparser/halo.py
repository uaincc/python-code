import feedparser


class RSS():
    def __init__(self, rss_url):
        self.rss_url = rss_url

    def parse_context(self):
        feed = feedparser.parse(self.rss_url)
        self.get_context(feed)

    def get_context(self, feed):
        for entry in feed.entries:
            item = {}
            item['title'] = entry.title
            item['url'] = entry.link
            item['desc'] = entry.description
            # published = entry.published_parsed
            # print(published)
            print(item)



if __name__ == '__main__':
    rss = RSS("https://uain.cc/rss.xml")
    rss.parse_context()
