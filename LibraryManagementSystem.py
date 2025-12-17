class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,iterations=1):
        for _ in range (iterations):
            print("Enter the details of the book you want to add\n")
            title = input("Enter the Book's Title: ").strip()
            author = input("Enter the Author's Name: ").strip()
            if title and author:
                self.books.append(Book(title,author))
                print(f"The Book '{title}' has been added to the library")
                print("---------------------------------------------")
            else:
                print("Both Title and Author must be non-empty strings\n")
        print("All Books have been added successfully\n")

    def list_books(self):
        if not self.books:
            print("No books in the library.\n")
        else:
             print(f"There are {len(self.books)} Books in the library\n")
             for book in self.books:
                 print(book)
                 print("--------------------------------------------------------------------\n")
                



    def run(self):
        while True:
            operation = int(input("What is your preferred operation now? (1-Add Books | 2-View Books)\n"))
            if operation in (1, 2):
                if operation == 1:
                    iterations=int(input("How Many books do you want to add\n"))
                    self.add_book(iterations)
                elif operation == 2:
                    self.list_books()
            else:
                raise ValueError("You Must pick Number from 1 or 2")
            choice=input("Would you Like to continue using the program?press any key to continue, press n to exit\n")
            if choice=='n':
                print("Thanks for using my program\n")
                break

if __name__=="__main__":
    lib=Library()
    lib.run()

        
                


        

