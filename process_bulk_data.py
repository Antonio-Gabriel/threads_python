from time import sleep
from random import choice
from threading import Thread

def comment(site, comment):
    """comments of website"""

    print(f"Enter in website: {site}")
    print(f"Lets an comment: {comment}")
    sleep(5)

    print(f"Processed data at: {site}")

threads = []
comments = [
    'Cool', 'Interesting', 
    'Incredible', 'Good idea', 
    'You can send me', 'I really like this'
    'Like', 'Love'
    ]

for site in range(30):
    new_thread = Thread(
                    target=comment, args=(site, choice(comments))
                )
    threads.append(new_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
