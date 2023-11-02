from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


"""
1. Dora Survey
- Questions
    - Special Language Clarifications
    - leadtime=3&deployfreq=5&chgfail=5&ttr=2&industry=government
- Answers
    - Same Format

- suveryIdentifiers - Logins

2. Surveyor/Roles:
Assumptions:
    - Free-flowing, submit whenever they want
3. Teams
- Collection
    - Survey
    -

################################
3. Visualization
- Collection
    - Teams

- Graphs/Charts - (interactive?)


######### NAPKIN ARCHITECURE ##########

"""


# Classes
@dataclass
class DoraSurveyResult:
    date_time_survey_submitted: datetime = field(default_factory=datetime.utcnow)
    lead_time: int = 0
    deploy_freq: int = 0
    chg_fail: int = 0
    time_to_recovery: int = 0


@dataclass
class Team:
    survey_list: list[DoraSurveyResult] = field(default_factory=list)

    def add_survey_to_list(
        self: Self, dora_survey: DoraSurveyResult, survey_list: list[DoraSurveyResult]
    ) -> None:
        survey_list.append(dora_survey)
