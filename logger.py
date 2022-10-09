import time

class logger():

    def __init__(self):
        self.storage = {}

    def set_fetch_log(self, url, started):
        stopped = time.time() - started
        if url in self.storage.keys():
            self.storage[url].append(stopped)
        else:
            self.storage[url] = [stopped]

        print("---")
        print(self.storage)
        print("---")

    def get_fetch_dict(self, url):
        return self.storage[url]

    #def crawlProgress(self):
        #Frontier image

    #def urlCrawled(self):

    #def frontierSize(self):
    #Should log:
    #Crawl progress
    #URLs crawled
    #Size of frontier
    #What else?