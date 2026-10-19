import ipaddress

entry = input("IPv4 address and prefix (example: 192.168.1.10/24): ").strip()
try:
    network = ipaddress.IPv4Network(entry, strict=False)
except ValueError:
    raise SystemExit("Please enter a valid IPv4 address and prefix.")

small = network.prefixlen >= 31
first = network.network_address if small else network.network_address + 1
last = network.broadcast_address if small else network.broadcast_address - 1
usable = network.num_addresses if small else network.num_addresses - 2

print(f"Network: {network}")
print(f"Subnet mask: {network.netmask}")
print(f"Broadcast address: {network.broadcast_address}")
print(f"First usable address: {first}")
print(f"Last usable address: {last}")
print(f"Usable addresses: {usable}")
