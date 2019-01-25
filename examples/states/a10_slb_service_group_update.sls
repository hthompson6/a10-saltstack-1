a10_slb_service_group_ex:
  a10:
    - update
    - a10_obj: slb_service_group
    - protocol: tcp
    - member_list: [{'host': '10.20.42.1', 'name': 'sg1-member1', 'port': 443}]
    - lb_method: dst-ip-hash
    - name: sg1
