# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/headphones.svg" card_color="#40DBB0" width="50" height="50" style="vertical-align:bottom"/> Spotify Sonos Bot
## About
Mycroft (https://mycroft.ai/) is an open source project that provides a local and controlled alternative to Google Assistant and Alexa. Mycroft can run on a Raspberry Pi. Similarly to Alexa, you can add functionalities to your Mycroft voice assistant setup by installing "skills".

This project is a **skill** for Mycroft that provides convenient voice commands to play Spotify music on Sonos speakers.

Kudos to the people involved in the project Node Sonos HTTP API (https://github.com/jishi/node-sonos-http-api/) which does most of the work and exposes an easy to use Sonos API.

**It is still very much WIP** but already allows in its current state the necessary commands for controlling Sonos and Spotify while cooking dinner. It currently only supports playing music on one Sonos speaker but using the node http api, it should be fairly easy to add support for several speakers.

## Supported Commands
* "Play some music"
* "Stop the music"
* "Play the playlist Morning Acoustic"
* "Play the album Parachute"
* "Sonos volume up"
* "Decrease the volume on Sonos"
* "Set the Sonos volume to 10"
* "Next song"
* "Previous song"
* "Play some music by Coldplay"
* "Play the radio for Coldplay"
* "Play the playlist Cool Stuff" (First looks at the user's own playlist, and fallbacks on Spotify's public playlists)

## Pre-requisites
* Get spotify developement credentials here: https://developer.spotify.com/. At the time of writing, anyone can get some.
* Be comfortable running command line commands. For example, you need to be able to install and run a node.js app for example.

## Installation On Raspberry Pi
- Install Picroft on a Raspberry Pi (version 3 or higher) https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft.
- Install the Node Sonos HTTP API server on the Raspberry Pi https://github.com/jishi/node-sonos-http-api/ and ideally make it run as a service with auto restart.
- Run `mycroft-msm install https://github.com/lnguyenh/spotify-sonos-bot-skill` on the Pi.
- Go in your skills settings https://account.mycroft.ai/skills and add
    - your Sonos default speaker
    - your Spotify username (only needed to playing non-popular public playlist)
    - your Spotify dev client ID (only needed to playing non-popular public playlist)
    - your Spotify dev client secret (only needed to playing non-popular public playlist)

## Todos
### Commands

* "What is this song?"
* "... on Living Room"
* "Skip 5 songs"
* Play the song Last Christmas"
* "What is the current Sonos volume?"

### Other
* Support for multiple Sonos speakers
* Make configuration less hardcoded
* Document and streamline the setup
* tests :)

## Credits
* Mycroft, the open source local voice assistant (https://mycroft.ai/)
* Node Sonos HTTP API, which does all the heavy lifting related to Sonos and Spotify (https://github.com/jishi/node-sonos-http-api/)

## Category
**Music & Audio**

## Tags
**Spotify**

**Sonos**
