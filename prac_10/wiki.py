"""
Wiki
A program to search wikipedia.
"""
import wikipedia


def main():
    search = input("Wiki search: ")
    print("Loading...")
    print(wikipedia.search(search))
    print("Loading...")
    wiki_page = wikipedia.page(search, auto_suggest=False)
    print(wiki_page)
    print(wiki_page.url)
    print(wiki_page.title)
    print(wiki_page.summary)


main()
