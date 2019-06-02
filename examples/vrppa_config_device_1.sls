vrppa_common_dev1:
  a10.vrrp_a:
    - common:
      - device_id: 1
      - action: enable
      - set_id: 1 

activ_part_dev1:
  a10.active_partition:
    - CorpA

vrppa_vrid_dev1:
  a10.vrrp_a:
    - vrid:
      - 0:
        - blade_parameters:
          - tracking_options:
            - interface: [{ "ethernet": 1, "priority-cost": 1 }]
