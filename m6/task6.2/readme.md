# Configuring DHCP, DNS servers and dynamic routing using OSPF protocol

# 1. Use already created internal-network for three VMs (VM1-VM3). VM1 has NAT and internal, VM2, VM3 – internal only interfaces.
<p><img src="screenshots/1.png"/></p>

# 2-3. Install and configure DHCP server on VM1. (3 ways: using VBoxManage, DNSMASQ and ISC-DHSPSERVER). You should use at least 2 of them. Check VM2 and VM3 for obtaining network addresses from DHCP server.

**Using DNSMASQ:**

Config file:
<p><img src="screenshots/2.png"/></p>
<p><img src="screenshots/3.png"/></p>

**Using VBoxManage:**

```vboxmanage dhcpserver add --netname intnet --ip 192.168.20.1 --netmask 255.255.255.0 --lowerip 192.168.20.100 --upperip 192.168.20.150 --enable```

<p><img src="screenshots/444.png"/></p>
<p><img src="screenshots/445.png"/></p>

# 4-5. Using existed network for three VMs (from p.1) install and configure DNS server on VM1. (You can use DNSMASQ, BIND9 or something else). Check VM2 and VM3 for gaining access to DNS server (naming services).
<p><img src="screenshots/5.png"/></p>
<p><img src="screenshots/4.png"/></p>
