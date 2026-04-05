# Part 1: Python Basics & Control Flow
# Student Grade Tracker Assignment

# --- Task 1: Data Parsing & Profile Cleaning ---
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma", "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ", "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA", "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ", "roll": "105", "marks_str": "75, 80, 70, 68, 85"}
]

cleaned_students = []

print("--- Task 1: Profile Verification ---")
for student in raw_students:
    # 1. Clean data: Strip whitespace and Title Case name
    clean_name = student["name"].strip().title()
    # Convert roll to integer
    clean_roll = int(student["roll"])
    # Split marks_str and convert each element to integer
    clean_marks = [int(m.strip()) for m in student["marks_str"].split(",")]
    
    # Store in a new dictionary
    cleaned_profile = {"name": clean_name, "roll": clean_roll, "marks": clean_marks}
    cleaned_students.append(cleaned_profile)
    
    # 2. Verify name (alphabetical characters only, allowing for spaces)
    is_valid = all(part.isalpha() for part in clean_name.split())
    status = "✔ Valid name" if is_valid else "✘ Invalid name"
    print(f"{clean_name}: {status}")

    # 3. Print Profile Card
    print("=" * 30)
    print(f"Student  : {clean_name}")
    print(f"Roll No  : {clean_roll}")
    print(f"Marks    : {clean_marks}")
    print("=" * 30)

# 4. Special requirement for Roll 103
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"\nStudent 103 - CAPS: {s['name'].upper()}, Lower: {s['name'].lower()}\n")


# --- Task 2: Marks Analysis Using Loops & Conditionals ---
student_name = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88, 72, 95, 60, 78]

print("--- Task 2: Subject Analysis ---")
# 1. Grade Label Loop
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90: grade = "A+"
    elif m >= 80: grade = "A"
    elif m >= 70: grade = "B"
    elif m >= 60: grade = "C"
    else: grade = "F"
    print(f"{subjects[i]}: {m} ({grade})")

# 2. Calculations
total = sum(marks)
avg = total / len(marks)
# Zip subjects and marks to find highest/lowest
sub_marks = list(zip(subjects, marks))
highest = max(sub_marks, key=lambda x: x[1])
lowest = min(sub_marks, key=lambda x: x[1])

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {round(avg, 2)}")
print(f"Highest Scoring Subject: {highest[0]} ({highest[1]})")
print(f"Lowest Scoring Subject: {lowest[0]} ({lowest[1]})")

# 3. While Loop System
print("\n--- Marks Entry System ---")
new_count = 0
while True:
    sub_input = input("Enter subject name (or type 'done' to finish): ").strip()
    if sub_input.lower() == 'done':
        break
    
    mark_input = input(f"Enter marks for {sub_input}: ")
    if mark_input.isdigit():
        m_val = int(mark_input)
        if 0 <= m_val <= 100:
            marks.append(m_val)
            new_count += 1
        else:
            print("Warning: Marks must be between 0-100.")
    else:
        print("Warning: Please enter a numeric value.")

updated_avg = sum(marks) / len(marks)
print(f"New subjects added: {new_count}")
print(f"Updated Average: {round(updated_avg, 2)}\n")


# --- Task 3: Class Performance Summary ---
class_data = [
    ("Ayesha Sharma", [88, 72, 95, 60, 78]),
    ("Rohit Verma",   [55, 68, 49, 72, 61]),
    ("Priya Nair",   [91, 85, 88, 94, 79]),
    ("Karan Mehta",   [40, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 70, 68, 85])
]

processed_class = []
pass_count = 0
fail_count = 0

print(f"{'Name':<15} | {'Average':<7} | {'Status'}")
print("-" * 35)

for name, m_list in class_data:
    s_avg = round(sum(m_list) / len(m_list), 2)
    status = "Pass" if s_avg >= 60 else "Fail"
    
    if status == "Pass": pass_count += 1
    else: fail_count += 1
    
    processed_class.append((name, s_avg))
    print(f"{name:<15} | {s_avg:<7.2f} | {status}")

class_topper = max(processed_class, key=lambda x: x[1])
class_avg = sum(s[1] for s in processed_class) / len(processed_class)

print("-" * 35)
print(f"Passed: {pass_count}, Failed: {fail_count}")
print(f"Class Topper: {class_topper[0]} ({class_topper[1]})")
print(f"Overall Class Average: {round(class_avg, 2)}\n")


# --- Task 4: String Manipulation Utility ---
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is easy to learn.  "

# 1. Strip and store as clean_essay (using lowercase as per Hint in step 3)
clean_essay = essay.strip().lower()

# 2. Title Case
print("--- Task 4: String Ops ---")
print(f"Title Case: {clean_essay.title()}")

# 3. Count "python"
p_count = clean_essay.count("python")
print(f"Count of 'python': {p_count}")

# 4. Replace "python"
replaced = clean_essay.replace("python", "Python 🐍")
print(f"Replaced: {replaced}")

# 5 & 6. Split and Numbered Print
sentences = clean_essay.split(". ")
print("Individual Sentences:")
for idx, sentence in enumerate(sentences, 1):
    sentence = sentence.strip()
    if not sentence: continue # skip empty strings
    # Ensure ends with "."
    if not sentence.endswith("."):
        sentence += "."
    print(f"{idx}. {sentence.capitalize()}")