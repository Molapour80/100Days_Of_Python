# 📚 Library Management System

![Library Banner](https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80)

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![OOP](https://img.shields.io/badge/Design-OOP-brightgreen)
![Status](https://img.shields.io/badge/Status-Stable-success)

A sophisticated Python-based library management system implementing Object-Oriented Programming principles with advanced features like loan tracking, overdue calculations, and comprehensive reporting.

## 🌟 Features

- **Book Management**:
  - Add/remove books
  - Track multiple copies
  - Search by title/author
- **Member Management**:
  - Member registration
  - Borrowing history
  - Overdue tracking
- **Loan System**:
  - Automatic availability checks
  - Due date calculations (14-day period)
  - Loan history tracking
- **Reporting**:
  - Real-time statistics
  - Overdue alerts
  - Inventory status

## 🖥️ Usage Example
```
# Create library
library = Library("Central Library")

# Add books
library.add_book(Book("B001", "Python Crash Course", "Eric Matthes", 2019, 3))

# Add members
library.add_member(Member("M001", "Ali Rezaei", "ali@example.com"))

# Borrow a book
library.borrow_book("M001", "B001")

# Generate report
report = library.generate_report()
```
