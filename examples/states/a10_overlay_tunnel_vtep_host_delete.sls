a10_overlay_tunnel_vtep_host_ex:
  a10.delete:
    - a10_obj: overlay_tunnel_vtep_host 
    - destination_vtep: 10.0.0.1
    - ip_addr: 10.0.0.1
    - vni: 1
