a10_cgnv6_ds_lite_port_reservation_ex:
  a10_cgnv6_ds_lite_port_reservation.create:
    - nat_end_port: 1
    - inside_start_port: 1
    - nat: 10.0.0.1
    - inside_end_port: 1
    - nat_start_port: 1
    - inside_addr: 10.0.0.1
