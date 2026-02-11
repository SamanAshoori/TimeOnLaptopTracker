from fastapi import FastAPI
from typing import List
from uuid import uuid4
from schemas import ActivitySchema

app = FastAPI(title="TimeOnLaptop Tracker")

#mock_data
fake_activites = [
    {
        "id":uuid4(),
        "name": "Studying",
        "color":"#00ff41"
    },
    {
        "id":uuid4(),
        "name": "Gaming",
        "color":"#ff00ff"
    }

]

#Get Endpoint
@app.get("/activities", response_model=List[ActivitySchema])
def get_activities():
    return fake_activites