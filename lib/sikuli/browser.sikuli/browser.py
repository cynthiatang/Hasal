from sikuli import *


class GeneralBrowser():
    def __init__(self):
        self.os = str(Settings.getOS())
        self.os_version = str(Settings.getOSVersion())

        if self.os.startswith("M"):
            self.control = Key.CMD
        else:
            self.control = Key.CTRL

    def enterLink(self, link):
        type(link)
        type(Key.ENTER)


class Chrome(GeneralBrowser):
    def __init__(self):
        GeneralBrowser.__init__(self)
        self._chrome = App("Chrome")

    # Need further permission in Mac OS X and might not be available in windows
    def launchBrowser(self):
        if self._chrome.isRunning():
            self._chrome.close()
        self._chrome.open()

    # Focus on launched Chrome Browser
    def focus(self):
        self._chrome.focus()

    # Wait for URL bar to appear
    def clickBar(self):
        wait(Pattern("pics/chrome_urlbar.png").similar(0.70))
        click(Pattern("pics/chrome_urlbar.png").similar(0.70).targetOffset(-40, 0))

    # Launch or close web console for developer
    def triggerConsole(self):
        if self.os.startswith("M"):
            type("j", self.control + Key.ALT)
        else:
            type("j", self.control + Key.SHIFT)

    # Get information from web console, e.g. info = "window.performance.timing"
    def getConsoleInfo(self, info):
        self.triggerConsole()
        wait(Pattern("pics/chrome_webconsole_arrow.png").similar(0.85).targetOffset(14,1))
        click(Pattern("pics/chrome_webconsole_arrow.png").similar(0.85).targetOffset(14,1))
        type("copy(" + info + ")")
        type(Key.ENTER)
        self.triggerConsole()
        return Env.getClipboard().strip()

    # Prevent cursor twinkling on screen
    def switchToContentWindow(self):
        type(Key.TAB)


class Firefox(GeneralBrowser):
    def __init__(self):
        GeneralBrowser.__init__(self)
        self._ff = App("Firefox")

    # Need further permission in Mac OS X and might not be available in windows
    # Might not working for Firefox (need alternative launch)
    def launchBrowser(self):
        if self._ff.isRunning():
            self._ff.close()
        self._ff.open()

    # Focus on launched Firefox Browser
    def focus(self):
        self._ff.focus()

    # Wait for URL bar to appear
    def clickBar(self):
        wait(Pattern("pics/ff_urlbar.png").similar(0.70))
        click(Pattern("pics/ff_urlbar.png").similar(0.70).targetOffset(-100, 0))

    # Launch web console for developer
    def triggerConsole(self):
        type("k", self.control + Key.SHIFT)

    def closeConsole(self):
        type(Key.F12)

    # Get information from web console, e.g. info = "window.performance.timing"
    def getConsoleInfo(self, info):
        self.triggerConsole()
        wait(Pattern("pics/ff_webconsole_arrow.png").similar(0.85).targetOffset(14,1))
        click(Pattern("pics/ff_webconsole_arrow.png").similar(0.85).targetOffset(14,1))
        type("copy(" + info + ")")
        type(Key.ENTER)
        self.closeConsole()
        return Env.getClipboard().strip()

    # Prevent cursor twinkling on screen
    def switchToContentWindow(self):
        type(Key.TAB)
        wait(3)
        type(Key.TAB)
