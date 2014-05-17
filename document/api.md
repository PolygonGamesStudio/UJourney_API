Описание API
=============

# version
 - Версия：0.0.1

# sample
```
curl -H "Content-Type: application/json" -d '{"user": {"name": "Mike","lastname": "Petrov", "user_id": "mike@gmail.com"}, "place": "True Burgers", "time": "2001-2-3 10:11:12", "rating": 5, "icon": "vk.com/icon.png", "id": 7}' http://localhost:8888/history
```

# request
- history
    - GET
        - url: '/history/([\w]+)'
        - format: json
        - request: user_id
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
- user
    - GET
        - url: '/user/([\w]+)'
        - format: json
        - request: user_id
        - response: {"name": "Mike", "lastname": "Petrov", "user_id": "hfdjaoqi21", "email": "mike@gmail.com", "picture": "https://pp.vk.me/c322222/v322222574/8319/KiennRC_ZAM.jpg"}
    - POST
        - url: '/user'
        - format: json
        - request: {"name": "Mike", "lastname": "Petrov", "user_id": "hfdjaoqi21", "email": "mike@gmail.com", "picture": "https://pp.vk.me/c322222/v322222574/8319/KiennRC_ZAM.jpg"}
        - response:
            - success: {"status": "ok"}
            - fail: {"status_code": "417", "status_txt": "Invalid POST request, check the data.", "status": "fail"}