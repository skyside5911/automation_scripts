from urllib.parse import quote

def text_to_link(text, url):
    return f'<a href="{url}{quote(text)}">{text}</a>'
text = "Aman"
url = "https://google.com/"
print(text_to_link(text, url))
