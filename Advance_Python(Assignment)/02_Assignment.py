# Decorator to display report format
def report_header(func):
    def wrapper(*args, **kwargs):
        print("-" * 45)
        print("        EMPLOYEE PERFORMANCE REPORT")
        print("-" * 45)

        func(*args, **kwargs)

        print("-" * 45)
        print("           Report Completed")
        print("-" * 45)

    return wrapper


class Employee:

    # Class Variable
    company = "TechNova Solutions"

    # Constructor
    def __init__(self, emp_id, emp_name, performance_score):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.performance_score = performance_score

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Magic Method
    def __str__(self):
        return (
            f"Employee ID   : {self.emp_id}\n"
            f"Employee Name : {self.emp_name}\n"
            f"Score         : {self.performance_score}"
        )

    # Performance Evaluation
    def performance_level(self):
        if self.performance_score >= 90:
            return "Excellent"
        elif self.performance_score >= 75:
            return "Very Good"
        elif self.performance_score >= 60:
            return "Good"
        elif self.performance_score >= 45:
            return "Average"
        else:
            return "Needs Improvement"

    # Decorated Method
    @report_header
    def show_report(self):
        print("Company :", Employee.company)
        print(self)

        level = self.performance_level()

        if self.performance_score >= 45:
            status = "Eligible for Bonus"
        else:
            status = "Training Required"

        print("Performance :", level)
        print("Status      :", status)


# Main Program

emp1 = Employee(501, "Rahul Sharma", 91)
emp1.show_report()

print()

# Updating company name using class method
Employee.change_company("NextGen Technologies")

emp2 = Employee(502, "Sneha Joshi", 40)
emp2.show_report()


# Output:

# --------------------------------------------
#         EMPLOYEE PERFORMANCE REPORT
# ---------------------------------------------
# Company : TechNova Solutions
# Employee ID   : 501
# Employee Name : Rahul Sharma
# Score         : 91
# Performance : Excellent
# Status      : Eligible for Bonus
# ---------------------------------------------
#            Report Completed
# ---------------------------------------------

# ---------------------------------------------
#         EMPLOYEE PERFORMANCE REPORT
# ---------------------------------------------
# Company : NextGen Technologies
# Employee ID   : 502
# Employee Name : Sneha Joshi
# Score         : 40
# Performance : Needs Improvement
# Status      : Training Required
# ---------------------------------------------
#            Report Completed
# ---------------------------------------------