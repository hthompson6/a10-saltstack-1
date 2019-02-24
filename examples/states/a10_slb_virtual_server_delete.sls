a10_slb_virtual_server_ex:
  a10:
    - delete
    - a10_obj: slb_virtual_server
    - port_list: [{'protocol': 'https', 'port-number': 443}, {'protocol': 'http', 'port-number': 80, 'template-persist-cookie': 'sg-cookie-persist'}, {'protocol': 'tcp', 'port-number': 22}]
    - ip_address: 192.168.42.1
    - netmask: 255.255.255.0
    - name: vs1
