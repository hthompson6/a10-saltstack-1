a10_ip_route_static_bfd_ex:
  a10.create:
    - a10_obj: ip_route_static_bfd
    - local_ip: 10.0.0.1
    - nexthop_ip: 10.0.0.1
