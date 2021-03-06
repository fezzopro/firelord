import logging
from typing import List

import pandas as pd
from fastapi import FastAPI

from .profiles import LandProfile
from .scoring import get_model

app = FastAPI()
model = get_model()


@app.get("/")
def root():
    """Root endpoint for detection by load balancers.
    """
    return {"message": "API running."}


@app.post("/score")
def score(profile: LandProfile):
    # return profile.dict()
    features = pd.DataFrame(profile.dict(), index=[0])
    payload = model.predict(features)
    # payload = features
    print(payload)
    status = True 
    response = {"success": status, "payload": payload}
