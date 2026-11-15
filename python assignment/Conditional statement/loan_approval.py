
salary = int(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
age = int(input("Enter your age: "))

if salary >= 30000:
    salary_ok = True
else:
    salary_ok = False

if credit_score >= 700:
    credit_ok = True
else:
    credit_ok = False

if age >= 21 and age <= 60:
    age_ok = True
else:
    age_ok = False

count = salary_ok + credit_ok + age_ok

if count == 3:
    print("Loan Approved")

elif count == 2:
    print("Conditionally Approved")

else:
    print("Loan Rejected")
