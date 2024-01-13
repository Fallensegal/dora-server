from uuid import UUID

from pydantic import BaseModel


class DoraMetric(BaseModel):
    user_id: UUID
    metric_1: int
    metric_2: int
    metric_3: int
    metric_4: int
    metric_5: int


class DoraMetricList(BaseModel):
    data: list[DoraMetric]
