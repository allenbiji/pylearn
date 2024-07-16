from fastapi import FastAPI

app = FastAPI()

student={
    1:{"name":"john",
       "class":"3"}
}
@app.get("/")
def index():
    return {"name":"First Data"}

@app.get("/get-student")
def get_student(student_id: int):
    return student[student_id]

