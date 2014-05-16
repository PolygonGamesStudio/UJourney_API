Описание API
=============

# version
 - Версия：0.0.1

# request
- history
    - GET
        - url: '/history'
        - format: json
        - request: {'user_id': 'hfdjaoqi21'}
        - response: {"user": {"name": "Mike", "lastname": "Petrov", "user_id": "hfdjaoqi21"}, "title": "True Burgers", "visit": "2001-2-3 10:11:12", "rating": 3, "picture": "vk.com/icon.png", "id": 0}
    - POST
        - url: '/history'
        - format: json
        - request: [{"user": {"name": "Mike", "lastname": "Petrov", "user_id": "hfdjaoqi21"}, "title": "True Burgers", "visit": "2001-2-3 10:11:12", "rating": 3, "picture": "vk.com/icon.png", "id": 0}, ...]
        - response:
            - success: {"status": "ok"}
            - fail: {"status_code": "417", "status_txt": "Invalid POST request, check the data.", "status": "fail"}
    - DELETE
        - url: '/history'
        - format: json
        - request: {"user_id": "hfdjaoqi21", "token": "123"}
        - response:
            - success: {"status": "ok"}
            - fail: {"status_code": "411", "status_txt": "Invalid DELETE request, check the data.", "status": "fail"}

