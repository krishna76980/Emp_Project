#Dictionary to store employee:
employees = {}

#Function to add employee:
def add_employee(emp_id,name,age,salary,department):
    
    employees[emp_id] ={
         "Name":name,
         "Age" :age,
         "Salary":salary,
         "Department":department
     }
     
    print(f"Employee {name} added Successfully")

#Function to view all employee:
def view_employee():
    
    if employees:
        for emp_id, emp_details in employees.items():
            print(f"ID :{emp_id}, Details:{emp_details}")
    else:
        print("No employees added yet!")    

#Function to update employee details

def update_employee(emp_id,name=None,age=None,salary=None,department=None):
    try:
        if emp_id in employees:
            
            if name:
                employees[emp_id]["Name"]=name
                
            if age:
                employees[emp_id]["Age"]=age
            
            if salary:
                employees[emp_id]["salary"]=salary
            
            if department:
                employees[emp_id]["Department"]=department
                        
            print(f"Employee ID {emp_id} updated successfully....!")
            
        else:
            print(f"Employee ID {emp_id} not found")    
     
    except KeyError as e:
        print(f"Error updating Employee details:{e}")        
#Function to remove employee:

def remove_employee(emp_id):
    try:
        emp =employees.pop(emp_id)
        
        print(f"Emoployee {emp['Name']} removed successfully....!")
    
    except KeyError:
        print(f"Employee ID {emp_id} not found")

#Function to save employee data in file without JSON:

def save_to_file(filename):
    
    try:
        
        with open(filename,"w") as file:
            
            for emp_id,details in employees.items():
                
                line =f"{emp_id},{details['Name']},{details['Age']},{details['Salary']},{details['Department']}\n"            
                file.write(line)
                
        print("Employee Data saved successfully.....!")
        
    except Exception as e:
        print(f"Error :{e}")
        
#Funtion to load File:

def load_from_file(filename):
    
    try:
        
        with open(filename,'r') as file:
            
            global employees
            
            employees = {} #clear the existing dictionary befor load
            
            for line in file:
                emp_data = line.strip().split(',')
                
                emp_id,name,age,salary,department = emp_data
                
                employees[emp_id] = {
                    "Name":name,
                    "Age" :age,
                    "Salary":salary,
                    "Department":department
                }
        
                
        print("Employee data successfully....!")
    
    except FileNotFoundError:
        print(f"File {filename} not found")
        
    except Exception as e:
        print(f"Error {e}")                        
                
# main menu functions:

def menu():
    
    while True:
        
        print("Welcome to Employee management system!\n")
        
        print("1.Add Employee:")
        print("2.View Employee:")
        print("3.Update Employee:")
        print("4.Delete Employee:")
        print("5.Save to file:")
        print("6.Load from file:")
        print("7.Exit:")
        
        choice =input("Enter the Choice:")
        
        if choice == "1":
            emp_id =input("Enter employee ID:")
            name =input("Enter Name:")
            age =input("Enter age:")
            salary =input("Enter salary:")
            department =input("Enter department:")
            
            add_employee(emp_id,name,age,salary,department)
        
        elif choice == "2":
            view_employee()
        
        elif choice == "3":
            
            emp_id =input("Enter employee ID to update:")
            name =input("Enter new name (leave blank or skip):")or None
            age =input("Enter age(leave blank or skip):")or None
            salary =input("Enter salary (leave blank or skip):")or None
            department =input("Enter department (leave blank or skip):")or None
            
            update_employee(emp_id,name,age,salary,department)
        
        elif choice == "4":
            emp_id=input("Enter employee ID to remove:")
            
            remove_employee(emp_id)
        
        elif choice == "5":
            
            filename = input("Enter filename to save to:")
            save_to_file(filename)
        
        elif choice == "6":
            
            filename =input("Enter filename to load from: ")
            
            load_from_file(filename)
        
        elif choice == "7":
            break
        

menu()        