from fastapi import FastAPI
from app.api import user, courses, enrollment,module,progress,auth,instructor

app = FastAPI(
    title="Learning Management System API",
)

app.include_router(user.router, prefix="/api")
app.include_router(auth.router,prefix="/api")
app.include_router(courses.router, prefix="/api")
app.include_router(enrollment.router, prefix="/api")
app.include_router(module.router, prefix="/api")
app.include_router(progress.router, prefix="/api")

app.include_router(instructor.router,prefix="/api")

@app.get("/")
def health_check():
    return {"status": "LMS backend running"}