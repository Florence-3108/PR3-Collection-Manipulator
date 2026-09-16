print("Welcome to Student Data Organizer!\n")

students = []

while True:
    print("\nSelect and option:")
    print("1. Add Student")
    print("2. Display All students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects offered")
    print("6. Exit\n")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\nEnter student details:")
            studentid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = (input("Date of Birth (YYYY-MM-DD): "))
            subjects = input("Subjects (comma-seperated): ")

            subject = set(subjects.split(","))
            identity = (studentid, dob)
            data = {"identity": identity,
                    "name": name,
                    "age": age,
                    "grade": grade,
                    "subjects": subjects}

            students.append(data)
            print("Student added Successfully!\n")

        case 2:
            print("---Display All Students---")
            if len(students) == 0:
                print("No Data found.")
            else:
                for data in students:
                    print(f"Student ID: {data['identity'][0]}")
                    print("Name: {}".format(data["name"]))
                    print("Age: %d" % data["age"])
                    print(f"Grade: {data['grade']}")
                    print("Subjects: ", data["subjects"])

        case 3: 
            studentid = int(input("Enter Student ID to update their information: "))

            for data in students:
                if data["identity"][0] == studentid:
                    data["name"] = input("Enter new name: ")
                    data["age"] = int(input("Enter new age: "))
                    data ["grade"] = input("Enter new grade: ")
                    new_subjects = input("Enter new subjects: ")
                    data["subjects"] = set(new_subjects.split(","))
                    print("Student information updated successfully!")
                    break
                else:
                    print("Student not found.")

        case 4:
            studentid = int(input("Student ID: "))

            for data in students:
                 if data["identity"][0] == studentid:
                     del students[students.index(data)]
                     print("Student deleted successfully!")
                     break
                 else:
                     print("Student not found.")

        case 5:
            print("Subjects offered: ")
            for data in students:
                print(data["subjects"])

        case 6:
            print("Thank you for using Student Data Organizer!")
            break

        case _:
            print("Invalid choice!")