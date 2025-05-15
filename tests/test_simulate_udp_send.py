import pytest
from unittest.mock import patch
from simulate_udp_send import simulate_udp_send  # Replace with your filename/module

def test_simulate_udp_send_all_success():
    payloads = [100, 200, 300]
    # Patch random.random() to always return 0.5 (so always successful)
    with patch("random.random", return_value=0.5):
        assert simulate_udp_send(payloads) == len(payloads)

def test_simulate_udp_send_all_fail():
    payloads = [100, 200, 300]
    # Patch random.random() to always return 0.05 (so always fail, since 0.05 <= 0.10)
    with patch("random.random", return_value=0.05):
        assert simulate_udp_send(payloads) == 0

def test_simulate_udp_send_partial_success():
    payloads = [100, 200, 300, 400]
    # Simulate sequence: success, fail, success, fail
    sequence = [0.5, 0.05, 0.7, 0.09]
    with patch("random.random", side_effect=sequence):
        assert simulate_udp_send(payloads) == 2

def test_simulate_udp_send_empty():
    assert simulate_udp_send([]) == 0

