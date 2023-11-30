from collections.abc import Generator

import pytest
from dora import app
from fastapi import status
from fastapi.testclient import TestClient


@pytest.fixture()
def test_client() -> Generator[TestClient, None, None]:
    with TestClient(app) as client:
        yield client


def test_api_healthcheck(test_client: TestClient) -> None:
    res = test_client.get("/healthz")
    assert res.status_code == status.HTTP_200_OK
