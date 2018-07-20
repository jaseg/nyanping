Nyanping
========

Nyanping is an audio-visual ping utility that you can use when you need to diagnose connection problems while you're away from your computer. Or any other time. Just turn it on, and turn your volume up.

Usage
-----

```
$ nyanping heise.de
```

Pitch and speed will be proportional to the ping latency. In case of a timeout, the video pauses and resumes when connectivity is restored.

Installation
------------

```
$ pip install nyanping
```

Requirements
------------

* python
* python-mpv
* libmpv
* youtube-dl

