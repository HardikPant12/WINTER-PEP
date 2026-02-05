-- SUB QUERY : query inside query.

-- here i am usnig the shop database which i have created previously
USE shop;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product VARCHAR(50),
    amount INT
    -- FOREIGN KEY (customer_id) REFERENCES customer(customer_id) its not required when we join two table
);
INSERT INTO customers VALUES
(1, 'Aman', 'Delhi'),
(2, 'Riya', 'Mumbai'),
(3, 'Kabir', 'Delhi'),
(4, 'Neha', 'Pune'),
(5, 'Arjun', 'Bangalore'),
(6, 'Simran', 'Mumbai'),
(7, 'Rahul', 'Delhi'),
(8, 'Pooja', 'Chennai'),
(9, 'Vikas', 'Pune'),
(10, 'Anita', 'Bangalore');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 60000),
(102, 1, 'Mouse', 1500),
(103, 2, 'Mobile', 30000),
(104, 3, 'Keyboard', 2500),
(105, 3, 'Monitor', 12000),
(106, 5, 'Tablet', 20000),
(107, 6, 'Laptop', 65000),
(108, 7, 'Mobile', 28000),
(109, 7, 'Earphones', 2000),
(110, 11, 'Camera', 40000);
-- SUBQUERY RELATED QUESTIONS
-- FIND THE NAME OF CUSTOMERS WHO HAVE PLACED ATLEAST ONE ORDER USING SUBQUERY
-- for two tables we need to use the common attributes
SELECT customer_name FROM customers WHERE customer_id IN (SELECT customer_id FROM orders);
-- FIND THE NAME OF CUSTOMERS WHO HAVE  NOT PLACED ATLEAST ANY ORDER USING SUBQUERY 
SELECT customer_name FROM customers WHERE customer_id NOT IN(SELECT customer_id FROM orders);
-- find customer who have placed an order with amount grater than the average order amount
SELECT customer_name FROM customers WHERE customer_id IN(SELECT customer_id FROM orders WHERE amount>(SELECT AVG(amount) FROM  orders));

-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

-- TRANSACTION : transaction is a set of operations that are executed as ONE logical unit.

-- CREATE DATABASE bank;
USE bank; 
DROP TABLE IF EXISTS bank_accounts;
CREATE TABLE bank_accounts(
acc_id INT,
acc_name VARCHAR(50),
balance INT 
);
INSERT INTO bank_accounts VALUES
(1,"RAHUL",5000),
(2,"NEHA",3000);

-- i want to update balance in rahuls account
-- this is wrong query -> UPDATE bank_accounts SET balance=balance -1000 WHERE acc_id=1;
START TRANSACTION;
UPDATE bank_accounts SET balance=balance - 1000 WHERE acc_id=1;
COMMIT;
SELECT * FROM bank_accounts;

-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

-- INDEXING : index help sql find data faster , just like a book index or page index number
/*
-- without index:
 -- start from page 1
 -- read every page
 -- very slow
 
 with index:
 -> go to index
 */
 -- syntax :
 create index idx_name on table1(name);
 
 use db;
 
 -- create index on name and try to fetch name anita;
 create index idx_name on customers(customer_name);
 select * from customers where customer_name="Anita";
 
 
 -- create index on id and try to fetch id 7;
 create index id_name on customers(customer_id);
 select * from customers where customer_id=7;
 
 
 -- DRAWBACKS OF INDEXING : 
 
 
 
 
 -- fetch earphone normally then do indexing and then fetch earphone
 
 select * from orders where product="Earphones";
 
 create index ind_product on orders(product);
  select * from orders where product="Earphones";
  
  -- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --
  
  /*
  SQL Commands:
  
  DDL -- structure(design)
  DML -- data(rows)
  DQL -- fetch data
  DCL -- security
  TCL -- transactions
  
  */
  
  
  -- DDL :Data Definition Language
  /*
  CREATE
  ALTER
  DROP
  RENAME
  TRUNCATE
  */
  
  -- DML : Data Manipulation Language
  /*
  INSERT
  UPDATE
  DELETE
  */
  
  -- DQL : Data query languange
  /*
  SELECT
  */
  
  -- DCL : data control language
  /*
  GRANT = give access to user
  REVOKE = take access from user
  */
  
  -- TCL : transition control language
  /*
  SAVEPOINT
  ROLLBACK
  COMMITp
  */
  
  
  create table Students(
  id INT,
  name VARCHAR(50),
  marks INT);
  
  insert into Students values(1,"Hardik",80),(2,"Rohit",84);
  
GRANT SELECT ON Students TO  student_user;
REVOKE SELECT ON students FROM student_user;

-- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --

-- NORMALIZATION : converting bad table to good table.alter
/*
WHY NORMALIZATION ?
-> data duplication
-> insert anomaly
-> upate anomaly
-> delete anomaly
*/
  
  -- EMPLOYEE :
  CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50)
);

INSERT INTO employee VALUES
(1,'Rahul','IT'),
(2,'Neha','HR'),
(3,'Amit','IT'),
(4,'Priya','Finance'),
(5,'Karan','HR');


-- PROJECTS :
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    budget INT
);

INSERT INTO projects VALUES
(101,'Website Revamp',100000),
(102,'Mobile App',150000),
(103,'Payroll System',80000);


-- EMPLOYEE_PROJECTS :
CREATE TABLE employee_projects (
    emp_id INT,
    project_id INT,
    hours_worked INT,
    FOREIGN KEY (emp_id) REFERENCES employee(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

INSERT INTO employee_projects VALUES
(1,101,40),
(1,102,30),
(2,103,20),
(3,101,50),
(3,102,25),
(4,103,35),
(5,103,30);

select * from employee;
select * from projects;
select * from employee_projects;
  /*
  1>>find total hours worked by each employee
  find total hours spent on each project
  find department wise total working hour
  */
  -- 1>>
  select t1.emp_name,t2.hours_worked from employee t1 join employee_projects t2
  on t1.emp_id = t2.emp_id
  order by t1.emp_name;
  
  -- 2>>
  select t1.project_name,t2.hours_worked from projects t1 join employee_projects t2
  on t1.project_id = t2.project_id;
  
  -- 3>>
  select t1.department,sum(t2.hours_worked) from employee t1 join employee_projects t2
  on t1.emp_id = t2.emp_id
  order by t1.department;
  
  