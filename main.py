import webview
from screeninfo import get_monitors

class Browser(object):
    url = "https://www.facebook.com/"

    def manage(self, window):
        print(window)

    def __init__(self):
        mon = get_monitors()[0]
        window = webview.create_window('', self.url, width=mon.width, height=mon.height)
        webview.start(self.manage, window, gui='cef')

if __name__ == '__main__':
    browser = Browser()