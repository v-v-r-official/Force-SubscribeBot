# Introduction
**A Telegram Bot to force users to join a specific channel before sending messages in a group.**
- Find it on Telegram as [SK4S](https://t.me/SK4S_SubscribeBot)

## Todo
- [ ] Add multiple channels support
- [X] Configure different groups with different channels
- [X] Clean messages after completion
- [ ] LOGGER support.

## Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/v-v-r-official/Force-SubscribeBot)

### Installation
- Clone this repo
```
git clone https://github.com/sachink4s/Force-SubscribeBot
```
- Change directory
```
cd Force-SubscribeBot
```
- Install requirements
```
pip3 install -r requirements.txt
```

### Configuration
Add [APP_ID](https://my.telegram.org/apps), [API_HASH](https://my.telegram.org/apps), [BOT_TOKEN](https://t.me/botfather) in [Config.py](Config.py) or in Environment Variables.

### Deploying
- Run bot.py
```
python3 bot.py
```

## Thanks to
- [PyroGram](https://PyroGram.org)
- [Hasibul Kabir](https://GitHub.com/hasibulkabir) and [Spechide](https://GitHub.com/spechide) for helping.
