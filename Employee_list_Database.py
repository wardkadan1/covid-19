import sqlite3

conn = sqlite3.connect('Employee_list.db')  # run line 4 and 6
# link to a temporary database

c = conn.cursor()

#USER STORY 2
#ABED ALHAFEED
#318849866

def __init__(self, first, last, id, job, sick):
    self.first = first
    self.last = last
    self.id = id
    self.job = job
    self.sick = sick


# c.execute("""CREATE TABLE Employees (   #MUST RUN ONCE BEFORE RUNNING THE OTHER PARTS TO CREATE TABLE
#    first text,                         #THIS WAS A TEMPORARY TABLE FOR TESTING ON A TEMPORARY
#    last text,                          #DATABASE
#    id integer,
#    job text,
#    sick text
#    )""")

#def add_employee(employee):  # works - wasnt linked yet
#    with conn:
#        c.execute("INSERT INTO Employees VALUES (:first, :last, :id, :job, :sick)",
#                  {'first': employee.first, 'last': employee.last, 'id': employee.id, 'job': employee.job,
#                   'sick': employee.sick})


def view_all():
    c.execute("SELECT * FROM Employees")
    # var1 = c.fetchall()
    # print(var1)


def find_employee_first(first):
    return c.execute("SELECT * FROM Employees WHERE first=:first", {'first': first})
    # var2= c.fetchall()
    # print(var2)


def find_employee_last(last):
    return c.execute("SELECT * FROM Employees WHERE last=:last", {'last': last})
    # var3= c.fetchall()
    # print(var3)


def find_employee_id(id):
    return c.execute("SELECT * FROM Employees WHERE id=:id", {'id': id})
    # var4= c.fetchall()
    # print(var4)


def find_employee_job(job):
    return c.execute("SELECT * FROM Employees WHERE job=:job", {'job': job})
    # var5= c.fetchall()
    # print(var5)


def find_employee_sick(sick):
    return c.execute("SELECT * FROM Employees WHERE sick=:sick", {'sick': sick})


#def remove_emp(emp):  #works - wasnt linked yet
#    with conn:
#        c.execute("DELETE from Employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})

# emp1=Employee('Abed', 'Haj', 318849866, 'Doctor', 'No')
# emp2=Employee('Ward', 'Kaedan', 123456789, 'Surgeon', 'No')
# emp3=Employee('Mohammed', 'Gab', 6969696969, 'Janitor', 'No')
# emp4=Employee('Ali', 'Yes', 5454545454,'Test', 'No')
# add_employee(emp1)
# add_employee(emp2)
# add_employee(emp3)
# add_employee(emp4)
# remove_emp(emp2)
