import requests
import re


class Query():
    def __init__(self, search: str):
        self.search = search
        self.results = []
        self.url = None
        self.html = None

    def lst(self):
        return self.results

    def get_html(self):
        self.html = requests.get(self.url).text

    def info(self):
        return {"Search term": self.search, "URL": self.url}

class YouTube(Query):
    def __init__(self, search: str):
        super().__init__(search)
    
    def get_html(self):
        return super().get_html()

    def scrape(self):
        r = r'(watch\?v=[\d\w\\&=_%+-]+)'
        self.results += (re.findall(r, self.html))[:5]
    
    def info(self):
        return super().info()
    
    def __str__(self):
        return "\n"+"\n".join([f"{i+1}: https://youtube.com/{self.results[i]}" for i in range(5)])
    
    def parse(self):
        self.url = f"https://www.youtube.com/results?search_query={self.search.replace(' ', '+')}"

class Amazon(Query):
    def __init__(self, search: str):
        super().__init__(search)
    
    def get_html(self):
        return super().get_html()
    
    def scrape(self):
        r = r'href="\/([\d\w\/=?-]+)\&'
        self.results += (re.findall(r, self.html))[:5]
    
    def info(self):
        return super().info()
    
    def __str__(self):
        return "\n"+"\n".join([f"{i+1} amazon.com/{self.results[i]}" for i in range(5)])
    
    def parse(self):
        self.url = f"https://www.amazon.com/s?k={self.search.replace(' ', '+')}"

