import os


print("STUDENT INFORMATION SYSTEM")
print("==========================")

student_record = {}

while True:
  print("A - ADD STUDENT RECORD")
  print("B - PRINT ALL STUDENTS RECORD")
  print("C - SEARCH STUDENT RECORD")
  print("D - DELETE STUDENT RECORD")
  print("E - EDIT/MODIFY STUDENT RECORD")
  print("F - EXPORT STUDENT DATA")
  print("G - EXIT SYSTEM")

  choice = input("SELECT FROM THE OPTIONS ABOVE ---> ").lower()

  if choice == 'a':
    print("\nADDING STUDENT RECORD ")

    id_no = input("Please input student ID number---> ")

    first_name = input("Please input Student First Name---> ").upper()
    second_name = input("Please input Student Second Name---> ").upper()
    age = eval(input("Input Student Age---> "))
    course = input("Input Student Course---> ").upper()
    section = input("Input Student Section---> ").upper()
    student_record[id_no] = [first_name, second_name, age, course, section]
    print("DATA SAVE SUCCESSFULLY")
    continue

  elif choice == 'b':
    os.system('cls')
    
    print("PRINTING STUDENT RECORD ")

    for i, j in student_record.items():
      print(f"Student ID - {i}, Information {j}")
    continue
  elif choice == 'c':
    os.system('cls')

    print("SEARCH STUDENT RECORD")

    search_id = input("Input Student ID for search").lower()

    for each_id in student_record.keys():
      if search_id in student_record.keys():
        print("============================== ")
        print("\n\nRECORD FOUND for ID {search_id}")
        for i in student_record[search_id]:
          print(f" --- {i}")
        print("============================== ")
      else:
        print("NO RECORD FOUND")
      break
    continue
  elif choice == 'd':
    os.system('cls')

    print("DELETE STUDENT RECORD")

    search_id = input("Input Student ID for search").lower()

    for each_id in student_record.keys():
      if search_id in student_record.keys():
        print("============================== ")
        print("\n\nRECORD FOUND for ID {search_id}")
        for i in student_record[search_id]:
          print(f" --- {i}")
        print("============================== ")

        student_record.pop(search_id)
        print("\nRECORD DELETED")
      else:
        print("NO RECORD FOUND")
      break
    continue
  elif choice == 'e':
    os.system('cls')

    print("EDIT/MODIFY STUDENT RECORD")

    search_id = input("Input Student ID for search").lower()

    for each_id in student_record.keys():
      if search_id in student_record.keys():
        print("============================== ")
        print("\n\nRECORD FOUND for ID {search_id}")
        for i in student_record[search_id]:
          print(f" --- {i}")
        print("============================== ")
        first_name = input("Please input Student First Name---> ").upper()
        second_name = input("Please input Student Second Name---> ").upper()
        age = eval(input("Input Student Age---> "))
        course = input("Input Student Course---> ").upper()
        section = input("Input Student Section---> ").upper()

        student_record[search_id][0] = first_name
        student_record[search_id][1] = second_name
        student_record[search_id][2] = age
        student_record[search_id][3] = course
        student_record[search_id][4] = section
       
      else:
        print("NO RECORD FOUND")

    pass
    continue
  elif choice == 'f':
    print("EXPPORT STUDENT DATA")

    with open('student_records.afuang', 'w') as new_file:
      afuang.dump(student_record,new_file, indent=4)

    print("\n\nDATA EXPORTED TO AFUANG")

    continue
  elif choice == 'g':
    break
  else:
    print("INVALID CHOICE, REENTER YOUR CHOICE")
    continue