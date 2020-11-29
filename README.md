# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/headphones.svg" card_color="#40DBB0" width="50" height="50" style="vertical-align:bottom"/> Spotify-Sonos Mycroft Skill

[![Join the chat at https://gitter.im/lnguyenh/sonos-spotify-mycroft](https://badges.gitter.im/lnguyenh/sonos-spotify-mycroft.svg)](https://gitter.im/lnguyenh/sonos-spotify-mycroft?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## About
**Mycroft** (https://mycroft.ai/) is an open source project that provides a local and controlled alternative to Google Assistant and Alexa. Mycroft can run on a Raspberry Pi. Similarly to Alexa, you can add functionalities to your Mycroft voice assistant setup by installing "skills".

This project is a **skill** for Mycroft that provides convenient voice commands to play Spotify music on Sonos speakers.

Big kudos to:
- the project **Node Sonos HTTP API** (https://github.com/jishi/node-sonos-http-api/) which does most of the work and exposes an easy to use Sonos API
- the project **Spotipy** (https://github.com/plamere/spotipy) that is used for populating the user's list of personal spotify playlists, and to play the most popular songs for a given artist.

In its current state, this project provides all the commands I have needed in order to voice-control Sonos and Spotify while cooking dinner :). **It currently only supports playing music on one Sonos speaker** but using the node http api, it should be fairly easy to add support for several speakers.

## Supported Commands
* "Play some music"
* "Stop the music"
* "Play the playlist Morning Acoustic"
* "Play the album Parachute"
* "Sonos volume up"
* "Decrease the volume on Sonos"
* "Set the Sonos volume to 10"
* "Next song"
* "Skip 5 songs"
* "Previous song"
* "Play the song Karma Police"
* "Play some music by Coldplay" (plays the most popular songs for this artist and not the curated Spotify playlist, that is how we like it :) 
* "Play the radio for Coldplay"
* "Play the playlist Cool Stuff" (first looks at the user's own playlist, and fallbacks on Spotify's public playlists. **The user's playlist has to be public** )
* "What is this song?"
* "What is the current Sonos volume?"


## Pre-requisites
* Get spotify developement credentials here: https://developer.spotify.com/. At the time of writing, anyone can get some.
* Be comfortable using the command line. For example, you need to be able to install and run a node.js app.

## Installation On Raspberry Pi
- Install Picroft on a Raspberry Pi (version 3 or higher) https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft.
- Install the Node Sonos HTTP API server on the Raspberry Pi https://github.com/jishi/node-sonos-http-api/ and ideally make it run as a service with auto restart.
    - Don't forget to add your Spotify dev credentials. They live in the file called settings.json in the root folder of `node-sonos-http-api`
    - `node-sonos-http-api` is expected to run on the Pi and be available ay `http://localhost:5005/`
    - Some helper files are included in the folder `node-sonos-http-api-resources`
    - Suggested installation should be something like:
    ```
  # -> Install node.js on the raspberry pi. Google it yourself or check https://linuxize.com/post/how-to-install-node-js-on-raspberry-pi/ for example
  cd /home/pi
  git clone https://github.com/jishi/node-sonos-http-api.git
  cd node-sonos-http-api
  touch settings.json
  # -> Add your spotify credentials in settings.json. See example in `node-sonos-http-api-resources/settings.json`
  # -> Place the file `node-sonos-http-api-resources/node-sonos-http-api.service` in /lib/systemd/system/`
  sudo systemctl enable node-sonos-http-api
  sudo systemctl start node-sonos-http-api
  ```
- Run `mycroft-msm install https://github.com/lnguyenh/spotify-sonos-bot-skill` on the Pi.
- Go in your skills settings https://account.mycroft.ai/skills and add
    - your Sonos default speaker
    - your Spotify username (optional but allows prioritizing your own playlists when searching)
    - your Spotify dev client ID (optional but allows prioritizing your own playlists when searching)
    - your Spotify dev client secret (optional but allows prioritizing your own playlists when searching)

## Todos

* Support for multiple Sonos speakers
* Make configuration less hardcoded
* Document and streamline the setup
* tests :)

## Credits
* Mycroft, the open source local voice assistant (https://mycroft.ai/)
* Node Sonos HTTP API, which does all the heavy lifting related to Sonos and Spotify (https://github.com/jishi/node-sonos-http-api/)
* Spotipy used for a few specific commands not supported by Node Sonos (https://github.com/plamere/spotipy) 

## Category
**Music & Audio**

## Tags
**Spotify**

**Sonos**
