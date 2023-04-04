# ptb-polling


## Table of contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Initial setup](#initial-setup)
- [Daemon setting](#daemon-setting)
- [Relative links](#relative-links)


## General info

Python polling telegram bot for website visitbudapest.ru


## Technologies

Project is created with:

- Python3.10
- python-telegram-bot v20.2


## Initial setup

Clone repository

```
git clone git@github.com:dnmos/ptb-polling.git
```

Fill token in .env

```
vim ./env/.env
```


## Daemon setting

```
vim /etc/systemd/system/vibot.service
```

```
[Unit]
Description=Python Telegram bot visitistanbul.ru
After=network.target

[Service]
User=www
Group=www-data
WorkingDirectory=/home/www/vi/bot
Restart=on-failure
RestartSec=2s
ExecStart=/home/www/vi/bot/env/bin/python -m main.py

[Install]
WantedBy=multi-user.target
END
```

```
sudo systemctl daemon-reload
```

```
sudo systemctl enable vibot.service
```

```
sudo systemctl start vibot.service
```


## Relative links

PTB [documentation](https://docs.python-telegram-bot.org/en/stable/)