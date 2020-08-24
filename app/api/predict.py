import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Campaign(BaseModel):
    """Use this data model to parse the request body JSON."""
    title: str
    blurb: str
    goal: int
    launch_date: str
    deadline: str
    category: str

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(campaign: Campaign):
    """Predicting the success rate of a Kickstarter campaign."""
    X_new = campaign.to_df()
    y_pred = '55%'
    return {'predicted_success': y_pred}
