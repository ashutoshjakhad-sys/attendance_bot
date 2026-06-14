import sqlite3
from sql import create_table, fetch_records, insert_record
create_table()  # Create the database table if it doesn't exist
class display:
    def display_info_student(self):
        print("Welcome to the Attendance Bot!")
        print("1. Report attendance")
        print("2. View attendance records")
        print("3. View absent records")
        print("4. Exit")
class Stat_Calculator:
    def calculate_statistics(self, attendance_records):
        total_classes = len(attendance_records)
        total_present = sum(1 for record in attendance_records if record['status'] == 'present')
        total_absent = sum(1 for record in attendance_records if record['status'] == 'absent')
        return total_classes, total_present, total_absent
        
class Attendance_Recorder:
    def __init__(self):
        records = fetch_records()
        self.attendance_records = [{'student_name': record[1], 'status': record[2]} for record in records]
    
    def refresh_records(self):
        records = fetch_records()
        self.attendance_records = [{'student_name': record[1], 'status': record[2]} for record in records]
    def report_attendance(self, student_name, status):
        insert_record(student_name, status)  # Insert the record into the database
        print(f"Attendance recorded for {student_name}: {status}")

    def view_attendance_records(self):
        self.refresh_records()  # Refresh the records from the database
        if not self.attendance_records:
            print("No attendance records found.")
            return
        print("Attendance Records:")
        for record in self.attendance_records:
            print(f"Student: {record['student_name']}, Status: {record['status']}")
    def view_absent_records(self):
        self.refresh_records()  # Refresh the records from the database
        absent_records = [record for record in self.attendance_records if record['status'] == 'absent']
        if not absent_records:
            print("No absent records found.")
            return
        print("Absent Records:")
        for record in absent_records:
            print(f"Student: {record['student_name']}, Status: {record['status']}")