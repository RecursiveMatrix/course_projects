# Introduction
This is a demo for a library system, which is a good practice of class construction and application in python for beginners.  
In this demo, five classes have been considered: `author`,`book`,`user`,`transaction` and `library`. For each class, particular class 
variables and functions have been considered according to the real requiements. All classes are logically linked to each other
with a detailed structure for reference.  
# Function

  - In this demo, txt files are used for mocking the databases for storing different kind of information in a distributted system.
There are four txt files which record the information of `author`,`book`,`transaction` and `user`.   
  - All classes could work independtely with each other while could be synchronized. For example, you could  find an author by
claiming name, nationality or the range of age as well as the book written by the author regardless of such information is not
stored in the same file, or same databases. (Although you could manipulate the data by modifying txt files by yourself, 
errors could occur since you need permission to do so in real world.) 
  - The `library` class is designed in a way of human-computer interface. Users could select functions according to their needs and 
bounce around the options. A more advanced design could be seperating the user with administrator in case of the fact we don't
want our custormer to access and modify the data of books and transactions in the library.

  
  
  
  

