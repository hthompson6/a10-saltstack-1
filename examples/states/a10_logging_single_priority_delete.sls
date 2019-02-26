a10_logging_single_priority_ex:
  a10.delete:
    - a10_obj: logging_single_priority 
    - levelname: emergency
