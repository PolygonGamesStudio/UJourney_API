Описание API
=============

# version
 - Версия：0.0.1

# request
- server
    - POST
        - url: '/game'
        - format: json
        - request: {"server":'127.0.0.1:80'}
        - response:
            - success:  {"id":2}
            - fail:     {"status_code": 400, "status_txt": "Invalid POST request, check the data."}

    - GET
       - url: '/game'
       - request: none
       - response:
            - success: {"address": "127.0.0.1:8880"}
            - fail: {"status_code": 404, "status_txt": "Invalid address"}

    - PUT
    - PATCH
    - DELETE
        - url: '/game/{game_id}'
        - request:  none
        - response:
            - success: HTTP 200
            - fail:
                - {"status_code": 403, 'status_txt': 'Access denied'}
                - {"status_code": 500, 'status_txt': 'Error unknown. May try latter'}
