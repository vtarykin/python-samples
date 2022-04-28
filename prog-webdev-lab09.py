import hashlib

books = input()
alg = input()

class PackDict: #преображает строку с названием и количеством книг в словарь
    def __init__(self, books):
        self.astr = books.split()
        self.adict = {}
        self.alist = []
        self.blist = []

    def makeDict(self):
        for i in self.astr:
            if i.isalpha():
                self.alist.append(i)
            else:
                self.blist.append(i)
        self.adict = dict(zip(self.alist, self.blist))
        self.adict = dict(sorted(self.adict.items()))

    def showDict(self):
        self.makeDict()
        for key in self.adict:
            print(key, self.adict[key])

    def __del__(self):
        pass


class HashBooks(PackDict): #преображает хэширует имена книг и выводит одной строкой

    def __init__(self, books, alg):
        self.astr = books
        self.hmd5 = alg

    def toHash(self):
        self.alist = []
        for i in self.astr.split():
            if i.isalpha():
                self.alist.append(i)
        self.astr = ""
        self.alist = list(map(lambda x: str(hashlib.md5(x.encode()).hexdigest()), self.alist))
        self.alist.sort()

        for j in self.alist:
            self.astr += self.hmd5 + " " + j + " "

        print(self.astr.strip())


newL = PackDict(books)
newL.showDict()

hashNew = HashBooks(books, alg)
hashNew.toHash()
