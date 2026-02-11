from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date

engine = create_engine("sqlite:///fintrack.db")

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    expenses = relationship("Expense", back_populates="category")


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(Date)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Float)
    next_date = Column(Date)


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    month = Column(String, unique=True)
    limit = Column(Float)


Base.metadata.create_all(engine)


class ExpenseManager:

    @staticmethod
    def add_expense():
        try:
            title = input("Title: ")
            amount = float(input("Amount: "))
            cat_name = input("Category: ")

            category = session.query(Category).filter_by(name=cat_name).first()
            if not category:
                category = Category(name=cat_name)
                session.add(category)
                session.commit()

            exp = Expense(
                title=title,
                amount=amount,
                date=date.today(),
                category=category
            )

            session.add(exp)
            session.commit()
            print("Expense added")

        except Exception as e:
            session.rollback()
            print("Error:", e)

    @staticmethod
    def update_expense():
        try:
            exp_id = int(input("Expense ID: "))
            expense = session.get(Expense, exp_id)   # correct method

            if not expense:
                print("Not found")
                return

            expense.amount = float(input("New amount: "))
            session.commit()
            print("Updated")

        except Exception as e:
            session.rollback()
            print("Error:", e)

    @staticmethod
    def delete_expense():
        try:
            exp_id = int(input("Expense ID: "))
            expense = session.get(Expense, exp_id)

            if expense:
                session.delete(expense)
                session.commit()
                print("🗑 Deleted")
            else:
                print("Not found")

        except Exception as e:
            session.rollback()
            print("Error:", e)

class SearchManager:

    @staticmethod
    def search_by_date():
        d = input("Date (YYYY-MM-DD): ")

        result = session.execute(
            text("SELECT title, amount FROM expenses WHERE date=:d"),
            {"d": d}
        )

        print("\nExpenses:")
        for row in result:
            print(row.title, "₹", row.amount)



class ReportManager:

    @staticmethod
    def category_report():
        sql = """
        SELECT c.name, SUM(e.amount)
        FROM categories c
        JOIN expenses e ON c.id = e.category_id
        GROUP BY c.name
        """

        result = session.execute(text(sql))

        print("\n📊 Category Report")
        for row in result:
            print(row[0], "→ ₹", row[1])


class BudgetManager:

    @staticmethod
    def set_budget():
        month = input("Month (YYYY-MM): ")
        limit_val = float(input("Limit: "))

        budget = session.query(Budget).filter_by(month=month).first()

        if budget:
            budget.limit = limit_val
        else:
            session.add(Budget(month=month, limit=limit_val))

        session.commit()
        print("Budget set")

    @staticmethod
    def check_budget():
        month = input("Month (YYYY-MM): ")

        budget = session.query(Budget).filter_by(month=month).first()
        if not budget:
            print("No budget")
            return

        spent = session.execute(
            text("""
            SELECT SUM(amount) FROM expenses
            WHERE strftime('%Y-%m', date)=:m
            """),
            {"m": month}
        ).scalar() or 0

        print(f"Spent ₹{spent} / ₹{budget.limit}")

        if spent > budget.limit:
            print("⚠️ Budget exceeded")


def menu():
    print("""
====== FINTRACK ======
1 Add Expense
2 Update Expense
3 Delete Expense
4 Search by Date
5 Category Report
6 Set Budget
7 Check Budget
0 Exit
""")

while True:
    menu()
    ch = input("Choice: ")

    if ch == "1":
        ExpenseManager.add_expense()
    elif ch == "2":
        ExpenseManager.update_expense()
    elif ch == "3":
        ExpenseManager.delete_expense()
    elif ch == "4":
        SearchManager.search_by_date()
    elif ch == "5":
        ReportManager.category_report()
    elif ch == "6":
        BudgetManager.set_budget()
    elif ch == "7":
        BudgetManager.check_budget()
    elif ch == "0":
        break
    else:
        print("Invalid")
