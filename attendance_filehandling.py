import json
from datetime import date, datetime, timedelta

USER_DATA_FILE = "user_data.json"
STUDENT_DATA_FILE = "student_data.json"

def load_user_data():
    try:
        with open(USER_DATA_FILE, 'r') as user_file:
            return json.load(user_file)
    except FileNotFoundError:
        return []
            

def save_user_data(data):
        with open(USER_DATA_FILE, 'w') as user_file:
            return json.dump(data, user_file)


def load_student_data():
    try:
        with open(STUDENT_DATA_FILE, 'r') as student_data:
            return json.load(student_data)
    except FileNotFoundError:
        return {}

    

def save_student_data(data):
    with open(STUDENT_DATA_FILE, 'w') as student_data:
        return json.dump(data, student_data)


    
def user_register(username, password):
    user_data = load_user_data()

    if not any(user['username'] == username for user in user_data):
        user_data.append({'username': username, 'password': password})
        save_user_data(user_data)
        print("Registration successful. You can now log in.")
    else:
        print("Username already exists. Please choose a different username.")

def login_user(username, password):
    user_data = load_user_data()

    if any(user['username'] == username and user['password'] == password for user in user_data):
        print(f"WELCOME {username}! ")
        return True
    else:
        print("Invalid username or password. Please try again.")
        return False

def add_student_info(roll_number, name, email, address):
    student_data = load_student_data()

    if roll_number not in student_data:
        student_data[roll_number] = {
            'name': name,
            'email': email,
            'address': address
            }
        save_student_data(student_data)        
        print(f"Student '{name}' information added successfully.")
    else:
        print(f"Student with Roll Number '{roll_number}'")

def view_student_info(roll_number):
    student_database = load_student_data()
    if roll_number in student_database:
        student_info = student_database[roll_number]
        print(f"Student Information for Roll Number '{roll_number}':")
        for key, value in student_info.items():
            print(f"{key}: {value}")
    else:
        print(f"Student with Roll Number '{roll_number}' not found in the database. Cannot view information.")




def update_student_info(roll_number, key, value):
    student_database =  load_student_data()
    if roll_number in student_database:
        student_info = student_database[roll_number]
        if key in student_info:
            student_info[key] = value
            save_student_data(student_database)
            print(f"Student with Roll Number '{roll_number}' information updated successfully.")
        else:
            print(f"Invalid key '{key}'. Cannot update.")
    else:
        print(f"Student with Roll Number '{roll_number}' not found in the database.")

def delete_student_info(roll_number):
    student_database =  load_student_data()
    if roll_number in student_database:
        del student_database[roll_number]
        print(f"Student with Roll Number '{roll_number}' information deleted successfully.")
    else:
        print(f"Student with Roll Number '{roll_number}' not found in the database. Cannot delete information.")


def validate_roll_number(roll_number):
    if not roll_number.isdigit():
        print("Invalid roll number. Roll number should contain digits only.")
        return False
    return True


def validate_email(email):
    # Simple email validation using a regular expression
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        print("Invalid email address.")
        return False
    return True

def mark_attendance(roll_number, date_str=None):
    student_database =  load_student_data()
    today = date.today().strftime("%Y-%m-%d") if date_str is None else date_str
    if roll_number in student_database:
        if 'Attendance' not in student_database[roll_number]:
            student_database[roll_number]['Attendance'] = {}
        attendance_data = student_database[roll_number]['Attendance']

        if today in attendance_data:
            print(f"Attendance for Roll Number '{roll_number}' on {today} has already been marked as '{attendance_data[today]}'.")
            save_student_data(student_database)
        else:
            while True:
                attendance = input(f"Mark attendance for Roll Number '{roll_number}' on {today} (P for Present, A for Absent): ").upper()
                if attendance in ['P', 'A']:
                    attendance_data[today] = attendance
                    print(f"Attendance marked for Roll Number '{roll_number}' on {today} as '{attendance}'.")
                    save_student_data(student_database)
                    break
                else:
                    print("Invalid input. Please enter 'P' for Present or 'A' for Absent.")
    else:
        print(f"Student with Roll Number '{roll_number}' not found in the database. Cannot mark attendance.")

def mark_attendance_forall(date_str=None):
    student_database =  load_student_data()
    today = date.today().strftime("%Y-%m-%d") if date_str is None else date_str
    for roll_number in student_database:
        if 'Attendance' not in student_database[roll_number]:
            student_database[roll_number]['Attendance'] = {}
        attendance_data = student_database[roll_number]['Attendance']

        if today in attendance_data:
            print(f"Attendance for Roll Number '{roll_number}' on {today} has already been marked as '{attendance_data[today]}'.")
            save_student_data(student_database)
        else:
            while True:
                attendance = input(f"Mark attendance for Roll Number '{roll_number}' on {today} (P for Present, A for Absent): ").upper()
                if attendance in ['P', 'A']:
                    attendance_data[today] = attendance
                    print(f"Attendance marked for Roll Number '{roll_number}' on {today} as '{attendance}'.")
                    save_student_data(student_database)
                    break
                else:
                    print("Invalid input. Please enter 'P' for Present or 'A' for Absent.")
    
    
                
