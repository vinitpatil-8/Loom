from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
from datetime import date

router = APIRouter()


# model for study data
class Study(BaseModel):
    # the date on which the data is getting registered
    day: date = Field(default_factory=lambda: date.today(), description="Date of the study entry")
    # the subject
    subject: str = Field(..., json_schema_extra={"example": "Mathematics"})
    # hours studied
    time: int = Field(..., description="Hours studied", json_schema_extra={"example": 3})

# this list consists all the study data
study_data : List[Study] = []



# shows the whole study data
@router.get("/study")
def read_study_data():
    return study_data

# shows the study data of the date user entered
@router.get("/study/{study_day}", status_code=status.HTTP_200_OK)
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
@router.put("/study/{study_day}/{subject}", status_code=status.HTTP_200_OK)
def update_study_time(study_day : date, subject : str, updated_study: Study):
    for index, study in enumerate(study_data):
        if study.day == study_day and study.subject.lower() == subject.lower() and updated_study.time > 0 and updated_study.time <= 24 and any(char.isalpha() for char in updated_study.subject):
            study_data[index] = updated_study
            return updated_study
    if updated_study.time <= 0 or updated_study.time > 24:
        error_text = 'Enter valid hours'
    elif any(char.isalpha() for char in updated_study.subject) == False:
        error_text = 'Enter a valid subject'
    else:
        error_text = f"No study logs found for the date: {study_day}"    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=error_text,
    )


# entering study data
@router.post("/study", status_code=status.HTTP_201_CREATED)
def post_study_time(study: Study):
    if study.time > 0 and study.time <= 24 and any(char.isalpha() for char in study.subject):
        study_data.append(study)
        return {"message": f"Logged {study.time} hours for {study.subject}"}
    else:
        if study.time <= 0 and study.time > 24:
            return {"Enter valid hours"}
        else:
            return {"Enter a valid subject"}

# deleting study data
@router.delete("/study/{study_date}/{del_subject}", status_code=status.HTTP_204_NO_CONTENT)
def delete_study(study_date: date, del_subject: str):
    for index, study in enumerate(study_data):
        if study.day == study_date and study.subject.lower() == del_subject.lower():
            study_data.pop(index)
            return {"Successfully deleted"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"No study logs found for {del_subject} on date: {study_date}"
    )