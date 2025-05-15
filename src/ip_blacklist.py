# src/ip_blacklist.py

# Given:
# - A function under test: is_blacklisted(ip: str) -> bool
# - A blacklist: ["192.168.1.1", "10.0.0.5", "172.16.0.100"]

# Implement parameterized pytest tests for the following IPs:
# - "192.168.1.1" (should be blacklisted)
# - "8.8.8.8" (should not be blacklisted)
# - "10.0.0.5" (should be blacklisted)

# The function under test
def is_blacklisted(ip: str) -> bool:
    blacklist = ["192.168.1.1", "10.0.0.5", "172.16.0.100"]
    return ip in blacklist
