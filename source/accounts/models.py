from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User, Group
from phonenumber_field.modelfields import PhoneNumberField

limit = 61     # Separation of Students in A and B

Departments = [
        ("1", "Aerospace"),
        ("2", "Civil"),
        ("3", "Computer Science"),
        ("4", "Electronics & Communication"),
        ("5", "Electrical"),
        ("6", "Mechanical"),
        ("7", "Materials & Metallurgical"),
        ("8", "Production & Industrial"),
    ]

Designations = [
        ("1", "Professor"),
        ("2", "Associate Professor"),
        ("3", "Assistant Professor"),
        ("4", "PhD Scholar")
    ]

CourseList = [
        ('CSN101', 'INTRODUCTION TO COMPUTER SCIENCE AND ENGINEERING', '2'),
        ('CSN103', 'DIGITAL ELECTRONIC AND LOGIC DESIGN', '4'),
        ('CSN201', 'DISCRETE STRUCTURES FOR COMPUTER SCIENCE', '4'),
        ('CSN202', 'COMPUTER ARCHITECTURE AND ORGANIZATION', '4'),
        ('CSN203', 'OBJECT ORIENTED PROGRAMMING', '4 '),
        ('CSN204', 'ANALYSIS AND DESIGN OF ALGORITHMS', '4'),
        ('CSN206', 'ENGINEERING ANALYSIS ', '4'),
        ('CSN207', 'MICROPROCESSOR AND ITS APPLICATIONS', '4'),
        ('CSN208', 'DATA BASE MANAGEMENT SYSTEM', '4'),
        ('CSN210', 'COMPUTER ', '4'),
        ('CSN301', 'THEORY OF COMPUTATION', '4'),
        ('CSN302', 'SOFTWARE ENGINEERING', '4'),
        ('CSN303', 'WEB TECHNOLOGIES', '4  '),
        ('CSN304', 'COMPUTER GRAPHICS', '4'),
        ('CSN305', 'ARTIFICIAL INTELLIGENCE', '4'),
        ('CSN401', 'COMPILER DESIGN', '4'),
        ('CSN402', 'SOFTWARE TESTING ', '4'),
        ('CSN403', 'SOFT COMPUTING', '4'),
        ('CSN404', 'DIGITAL IMAGE PROCESSING', '4'),
        ('CSN405', 'CLOUD COMPUTING', '4'),
        ('CSN406', 'AGILE SOFTWARE DEVELOPMENT ', '4'),
        ('CSN407', 'Natural Language Processing', '4'),
        ('CSN408', 'SOFTWARE PROJECT MAN', '4'),
        ('CSN409', 'BIG DATA ANALYTICS', '4'),
        ('CSN410', 'BIOINFORMATICS', '4'),
        ('CSN411', 'NETWORK SECURITY', '4'),
        ('CSN412', 'APPLIED CRYPTOGRAPHY', '4'),
        ('CSN413', 'COMPUTER CRIME INVESTIGATION AND FORENSICS', '4'),
        ('CSN414', 'BIOMETRIC SECURITY', '4'),
        ('CSN415', 'Advanced', '4'),
        ('CSN416', 'ADVANCED WIRELESS AND MOBILE NETWORKS', '4'),
        ('CSN417', 'WIRELESS SENSOR NETWORKS', '4'),
        ('CSN 418', 'MOBILE COMPUTING', '4'),
        ('CSN461', 'OBJECT ORIENTED PROGRAMMING', '4'),
        ('CSN462', 'OPERATING SYSTEMS', '4'),
        ('CSN463', 'WEB ', '4  '),
        ('CSN421', 'MACHINE LEARNING', '4'),
        ('CSN422', 'ADVANCED DATABASE SYSTEMS', '4'),
        ('CSN423', 'ADVANCED SOFTWARE EN', '4'),
        ('CSN424', 'ADVANCED ALGORITHM DESIGN AND ANALYSIS', '4'),
        ('CSN425', 'ADVANCED COMPUTER ARCHITECTURE', '4'),
        ('CSN431', 'DATA STRUCTURES ', '4 '),
        ('CSN432', 'COMPUTER NETWORKS', '4'),
        ('CSN433', 'COMPUTER CRIME INVESTIGATION AND FORENSICS', '4 '),
        ('CSN434', 'DATA BASE SYSTEMS', '4'),
        ('CSN435', 'SOFTWARE ENGINEERING', '4'),
        ('GSC101', 'ENVIRONMENTAL SCIENCES', '3'),
        ('MAN 101', 'MATHEMATICS I', '4'),
        ('MAN 103', 'PROBABILITY AND STATISTICS', '4'),
        ('MAN105', 'VECTOR CALCULUS, FOURIER SERIES AND LAPLACE ', '4'),
        ('MAN 106', 'PARTIAL DIFFERENTIAL EQUATIONS AND SPECIAL ', '4'),
        ('PYN101', 'OSCILLATIONS AND OPTICS', '4'),
        ('PYN102', 'CONDENSED MATTER PHYSICS', '4'),
        ('PYN', 'MECHANICS', '4'),
        ('CHN101', 'APPLIED CHEMISTRY', '4'),
        ('CHN', 'PHYSICAL CHEMISTRY', '4'),
        ('CHN', 'INORGANIC ', '4'),
        ('CHN', 'PHYSICAL CHEMISTRY', '4'),
        ('HSS 101', 'ETHICS AND SELF AWARENESS     ', '2'),
        ('HSS 103', 'COMMUNICATION SKILLS (ADVANCED)', '2'),
        ('HSS 201', 'ECONOMICS', '3'),
        ('HSS 202', 'PSYCHOLOGY', '3'),
        ('HSS 203', 'SOCIOLOGY', '3'),
        ('HSS 204', 'FRENCH   ', '3'),
        ('HSM 401', 'PRINCIPLES OF MANAGEMENT', '3'),
        ('HSM 402', 'BUSINESS ENVIRONMENT AND BUSINESS LAWS     ', '3'),
        ('HSM 403', 'ENTREPRENEURSHIP AND PROJECT MANAGEMENT', '3'),
        ('HSM 405', 'MARKETING MANAGEMENT     ', '3'),
        ('HSM 406', 'HUMAN RESOURCE MANAGEMENT     ', '3'),
        ('CSN104', 'COMPUTER PROGRAMMING (BASIC)', '4'),
        ('CSN105', 'COMPUTER PROGRAMMING (ADVANCED)', '4'),
        ('ESC 101', 'ENGINEERING DRAWING ', '4'),
        ('ESC102', 'FLUID MECHANICS', '4'),
        ('ESC 103', 'INTRODUCTION TO MANUFACTURING', '4'),
        ('ESC 201', 'THERMODYNAMICS', '4'),
        ('ESC202', 'ESSENTIALS OF INFORMATION TECHNOLOGY', '4'),
        ('ESC 203', 'MATERIALS SCIENCE', '04'),
        ('ESC 204', 'SOLID MECHANICS', '4'),
        ('ESC 205', 'INTRODUCTION TO ELECTRONICS', '4'),
        ('ESC 206', 'BASIC ELECTRICAL SCIENCES', '04'),
        ('ESC 207', 'MECHATRONICS', '4'),
        ('ESC', 'MECHANICAL ENGINEERING DRAWING', '4'),
        ('CSN205', 'TECHNICAL COMMUNICATION', '2'),
        ('MAN 401', 'OPERATIONS  RESEARCH', '4'),
        ('PYN', 'ADVANCED PHYSICS ', '4'),
        ('PYN', 'CRYSTAL PHYSICS', '4'),
        ('CHN 401', 'MODERN INSTRUMENTAL METHODS OF CHEMICAL ANALYSIS', '4'),
        ('HSM 401', 'PRINCIPLES OF MANAGEMENT', '4'),
        ('HSM 402', 'BUSINESS ENVIRONMENT AND BUSINESS LAWS     ', '4'),
        ('HSM 404', 'FINANCIAL MANAGEMENT', '4'),
        ('HSM 405', 'MARKETING MANAGEMENT', '4'),
        ('HSM 406', 'HUMAN RESOURCE MANAGEMENT', '4'),
        ('HSM 431', 'MANAGING INNOVATION AND CHANGE', '4'),
        ('HSM 432', 'BUSINESS RESEARCH ', '4'),
        ('MAN 431', 'ALGEBRA ', '4'),
        ('MAN 432', 'NUMBER THEORY ', '4'),
        ('MAN 433', 'FOURIER SERIES AND INTEGRAL TRANSFORMS', '4'),
        ('MAN 434', 'CALCULUS OF VARIATIONS', '4'),
        ('PYN', 'QUANTUM MECHANICS', '4'),
        ('PYN', 'STATISTICAL PHYSICS', '4'),
        ('PYN', 'NUCLEAR PHYSICS', '4'),
        ('PYN', 'EXPERIMENTAL NUCLEAR PHYSICS', '4'),
        ('PYN', 'X', '4'),
        ('CHN', 'ANALYTICAL CHEMISTRY', '4'),
        ('CHN', 'ENVIRONMENTAL CHEMISTRY', '4'),
        ('CHN', 'RECENT ADVANCES IN CHEMICAL SCIENCES', '4'),

]


