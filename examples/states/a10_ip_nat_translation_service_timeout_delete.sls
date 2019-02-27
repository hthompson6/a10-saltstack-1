ip_nat_translation_service_timeout:
  a10.delete:
    - a10_obj: ip_nat_translation_service_timeout 
    - service_type: tcp
    - port: 1
