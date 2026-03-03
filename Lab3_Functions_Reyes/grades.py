# grades.py

def compute_average(grades):
    avg = sum(grades) / len(grades)
    return avg

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
    
def generate_remark(grade):
    if grade == "F":
        return "Needs Improvement"
    else:
        return "Passing Performance"
