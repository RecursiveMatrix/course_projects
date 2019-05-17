from datetime import date
from datetime import datetime
import csv

## 1. Author class

class Author:

    def __init__(self,name,date_of_birth=None,nationality=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.nationality = nationality

    def get_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def __str__(self):
        return self.name+','+str(self.date_of_birth)+','+self.nationality

    def __add__(self,other):
        self.name = other.name
        self.date_of_birth = other.date_of_birth
        self.nationality = other.nationality
        return self

    @staticmethod
    def txt_to_dict():
        lines = [line.rstrip('\n') for line in open('author.txt')]
        author_dict = {}
        for index in range(len(lines)):
            name, year, month, day, nationality = lines[index].split(',')
            birthday = date(int(year), int(month), int(day))
            author_dict[index] = Author(name,birthday, nationality)
        return author_dict

    @staticmethod
    def load_author():
        authorlist = []
        for index in Author.txt_to_dict():
            if Author.txt_to_dict()[index].name not in authorlist:
                authorlist.append(Author.txt_to_dict()[index].name)
        return authorlist

    def save_new_author(self):
        with open('author.txt', 'a+') as f:
            csv_Writer = csv.writer(f)

            csv_Writer.writerow([self.name,self.date_of_birth.year,self.date_of_birth.month,self.date_of_birth.day,self.nationality])


    def delete_author(self):
        with open('author.txt', 'r') as r:
            lines = r.readlines()
        with open('author.txt', 'w') as w:
            for l in lines:
                if self.name not in l.split(',')[0]:
                    w.write(l)

    @staticmethod
    def search_by_name():
        search_authorname = str(input('Please indicate the name of the author: '))
        for index in Author.txt_to_dict():
            if Author.txt_to_dict()[index].name == search_authorname:
                result = Author(Author.txt_to_dict()[index].name,Author.txt_to_dict()[index].date_of_birth,Author.txt_to_dict()[index].nationality)
                if result =={}:
                    print('The author you are searching is not registered!')

        return result

    @staticmethod
    def search_by_nationality():
        search_nationality = str(input('Please indicate the nationality of the author: ')).upper()
        authorlist =[]
        for index in Author.txt_to_dict():
            if Author.txt_to_dict()[index].nationality == search_nationality:
                authorlist.append(Author.txt_to_dict()[index].name)
        if authorlist ==[]:
            return print('There is no author with such nationality!')
        else:
            return authorlist

    @staticmethod
    def search_by_age_range():
        search_age_start = int(input('Please indicate the minimum age of the author: '))
        search_age_end = int(input('Please indicate the maximum age of the author: '))
        authorlist =[]
        for index in Author.txt_to_dict():
            if Author.txt_to_dict()[index].get_age()>=search_age_start and Author.txt_to_dict()[index].get_age()<=search_age_end:
                authorlist.append(Author.txt_to_dict()[index].name)
        if authorlist ==[]:
            return print('There is no author within in the given age range!')
        else:
            return authorlist


# a = Author('LS',date(1989,12,18),'CN')
# b = Author('ztl',date(2000,3,14),'CA')
# print(a.get_age())
# print(a)
# print(a+b)
# print(Author.load_author())
# a.save_new_author()
# a.delete_author()
# print(Author.search_by_name())
# print(Author.search_by_nationality())
# print(Author.search_by_age_range())



## 2. Book class

class Book:

    def __init__(self,bookname,authorname=None,publisher=None):
        self.bookname = bookname
        self.authorname = authorname
        self.publisher = publisher

    def __str__(self):
        return self.bookname+','+self.authorname+','+self.publisher

    def __add__(self,other):
        self.bookname = other.bookname
        self.authorname = other.authorname
        self.publisher = other.publisher
        return self

    @staticmethod
    def txt_to_dict():
        # get all information in a form of list
        lines = [line.rstrip('\n') for line in open('book.txt')]
        book_dict = {}

        for index in range(len(lines)):
            bookname, authorname,publisher = lines[index].split(',')
            book_dict[index] = Book(bookname,authorname,publisher)

        return book_dict

    @staticmethod
    def load_book():
        booklist = []
        for index in Book.txt_to_dict():
            if Book.txt_to_dict()[index].bookname not in booklist:
                booklist.append(Book.txt_to_dict()[index].bookname)
        return booklist

    def save_new_book(self):
        with open('book.txt', 'a+') as f:
            csv_Writer = csv.writer(f)
            csv_Writer.writerow([self.bookname,self.authorname,self.publisher])

    def delete_book(self):
        with open('book.txt', 'r') as r:
            lines = r.readlines()
        with open('book.txt', 'w') as w:
            for l in lines:
                if self.bookname not in l.split(',')[0]:
                    w.write(l)


    @staticmethod
    def search_by_name():
        search_bookname = str(input('Please indicate the name of the book: '))
        for index in Book.txt_to_dict():
            if Book.txt_to_dict()[index].bookname == search_bookname:
                result = Book(search_bookname,Book.txt_to_dict()[index].authorname,Book.txt_to_dict()[index].publisher)
        if result == None:
            print('The book you are searching is not registered!')
        return result


    @staticmethod
    def search_by_authorname():
        booklist = []
        search_authorname = input('Please type in the name of an author: ')
        for index in Book.txt_to_dict():
            if Book.txt_to_dict()[index].authorname == search_authorname:
                booklist.append(Book.txt_to_dict()[index].bookname)
        if booklist == []:
            print('The book you are searching is not registered!')
        return booklist

    @staticmethod
    def search_by_nationality():
        booklist =[]
        authorlist_buffer = Author.search_by_nationality()
        for index in Book.txt_to_dict():
            for name in authorlist_buffer:
                if name == Book.txt_to_dict()[index].authorname:
                    booklist.append(Book.txt_to_dict()[index].bookname)
        if booklist == []:
            print('The book you are searching is not registered!')
        return booklist

    @staticmethod
    def search_by_age():
        booklist = []
        booklist_buffer = Author.search_by_age_range()
        for index in Book.txt_to_dict():
            for name in booklist_buffer:
                if name == Book.txt_to_dict()[index].authorname:
                    booklist.append(Book.txt_to_dict()[index].bookname)
        if booklist == []:
            print('There is no such book according to the given nationality of the author!')

        return booklist




    # comprehensive search
    # @staticmethod
    # def search_by_authorinfo():
    #     booklist =[]
    #     choice = input('Please indicate your preference of searching: \n'
    #                        '1. Search book by authorname\n'
    #                        '2. Search book by nationality of an author\n'
    #                        '3. Search book by the age of an author')
    #     if choice == str(1):
    #
    #         search_authorname = str(input('Please type in the name of an author: '))
    #         for index in Book.txt_to_dict():
    #             if Book.txt_to_dict()[index].authorname == search_authorname:
    #                 booklist.append(Book.txt_to_dict()[index].bookname)
    #
    #     elif choice == str(2):
    #
    #         if Author.search_by_nationality() != None:
    #             for name in Author.search_by_nationality():
    #                 for index in Book.txt_to_dict():
    #                     if name == Book.txt_to_dict()[index].authorname:
    #                         booklist.append(Book.txt_to_dict()[index].bookname)
    #
    #         else:
    #             print('There is no such book according to the given nationality of the author!')
    #
    #     elif choice == str(3):
    #         search_age = int(input('Please type in the age of an author: '))
    #         for index in Author.txt_to_dict():
    #             if Author.txt_to_dict()[index].get_age() == search_age:
    #                 for authorname in Book.txt_to_dict():
    #                     if Book.txt_to_dict()[authorname].authorname == Author.txt_to_dict()[index].name:
    #                         booklist.append(Book.txt_to_dict()[authorname].bookname)
    #
    #     else:
    #         print('Sorry,your request cannot be recognized!')
    #
    #     if booklist == []:
    #         return print('Book information is not found!')
    #     return booklist


# b = Book('The old man and the sea','Haminwei','RU PRESS')
# b1 = Book('The old time','Hiroki','JP PRESS')
# print(b)
# print(b+b2)
# print(Book.txt_to_dict())
# print(Book.load_book())
# b.save_new_book()
# b1.save_new_book()
# b.delete_book()
# print(Book.search_by_name())
# print(Book.search_by_nationality())
# print(Book.search_by_authorname())
# print(Book.search_by_age())


## 3. User class

class User:

    def __init__(self,username,birthyear=None,street_NO=None,city=None,country=None,phone=None):

        self.username = username
        self.birthyear = birthyear
        self.street_NO = street_NO
        self.city = city
        self.country = country
        self.phone = phone

    def __str__(self):
        return self.username+','+str(date.today().year-self.birthyear)+','+self.city+','+self.country+','+self.phone

    def __add__(self,other):
        self.username = other.username
        self.country = other.country
        self.city = other.city
        self.street_NO = other.street_NO
        self.phone = other.phone
        return self

    @staticmethod
    def txt_to_dict():
        lines = [line.rstrip('\n') for line in open('user.txt')]
        user_dict = {}
        for index in range(len(lines)):
            # print(len(lines[index].split(',')))
            username, birthyear, street_NO, city, country, phone = lines[index].split(',')
            user_dict[index] = User(username,int(birthyear),street_NO,city,country,phone)
        return user_dict



    @staticmethod
    def load_user():
        userlist = []
        for index in User.txt_to_dict():
            if User.txt_to_dict()[index].username not in userlist:
                userlist.append(User.txt_to_dict()[index].username)
        return userlist

    def save_new_user(self):
        with open('user.txt', 'a+') as f:
            csv_Writer = csv.writer(f)
            csv_Writer.writerow([self.username,self.birthyear,self.street_NO,self.city,self.country,self.phone])

    def delete_user(self):
        with open('user.txt', 'r') as r:
            lines = r.readlines()
        with open('user.txt', 'w') as w:
            for l in lines:
                if self.username not in l.split(',')[0]:
                    w.write(l)


    @staticmethod
    def search_by_name():
        search_name = input('Please indicate the name of the user: ')
        for index in User.txt_to_dict():
            if User.txt_to_dict()[index].username == search_name:
                result = User(User.txt_to_dict()[index].username,User.txt_to_dict()[index].birthyear,User.txt_to_dict()[index].street_NO,
                              User.txt_to_dict()[index].city,User.txt_to_dict()[index].country,User.txt_to_dict()[index].phone)

                return result


    @staticmethod
    def search_by_lastname():
        userlist =[]
        search_lastname = input('Please indicate the last name of the user: ')
        for index in User.txt_to_dict():
            if User.txt_to_dict()[index].username.split(' ')[-1] == search_lastname:
                userlist.append(User.txt_to_dict()[index].username)
        if userlist == None:
            print('The user you are searching is not registered!')
        return userlist


    @staticmethod
    def search_by_city():
        userlist =[]
        search_city = input('Please type in the city of a user: ')
        for index in User.txt_to_dict():
            if User.txt_to_dict()[index].city == search_city:
                userlist.append(User.txt_to_dict()[index].username)
        return userlist

    @staticmethod
    def search_by_phone():
        userlist = []
        search_phone = str(input('Please type in the phone number of a user: '))
        for index in User.txt_to_dict():
            if User.txt_to_dict()[index].phone == search_phone:
                userlist.append(User.txt_to_dict()[index].username)
        if userlist == None:
            print('The user you are searching is not registered!')
        return userlist

    # @staticmethod
    # def search_by_userinfo():
    #     userlist = []
    #     choice = input('Please indicate your preference of searching: \n'
    #                    '1. Search book by the city of a user\n'
    #                    '2. Search book by the phone of a user\n'
    #                    '3. Search book by the last name of a user')
    #
    #     if choice == str(1):
    #
    #         search_city = str(input('Please type in the city of a user: '))
    #         for index in User.txt_to_dict():
    #             if User.txt_to_dict()[index].city == search_city:
    #                 userlist.append(User.txt_to_dict()[index].username)
    #
    #     elif choice == str(2):
    #
    #         search_phone = str(input('Please type in the phone number of a user: '))
    #         for index in User.txt_to_dict():
    #             if User.txt_to_dict()[index].phone == search_phone:
    #                 userlist.append(User.txt_to_dict()[index].username)
    #
    #     elif choice == str(3):
    #         search_lastname = str(input('Please type in the last name of a user: '))
    #         for index in User.txt_to_dict():
    #             if User.txt_to_dict()[index].username.split(' ')[-1] == search_lastname:
    #                 userlist.append(User.txt_to_dict()[index].username)
    #
    #     else:
    #         print('Sorry,your request cannot be recognized!')
    #
    #
    #     if userlist == []:
    #         return print('User information is not found!')
    #     return userlist


# c = User('Li Shuo',1989,'proudfoot lane 605','london','CA','2262290987')
# c1 = User('Liu shang',2001,'cherryhill','pairs','CN','12239485577')
# print(c)
# print(c+c1)
# print(User.txt_to_dict())
# c.save_new_user()
# c1.save_new_user()
# c.delete_user()
# print(User.search_by_lastname())
# print(User.search_by_city())
# print(User.search_by_phone())
# print(User.search_by_userinfo())




## 4. Transaction class

class Transaction:


    def __init__(self,bookname,username,year=None,month=None,day=None,hour=None,minute=None,second=None,transaction_type=None):
        self.bookname = bookname
        self.username = username
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
        self.datetime = datetime(year,month,day,hour,minute,second)
        self.transaction_type = transaction_type



    @staticmethod
    def txt_to_dict():
        # get all information in a form of list
        lines = [line.rstrip('\n') for line in open('transaction.txt')]
        transaction_dict = {}

        for index in range(len(lines)):
            bookname,username,year,month,day,hour,minute,second,transaction_type = lines[index].split(',')
            transaction_dict[index] = Transaction(bookname,username,int(year),int(month),int(day),int(hour),int(minute),int(second),transaction_type)

        return transaction_dict


    def __str__(self):
        return str(self.datetime)+','+self.username+','+self.bookname+','+str(self.transaction_type)

    @staticmethod
    def load_transaction():
        transactionlist = []
        for index in Transaction.txt_to_dict():
            transactionlist.append(str(Transaction.txt_to_dict()[index].datetime)+','+Transaction.txt_to_dict()[index].username+','+Transaction.txt_to_dict()[index].bookname+','+Transaction.txt_to_dict()[index].transaction_type)
        return transactionlist


    def save_new_transaction(self):
        with open('transaction.txt', 'a+') as f:
            csv_Writer = csv.writer(f)
            csv_Writer.writerow([self.bookname,self.username,self.year,self.month,self.day,self.hour,self.minute,self.second,self.transaction_type])

    def delete_transaction(self):

        with open('transaction.txt', 'r') as r:
            lines = r.readlines()
        with open('transaction.txt', 'w') as w:
            for l in lines:
                itself = [self.bookname,self.username,str(self.year),str(self.month),str(self.day),str(self.hour),str(self.minute),str(self.second),str(self.transaction_type)]
                if itself[:-1] != l.split(',')[:-1]:
                        w.write(l)

        # considering transaction type

        # with open('transaction.txt', 'r') as r:
        #     lines = r.readlines()
        # with open('transaction.txt', 'w') as w:
        #     for l in lines:
        #         itself = [self.bookname,self.username,str(self.year),str(self.month),str(self.day),str(self.hour),str(self.minute),str(self.second),str(self.transaction_type)]
        #         if itself[-1] == l.split(',')[-1].replace('\n',''):
        #             if itself[:-1] != l.split(',')[:-1]:
        #                 w.write(l)
        #         else:
        #             w.write(l)

    @staticmethod
    def search_by_transaction():
        transactionlist = []
        search_date_year = str(input('Please type in the year: '))
        search_date_month = str(input('Please type in the month: '))
        search_date_day = str(input('Please type in the day: '))
        search_user = input('Please type in the user: ')
        search_book = input('Please type in the book name: ')

        for index in Transaction.txt_to_dict():
            if str(Transaction.txt_to_dict()[index].year) == search_date_year and str(Transaction.txt_to_dict()[index].month) == search_date_month and str(Transaction.txt_to_dict()[index].day) == search_date_day and str(Transaction.txt_to_dict()[index].username) == search_user and str(Transaction.txt_to_dict()[index].bookname==search_book):
                transactionlist.append(print(Transaction.txt_to_dict()[index]))
        else:
            print('There is no match information for this!')

        return transactionlist


    @staticmethod
    def search_by_transaction_time():
        transactionlist =[]
        search_date_year = str(input('Please type in the year: '))
        search_date_month = str(input('Please type in the month: '))
        search_date_day = str(input('Please type in the day: '))
        for index in Transaction.txt_to_dict():
            if str(Transaction.txt_to_dict()[index].year) == search_date_year and str(Transaction.txt_to_dict()[index].month) == search_date_month and str(Transaction.txt_to_dict()[index].day) == search_date_day:
                transactionlist.append(print(Transaction.txt_to_dict()[index]))
        if transactionlist ==[]:
            print('There is no match information for this!')
        else:
            return transactionlist

    @staticmethod
    def search_by_transaction_user():
        transactionlist = []
        search_user = input('Please type in the user: ')
        for index in Transaction.txt_to_dict():
            if str(Transaction.txt_to_dict()[index].username) == search_user:
                transactionlist.append(print(Transaction.txt_to_dict()[index]))
        if transactionlist == []:
            print('There is no match information for this!')
        else:
            return transactionlist

    @staticmethod
    def search_by_transaction_book():
        transactionlist = []
        search_book = input('Please type in the book name: ')
        for index in Transaction.txt_to_dict():
            if str(Transaction.txt_to_dict()[index].bookname) == search_book:
                transactionlist.append(print(Transaction.txt_to_dict()[index]))
        if transactionlist ==[]:
            print('There is no match information for this!')
        else:
            return transactionlist


# d = Transaction('Mysterious universe','ZTL',2018,10,2,8,23,40,0)
# print(Transaction.load_transaction())
# d.save_new_transaction()
# d.delete_transaction()
# Transaction.search_by_transaction_time()
# Transaction.search_by_transaction_user()
# Transaction.search_by_transaction_book()

# d.save_new_transaction()
# d.delete_transaction()
# For deleting any transaction by bookname, username or time and date, create such instance and then call delete.


# 5. Library


class Library:
    userlist = User.load_user()
    authorlist = Author.load_author()
    booklist = Book.load_book()
    transactionlist = Transaction.load_transaction()
    libdict = {'B1':2,'B2':1,'B3':3,'B4':2,'B5':5}

    def __init__(self, bookname,quantity):
        self.bookname = bookname
        self.quantitly = quantity

    @staticmethod
    def mainmenu():
        while True:
            primarychoice = input('Welcome to the Library Management System: \ni. AUTHORS\n'
                                  'ii. BOOKS\niii. USERS\niv. LIBRARY\nv.EXIT')

            searchauthor = False
            searchbook = False
            searchuser = False
            searchlibrary = False

            if primarychoice == '1':
                searchauthor = True
                if searchauthor == True:
                    while True:
                        authorchoice = input('What would you like to do with the author?\n'
                                      '1. ADD\n2. UPDATE\n3. DELETE\n4. SEARCH BY NAME\n5. SEARCH BY AGE\n'
                                        '6. SEARCH BY NATIONALITY\n7. GO BACK TO PREVIOUS MENU')

                        if authorchoice == '1':
                            authorname = input('Please type in the name of the author: ')
                            authorYear = int(input('Please type in the year of the author: '))
                            authorMonth = int(input('Please type in the month of the author: '))
                            authorDay = int(input('Please type in the date of the author: '))
                            authorDOB = date(authorYear,authorMonth,authorDay)
                            authornationality = input('Please type in the nationality of the author: ')
                            Author(authorname,authorDOB,authornationality).save_new_author()
                            print('The author has successfully been added to the system!')
                        elif authorchoice == '2':
                               author_inlist = Author.search_by_name()
                               authorname = input('Please type in the new name of the author: ')
                               authorYear = int(input('Please type in the new year of the author: '))
                               authorMonth = int(input('Please type in the new month of the author: '))
                               authorDay = int(input('Please type in the new date of the author: '))
                               authorDOB = date(authorYear, authorMonth, authorDay)
                               authornationality = input('Please type in the new nationality of the author: ')
                               author_inlist.delete_author()
                               Author(authorname, authorDOB, authornationality).save_new_author()
                               print('The author has successfully been updated in the system!')
                        elif authorchoice == '3':
                               authorname = input('Please type in the name of the author you want to delete: ')
                               Author(authorname).delete_author()
                               print('The author has successfully been deleted in the system!')
                        elif authorchoice == '4':
                               print(Author.search_by_name())
                        elif authorchoice == '5':
                               print(Author.search_by_age_range())
                        elif authorchoice == '6':
                               print(Author.search_by_nationality())
                        elif authorchoice == '7':
                           break
                        else:
                            print('Sorry, your request could not be recognized!')

            elif primarychoice == '2':
                searchbook = True
                if searchbook == True:
                    while True:
                        bookchoice = input('1. ADD\n2. UPDATE\n3. DELETE\n4. SEARCH BY NAME\n'
                                               '5. SEARCH BY AUTHOR OR NAME OR NATIONALITY\n6. GO BACK TO PREVIOUS MENU')
                        if bookchoice == '1':
                            bookname = input('Please type in the name of the book: ')
                            bookauthor = input('Please type in the author of the book: ')
                            bookpublisher = input('Please type in the publisher of the author: ')
                            newbook = Book(bookname,bookauthor,bookpublisher)
                            newbook.save_new_book()
                            print('The book has successfully been added to the system!')
                        elif bookchoice =='2':
                            book_inlist = Book.search_by_name()
                            bookname = input('Please type in the name of the book: ')
                            bookauthor = input('Please type in the author of the book: ')
                            bookpublisher = input('Please type in the publisher of the author: ')
                            newbook = Book(bookname, bookauthor, bookpublisher)
                            book_inlist.delete_book()
                            newbook = Book(bookname,bookauthor,bookpublisher)
                            newbook.save_new_book()
                            print('The book has successfully been updated in the system!')

                        elif bookchoice == '3':
                            bookname = input('Please type in the name of the book: ')
                            Book(bookname).delete_book()
                            print('The book has successfully been deleted in the system!')
                        elif bookchoice == '4':
                            print(Book.search_by_name())
                        elif bookchoice == '5':
                            booksubchoice = input('Would you like to search by:\n1.author name\n2.nationality\n3.age')
                            if booksubchoice =='1':
                                print(Book.search_by_authorname())
                            elif booksubchoice =='2':
                                print(Book.search_by_nationality())
                            elif booksubchoice =='3':
                                print(Book.search_by_age())
                            else:
                                print('Sorry, your request could not be recognized!')
                        elif bookchoice == '6':
                            break
                        else:
                            print('Sorry, your request could not be recognized!')

            elif primarychoice == '3':
                searchuser = True
                if searchuser == True:
                    while True:
                        userchoice = input('1. ADD\n2. UPDATE\n3. DELETE\n4. SEARCH BY NAME\n5. SEARCH BY CITY\n6.GO BACK TO PREVIOUS MENU')
                        if userchoice == '1':
                            username = input('Please type in the name of the user: ')
                            useryear = input('Please type in the year of the user: ')
                            userstreet = input('Please type in the street of the user: ')
                            usercity = input('Please type in the city of the user: ')
                            usercountry =input('Please type in the country of the user: ')
                            userphone = input('Please type in the phonenumber of the user: ')
                            newuser = User(username,useryear,userstreet,usercity,usercountry,userphone)
                            newuser.save_new_user()
                            print('The user has successfully been added to the system!')

                        elif userchoice == '2':
                            user_inlist = User.search_by_name()
                            username = input('Please type in the name of the user: ')
                            useryear = input('Please type in the year of the user: ')
                            userstreet = input('Please type in the street of the user: ')
                            usercity = input('Please type in the city of the user: ')
                            usercountry = input('Please type in the country of the user: ')
                            userphone = input('Please type in the phonenumber of the user: ')
                            newuser = User(username, useryear, userstreet, usercity, usercountry, userphone)
                            newuser.save_new_user()
                            user_inlist.delete_user()
                            print('The user has successfully been updated in the system!')

                        elif userchoice == '3':
                            username = input('Please type in the name of the user you want to delete: ')
                            User(username).delete_user()
                            print('The user has successfully been deleted in the system!')

                        elif userchoice == '4':
                            print(User.search_by_name())

                        elif userchoice == '5':
                            print(User.search_by_city())
                        elif userchoice == '6':
                            break
                        else:
                            print('Sorry, your request could not be recognized!')

            elif primarychoice == '4':
                searchlibrary = True
                if searchlibrary == True:
                    while True:
                        librarychoice = input('1. BORROW BOOK\n2. RETURN BOOK\n3. SHOW BOOK AILABILITY BY NAME\n'
                                          '4. SHOW BOOK AVAILABILITY BY AUTHOR NAME\n'
                                          '5. SHOW BOOK AVAILABILITY BY AUTHOR NATIONALITY\n'
                                          '6. SHOW BORROWED BOOK BY USER NAME\n7. SHOW BORROWED BOOK BY PHONE\n'
                                              '8. GO BACK TO PREVIOUS MENU')
                        if librarychoice =='1':
                            userborrow = input('Please indicate your name: ')
                            borrowbook = input('Please indicate the name of the book you want to borrow: ')
                            if borrowbook in Library.libdict and Library.libdict[borrowbook]>0:
                                Library.libdict[borrowbook] -= 1
                                Transaction(borrowbook, userborrow, datetime.now().year, datetime.now().month, datetime.now().day,
                                            datetime.now().hour, datetime.now().minute, datetime.now().second,transaction_type=1
                                            ).save_new_transaction()
                                print('The book has successfully been borrowed!')
                            else:
                                print('The book you want is not currently in the library!')

                        elif librarychoice =='2':
                            userborrow = input('Please indicate your name: ')
                            borrowbook = input('Please indicate the name of the book you want to return: ')
                            if borrowbook in Library.libdict:
                                Library.libdict[borrowbook] += 1
                                Transaction(borrowbook, userborrow, datetime.now().year, datetime.now().month, datetime.now().day,
                                            datetime.now().hour, datetime.now().minute, datetime.now().second,
                                            transaction_type=0).save_new_transaction()
                                print('The book has successfully been returned!')

                        elif librarychoice =='3':
                            showbookbyname = input('Please type in the bookname you want to check: ')
                            if showbookbyname in Library.libdict:
                                print('There are ',Library.libdict[showbookbyname],'of such book avaliable in the library.')
                            else:
                                print('Sorry, there is no such book in the library.')

                        elif librarychoice =='4':
                            showbookbyauthor_list = Book.search_by_authorname()
                            bookdict ={}
                            for book in showbookbyauthor_list:
                                if book in Library.libdict:
                                    bookdict[book] = Library.libdict[book]
                            if bookdict ==None:
                                print('Sorry, there is no such book in the library.')
                            else:
                                print(bookdict)

                        elif librarychoice == '5':
                            showbookbynationality_list = Book.search_by_nationality()
                            bookdict = {}
                            for book in showbookbynationality_list:
                                if book in Library.libdict:
                                    bookdict[book] = Library.libdict[book]
                            if bookdict == None:
                                print('Sorry, there is no such book in the library.')
                            else:
                                print(bookdict)

                        elif librarychoice =='6':
                            booklist = []
                            bufferdict ={}
                            search_bookbyuser = input('Please type in the user who borrowed book: ')
                            for index in Transaction.txt_to_dict():
                                if Transaction.txt_to_dict()[index].username == search_bookbyuser:
                                    bufferdict[Transaction.txt_to_dict()[index].bookname] = int(Transaction.txt_to_dict()[index].transaction_type)
                            for key in bufferdict:
                                if bufferdict[key]>0:
                                    booklist.append(key)
                            if booklist == []:
                                print('There is no match information for this!')
                            else:
                                print(booklist)


                        elif librarychoice == '7':
                            userbuffer =[]
                            booklist = []
                            bufferdict = {}
                            search_bookbyphone = input('Please type in the phone number of a user who borrowed book: ')
                            for index in User.txt_to_dict():
                                if User.txt_to_dict()[index].phone == search_bookbyphone:
                                    userbuffer.append(User.txt_to_dict()[index].username)
                            for user in userbuffer:
                                for index in Transaction.txt_to_dict():
                                    if Transaction.txt_to_dict()[index].username == user:
                                        bufferdict[Transaction.txt_to_dict()[index].bookname] = int(
                                            Transaction.txt_to_dict()[index].transaction_type)
                            for key in bufferdict:
                                if bufferdict[key] > 0:
                                    booklist.append(key)
                            if booklist == None:
                                print('There is no match information for this!')
                            else:
                                print(booklist)
                        elif librarychoice == '8':
                            break
                        else:
                            print('Sorry, your request could not be recognized!')

            elif primarychoice == '5':
                print('Thanks for using our library system!')
                exit()

            else:
                print('Sorry, your request could not be recognized!')



print(Library.mainmenu())
