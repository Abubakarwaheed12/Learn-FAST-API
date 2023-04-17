from fastapi import FastAPI  , Path


app=FastAPI()

@app.get("/")
def index():
    return {'name': 'Abu Bakar Waheed'}


# Path Parameters

student={
    1:{
        'name':'abu bakar waheed',
        'program':'Bs Computer Science',
        'smester':'5',
        'age':'21',
    },
    2:{
        'name':'Amir',
        'program':'Bs Computer Science',
        'smester':'1',
        'age':'21',
    },
    3:{
        'name':'Ali Hamza',
        'program':'Bs Computer Science',
        'smester':'1',
        'age':'24',
    },
            
    4:{
        'name':'Abdul rehman',
        'program':'Bs Computer Science',
        'smester':'1',
        'age':'27',
    },
}

@app.get("/get_student/{st_id}")
def student_data(
    st_id: int = Path( description="The id of the student you want to view" , gt=0)
    ):
    return student[st_id]


# Query Parameter
@app.get("/get_student_by_name")
def get_student_by_name(name : str ):
    
    for id in student:
        if student[id]['name']==name:
            return student[id]
        
    return {'data': student}
        
