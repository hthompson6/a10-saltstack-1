a10_route_map_ex:
  a10.delete:
    - a10_obj: route_map 
    - sequence: 1
    - action: permit
