import urllib.error
import bs4
import requests
from bs4 import BeautifulSoup
import time
from urllib.robotparser import RobotFileParser
import Logger

class Fetch:

    #TODO: Fix returværdier på funktioner
    #Get HTML from provided url - returns bs4 html file

    def fetchHTML(self, url: str) -> bs4.BeautifulSoup:
        try:
            robot_parser = RobotFileParser()
            log = Logger.logger()
            robot_parser.set_url(url)
            robot_parser.read()
            if robot_parser.can_fetch("*", url):
                start = time.time()
                html = requests.get(url, timeout=1)
                log.set_fetch_log(url, start)

            return html

        except requests.exceptions.Timeout:
            print("Could not connect to server. Timed out")

        except urllib.error.URLError:
            print("Not possible to fetch from URL. DNS Error")

    #Parse HTML

    def parseHTML(self, html: bs4.BeautifulSoup) -> bs4.BeautifulSoup:
        try:
            parsed_html = BeautifulSoup(html.text, "html.parser")

            print(type(parsed_html))

            return parsed_html

        except AttributeError:
            print("Crawler.extractTextHTML - file error")

    #Extract links from HTML
    def extractLinksHTML(self, html):
        if html:
            for a in html.find_all('a'):
                if a['href'].startswith("http"):
                    print("Full links " + a['href'])
                elif a['href'].startswith("/"):
                    print("Internal links " + a['href'])


#TODO: URL Frontier
#TODO: Content seen, URL filter, Duplicate URL Elimination