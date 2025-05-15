# For each IP, maintain a sliding window (dequeue) of timestamps within the last 60 seconds.
# If at any point the window exceeds 100 requests, flag the IP as a potential attacker.

from collections import defaultdict, deque
from typing import List, Tuple

def detect_ddos(logs: List[Tuple[int, str]]) -> List[str]:
    """
    logs: List of (timestamp: int, ip_address: str) sorted by timestamp.
    Returns list of IPs that sent more than 100 requests in any 60-second window.
    """
    # Map each IP to a deque of recent timestamps (within 60s)
    ip_windows = defaultdict(deque)
    ddos_ips = set()

    for timestamp, ip in logs:
        dq = ip_windows[ip]
        dq.append(timestamp)
        # Remove timestamps older than 60s from current
        while dq and dq[0] < timestamp - 59:
            dq.popleft()
        if len(dq) > 100:
            ddos_ips.add(ip)

    return list(ddos_ips)

# Example usage
if __name__ == "__main__":
    logs = [
        # Example: 101 requests from "1.2.3.4" between timestamps 0-59
        *[(i, "1.2.3.4") for i in range(101)],
        # Not enough for "5.6.7.8"
        *[(i, "5.6.7.8") for i in range(50)],
    ]
    print(detect_ddos(logs))  # Output: ['1.2.3.4']
