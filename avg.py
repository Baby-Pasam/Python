def calculate_average(grades):
  """
  Calculates the average grade from a dictionary of grades.

  Args:
      grades: A dictionary containing subject names as keys and grades as values.

  Returns:
      The average grade as a float.
  """
  total_grade = sum(grades.values())
  number_of_subjects = len(grades)
  average_grade = total_grade / number_of_subjects if number_of_subjects > 0 else 0.0
  return average_grade

def letter_grade(grade):
  """
  Converts a numerical grade to a letter grade based on a basic scale.

  Args:
      grade: The numerical grade.

  Returns:
      The corresponding letter grade (A, B, C, D, or F).
  """
  if grade >= 90:
    return "A"
  elif grade >= 80:
    return "B"
  elif grade >= 70:
    return "C"
  elif grade >= 60:
    return "D"
  else:
    return "F"

def gpa_conversion(grade):
  """
  Converts a numerical grade to a GPA value based on a 4.0 scale.

  Args:
      grade: The numerical grade.

  Returns:
      The corresponding GPA value (as a float).
  """
  grade_point = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0,
  }
  return grade_point.get(letter_grade(grade), 0.0)

def main():
  student_grades = {}
  while True:
    subject = input("Enter subject name (or 'done' to finish): ")
    if subject.lower() == "done":
      break

    try:
      grade = float(input("Enter grade for {}: ".format(subject)))
      if 0 <= grade <= 100:
        student_grades[subject] = grade
      else:
        print("Invalid grade. Please enter a value between 0 and 100.")
    except ValueError:
      print("Invalid input. Please enter a numerical grade.")

  # Calculate and display results
  if student_grades:
    average_grade = calculate_average(student_grades)
    letter_grade_value = letter_grade(average_grade)
    gpa = gpa_conversion(average_grade)
    print("\nStudent Grades:")
    for subject, grade in student_grades.items():
      print(f"  - {subject}: {grade}")
    print(f"\nAverage Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade_value}")
    print(f"GPA: {gpa:.2f}")
  else:
    print("\nNo grades entered.")

if _name_ == "_main_":
  main()