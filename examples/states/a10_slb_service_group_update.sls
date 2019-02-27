slb_service_group:
  a10.update:
    - protocol: tcp
    - member_list: [{'host': '10.20.42.1', 'name': 'sg1-member1', 'port': 443}]
    - lb_method: dst-ip-hash
    - a10_name: sg1
