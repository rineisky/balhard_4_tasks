from tasks.dict_tasks.month_to_seazon import month_to_season


def test_month_to_season():
    assert month_to_season(4).lower() == "весна"
    assert month_to_season(20) is None
