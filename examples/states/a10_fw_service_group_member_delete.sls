a10_fw_service_group_member_ex:
  a10.delete:
    - a10_obj: fw_service_group_member 
    - port: 1
    - name: my_member
