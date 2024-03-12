from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        comments = data.split("\n")
        if len(comments) == 1:
            print(">>> Single-line Comment")
            print(data)
        else:
            print(">>> Multi-line Comment")
            print(data)
        return
    
    def handle_data(self, data):
        if data == "\n":
            pass
            # print("# SKIP BLANK DATA")
        else:
            print(">>> Data")
            print(data)
        return

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

