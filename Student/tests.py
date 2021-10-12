from django.http import request
from django.test import TestCase
from django.urls.base import reverse
from.models import Student
import datetime
class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student=Student(first_name="Daisi",
        last_name="Caroline",
        age=20,
        nationality="Kenyan",
        email_adress="daissiodawa@gmail.com",
        id_number=37063098,)

    def test_fullname_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name ())  

    def test_fullname_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name ())

    def test_sudent_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth),

    def test_register_student_view(self):
        url=reverse("register_student")
        data={"first_name":self.student.first_name,
               "last_name":self.student.last_name,
               "age":self.student.last_name,
               "nationality":self.student.last_name,
               "email_adress":self.student.last_name,
               "id_number":self.student.last_name,
        }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)    
