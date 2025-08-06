from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Book:
    def __init__(self , book_id:str , title:str, author:str, publication_year: int, total_copies: int = 1 ):
        self.book_id = book_id  
        self.title = title  
        self.author = author  
        self.publication_year = publication_year 
        self.total_copies = total_copies  
        self.available_copies = total_copies


    def __str__(self):
         return f"{self.title} by {self.author} ({self.publication_year}) - Available: {self.available_copies}/{self.total_copies}"


    def check_availability(self) -> bool:
        
        return self.available_copies > 0
    
    def borrow_copy(self) -> bool:
        
        if self.check_availability():
            self.available_copies -= 1
            return True
        return False
    
    def return_copy(self) -> None:

        if self.available_copies < self.total_copies:
            self.available_copies += 1


class Member:
        def __init__(self, member_id: str, name: str, email: str):
           self.member_id = member_id  
           self.name = name  
           self.email = email 
           self.borrowed_books: Dict[str, datetime] = {}  


        def __str__(self):
            return f"Member: {self.name} (ID: {self.member_id}) - Borrowed books: {len(self.borrowed_books)}"
    
        def borrow_book(self, book_id: str, borrow_date: datetime = datetime.now()) -> bool:
        
            if book_id not in self.borrowed_books:
                self.borrowed_books[book_id] = borrow_date
                return True
            return False
    
        def return_book(self, book_id: str) -> bool:
        
            if book_id in self.borrowed_books:
               del self.borrowed_books[book_id]
               return True
            return False
        
        def get_overdue_books(self) -> Dict[str, datetime]:
        
            overdue_books = {}
            for book_id, borrow_date in self.borrowed_books.items():
                if datetime.now() - borrow_date > timedelta(days=14):
                    overdue_books[book_id] = borrow_date
            return overdue_books

class LoanManagement:
    def __init__(self):
        self.loans: Dict[str, List[str]] = {}  # کتاب‌های امانت داده شده به هر عضو
        self.book_status: Dict[str, str] = {}  # وضعیت هر کتاب (امانت داده شده یا آزاد)
        
    def loan_book(self, member_id: str, book_id: str) -> bool:
        """ثبت امانت دادن یک کتاب به یک عضو"""
        if book_id in self.book_status: 
            return False  
            
        if member_id not in self.loans:
            self.loans[member_id] = []
            
        self.loans[member_id].append(book_id)
        self.book_status[book_id] = member_id  
        return True
    
    def return_loan(self, member_id: str, book_id: str) -> bool:
        """ثبت بازگشت یک کتاب از یک عضو"""
        if member_id in self.loans and book_id in self.loans[member_id]:
            self.loans[member_id].remove(book_id)
            del self.book_status[book_id]  
            return True
        return False
    
    def get_member_loans(self, member_id: str) -> List[str]:
        """لیست کتاب‌های امانت گرفته شده توسط یک عضو"""
        return self.loans.get(member_id, [])
    
    def get_book_borrower(self, book_id: str) -> Optional[str]:
        """عضو امانت‌گیرنده یک کتاب خاص"""
        return self.book_status.get(book_id)  
    


class Library:
    def __init__(self, name: str):
        self.name = name  # نام کتابخانه
        self.books: Dict[str, Book] = {}  # دیکشنری کتاب‌ها با کلید book_id
        self.members: Dict[str, Member] = {}  # دیکشنری اعضا با کلید member_id
        self.loan_manager = LoanManagement()  # مدیر امانت‌ها
        
    def add_book(self, book: Book) -> bool:
        """اضافه کردن یک کتاب جدید به کتابخانه"""
        if book.book_id in self.books:
            return False
        self.books[book.book_id] = book
        return True
    
    def add_member(self, member: Member) -> bool:
        """اضافه کردن یک عضو جدید به کتابخانه"""
        if member.member_id in self.members:
            return False
        self.members[member.member_id] = member
        return True
    
    def borrow_book(self, member_id: str, book_id: str) -> bool:
        """امانت دادن یک کتاب به یک عضو"""
        if member_id not in self.members or book_id not in self.books:
            return False
            
        book = self.books[book_id]
        member = self.members[member_id]
        
        if not book.borrow_copy():
            return False
            
        if not self.loan_manager.loan_book(member_id, book_id):
            book.return_copy()  
            return False
            
        member.borrow_book(book_id)
        return True
    
    def return_book(self, member_id: str, book_id: str) -> bool:
        """بازگرداندن یک کتاب از یک عضو"""
        if member_id not in self.members or book_id not in self.books:
            return False
            
        book = self.books[book_id]
        member = self.members[member_id]
        
        if not self.loan_manager.return_loan(member_id, book_id):
            return False
            
        book.return_copy()
        member.return_book(book_id)
        return True
    
    def search_books(self, title: str = None, author: str = None) -> List[Book]:
        """جستجوی کتاب بر اساس عنوان و/یا نویسنده"""
        results = []
        for book in self.books.values():
            if (title is None or title.lower() in book.title.lower()) and \
               (author is None or author.lower() in book.author.lower()):
                results.append(book)
        return results
    
    def get_overdue_loans(self) -> Dict[str, List[str]]:
        """لیست تمام امانت‌های گذشته از موعد"""
        overdue_loans = {}
        for member_id, member in self.members.items():
            overdue_books = member.get_overdue_books()
            if overdue_books:
                overdue_loans[member_id] = list(overdue_books.keys())
        return overdue_loans
    
    def generate_report(self) -> Dict:
        """تولید گزارش از وضعیت کتابخانه"""
        return {
            "total_books": len(self.books),
            "total_members": len(self.members),
            "available_books": sum(1 for book in self.books.values() if book.available_copies > 0),
            "borrowed_books": sum(1 for book in self.books.values() if book.available_copies < book.total_copies),
            "overdue_loans": len(self.get_overdue_loans())
        }
    

def main():
    library = Library("Central Library")

    # اضافه کردن کتاب‌ها
    library.add_book(Book("B001", "Python Crash Course", "Eric Matthes", 2019, 3))
    library.add_book(Book("B002", "Clean Code", "Robert C. Martin", 2008, 2))
    library.add_book(Book("B003", "Design Patterns", "Erich Gamma", 1994, 1))

    # اضافه کردن اعضا
    library.add_member(Member("M001", "Ali Rezaei", "ali@example.com"))
    library.add_member(Member("M002", "Maryam Mohammadi", "maryam@example.com"))

    # نمایش وضعیت اولیه
    print("=== Initial State ===")
    for book in library.books.values():
        print(book)
    for member in library.members.values():
        print(member)

    # امانت دادن کتاب‌ها
    print("\n=== Borrowing Books ===")
    library.borrow_book("M001", "B001")  # Ali borrows Python
    library.borrow_book("M002", "B002")  # Maryam borrows Clean Code

    # نمایش وضعیت پس از امانت
    print("\n=== After Borrowing ===")
    for book in library.books.values():
        print(book)
    for member in library.members.values():
        print(member)

    # جستجوی کتاب
    print("\n=== Search Results ===")
    print("Books with 'Python' in title:")
    for book in library.search_books(title="Python"):
        print(f"- {book}")

    # بازگرداندن کتاب
    print("\n=== Returning Books ===")
    library.return_book("M001", "B001")

    # گزارش نهایی
    print("\n=== Final Report ===")
    report = library.generate_report()
    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()