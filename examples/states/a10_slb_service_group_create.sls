a10_slb_service_group_ex:
  a10_slb_service_group.create:
    - protocol: tcp
    - member_list: [{'host': '10.20.42.1', 'name': 'sg1-member1', 'port': 443}]
    - lb_method: dst-ip-hash
    - name: sg1
