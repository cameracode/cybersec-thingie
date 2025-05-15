import pytest
from detect_ddos import detect_ddos  # Replace with your actual module name

def test_detect_ddos_single_attacker():
    # 101 requests from same IP, all within 60 seconds
    logs = [(i % 60, "1.2.3.4") for i in range(101)]
    assert detect_ddos(logs) == ["1.2.3.4"]

def test_detect_ddos_no_attacker():
    # 100 requests in 60s is not enough
    logs = [(i, "5.6.7.8") for i in range(100)]
    assert detect_ddos(logs) == []

def test_detect_ddos_multiple_ips():
    logs = (
        [(i, "1.1.1.1") for i in range(50)] +             # Not enough
        [(i % 60, "2.2.2.2") for i in range(200)] +        # 200 requests in 60s
        [(100 + (i % 60), "3.3.3.3") for i in range(101)]  # 101 requests, all in the window 100-159
    )
    result = set(detect_ddos(logs))
    assert result == {"2.2.2.2", "3.3.3.3"}

def test_detect_ddos_out_of_window():
    # 101 requests, but spread over 2+ minutes (not within any 60s window)
    logs = [(i*2, "4.4.4.4") for i in range(101)]
    assert detect_ddos(logs) == []

def test_detect_ddos_unsorted_logs():
    # Function assumes sorted logs; test that (if you want to support unsorted)
    logs = [
        (10, "6.6.6.6"), (2, "6.6.6.6"), (15, "6.6.6.6"),
        # Next line: 101 requests, timestamps 101 % 60 = 41, 102 % 60 = 42, ..., wrapping around, so all in 0-59
        *[(101 + (i % 60), "6.6.6.6") for i in range(101)]
    ]
    # Now, after sorting, more than 100 requests are within the same 60-second window
    assert detect_ddos(sorted(logs)) == ["6.6.6.6"]

@pytest.mark.parametrize("ip, count, expected", [
    ("7.7.7.7", 101, True),
    ("8.8.8.8", 100, False),
])
def test_detect_ddos_param(ip, count, expected):
    logs = [(i % 60, ip) for i in range(count)]
    result = detect_ddos(logs)
    if expected:
        assert ip in result
    else:
        assert ip not in result
