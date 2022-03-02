import win32clipboard
from musher import mush

win32clipboard.OpenClipboard()
cdata = win32clipboard.GetClipboardData()#.encode('utf-8')
cdata = mush(cdata)
win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT, cdata)
win32clipboard.CloseClipboard()

