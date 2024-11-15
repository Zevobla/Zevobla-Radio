from librespot.core import Session
from librespot.audio import PlayableContentFeeder
from librespot.metadata import TrackId
from librespot.audio.decoders import AudioQuality, VorbisOnlyAudioQuality
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class StreamFromSpotify():
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.session = Session.Builder().stored_file().create()

        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id, client_secret))
    
    def get_playlist(self, playlist_id: str) -> list[TrackId]:
        """Return byte stream"""

        tracks = self.client.playlist_items(playlist_id)

        streams: list[PlayableContentFeeder] = []

        for _, item in enumerate(tracks['items']):
            track = item['track']
            track_id = TrackId.from_uri("spotify:track:" + str(track["id"]))
            streams.append(track_id)
        
        return streams
        
    def stream_track(self, track_id: TrackId, quality: VorbisOnlyAudioQuality = VorbisOnlyAudioQuality(AudioQuality.VERY_HIGH)) -> PlayableContentFeeder:
        """Returns track stream"""
        
        try:
            return self.session.content_feeder().load(track_id, quality, False, None)
        except RuntimeError as e:
            print(f"Tried download {track_id} with {quality} quality but got error {e}")