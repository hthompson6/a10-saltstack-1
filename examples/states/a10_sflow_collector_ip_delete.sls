a10_sflow_collector_ip_ex:
  a10.delete:
    - a10_obj: sflow_collector_ip 
    - port: 1
    - addr: 10.0.0.1
