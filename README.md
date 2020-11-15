# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/headphones.svg" card_color="#40DBB0" width="50" height="50" style="vertical-align:bottom"/> Spotify Sonos Bot
## About
Mycroft (https://mycroft.ai/) is an open source project that provides a local and controlled alternative to Google Assistant and Alexa. Mycroft can run on a Raspberry Pi. Similarly to Alexa, you can add functionalities to your Mycroft voice assistant setup by installing "skills".

This project is a **skill** for Mycroft that provides convenient voice commands to play Spotify music on Sonos speakers.

Kudos to the people involved in the project Node Sonos HTTP API (https://github.com/jishi/node-sonos-http-api/) which does most of the work and exposes an easy to use Sonos API, and to the project Spotipy (https://github.com/plamere/spotipy) that is used for things not available directly from the Node Sonos project. 

**It is still very much WIP** but already provides in its current state the necessary commands for controlling Sonos and Spotify while cooking dinner. **It currently only supports playing music on one Sonos speaker** but using the node http api, it should be fairly easy to add support for several speakers.

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
* "Play the playlist Cool Stuff" (first looks at the user's own playlist, and fallbacks on Spotify's public playlists)

## Pre-requisites
* Get spotify developement credentials here: https://developer.spotify.com/. At the time of writing, anyone can get some.
* Be comfortable using the command line. For example, you need to be able to install and run a node.js app.

## Installation On Raspberry Pi
- Install Picroft on a Raspberry Pi (version 3 or higher) https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft.
- Install the Node Sonos HTTP API server on the Raspberry Pi https://github.com/jishi/node-sonos-http-api/ and ideally make it run as a service with auto restart.
- Run `mycroft-msm install https://github.com/lnguyenh/spotify-sonos-bot-skill` on the Pi.
- Go in your skills settings https://account.mycroft.ai/skills and add
    - your Sonos default speaker
    - your Spotify username (optional but allows prioritizing your own playlists when searching)
    - your Spotify dev client ID (optional but allows prioritizing your own playlists when searching)
    - your Spotify dev client secret (optional but allows prioritizing your own playlists when searching)

## Todos
### Commands

* "What is this song?"
* "... on Living Room"
* "What is the current Sonos volume?"

### Other
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
