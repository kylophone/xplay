xplay
=====
xplay is a tool for playing Axia Livewire AoIP streams from the command line. Functionally the same as Axia iPlay on Windows, this is a an option for broadcast engineers using Linux/OSX/UNIX. xplay works by piping the audio payload from a multicast RTP stream directly into the SoX utility \`play\` along with a few stream parameters. 

dependancies
=====
You'll need \`play\` which comes with <a href = "http://sox.sourceforge.net/">SoX</a>, and also \`rtpdump\` from <a href = "http://www.cs.columbia.edu/irt/software/rtptools/">RTP Tools</a>.

setup
=====
If you've installed play and rtpdump somewhere that's not /usr/bin, you'll need to update those paths in xplay.py
```bash
$ chmod +x xplay.py
$ cp xplay.py /usr/bin/xplay
```
usage
=====
Make sure you assign your computer an IP address that is on the Axia network. Call xplay with the Axia channel number you'd like to listen in on, and you should be able to hear the Livewire stream. ^C to end.
```bash
$ xplay 32767
```
