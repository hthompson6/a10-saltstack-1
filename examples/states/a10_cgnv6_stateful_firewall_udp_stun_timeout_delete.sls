a10_cgnv6_stateful_firewall_udp_stun_timeout_ex:
  a10.delete:
    - a10_obj: cgnv6_stateful_firewall_udp_stun_timeout 
    - port_end: 1
    - port: 1
