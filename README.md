# 💩 doodoo
a simple LiveSplit.Server Receiver.

![screenshot](https://i.imgur.com/jsR1u46.png "A shot of the program running, duh")

## About
The objetive with this program was making a LiveSplit.Server information fetcher in the most basic way. The primary use intended for this is to show the timer from a LAN connected device when there's no way too see it on the source device. For example if you only have one monitor and have to run a game fullscreen, you can see the timer on a laptop.

This code has been rushed and it's structure has been improvised, so don't hesitate to share refactoring suggestions!

This program uses [`tkinter`](https://wiki.python.org/moin/TkInter) to serve a minimal GUI. The configuration can be altered by changing them directly from the `doodoo.py` file.

## Getting started
This program requires `Python 3` with `tkinter` to run. Once it has been installed, modify `doodoo.py`'s configuration to your needs. By default uses Livesplit's default fonts. The most important setting is `serverAddress`, that should point towards your server's IP and by default is `localhost`.

Then just run `python3 doodoo.py` and I'll start getting information from LiveSplit.Server!

If you encounter any problem contact me @Supongo#8868 on discord.

## License
This program is licensed under the MIT license, more information on the LICENSE file.
