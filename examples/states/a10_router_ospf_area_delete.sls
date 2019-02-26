a10_router_ospf_area_ex:
  a10.delete:
    - a10_obj: router_ospf_area 
    - area_ipv4: 10.0.0.1
