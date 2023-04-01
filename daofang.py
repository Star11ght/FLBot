from pydub import AudioSegment

from pydub.playback import play

ted = AudioSegment.from_file("H:/test.mp3")

backwards = ted.reverse()

backwards.export("H:/reverse.mp3" , format="mp3")
