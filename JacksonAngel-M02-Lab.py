# Angel Jackson
# JacksonAngel-M02-Lab.py
# This app will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.

# Create a function named main to check student qualifications
def main():
  # Get the student's last name.
  last_name = input("Enter the student's last name: ")
  # If the last name is 'ZZZ', quit the program.
  if last_name == "ZZZ":
    return
  # Get the student's first name.
  first_name = input("Enter the student's first name: ")
  # Get the student's GPA.
  gpa = float(input("Enter the student's GPA: "))
  # Test if the student's GPA is 3.5 or greater.
  if gpa >= 3.5:
    print("The student has made the Dean's List.")
  # Test if the student's GPA is 3.25 or greater.
  elif gpa >= 3.25 and gpa < 3.5:
    print("The student has made the Honor Roll.")
# Call the main function. 
main()
