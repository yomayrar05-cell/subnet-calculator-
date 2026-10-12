# Subnet Calculator

A command-line tool that takes an IP address in CIDR notation (e.g. `192.168.1.0/24`)
and calculates the key facts about that subnet: network address, broadcast address,
subnet mask, wildcard mask, usable host range, and host count.

## How to run

```bash
python3 subnet_calc.py
```

Then enter an address like `192.168.1.0/24` when prompted. Type `q` to quit.

## Example

```
=== Subnet Calculator ===

Enter IP in CIDR notation (e.g. 192.168.1.0/24), or 'q' to quit: 192.168.1.0/24

  Network Address    192.168.1.0
  Broadcast Address  192.168.1.255
  Subnet Mask        255.255.255.0
  Wildcard Mask      0.0.0.255
  Prefix Length      24
  Total Addresses    256
  Usable Hosts       254
  First Usable       192.168.1.1
  Last Usable        192.168.1.254
```

## Concepts demonstrated

- IP addressing and CIDR notation
- Subnet masks, wildcard masks, network and broadcast addresses
- Usable host range and host count
- Python's built-in `ipaddress` module and input validation / error handling

## Requirements

Python 3 (no extra packages needed — uses only the standard library).
