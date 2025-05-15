# tests/test_ip_blacklist.py

import pytest
from ip_blacklist import is_blacklisted

@pytest.mark.parametrize(
    "ip,expected",
    [
        ("192.168.1.1", True),
        ("8.8.8.8", False),
        ("10.0.0.5", True),
    ]
)
def test_is_blacklisted(ip, expected):
    assert is_blacklisted(ip) == expected
