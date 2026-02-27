from fastapi import HTTPException
from app.schemas.instructor import CourseAnalyticsRead, StudentProgressRead, InstructorDashboardResponse

class InstructorService:
    def __init__(self, course_repo, enrollement_repo, module_repo, progress_repo, user_repo):
        self.course_repo = course_repo
        self.enrollement_repo = enrollement_repo
        self.module_repo = module_repo
        self.progress_repo = progress_repo
        self.user_repo = user_repo

    def get_dashboard_analytics(self, instructor_id: int) -> InstructorDashboardResponse:
        
        courses = self.course_repo.get_courses_by_instructor(instructor_id)
        
        course_analytics = []
        total_students_all_courses = 0

        for course in courses:
            enrollments = self.enrollement_repo.get_enrollments_by_course(course.id)
            modules = self.module_repo.get_modules_by_course(course.id)
            
            student_count = len(enrollments)
            total_students_all_courses += student_count
            
            course_analytics.append(CourseAnalyticsRead(
                course_id=course.id,
                title=course.title,
                total_students=student_count,
                total_modules=len(modules)
            ))

        return InstructorDashboardResponse(
            instructor_id=instructor_id,
            total_active_courses=len(courses),
            total_students_across_courses=total_students_all_courses,
            courses=course_analytics
        )

    def get_course_student_progress(self, instructor_id: int, course_id: int) -> list[StudentProgressRead]:
        
        course = self.course_repo.get_by_id(course_id)
        if not course or course.instructor_id != instructor_id:
            raise HTTPException(status_code=403, detail="You do not have access to this course's analytics.")

        enrollments = self.enrollement_repo.get_enrollments_by_course(course_id)
        total_modules = len(self.module_repo.get_modules_by_course(course_id))
        
        progress_list = []
        for enrollement in enrollments:
            student = self.user_repo.get_by_id(enrollement.student_id)
            
            if total_modules == 0:
                percentage = 0.0
            else:
                completed = self.progress_repo.count_completed_modules(student.id, course_id)
                percentage = (completed / total_modules) * 100

            progress_list.append(StudentProgressRead(
                student_id=student.id,
                student_email=student.email,
                completion_percentage=round(percentage, 2),
                is_finished=percentage == 100.0
            ))
            
        return progress_list