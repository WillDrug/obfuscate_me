from musher import mush
import time
import re
from pynput import keyboard
from pynput.keyboard import Key, Controller
from pynput.keyboard import Listener

MODIFIERS = [Key.shift_l, Key.shift, Key.shift_r, Key.ctrl_l, Key.ctrl, Key.cmd_r, Key.cmd_r, Key.cmd, Key.cmd_l]

EXIT_KEY = Key.f14
PAUSE = 2

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
        self.clear_buffer()
        self.capture = re.compile('\w')
        self.modifiers = {
            Key.ctrl: False,  # todo: move to CTRL = [Key.ctrl, Key.ctrl_l, etc.] const list
            Key.alt: False,
            Key.cmd: False,
            Key.ctrl_l: False,
            Key.ctrl_r: False,
            Key.alt_l: False,
            Key.alt_r: False,
            Key.alt_gr: False,
            Key.cmd_l: False,
            Key.cmd_r: False
        }

    def run(self):
        while self.keepalive:
            self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
            self.listener.start()
            self.listener.join()
            self.digest()

    def clear_modifiers(self):
        for k in self.modifiers:
            self.modifiers[k] = False

    def clear_buffer(self):
        self.buffer.clear()

    def ingest(self, char):
        for k in self.modifiers:
            if self.modifiers[k]:
                if char in ['X', 'x'] and self.modifiers[Key.ctrl_l]:  # some bullshittery is afoot
                    self.clear_buffer()
                return
        if self.capture.match(char):
            self.buffer.append(char)
        else:
            if self.buffer.__len__() > 0:  # recording started already so this is a word finished
                #self.digest()  # changed to stoppign listener first
                self.listener.stop()

    def digest(self):
        # print(f'digesting {self.buffer}')
        if self.buffer.__len__() == 0:
            return
        for k in self.modifiers:
            self.keyboard_controller.release(k)
        # todo: exception handling
        backtrack = self.buffer.__len__()
        out = ''.join(self.buffer)
        out = mush(out, single=True)
        self.keyboard_controller.press(Key.left)
        for i in range(backtrack):
            self.keyboard_controller.press(Key.backspace)
            self.keyboard_controller.release(Key.backspace)
        #self.keyboard_controller.type(''.join(out))
        for l in out:  # not letting shift bother us
            [self.keyboard_controller.release(key) for key in MODIFIERS]
            self.keyboard_controller.press(l)
            self.keyboard_controller.release(l)

        self.keyboard_controller.press(Key.right)
        #
        # if self.break_key is not None:
        #     self.keyboard_controller.press(self.break_key)
        #     self.keyboard_controller.release(self.break_key)
        #     self.break_key = None
        self.clear_buffer()

    def on_press(self, key):
        # self.break_key = key
        try:  # if the key is alphanumeric
            self.ingest(key.char)
        except AttributeError:  # for special keys:
            if key in [Key.space, Key.enter]:
                return False  # digest then restart
            # todo: refactor
            if key == Key.backspace:
                try:
                    self.buffer.pop()
                except IndexError:
                    pass  #if we've finished a word we do not return. for now.
            # not processing shift because inbound alphanumeric contains case.
            if key == self.exit_key:  #
                self.keepalive = False
                # self.digest()
                return False  # digest and quit
            if key in self.modifiers.keys():
                self.modifiers[key] = True

    def on_release(self, key):
        if key in self.modifiers.keys():
            self.modifiers[key] = False


if __name__ == '__main__':
    sm = StreamMusher(EXIT_KEY)
    sm.run()

