class School(object):
    def __init__(self, name, email, username, password, district, degrees, majors, address):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.district = district
        self.degrees = degrees
        self.majors = majors
        self.address = address

    def __str__(self):
        return self.name+" ("+self.majors+") ,"+self.address

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_district(self):
        return self.district

    def get_degrees(self):
        return self.degrees

    def get_majors(self):
        return self.majors

    def get_address(self):
        return self.address


class Student(object):
    def __init__(self, name, email, username, password, degree):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.degree = degree

    def __str__(self):
        return self.name+" "+self.surname+" ("+self.username+")"

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_degree(self):
        return self.degree