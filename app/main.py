from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

courses_db = {
    "CS-E4190": {
        "id": "CS-E4190",
        "name": "Cloud software and systems",
        "instructor": "Mario Di francesco",
        "keyword": ["cloud", "container"],
    },
    "CS-0374": {
        "id": "CS-0374",
        "name": "Algorithms",
        "instructor": "Jeff Erickson",
        "keyword": ["complexity", "sorting"],
    },
}

app = FastAPI()


class Course(BaseModel):
    id: str
    name: str
    instructor: str
    keyword: Optional[List] = None


@app.get("/")
async def read_all_course():
    return courses_db


@app.get("/courses/{course_id}", response_model=Course)
async def get_course(course_id: str):
    print(course_id)
    if course_id not in courses_db:
        raise HTTPException(status_code=404, detail="Course does not exist")
    return courses_db[course_id]


@app.post("/courses/", response_model=Course)
async def create_course(course: Course):
    if course.id in courses_db:
        raise HTTPException(status_code=400, detail="Course already exists")
    courses_db[course.id] = course
    return course