def view_attendance_records(rollno):
    student_database =  load_student_data()
    if rollno in student_database:
        student_data = student_database[rollno]
        if 'Attendance' in student_data:
            attendance_dates = student_data['Attendance']
            print(f"Attendance records for '{rollno}':")
            for date_str, attendance_status in attendance_dates.items():
                print(f"{date_str}: {attendance_status}")
        else:
            print(f"No attendance records found for '{rollno}'.")
    else:
        print(f"Student '{rollno}' not found in the database. Cannot view attendance records.")

def view_attendance_records_forall():
    student_database =  load_student_data()
    for rollno in student_database:
        student_data = student_database[rollno]
        if 'Attendance' in student_data:
            attendance_dates = student_data['Attendance']
            print(f"Attendance records for '{rollno}':")
            for date_str, attendance_status in attendance_dates.items():
                print(f"{date_str}: {attendance_status}")
        else:
            print(f"No attendance records found for '{rollno}'.")
    

def view_attendance_by_date(date_str):
    student_database =  load_student_data()
    try:
        specific_date = datetime.strptime(date_str, "%Y-%m-%d")
        present_students = []

        for roll_number, student_data in student_database.items():
            if 'Attendance' in student_data:
                attendance_dates = student_data['Attendance']
                if date_str in attendance_dates and attendance_dates[date_str] == 'P':
                    present_students.append(roll_number)

        if present_students:
            print(f"Students present on {date_str}:")
            for value in present_students:
                print(f"Roll Number: {value}")
        else:
            print(f"No students were present on {date_str}.")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD' format.")



def main():

    logged_in = False
    should_continue = True

    while should_continue:
        print("\nAttendance Management System")
        if not logged_in:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
        else:
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Mark Attendance")
            print("4. View Attendance")
            print("5. Manage Student Information")
            print("6. View Attendance Records Filter by Date")
            print("7. Generate Attendance Report")
            print("8. Logout")
            print("9. Exit")


        choice = int(input("Enter your choice: "))

        if not logged_in:
            if choice == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                user_register(username, password)

            elif choice == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                logged_in = login_user(username, password)

            elif choice == 3:
                print("\nYOU EXIT FROM THE SYSTEM")
                should_continue = False

            else:
                print("Invalid choice. Please try again.")

        else:
            if choice == 1:
                 name = input("Enter student name: ")
                 while True:
                     roll_number = input("Enter student roll number: ")
                     if validate_roll_number(roll_number):
                         break;

                 while True:
                     email = input("Enter student email: ")
                     if validate_email(email):
                         break;
                 
                 
                 address = input("Enter address: ")
                 add_student_info(roll_number, name, email, address)
                    

            elif choice == 2:
                roll_number = input("Enter student roll number: ")
                delete_student_info(roll_number)

            elif choice == 3:
                print("1. mark attendance for all student")
                print("2. mark attendance of one student")
                att_choice = int(input("Enter your choice"))

                if att_choice == 1:
                    date_str = input("Enter date (YYYY-MM-DD) to mark attendance (press Enter for today's date): ")
                    if not date_str:
                        mark_attendance_forall()
                        
                    else:
                        mark_attendance_forall(date_str)
                        
                elif att_choice == 2:                   
                    roll_number = input("Enter student roll number: ")
                    date_str = input("Enter date (YYYY-MM-DD) to mark attendance (press Enter for today's date): ")
                    if not date_str:
                        mark_attendance(roll_number)
                    else:
                        mark_attendance(roll_number, date_str)

                else:
                    print("Invalid choice. Please try again.")
       
            
            elif choice == 4:
                print("1. View attendance for all student")
                print("2. View attendance of one student")
                att_choice = int(input("Enter your choice"))

                if att_choice == 1:
                    view_attendance_records_forall()
                elif att_choice == 2:
                    roll_number = input("Enter student roll number: ")
                    view_attendance_records(roll_number)
                else:
                    print("Invalid choice. Please try again.")
                
                              

            elif choice == 5:
                print("\nManage student Information")
                roll_number = input("Enter student roll number: ")
                       
                print("1. View Student Information")
                print("2. Update Student Information")
                print("3. Delete Student Information")

                info_choice = int(input("Enter your choice: "))

                if info_choice == 1:
                    view_student_info(roll_number)

                elif info_choice == 2:
                    key = input("Enter key (e.g., 'Address', 'Email'): ")
                    value = input("Enter new value: ")
                    #if key == 'Address' and not validate_roll_number(value):
                        #continue
                    if key == 'Email' and not validate_email(value):
                        continue
                    update_student_info(roll_number, key, value)
                    
                elif info_choice == 3:
                    delete_student_info(roll_number)

                else:
                    print("Invalid choice. Please try again.")

            elif choice == 6:               
                date_str = input("Enter date (YYYY-MM-DD) to filter records: ")
                view_attendance_by_date(date_str)

            #elif choice == 7:
             #   roll_number = input("Enter student roll number: ")
              #  time_period = input("Enter time period ('monthly', 'weekly', or 'daily'): ")
               # generate_attendance_report(roll_number, time_period)
                 
        
            elif choice == 8:
                logged_in = False
                print("\nLOGGED OUT")
                
            elif choice == 9:
                print("\nYOU EXIT FROM THE SYSTEM")
                should_continue = False

            else:
                print("Invalid choice. Please try again.")
                                
                   
                
if __name__ == "__main__":
    main()           
                
                

    
        



        

        
    
