a10_health_monitor_ex:
  a10_health_monitor.update:
    - up_retry: 1
    - retry: 1
    - method: {'tcp': {'port-send': '[42, 42, 42]', 'method-tcp': 1, 'port-resp': {'port-contains': '[45, 45, 45]'}, 'tcp-port': 80}}
    - name: my_monitor
