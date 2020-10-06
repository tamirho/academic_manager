from academic_manager.models import Student, Teacher, Enrollment, Course
from academic_manager.extensions import db
from academic_manager.models import Student, Course, Teacher, Enrollment, Task


def validate_course_name(course_name):
    course = Course.query.filter_by(course_name=course_name).first()
    if course:
        return False
    else:
        return True


def make_new_course_by_names(course_name, teacher_name):
    current_teacher = Teacher.query.filter_by(user_name=teacher_name).first()
    new_course = Course(course_name, current_teacher.id)
    db.session.add(new_course)
    db.session.commit()


def make_new_task(title, content, course_id):
    task = Task(title, content, course_id)
    db.session.add(task)
    db.session.commit()



