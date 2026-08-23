from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
from datetime import date


# model for study data
class Study(BaseModel):
    # the date on which the data is getting registered
    day: date = Field(default_factory=lambda: date.today(), description="Date of the study entry", json_schema_extra={"example": "2026-08-23"})
    # the subject
    subject: str = Field(..., json_schema_extra={"example": "Mathematics"})
    # hours studied
    time: int = Field(..., description="Hours studied", json_schema_extra={"example": 3})

# this list consists all the study data
study_data : List[Study] = []

app = FastAPI()

# main page
@app.get("/")
def read_root():
    return {"Hello": "World"}

# shows the whole study data
@app.get("/study")
def read_study_data():
    return study_data

# shows the study data of the date user entered
@app.get("/study/{study_day}", status_code=status.HTTP_200_OK)
def read_study_day(study_day : date):
    # the study data of the day
    output_data: List[Study] = []

    for index, study in enumerate(study_data):
        if study.day == study_day:
            output_data.append(study_data[index])

    # no data found on that date
    if not output_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No study logs found for the date: {study_day}"
        )
    return output_data

# update the study data of the date user entered
@app.put("/study/{study_day}/{subject}", status_code=status.HTTP_200_OK)
def update_study_time(study_day : date, subject : str, updated_study: Study):
    for index, study in enumerate(study_data):
        if study.day == study_day and study.subject.lower() == subject.lower():
            study_data[index] = updated_study
            return updated_study
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No study logs found for the date: {study_day}",
    )


# entering study data
@app.post("/study", status_code=status.HTTP_201_CREATED)
def post_study_time(study: Study):
    study_data.append(study)
    return {"message": f"Logged {study.time} hours for {study.subject}"}



# Testing remaining