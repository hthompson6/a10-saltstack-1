a10_router_ipv6_ospf_area_ex:
  a10.delete:
    - a10_obj: router_ipv6_ospf_area 
    - area_ipv4: 10.0.0.1
