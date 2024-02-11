import time
from soco import discover
import requests

while True:
    for zone in discover():
        # Check if this zone is part of a group and not the coordinator
        if zone.group.coordinator.player_name != zone.player_name:
            # Get track info from the coordinator
            track_info = zone.group.coordinator.get_current_track_info()
        else:
            # Get track info from this zone
            track_info = zone.get_current_track_info()

        # Check if the track_info is not empty -> music is playing
        if track_info["title"] != "":
            music_info = f"{zone.volume}% | {track_info['title']} | {track_info['artist']}"
        else:
            music_info = f"{zone.volume}% | Idle"

        print(f"{zone.player_name}: {music_info}")
        # Send the music info to the Loxone Miniserver
        r = requests.get(f"http://USER:PASSWORT@IPADDRESS/dev/sps/io/Sonos {zone.player_name}/{music_info}")

    time.sleep(10)
