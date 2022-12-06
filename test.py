import requests, json


def test_get_solutions():
    response = requests.post(
        "http://localhost:8000/solutions/", json={"size":4}
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
