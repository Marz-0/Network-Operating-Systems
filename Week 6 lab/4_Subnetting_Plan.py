import ipaddress

network = ipaddress.IPv4Network('172.16.0.0/16', strict=False)

# Engineering: 30 hosts → Needs at least /27
eng_subnet = list(network.subnets(new_prefix=27))[0]

# Marketing: 15 hosts → Needs at least /28
mkt_subnet = list(network.subnets(new_prefix=28))[1]

# Finance: 10 hosts → Needs at least /28
fin_subnet = list(network.subnets(new_prefix=28))[2]

# HR: 5 hosts → Needs at least /29
hr_subnet = list(network.subnets(new_prefix=29))[3]

print("Subnetting Plan:")
print(f"Engineering: {eng_subnet}")
print(f"Marketing: {mkt_subnet}")
print(f"Finance: {fin_subnet}")
print(f"HR: {hr_subnet}")
