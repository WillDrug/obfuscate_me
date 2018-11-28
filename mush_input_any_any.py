from musher import mush
import time
import re
from pynput import keyboard
from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener


EXIT_KEY = Key.f14
PAUSE = 2

BREAKAGE = [',', '.', ')', '(', ']', '[', '!', '?', Key.space, Key.enter] + [q for q in range(10)]
UPPER_MOD = [Key.shift_l, Key.shift_r, Key.shift]

# TODO: Stream in ALT+CODE characters
# TODO: supress multiple press events for held keys

class StreamMusher:
    def __init__(self, exit_key):
        self.keepalive = True
        self.exit_key = exit_key
        # self.break_key = None
        self.keyboard_controller = Controller()
        # self.shift = False # not needed for now
        # .press('a')
        # .release('a')
        # .type('dsfsdf')
        self.buffer = list()
        self.modbuffer = list()
        self.clear_buffer()
        self.capture = re.compile('\w')
        self.upper = {q: False for q in UPPER_MOD}
        self.breaker = None

    def run(self):
        while self.keepalive:
            # Todo: rewrite to use suppress event!
            self.breaker = None
            self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)#, suppress=True)
            self.listener.start()
            self.listener.join()
            self.digest()

    def clear_buffer(self):
        self.buffer.clear()
        self.modbuffer.clear()

    def ingest(self, char):
        if char in BREAKAGE:
            self.breaker = char
            self.listener.stop()
            return  # digest and rerun

        if self.capture.match(char):
            self.buffer.append(char)
            self.modbuffer.append(any([self.upper[q] for q in self.upper]))
        else:  # capturing all missed in BREAKAGE, though shouldn't be much
            if self.buffer.__len__() > 0:  # recording started already so this is a word finished
                #self.digest()  # changed to stoppign listener first
                self.listener.stop()
                return

    def digest(self):
        print(f'digesting {self.buffer} \n with mod {self.modbuffer}')
        if self.buffer.__len__() == 0:
            return

        # todo: exception handling
        out = ''.join(self.buffer)
        out = mush(out, single=True)

        self.keyboard_controller.press(Key.left)
        self.keyboard_controller.release(Key.left)
        for l in range(self.buffer.__len__()):
            self.keyboard_controller.press(Key.backspace)
            self.keyboard_controller.release(Key.backspace)

        for m, c in zip(self.modbuffer, out):  # not letting shift bother us
            if m:
                self.keyboard_controller.press(Key.shift_l)
                self.keyboard_controller.press(c)
                self.keyboard_controller.release(c)
            else:
                self.keyboard_controller.release(Key.shift_l)
                self.keyboard_controller.press(c)
                self.keyboard_controller.release(c)
        self.keyboard_controller.release(Key.shift_l)


        # if self.breaker is not None:
        #     self.keyboard_controller.press(self.breaker)
        #     self.keyboard_controller.release(self.breaker)
        self.keyboard_controller.press(Key.right)
        self.keyboard_controller.release(Key.right)
        self.clear_buffer()

    def on_press(self, key):
        if hasattr(key, 'char'):
            self.ingest(key.char)
            return
        if key in BREAKAGE:
            self.breaker = key
            return False  # digest then restart

        if key == Key.backspace:
            try:
                self.buffer.pop()
            except IndexError:
                pass  #if we've finished a word we do not return. for now.
            try:
                self.modbuffer.pop()
            except IndexError:
                pass
            return

        # not processing shift because inbound alphanumeric contains case.
        if key == self.exit_key:  #
            self.keepalive = False
            return False  # digest and quit

        if key in self.upper.keys():
            self.upper[key] = True

        return

    def on_release(self, key):
        if key in self.upper.keys():
            self.upper[key] = False


if __name__ == '__main__':
    sm = StreamMusher(EXIT_KEY)
    sm.run()

