def readfile():
    with open("data.txt", "r") as file:
        data  = file.readlines()
        for line in data:
            res = line.split(" ")
            print(res)
            for word in res:
                print(word)

readfile()