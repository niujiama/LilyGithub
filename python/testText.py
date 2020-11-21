with open('data/testText.txt') as f:
    rows = f.readlines()
    for i in range(len(rows)):
        print(rows[i])