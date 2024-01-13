from collections.abc import Generator

import pytest
from dora import app
from fastapi import status
from fastapi.testclient import TestClient


@pytest.fixture()
def test_client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client


def test_submission_then_retrieval_of_dora_metrics(test_client: TestClient) -> None:
    res = test_client.post(
        "/metrics",
        json={
            "user_id": "b0098d7a-b10e-44af-b61d-3e87c69c197c",
            "metric_1": 1,
            "metric_2": 2,
            "metric_3": 3,
            "metric_4": 4,
            "metric_5": 5,
        },
    )

    res_get = test_client.get(
        "/metrics"
    )

    assert res.status_code == status.HTTP_201_CREATED
    assert res_get.status_code == status.HTTP_200_OK
    assert res_get.json() == {
            "data":[{
            "user_id": "b0098d7a-b10e-44af-b61d-3e87c69c197c",
            "metric_1": 1,
            "metric_2": 2,
            "metric_3": 3,
            "metric_4": 4,
            "metric_5": 5,
            }]
        }

def test_api_healthcheck(test_client: TestClient) -> None:
    res = test_client.get("/healthz")
    assert res.status_code == status.HTTP_200_OK
