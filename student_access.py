#This code is the student class it allows students to access the attendance system and report their attendance.
from sql import insert_record, fetch_records
from function import display, Stat_Calculator, Attendance_Recorder
class Student_Access:
    def __init__(self):
        display_obj = display()
        stat_calculator = Stat_Calculator()
        attendance_recorder = Attendance_Recorder()
        user_input = int(input("Enter your choice: "))
        while user_input != 4:
            if user_input == 1:
                student_name = input("Enter student name: ")
                status = input("Enter attendance status (present/absent): ")
                attendance_recorder.report_attendance(student_name, status)
            elif user_input == 2:
                records = fetch_records()  # Fetch records from the database
                if not records:
                    print("No attendance records found.")
                else:
                    print("Attendance Records:")
                for record in records:
                    print(f"Student: {record[1]}, Status: {record[2]}")
                total_classes, total_present, total_absent = stat_calculator.calculate_statistics(
                    [{'student_name': record[1], 'status': record[2]} for record in records]
                )
                print(f"Total Classes: {total_classes}, Total Present: {total_present}, Total Absent: {total_absent}")
            elif user_input == 3:
                attendance_recorder.view_absent_records()
            else:
                print("Invalid choice. Please try again.")

            display_obj.display_info_student()
            user_input = int(input("Enter your choice: "))