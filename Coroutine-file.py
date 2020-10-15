def searcher():
    import time
    book = "This is the best book of wisdom"
    time.sleep(3)

    while True:
        text =(yield)
        if text in book:
            print("Your text in book")
        else:
            print("Text is not present")

search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("pal")

search.close()
