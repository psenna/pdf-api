from fastapi.testclient import TestClient


def test_get_root(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200

def test_get_join_pdf(client: TestClient) -> None:
    response = client.get("/join_pdf")
    assert response.status_code == 200