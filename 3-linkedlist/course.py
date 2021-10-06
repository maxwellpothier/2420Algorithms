class Course:

    def __init__(self, number=0, name="", credit_hr=0.0, grade=0.0):
        if type(number) != int:
            raise ValueError("Error: Number must be an integer.")
        if number < 0:
            raise ValueError("Error: Number must be positive.")
        if type(name) != str:
            raise ValueError("Error: Name must be a string.")
        if type(credit_hr) != float:
            raise ValueError("Error: Credit Hours must be a float.")
        if credit_hr < 0:
            raise ValueError("Error: Credit Hours must be positive.")
        if type(grade) != float:
            raise ValueError("Error: Grade must be a float.")
        if grade < 0:
            raise ValueError("Error: Grade must be positive.")
        self.course_number = number
        self.course_name = name
        self.course_credit_hr = credit_hr
        self.course_grade = grade
        self.next = None

    def number(self):
        return self.course_number

    def name(self):
        return self.course_name

    def credit_hr(self):
        return self.course_credit_hr

    def grade(self):
        return self.course_grade

    def set_next(self, node):
        self.next = node

    def __str__(self):
        return "foo"
