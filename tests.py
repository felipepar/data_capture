import pytest

from data_capture import DataCapture


@pytest.fixture
def data_capture():
    return DataCapture()
    
def _add_and_build_stats(data_capture, elements):
    for element in elements:
        data_capture.add(element)
    return data_capture.build_stats()


@pytest.fixture
def stats(data_capture):
    return _add_and_build_stats(data_capture, [1,2,3,4,5,6,7])


def test_data_capture(data_capture):
    data_capture.add(2)
    data_capture.add(3)
    data_capture.add(10)
    data_capture.add(10)

    assert data_capture.storage == {2: 1, 3: 1, 10: 2}

def test_build_stats_with_empty_storage(data_capture):
    with pytest.raises(ValueError, match='Data capture is empty!'):
        data_capture.build_stats()

def test_invalid_key(stats):
    with pytest.raises(ValueError, match='Invalid key: 76'):
        assert stats.less(76)

def test_invalid_input(stats):
    with pytest.raises(ValueError, match='Invalid input'):
        stats.less(-2)
    with pytest.raises(ValueError, match='Invalid input'):
        stats.less(1001)

def test_less(stats):
    expected_result = 2
    assert stats.less(3) == expected_result

def test_greater(stats):
    expected_result = 2
    assert stats.greater(5) == expected_result

def test_between(stats):
    expected_result = 5
    assert stats.between(3, 7) == expected_result

def test_between_same_value(stats):
    with pytest.raises(ValueError, match='Start must be different from end'):
        stats.between(3,3)
