from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.executestatus import ExecuteStatus
import unittest, pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = ExecuteStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "1220", "444"),
          ("Learn Python 3 from scratch", "1234 5678 9012 3456", "1220", "444"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCCV):
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCCV, zip="12345")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.courses.goBack()
        self.courses.clickOnAllCourses()