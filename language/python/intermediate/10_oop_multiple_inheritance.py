class AudioPlayer:
    def play_music(self):
        print("Audio Player is playing Music")
class VideoPlayer:
    def play_video(self):
        print("Video Player is playing video")
class BluetoothMixin:
    def connect_bluetooth(self):
        print("Bluetooth is connected")

class MediaDevice(AudioPlayer, VideoPlayer, BluetoothMixin):
    pass

mydevice = MediaDevice()
mydevice.play_music()
mydevice.play_video()
mydevice.connect_bluetooth()