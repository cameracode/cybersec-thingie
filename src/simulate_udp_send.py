
# Explanation
#   - For each payload, a random number between 0 and 1 is generated.
#   - If the number is greater than 0.10 (i.e., not in the bottom 10%), the packet is counted as successfully sent.
#   - On average, about 10% of packets will be dropped.


# This code simulates sending UDP packets and counts how many were sent successfully.
# It uses a 10% packet loss rate to determine if a packet was successfully sent.
# The function `simulate_udp_send` takes a list of payload sizes and returns the number of packets that were sent successfully.
# The example usage at the end demonstrates how to call the function with a list of payload sizes.
# The function simulates sending UDP packets and counts how many were sent successfully.
import random
from typing import List

def simulate_udp_send(payloads: List[int]) -> int:
    successful = 0
    for _ in payloads:
        # Simulate 10% packet loss
        if random.random() > 0.10:
            successful += 1
    return successful

# Example usage
if __name__ == "__main__":
    payloads = [512, 1024, 256, 4096, 128, 2048, 512]  # example payload sizes
    print(f"Packets sent successfully: {simulate_udp_send(payloads)}")

