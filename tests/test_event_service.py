from src.services.EventService import get_user_count


def test_get_user_count():
    response = get_user_count(date_time='2022-01-01')
    assert type(
        response).__name__ == 'dict' and 'number_of_unique_user' in response
