from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for J in attrs:
            print("-> {} > {}".format(*J))
        return

    def handle_endtag(self, tag):
        print("End   : {}".format(tag))
        return

    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for J in attrs:
            print("-> {} > {}".format(*J))
        return

html = ""
N = int(input())
for i in range(N):
    html += input().rstrip()
    html += "\n"

parser = MyHTMLParser()
parser.feed(html)
parser.close()

