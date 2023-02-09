from src.services.PageviewService import get_analysis


def test_get_analysis():
    response = get_analysis(date_time='2022-01-01', show_succeeded_ad=True)
    assert type(response).__name__ == 'dict'(
    ) and "pageview_count" in response and "succeeded_ad_count" in response
