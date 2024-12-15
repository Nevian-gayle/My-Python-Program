# Class to represent a Course with an ID, name, and fee
class Course:
    def __init__(self, course_id, name, fee):
        self.course_id = course_id # Store the unique course ID
        self.name = name # Store the course name
        self.fee = float(fee) # Ensure the fee is stored as a float

# Class to represent a Student with their details, enrolled courses, and balance
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id # Store the student ID
        self.name = name # Store the student's name
        self.email = email # Store the student's email address
        self.courses = [] # Initialize an empty list to hold enrolled courses
        self.balance = 0.0 # Set the student's balance to zero

    def enroll(self, course):
        if course not in self.courses:  # Ensure the student isn't already enrolled in the course
            self.courses.append(course)  # Add the course to the student's list of courses
            self.balance += course.fee # Add the course fee to the student's balance

    # Calculate the total fee of all enrolled courses.
    def get_total_fee(self):
        return sum(course.fee for course in self.courses) # Sum up the fees for all enrolled courses


# Class to represent the registration system to manage courses and students
class RegistrationSystem:
    def __init__(self):
        self.courses = [] # Set an empty list to hold all available courses
        self.students = {} # Use a dictionary to store students by their IDs

    #Add a new course to the system.
    def add_course(self, course_id, name, fee):

        for course in self.courses: # Check if a course with the same ID already exists
            if course.course_id == course_id:
                print("Course ID already exists.") # Display an error message
                return

        new_course = Course(course_id, name, fee) # Create a new Course object
        self.courses.append(new_course) # Add the new course to the list of courses
        print("Course added successfully.") # Confirm the course has been added

# Register a new student in the system
    def register_student(self, student_id, name, email):
        if not str(student_id).isdigit(): # Ensure the student ID is numeric
            print("Error: Student ID should be a number.") # Display an error message
            return
        elif student_id in self.students: # Check if the student ID already exists
            print("Student ID already exists.") # Display an error message
            return
        else:
            new_student = Student(student_id, name, email) # Create a new Student object
            self.students[student_id] = new_student # Add the student to the dictionary
            print("Student registered successfully.") # Confirm the student has been registered



    def enroll_in_course(self, student_id, course_id):
# Check if the student exists in the students dictionary

        if student_id not in self.students: # Check if the student exists
            print("The student with the given ID does not exist.")  # Display an error message
            return
        elif student_id in self.students: # Retrieve the student object
            print("Student found.")

            student = self.students[student_id]
            # Flag to check if the course is found
            course_found = False

            # Iterate through the list of courses
            for course in self.courses:
                # Check if the current course has the same ID as the course_id
                if course.course_id == course_id:
                    # Enroll the student in the found course
                    student.enroll(course)
                    course_found = True
                    print(f"Student {student_id} has been enrolled in course {course_id}.")
                    break

            # If no course was found with the given course_id, inform the user
            if not course_found:
                print("The course with the given ID does not exist.")

    def calculate_payment(self, student_id, amount):
        student = self.students[student_id]
        # Check if the student exists
        if student_id not in self.students:
            print("Student not found.")
            return
        elif student_id in self.students:

            while True:

                if amount >= 0.4 * student.balance: # Ensure the payment meets the 40% minimum requirement
                    student.balance -= amount  # Deduct the payment from the student's balance
                    print(f"Payment of ${amount:.2f} processed successfully.") # Confirm payment
                    print(f"New balance: ${student.balance:.2f}") # Display the updated balance

                    break

                elif amount < 0.4 * student.balance:
                    print("Payment must be 40% or more") # Display an error message
                    break

    def check_student_balance(self, student_id):
        # Check if the student exists
        if student_id in self.students:
            student = self.students[student_id]
            # Return the student's balance
            return student.balance
        # If the student does not exist, return None
        return None

    def show_courses(self,):
        return self.courses

    def show_registered_students(self):
        return self.students.values()

    def show_students_in_course(self, course_id):
        students_in_course = []
        # Loop through all students
        for student in self.students.values():
            # Loop through each student's courses
            for course in student.courses:
                # Check if the student is in the course
                if course.course_id == course_id:
                    students_in_course.append(student)  # Add student to the list
                    break  # Stop checking more courses for this student

        return students_in_course

# Main function to provide a menu-driven interface for the registration system
def main():

    system = RegistrationSystem() # Create a new RegistrationSystem object
    while True:
        # Display the menu options
        print("\nCourse Registration System")
        print("1. Add Course")
        print("2. Register Student")
        print("3. Enroll in Course")
        print("4. Calculate Payment")
        print("5. Check Student Balance")
        print("6. Show Courses")
        print("7. Show Registered Students")
        print("8. Show Students in Course")
        print("9. Exit")

        # Prompt the user to select an option
        option = input("Enter option: ")

        if option == '1':
            # Add a new course
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")

            while True:
                fee = (input("Enter course fee: "))
                try:
                    system.add_course(course_id, name, fee)
                    break  # Exit the loop if the course is added successfully
                except ValueError as e:
                    print(e)


        elif option == '2':
            # Register a new student
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            system.register_student(student_id, name, email)


        elif option == '3':
            # Enroll a student in a course
            student_id = input("Enter student ID: ")
            course_id = input("Enter course ID: ")
            system.enroll_in_course(student_id, course_id)
           

        elif option == '4':
            # Process a payment
            student_id = input("Enter student ID: ")
            amount = float(input("Enter payment amount: "))
            system.calculate_payment(student_id, amount)


        elif option == '5':
            student_id = input("Enter student ID: ")
            balance = system.check_student_balance(student_id)
            print(f"Balance: {balance}")

        elif option == "6":
            # Display all available courses
            courses = system.show_courses() # Retrieve the list of courses
            if not courses:  # Check if the courses list is empty
                print("No courses have been added yet.") # Inform the user if no courses exist
            else:
                # Loop through the courses and display their details
                for course in courses:
                    print(f"ID: {course.course_id}, Name: {course.name}, Fee: ${course.fee:.2f}")

        elif option == '7':
            # Display all registered students
            students = system.show_registered_students() # Retrieve the list of registered students
            # Loop through the students and display their details
            for student in students:
                print(f"ID:{student.student_id}: Name: {student.name} - Email: {student.email}")


        elif option == '8':
            # Show students enrolled in a specific course

            course_id = input("Enter course ID: ") # Prompt user for the course ID
            try:
                students = system.show_students_in_course(course_id) # Retrieve the students in the course
                if students: # Check if there are any students enrolled in the course
                    # Loop through the students and display their details
                    for student in students:
                        print(f"ID: {student.student_id}, Name: {student.name} - Email: {student.email}")
                else:
                    print("No students are enrolled in this course.") # Inform if the course has no students
            except Exception as e:
                # Catch and display any unexpected errors
                print(f"An error occurred: {e}")

        elif option == "9":
            # Exit the program
            print("Exiting system. Goodbye!") # Display a goodbye message
            break # Break out of the loop to exit the program

        # Handle invalid menu options
        else:
            print ("Invalid option. Please try again.")  # Inform the user of an invalid option


if __name__ == "__main__":
    main()