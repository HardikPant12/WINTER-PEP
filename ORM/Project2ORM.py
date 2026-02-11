
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date

engine = create_engine("sqlite:///fintrack.db")                         # creates DB file
Base = declarative_base()                                               # base class
Session = sessionmaker(bind=engine)                                     # create session object
session = Session()


class Category(Base):
    __tablename__ = "categories"                                            # define table name

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    expenses = relationship("Expense", back_populates="category")               #two way connection from class


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(Date)

    category_id = Column(Integer, ForeignKey("categories.id"))                       # FK connects expense to category
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


Base.metadata.create_all(engine)                            # create karega sab tables


def add_expense():
    title = input("Title: ")
    amount = float(input("Amount: "))
    cat_name = input("Category: ")

    category = session.query(Category).filter(name=cat_name).first()         # search where name __.first --only 1st matching record

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


def update_expense():
    exp_id = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == exp_id).first()

    if expense:
        expense.amount = float(input("New amount: "))
        session.commit()
        print("Updated")
    else:
        print("Not found")


def delete_expense():
    exp_id = int(input("Expense ID: "))
    expense = session.query(Expense).filter(Expense.id == exp_id).first()

    if expense:
        session.delete(expense)
        session.commit()
        print("Deleted")
    else:
        print("Not found")


def search_by_date():
    d = input("Date YYYY-MM-DD: ")

    result = session.execute(                                               # runs raw sql query
        text("SELECT title, amount FROM expenses WHERE date=:d"),
        {"d": d}
    )

    print("Expenses:")
    for row in result:
        print(row.title, "Rs.", row.amount)


def category_report():
    sql = """
    SELECT c.name, SUM(e.amount)                                            # join === two table 
    FROM categories c
    JOIN expenses e ON c.id = e.category_id
    GROUP BY c.name
    """

    result = session.execute(text(sql))

    print("Category Report")
    for row in result:
        print(row[0], "Rs", row[1])


def set_budget():
    month = input("Month YYYY-MM: ")
    limit_val = float(input("Limit: "))

    budget = session.query(Budget).filter(Budget.month == month).first()

    if budget:
        budget.limit = limit_val
    else:
        session.add(Budget(month=month, limit=limit_val))

    session.commit()
    print("Budget set")


def check_budget():
    month = input("Month YYYY-MM: ")

    budget = session.query(Budget).filter(Budget.month == month).first()

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

    print("Spent:", spent, "/", budget.limit)

    if spent > budget.limit:
        print("Budget exceeded")
    else:
        print("Within budget")

# ---------- MENU ----------

while True:
    print("""
===== FINTRACK =====
1 Add Expense
2 Update Expense
3 Delete Expense
4 Search by Date
5 Category Report
6 Set Budget
7 Check Budget
8 Exit
""")

    ch = input("Choose: ")

    if ch == "1":
        add_expense()
    elif ch == "2":
        update_expense()
    elif ch == "3":
        delete_expense()
    elif ch == "4":
        search_by_date()
    elif ch == "5":
        category_report()
    elif ch == "6":
        set_budget()
    elif ch == "7":
        check_budget()
    elif ch == "8":
        break
    else:
        print("Invalid choice")
