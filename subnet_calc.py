"""
subnet_calc.py — Subnet Calculator
----------------------------------
Enter an IP address in CIDR notation (e.g. 192.168.1.0/24) and this script
calculates the key facts about that subnet.

Concepts this project demonstrates:
- IP addressing and CIDR notation
- Subnet mask, wildcard mask, network address, broadcast address
- Usable host range and host count
- Python's built-in `ipaddress` module and basic error handling
"""

import ipaddress


def calculate_subnet(cidr: str) -> dict:
    """Take a CIDR string like '192.168.1.0/24' and return subnet facts."""
    # ip_network parses the address; strict=False allows host bits set,
    # e.g. typing 192.168.1.10/24 instead of the network address.
    network = ipaddress.ip_network(cidr, strict=False)

    # .hosts() yields every usable host address (excludes network + broadcast).
    hosts = list(network.hosts())

    return {
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "subnet_mask": str(network.netmask),
        "wildcard_mask": str(network.hostmask),
        "prefix_length": network.prefixlen,
        "total_addresses": network.num_addresses,
        "usable_hosts": len(hosts),
        "first_usable": str(hosts[0]) if hosts else "N/A",
        "last_usable": str(hosts[-1]) if hosts else "N/A",
    }


def main():
    print("=== Subnet Calculator ===\n")
    while True:
        cidr = input("Enter IP in CIDR notation (e.g. 192.168.1.0/24), or 'q' to quit: ").strip()
        if cidr.lower() == "q":
            print("Goodbye!")
            break
        try:
            result = calculate_subnet(cidr)
        except ValueError:
            # Catches malformed input like "192.168.1.999/24" or "hello".
            print("Invalid input. Use the format: <ip>/<prefix>, e.g. 10.0.0.0/8\n")
            continue

        print()
        for key, value in result.items():
            print(f"  {key.replace('_', ' ').title():<18} {value}")
        print()


if __name__ == "__main__":
    main()