class Course(models.Model):

    CourseId = models.CharField(max_length=8, blank=False, unique=False)
    CourseName = models.CharField(max_length=250)
    Credit = models.IntegerField( validators=[
            MaxValueValidator(4),
            MinValueValidator(1)
        ])

    def __str__(self):
        return self.CourseId + " - " + self.CourseName


class Student(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    StudentID = models.CharField(max_length=8, blank=False, unique=True)
    Name = models.CharField(max_length=50)
    Branch = models.IntegerField()
    YearOfStudy = models.IntegerField()
    ContactNumber = PhoneNumberField(blank=False)
    Email = models.EmailField(blank=False)
    Courses = models.ManyToManyField(Course, through='StudentCourse')

    def add_into_group(self):

        if self.StudentID[:5] == "16103":

            maingroup = Group.objects.get(name="CSE")
            self.User.groups.add(maingroup)

            if int(self.StudentID[5:]) < limit:
                self.User.groups.add(Group.objects.get(name="CSEA"))
            else:
                self.User.groups.add(Group.objects.get(name="CSEB"))

    def __str__(self):
        return self.StudentID

    def get_branch_display(self):

        return Departments[int(self.Branch)][1]


class Faculty(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    FacultyID = models.CharField(max_length=8, blank=False, unique=True)
    Name = models.CharField(max_length=50)
    Department = models.IntegerField()
    Designation = models.IntegerField()
    ContactNumber = PhoneNumberField(blank=False)
    Email = models.EmailField(blank=False)
    Courses = models.ManyToManyField(Course, through='FacultyCourse')

    def add_into_group(self):

        maingroup = Group.objects.get(name="FAC")
        self.User.groups.add(maingroup)

    def get_department_display(self):

        return Departments[int(self.Department)][1]

    def get_designation_display(self):

        return Designations[int(self.Designation)][1]

    def __str__(self):
        return self.FacultyID


class StudentCourse(models.Model):

    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    User = models.ForeignKey(Student, on_delete=models.CASCADE)
    Semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])


class FacultyCourse(models.Model):

    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    User = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])

