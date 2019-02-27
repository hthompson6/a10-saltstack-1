health_monitor:
  a10.update:
    - up_retry: 1
    - retry: 1
    - method: {'tcp': {'port-send': '[42, 42, 42]', 'method-tcp': 1, 'port-resp': {'port-contains': '[45, 45, 45]'}, 'tcp-port': 80}}
    - a10_name: my_monitor
