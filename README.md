# News Board API
This is the simple news board API.
There is a list of news with functionality to upvote and comment on them.

To start application using Docker use the following command:
```
docker-compose up
```
## API documentation
There is [link](https://documenter.getpostman.com/view/12026468/TVRoYSNx) to Postman collection

## Recurring Job
In order to implement recurring jobs I use [django-crontab](https://github.com/kraiz/django-crontab).

There are cronjob settings in settings.py:
```
CRONJOBS = [
    ('30 0 * * *', 'news.cron.reset_votes')
]
```
