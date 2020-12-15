class WordSearch(object):
    def __init__(self, grid):
        self.__ROW_LENGTH = int(len(grid) ** 0.5)  # Intended to be fixed, but dynamically determined for testing
        self.__horizontals = [grid[i:i + self.__ROW_LENGTH] for i in range(0, len(grid), self.__ROW_LENGTH)]
        self.__verticals = [''.join([grid[j + i] for j in range(0, len(grid), self.__ROW_LENGTH)]) for i in
                            range(self.__ROW_LENGTH)]
        # Verticals exists to make searching for the string easier.
        # Using list comprehension over a nested loop as it's significantly faster

    def is_present(self, word):
        return any(word in line for line in self.__horizontals) or any(word in line for line in self.__verticals)


"""
Bonus Question:
The primary place where parrelisation could be used to speed up execution with a multi core system is with the class usage code:

for word in words_to_find:
    if ws.is_present(word):
        print "found {}".format(word)

Provided there wasn't a requirement to loop through the words in a specific order, then you could simply break the list into n sub-lists, 
where n is the number of threads capable of being used in your system (PoC example):

import threading


n = 16 # no of threads
size = int(len(words_to_find)/n)

def find_words(list):
    for word in list:
        if ws.is_present(word):
        print("found {}".format(word)


threads = []
start = datetime.now()
for i in range(n):
    arr = words_to_find[i * size:(i + 1) * size]
    print(len(arr))
    thr = threading.Thread(target=find_words, args=(arr,))
    thr.start()
    threads.append(thr)

for thread in threads:
    thread.join()



It's important to consider data access when using threading, however in the above example, data is only ever being read 
Although you might want some way to store the output to print it in a more orderly fashion
"""
