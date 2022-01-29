from prproj.lib import try_me


def test_try_me():
    assert 'weather' in try_me()
