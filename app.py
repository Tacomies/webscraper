from webscraper import YouTube, Amazon


s = input("Search: ").lower()
if "-amazon" in s:
    q = Amazon(s.replace("-amazon", ""))
if "-youtube" in s:
    q = YouTube(s.replace("-youtube", ""))

try:
    q.parse()
    q.get_html()
    q.scrape()
    print(q)
except NameError:
    print("No site selected!")
