a10_cgnv6_lsn_port_reservation_ex:
  a10.delete:
    - a10_obj: cgnv6_lsn_port_reservation 
    - inside_port_start: 1
    - nat_port_start: 1
    - inside_port_end: 1
    - inside: 10.0.0.1
    - nat: 10.0.0.1
    - nat_port_end: 1
