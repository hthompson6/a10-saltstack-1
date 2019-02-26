a10_fw_server_port_ex:
  a10.delete:
    - a10_obj: fw_server_port 
    - protocol: tcp
    - port_number: 1
