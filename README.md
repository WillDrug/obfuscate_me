# obfuscate_me
General purpose chatting obfuscation for fun.

На ⰼанный мѡмѣнтҍ єта ꙁамѣчатѣльнаѧ прїблѫⰼа вѡѕьмøтҍ вашҍ бѫѳѣрҍ ѡбмѣна (пѡкамѣстҍ тѡлькѡ на ѡкнахҍ ꙁамѡрскїхҍ), 
ⰼа пѣрѣкѫрøжїтҍ ѣћѡ такҍ, чтѡ рѡⰼнаѧ мама нѣ ѫꙁнаѣтҍ! Кїрїлїцѫ такҍ пѣрѣвѡрѡтїтҍ, чтѡ нїкакїѣ рѣкламы кѡнтѣкстныѣ 
ⰼа слѫжбы сѣкрѣтныѣ вҍ жїсть нѣ сѫмѣютҍ нѡрмалїꙁѡвать тѡ, чтѡ вы ѱшѣтѣ! Пѡльѕѫйтѣсь, ⰼа нѣ ѕабывайтѣ барьѣрҍ пѡⰼстраївать! 
Тѡ, чтѡ вы чїтаѣтѣ сⰼѣланѡ на -1, нѡ ѣслї пѡставїть 0.7, ѣсть хѡть какѡй-тѡ шансҍ пѡнѧть, чтѡ їмѣннѡ наѱсанѡ.
## This is not a code obfuscation tool.
This is, rather, a thing to change the text you're about to send to something aweful.

## Usage
Please refer to usage in the changelog for now. Before usage requirements should be installed.
There is no requirements.txt because it would be an overkill for each one script. All requirements are listed here

The requirements for the main obfuscation tool now include:
* pymorphy2

## Changelog
### v1.1


### v1.0
win_clipboard_musher.py
Basic windows clipboard musher. I use it with AutoHotKey with this (I do have a way of pressing F13, 
but you can change the key used).
```lua
^!n::
return
F13::run python obfuscate_me\win_clipboard_musher.py
```
Requirements to run mush_clipboard_win_any.py
* win32clipboard


### Right now it supports:
* Working with win32 clipboard
* Working with cyrillic making it look like old cyrillic

### It requires:

### I would like to add:
* Linux support
* Old\Middle english style changes

So feel free to pull request.

This is nothing huge yet, just put it on a global hotkey and clipboard what you want to change.