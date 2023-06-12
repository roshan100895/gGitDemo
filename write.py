# file = open('text') --> to open a text file
# file.close() --> to close a file
# with open('text') as file --> to open and close file in one line

with open('text','r') as reader:
    contentList = reader.readlines() # values = [apple, banana, cat, dog, elephant]
    reversed(contentList) # reversed list [elephant, dog, cat, banana, apple]
    with open('text','w') as writer:
        for line in reversed(contentList):
            writer.write(line)
