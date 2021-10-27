#!/usr/bin/python3

class Author:

  def __init__(self, name):
    self.name = name

class Book:

  def __init__(self, name, year, author):
    self.name = name
    self.year = year
    self.author = author

  def get_info(self):
    return f"{self.name} ({self.year}) by {self.author.name}"

def main():
  author = Author("Robert E. Howard")
  book = Book("Conan", 1967, author)
  print(book.get_info())

if __name__ == "__main__":
  main()
