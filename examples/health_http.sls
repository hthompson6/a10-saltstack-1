http_health_montitor_example:
  a10.health:
    - monitor:
      - h1:
        - method:
          - http:
            - http_port: 80
            - http: 1
            - http_url: 0
