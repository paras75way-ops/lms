from fastapi import HTTPException
from app.models.user import UserRole
from app.models.enrollment import Enrollment

class EnrollementService:
    def __init__(self, user_repo, course_repo, enrollment_repo):
        self.user_repo = user_repo
        self.course_repo = course_repo
        self.enrollment_repo = enrollment_repo

    
    def enroll_student(self, student_id: int, course_id: int):
        
        student = self.user_repo.get_by_id(student_id)
        if not student or student.role != UserRole.STUDENT:
            raise HTTPException(status_code=400, detail="Only students can enroll")

         
        course = self.course_repo.get_by_id(course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")

     
        existing = self.enrollment_repo.get_enrollment(student_id, course_id)
        if existing:
            raise HTTPException(status_code=400, detail="Already enrolled in this course")

      
        new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
        return self.enrollment_repo.create(new_enrollment)