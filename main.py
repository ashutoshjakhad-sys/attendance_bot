# This is the main class that runs the attendance system. It imports the necessary classes and functions from other files and provides a menu for the user to interact with the system.
import function
import sql
import student_access as student_access_
import admin

_id = input("Are you a student or an admin? (Enter 'student' or 'admin'): ")
if _id == "student":
    stat_calculator = function.Stat_Calculator()
    attendance_recorder = function.Attendance_Recorder()
    sql.create_table()  # Create the database table if it doesn't exist
    display_obj = function.display()
    display_obj.display_info_student()
    student_access = student_access_.Student_Access()
elif _id == "admin":
    display_obj = function.display()
    stat_calculator = function.Stat_Calculator()
    attendance_recorder = function.Attendance_Recorder()
    sql.create_table()  # Create the database table if it doesn't exist
    admin_access = admin.Admin_Access()
    admin_access.search_attendance_records()
else:
    print("Invalid input. Please enter 'student' or 'admin'.")