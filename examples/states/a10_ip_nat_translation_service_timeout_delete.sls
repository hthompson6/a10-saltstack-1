a10_ip_nat_translation_service_timeout_ex:
  a10.delete:
    - a10_obj: ip_nat_translation_service_timeout 
    - service_type: tcp
    - port: 1
