links=["https://www.thehindu.com/news/international/157-killed-as-strong-earthquake-jolts-nepals-mountainous-western-region/article67498659.ece","https://www.businesstoday.in/latest/in-focus/story/nepal-earthquake-death-toll-hits-140-pm-modi-offers-help-says-india-stands-in-solidarity-404563-2023-11-04","https://www.thehindu.com/news/international/nepal-jajarkot-earthquake-death-toll-november-4-2023/article67496449.ece"]
def getDocuments(urls):
    articles = list()
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraph_texts = soup.find_all('p')
        print("Hello")
        content = [re.sub(r'<.+?>', r'', str(p)) for p in paragraph_texts]
        content = [re.sub(
            r"[\"\#\%\&\(\)\*\+\/\:\<\=\>\@\[\\\]\^\_\`\{\|\}\~]+", " ", document) for document in content]
        content = [re.sub(r"[ \t\n\r\x0b\x0c]+", " ", document)
                   for document in content]
        print("Bye")
        if content:
            articles.append(" ".join(content))
    return articles

    articles =getDocuments(links)
    for a in articles:
      print(a)
