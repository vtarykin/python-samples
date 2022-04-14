class LibReg(object):
    def __init__(self):
        a_str = ''
        b_list = []
        a = 0
        self.a_str = a_str
        self.b_list = b_list
        self.a = a

    def borB(self):                         #borrow book -1 to book volume
        self.a -= 1
        print(self.a, end=' ')

    def retB(self):                         #return book to library +1 book
        self.a += 1
        print(self.a, end=' ')

    def showItem(self):                     #borrow book then return and show
        self.b_list.clear()                 #how the book's volume changed from
        self.a_str = input()                #every action
        self.b_list = self.a_str.split()
        m = 0
        n = 0
        while m < len(self.b_list):
            n = self.b_list[m]
            if n.isdigit():
                print(n, end=' ')
                self.a = int(n)
                LibReg.borB(self)
                LibReg.retB(self)
            else:
                print(n, end=' ')
            m += 1

    def __del__(self):
        print('sample has been destroyed')

a = LibReg()
a.showItem() # user prints any name and volume of books stored