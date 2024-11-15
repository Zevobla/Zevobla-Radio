"""This module helps stream to telegram live stream via rtmp protocol with helps FFMPEG"""
from subprocess import Popen


class Stream:
    """This class wrapps ffmpeg process for easily manipulate them"""

    def __init__(self, input_codec: str = "ogg", input_codec_provider: str = "vorbis", codec: str = "aac", otype: str = "flv", path: str = "/var/www/site/radio") -> None:
        if otype == "hls":
            self.ffmpeg_state: Popen = Popen(f'ffmpeg -f {input_codec} -acodec {input_codec_provider} -ac 2 -i pipe:0 -f {otype} -acodec {codec} -ac 2 -hls_time 10 -hls_list_size 5 -hls_flags "delete_segments" -segment_filename "{path}/segment_%03d.ts" -b:a 320k -af "atempo=1" -buffer_size 1000k -y {path}')
        else:
            self.ffmpeg_state: Popen = Popen(f'ffmpeg -f {input_codec} -acodec {input_codec_provider} -ac 2 -i pipe:0 -f {otype} -acodec {codec} -ac 2 -b:a 320k -af "atempo=1" -buffer_size 1000k -y {path}')

    def start(self, stream):
        """Streams to Telegram's rtmps server through ffmpeg"""

        try:
            if stream.input_stream.stream().pos() >= stream.input_stream.stream().size():
                return True

            data = stream.input_stream.stream().read(500 * 1024)  # 500KB chunks

            if data:
                self.ffmpeg_state.stdin.write(data)
            else:
                return False
        except Exception:
            pass

        self.ffmpeg_state.stdin.close()

    def stop(self):
        """Stops ffmpeg process"""

        self.ffmpeg_state.kill()

        return True
