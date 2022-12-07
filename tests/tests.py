import requests, json, pytest
from conftest import http_service


def test_get_solutions(http_service):
    response = requests.post(
        "http://localhost:8000/solutions/", json={"size": 4}
    )

    first_solution = [
        {"x": 1, "y": 0},
        {"x": 3, "y": 1},
        {"x": 0, "y": 2},
        {"x": 2, "y": 3},
    ]

    content = json.loads(response.content.decode("utf-8"))
    solutions = content["solutions"]

    for solution in solutions:
        if first_solution == solution["queens"]:
            assert True
            return

    assert False


@pytest.mark.parametrize(
    "http_service, input_a, expected_value",
    [(http_service, 4, 2), (http_service, 5, 10), (http_service, 6, 4)]
)
def test_number_of_solutions(http_service, input_a, expected_value):
    response = requests.post(
        "http://localhost:8000/solutions/", json={"size": input_a}
    )

    content = json.loads(response.content.decode("utf-8"))
    solutions = content["solutions"]

    assert len(solutions) == expected_value

