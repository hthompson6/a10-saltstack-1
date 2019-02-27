slb_virtual_server:
  a10.delete:
    - port_list: [{'protocol': 'https', 'port-number': 443}, {'protocol': 'http', 'port-number': 80, 'template-persist-cookie': 'sg-cookie-persist'}, {'protocol': 'tcp', 'port-number': 22}]
    - ip_address: 192.168.42.1
    - netmask: 255.255.255.0
    - a10_name: vs1
