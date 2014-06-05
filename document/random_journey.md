Случайное путешествие
=====

Пример запроса, возвращающего "случайное путешествие":
-----

```sh
curl -XGET 'http://go.openrise.org/journey?time=75&cost=500&category_id=3'
```

Параметры запроса:
-----

 - время time - required
 - стоимость cost - required
 - id категории category_id

Пример хранимого json:
-----

```json
{
    "title" : "hamleys",
    "description" : "магазин игрушек",
    "position" : {
        "latitude" : 55.744277,
        "longitude" : 37.567595
    },
    "time" : 40,
    "cost" : 300,
    "category_id" : 3,
    "significance" : 13,
    "route": [
        {
            "description" : "метро Смоленская",
            "position" : {
                "latitude" : 55.747719,
                "longitude" : 37.583925
            }
        },
        {
            "description" : "пройдите до улицы Смоленская",
                "position" : {
                    "latitude" : 55.746632,
                    "longitude" : 37.582165
                }
        },
        {
            "description" : "пройдите до площади Европы",
            "position" : {
                "latitude" : 55.744241,
                "longitude" : 37.570277
            }
        }
    ]
}
```

```json
{
    "title" : "Piccolo Diabolo",
    "description" : "Пицца, бар, пиво, соки. Но в первую очередь - пицца!",
    "position" : {
        "latitude" : 55.788694,
        "longitude" : 37.787324
    },
    "time" : 40,
    "cost" : 700,
    "category_id" : 1,
    "significance" : 25,
    "route": [
        {
            "description" : "общага",
            "position" : {
                "latitude" : 55.788802,
                "longitude" : 37.791422
            }
        },
        {
            "description" : "середина какой-то улицы",
                "position" : {
                    "latitude" : 55.788573,
                    "longitude" : 37.789555
                }
        },
        {
            "description" : "рядом с ярмаркой",
            "position" : {
                "latitude" : 55.788543,
                "longitude" : 37.787334
            }
        }
    ]
}
```

```json
{
    "title" : "Burger King",
    "description" : "жрака. хавка. быстро",
    "position" : {
        "latitude" : 55.792765,
        "longitude" : 37.787077
    },
    "time" : 15,
    "cost" : 200,
    "category_id" : 1,
    "significance" : 7,
    "route": [
        {
            "description" : "общага",
            "position" : {
                "latitude" : 55.788802,
                "longitude" : 37.791422
            }
        },
        {
            "description" : "дойди до 5-ой Парковой",
            "position" : {
                "latitude" : 55.788591,
                "longitude" : 37.788472
            }
        },
        {
            "description" : "дойди до Первомайской",
                "position" : {
                    "latitude" : 55.793097,
                    "longitude" : 37.788236
                }
        },
        {
            "description" : "поврнись налево, пройди 50 метров",
            "position" : {
                "latitude" : 55.793085,
                "longitude" : 37.787281
            }
        }
    ]
}
```