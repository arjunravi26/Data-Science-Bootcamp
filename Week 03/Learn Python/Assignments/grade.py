if __name__ == "__main__":
    percentage = int(input("Enter your percentage: "))
    if percentage >= 90 and percentage <= 100:
        grade = "A"
    elif percentage >= 80 and percentage < 90:
        grade = "B"
    elif percentage >= 70 and percentage < 80:
        grade = "C"
    elif percentage >= 60 and percentage < 70:
        grade = "D"
    elif percentage >= 50 and percentage < 60:
        grade = "E"
    elif percentage < 50 and percentage >= 0:
        grade = "You failed"
    else:
        grade = "Enter a valid percentage"
    print(f"your grade is {grade}")
