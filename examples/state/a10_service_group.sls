a10_service_group:
  a10_service_group.create:
    - name: sg1
    - protocol: tcp
    - lb_method: round-robin
