from tasks.dict_tasks.planet import get_planet_name


def test_get_planet_name():
    assert get_planet_name(3).lower() == "земля"
    assert get_planet_name(7).lower() == "уран"
    assert get_planet_name(20) is None
