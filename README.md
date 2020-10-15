# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/headphones.svg" card_color="#40DBB0" width="50" height="50" style="vertical-align:bottom"/> Spotify Sonos Bot
Mycroft is an open source project that provides a local and controlled alternative to Google Assistant and Alexa. Mycroft can run on a Raspberry Pi. Similarly to Alexa, you can add functionalities to your Mycroft voice assistant setup by installing "skills".

This project is a skill for Mycroft that provides convenient voice commands to play Spotify music on Sonos speakers.


**It is still very much WIP** but already allows in its current state the necessary commands for controlling Sonos and Spotify while cooking dinner.

## Supported Commands
* "Play some music"
* "Stop the music"
* "Play the playlist Morning Acoustic"
* "Play the album Parachute"

## Installation On Raspberry Pi
- Install Picroft https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft
- Install the Node Sonos HTTP API server https://github.com/jishi/node-sonos-http-api/
- Run `mycroft-msm install https://github.com/lnguyenh/spotify-sonos-bot-skill`


## Todos
### Commands
* "Next song"
* "Previous song"
* "Play some music by Coldplay"
* "What is this song?"
* "... on Living Room"
* "Sonos volume up"
### Misc
* Make configuration less hardcoded
* Document and improve the setup

## Credits
* Mycroft, the open source local voice assistant (https://mycroft.ai/)
* Node Sonos HTTP API, which does all the heavy lifting related to Sonos and Spotify (https://github.com/jishi/node-sonos-http-api/)

## Category
**Music & Audio**

## Tags
**Spotify**

**Sonos**
