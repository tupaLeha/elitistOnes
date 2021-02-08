class Employee(object):
    def __init__(self, name, email, salary):
        self.name = name
        self.mail = email
        self.salary = salary

    def work(self):
        return (self.name + ' has come to the office.')

    def chek_salary(self, days):
        return days * self.salary


class Recruiter(Employee):
    def work(self):
        return (self.name + ' has come to the office and start to hiring.')

    def __str__(self):
        return (self.__class__.__name__ + ':' + self.name)


class Programmer(Employee):
    def work(self):
        return (self.name + ' has come to the office and start to coding.')

    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__, self.name)


class Candidate(object):
    def __init__(self, full_name, email,
                 technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade


class Vacancy(object):
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
