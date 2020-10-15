import sqlite3
print()

connection = sqlite3.connect('employees.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
check = cursor.fetchall()
if not check:
    cursor.execute("CREATE TABLE employees (name text, wage float, hours float)")
    connection.commit()

choice = None

while choice != "7":
    print("1) ADD EMPLOYEE")
    print("2) CLOCK HOURS")
    print("3) PAY EMPLOYEES")
    print("4) UPDATE WAGE")
    print("5) DISPLAY EMPLOYEES")
    print("6) DELETE EMPLOYEES")
    print("7) EXIT")
    choice = input(">>")

    if choice == "1": # ADD EMPLOYEE
        name = input("Name: ")
        wage = float(input("Wage: "))
        hours = 0.00
        values = (name, wage, hours)
        cursor.execute('INSERT INTO employees VALUES (?,?,?)', values)
        connection.commit()

    elif choice =="2": # CLOCK HOURS
        name = input("Name: ")
        hours = float(input("Hours: "))
        values = (hours, name)
        cursor.execute('UPDATE employees SET hours = hours + ? WHERE name = ?', values)
        connection.commit()

    elif choice =="3": # PAY EMPLOYEES
        name = input("Name: ")
        values = (name, )
        cursor.execute('SELECT * FROM employees WHERE name = ?', values)
        for record in cursor.fetchall():
            wage = record[1]
            hours = record[2]
        cursor.execute('UPDATE employees SET hours = 0 WHERE name = ?', values)
        connection.commit()
        print("Pay owed to {} is ${}".format(name, (wage * hours)))

    elif choice =="4": # UPDATE WAGE
        name = input("Name: ")
        wage = float(input("Wage: "))
        values = (wage, name)
        cursor.execute('UPDATE employees SET wage = ? WHERE name = ?', values)
        connection.commit()


    elif choice =="5": # DISPLAY EMPLOYEES
        show = input('Show Wage? (y/n) ')
        if show == 'n':
            cursor.execute("SELECT * FROM employees")
            print("{:>10}".format("Name"))
            print()
            for record in cursor.fetchall():
                print('{:>10}'.format(record[0]))
        else:
            cursor.execute("SELECT * FROM employees")
            print('{:>10}  {:>10}  {:>10}'.format("Name", "Wage", "Hours"))
            print()
            for record in cursor.fetchall():
                print('{:>10}  {:>10}  {:>10}'.format(record[0], record[1], record[2]))

    elif choice =="6": # DELETE EMPLOYEES
        name = input("Name: ")
        values = (name, )
        cursor.execute("DELETE FROM employees WHERE name = ?", values)
        connection.commit()

    print()


connection.close()