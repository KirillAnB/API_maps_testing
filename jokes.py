import requests
import pytest
import pytest_ordering


base_url = "https://api.chucknorris.io/jokes/random"
chuck_answer = requests.get(base_url)
chuck_json = chuck_answer.json()


@pytest.mark.parametrize("code", [chuck_answer])
def test_status_code(code):
    assert code.status_code == 200

# @pytest.mark.skip(reason = "No idea if there is a category in answer")
@pytest.mark.parametrize("result, cat", [(chuck_answer, "sport"), (chuck_answer, "planet")])
def test_category(result, cat):
    jokes_data = result.json()
    assert jokes_data["categories"] != [cat]


@pytest.mark.parametrize("answer_data", [chuck_json])
def test_if_joke(answer_data):
    print(answer_data['value'])
    assert answer_data['value'] != None
