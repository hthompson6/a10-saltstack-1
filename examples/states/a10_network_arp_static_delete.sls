a10_network_arp_static_ex:
  a10.delete:
    - a10_obj: network_arp_static 
    - vlan: 2
    - ip_addr: 10.0.0.1
