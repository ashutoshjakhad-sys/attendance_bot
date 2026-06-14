# This code is to allow admins to access the attendance system and view the attendance records of students.
from sql import fetch_records, delete_all_records
from function import display, Stat_Calculator, Attendance_Recorder
import sqlite3

class Admin_Access:
    def __init__(self):
        pass

    def search_attendance_records(self):
        cal_ = Stat_Calculator()
        atd_recorder = Attendance_Recorder()
        while True:
            try:
                user_input = int(input("\nAdmin Menu:\n1. View all records\n2. Search by student name\n3. View absent records\n4. Delete all records\n5. Exit\nChoose an option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if user_input == 1:
                records = fetch_records()
                if not records:
                    print("No attendance records found.")
                else:
                    print("Attendance Records:")
                    for record in records:
                        print(f"Student: {record[1]}, Status: {record[2]}")
                    total_classes, total_present, total_absent = cal_.calculate_statistics(
                        [{'student_name': record[1], 'status': record[2]} for record in records]
                    )
                    print(f"Total Classes: {total_classes}, Total Present: {total_present}, Total Absent: {total_absent}")

            elif user_input == 2:
                name = input("Enter student name: ").strip()
                records = fetch_records()
                matched = [r for r in records if r[1].lower() == name.lower()]
                if not matched:
                    print("No records found for that student.")
                else:
                    for record in matched:
                        print(f"Student: {record[1]}, Status: {record[2]}")

            elif user_input == 3:
                atd_recorder.view_absent_records()

            elif user_input == 4:
                print ("Are you sure you want to delete all records? This action cannot be undone. (yes/no)")
                confirm = input().strip().lower()
                if confirm == "yes":
                    delete_all_records()
                    print("Attendance records deleted successfully.")
                else:
                    print("Deletion cancelled.")
            elif user_input == 5:
                break

            else:
                print("Invalid choice. Please try again.")