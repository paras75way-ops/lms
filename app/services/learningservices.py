from app.models.module import Module

class LearningService:
    def __init__(self, module_repo, progress_repo):
        self.module_repo = module_repo
        self.progress_repo = progress_repo

    def create_module(self, course_id: int, title: str, content_type: str, content_url: str):
        new_module = Module(course_id=course_id, title=title, content_type=content_type, content_url=content_url)
        return self.module_repo.create(new_module)

    def mark_module_complete(self, student_id: int, module_id: int):
        return self.progress_repo.mark_completed(student_id, module_id)

    def get_course_progress(self, student_id: int, course_id: int):
        total_modules = len(self.module_repo.get_modules_by_course(course_id))
        if total_modules == 0:
            return {
                "total_modules": 0,
                "completed_modules": 0,
                "completion_percentage": 0.0,
                "is_course_finished": False
            }
            
        completed = self.progress_repo.count_completed_modules(student_id, course_id)
        percentage = (completed / total_modules) * 100
        
        return {
            "total_modules": total_modules,
            "completed_modules": completed,
            "completion_percentage": round(percentage, 2),
            "is_course_finished": percentage == 100.0
        }
    
    def check_module_status(self, student_id: int, module_id: int):
        is_completed = self.progress_repo.check_status(student_id, module_id)
        return {
            "student_id": student_id,
            "module_id": module_id,
            "is_completed": is_completed
        }