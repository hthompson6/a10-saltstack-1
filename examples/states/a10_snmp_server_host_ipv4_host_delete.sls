a10_snmp_server_host_ipv4_host_ex:
  a10.delete:
    - a10_obj: snmp_server_host_ipv4_host 
    - ipv4_addr: 10.0.0.1
    - version: v1
