ip_route_static_bfd:
  a10.delete:
    - a10_obj: ip_route_static_bfd 
    - local_ip: 10.0.0.1
    - nexthop_ip: 10.0.0.1
