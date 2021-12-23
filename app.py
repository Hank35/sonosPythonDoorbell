import soco
import time
from flask import Flask

app = Flask(__name__)
doorbell = "https://raw.githubusercontent.com/jfarcher/esp8266-mqtt-sonos-doorbell/master/doorbell-1.mp3"


@app.route('/ring')
def ring():
    device = soco.discovery.by_name("Penthouse")
    track = device.get_current_track_info()
    initial_playlist_position = int(track["playlist_position"]) - 1

    initial_track_position = (track["position"])
    initial_state = device.get_current_transport_info().get("current_transport_state")
    initial_volume = device.volume
    device.volume=15
    device.play_uri(uri=doorbell, meta='')
    time.sleep( 2 )
    device.volume=initial_volume  
    device.play_from_queue(initial_playlist_position)
    device.seek(initial_track_position)
    # doesnt seem to work if you stream from spotify yet.
    if initial_state != 'PLAYING':
                device.pause()


if __name__ == '__main__':
    app.run(debug=True, port=1337, host='0.0.0.0')