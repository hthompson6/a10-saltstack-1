a10_ip_nat_inside_source_static_ex:
  a10.update:
    - a10_obj: ip_nat_inside_source_static
    - nat_address: 10.0.0.1
    - src_address: 10.0.0.1
