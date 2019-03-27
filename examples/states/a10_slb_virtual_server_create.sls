VS2:
  a10.create:
    - a10_obj: slb_virtual_server
    - ip_address: 192.168.43.6
    - netmask: 255.255.255.0
    - a10_name: vs2
    - port-list:
      - 22:
        - protocol: tcp
      - 80:
        - protocol: tcp
    - service_group-list:
      - sg1:
        - member-list:
          - m1:
            - port: 0
          - m2:
            - port: 1
        - lb_method: round_robin
