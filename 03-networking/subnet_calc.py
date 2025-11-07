import sys, ipaddress
def main():
    if len(sys.argv) != 2:
        print("Usage: python subnet_calc.py 192.168.68.0/24")
        sys.exit(1)
    net = ipaddress.ip_network(sys.argv[1], strict=False)
    hosts = list(net.hosts())
    print(f"Network:   {net.network_address}")
    print(f"Netmask:   {net.netmask}")
    print(f"Broadcast: {net.broadcast_address}")
    print(f"Usables:   {len(hosts)}")
    if hosts:
        print(f"First IP:  {hosts[0]}")
        print(f"Last IP:   {hosts[-1]}")
if __name__ == "__main__":
    main()
