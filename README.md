# digital-advertisement-attribution-analytics



## Features
- Add signup event
- Get distinct user count since time
- Add pageview event
- Get analysis which contain pageview count and successfull advertisement count


## Installation
It requires Python3, pipenv to run.
Install the dependencies


```sh
pipenv shell
python app.py
```

## Api
Add event:
POST http://127.0.0.1:5000/event

Payload
```json
{
  "name": "signup",
  "fingerprint": "b998efcb-1af3-4149-9b56-34c4482f6691",
  "user_id": "5566bd0538665441d6ad80011",
  "created_at": "2021-01-02 12:33:41.127641"
}
```

Response
```json
{
    "status": "successfully added"
}
```
Get distinct user count since a date time

GET http://127.0.0.1:5000/event?date_time=2023-02-01
 
Response
```json
{
    "number_of_unique_user": "10"
}
```
Add pageview event

POST http://127.0.0.1:5000/pageview

Payload
```json
{
  "fingerprint": "b998efcb-1af3-4149-9b56-34c4482f6691",
  "user_id": null,
  "url": "https://www.company.com/en/library",
  "referrer_url": "https://www.google.com",
  "created_at": "2023-01-01 12:33:41.127641"
}
```

Response
```json
{
    "status": "successfully added"
}
```

Get analysis

GET http://127.0.0.1:5000/pageview?date_time=2022-02-06&show_succeeded_ad=true

Response
```json
{
  "pageview_count": [
    {
      "null": 1
    },
    {
      "facebook": 1
    },
    {
      "google": 3
    }
  ],
  "succeeded_ad_count": [
    {
      "null": 1
    },
    {
      "google": 1
    }
  ]
}
```
Here null means direct visit
 
