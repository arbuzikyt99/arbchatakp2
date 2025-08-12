from kivy.app import App
from kivy.lang import Builder
from kivy.clock import mainthread
from kivy.uix.boxlayout import BoxLayout
from threading import Thread
import time

from bluetooth_service import BluetoothService

KV = """
BoxLayout:
    orientation: 'vertical'
    padding: dp(8)
    spacing: dp(8)

    Label:
        text: 'Arbchat'
        size_hint_y: None
        height: dp(48)

    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
        BoxLayout:
            id: msgs
            orientation: 'vertical'
            size_hint_y: None
            height: self.minimum_height

    BoxLayout:
        size_hint_y: None
        height: dp(48)
        spacing: dp(8)
        TextInput:
            id: message_input
            multiline: False
        Button:
            text: 'Send'
            size_hint_x: None
            width: dp(100)
            on_release: app.root.on_send()
        Button:
            text: 'Scan/Connect'
            size_hint_x: None
            width: dp(120)
            on_release: app.root.on_scan_connect()
        Button:
            text: 'Disconnect'
            size_hint_x: None
            width: dp(100)
            on_release: app.root.disconnect()
"""

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_string(KV)
        self.bt = BluetoothService(on_receive=self.on_receive, on_status=self.on_status)
        self.bt.start_receiving()

    @mainthread
    def display_message(self, text):
        from kivy.uix.label import Label
        lbl = Label(text=text, size_hint_y=None, height=dp(30), halign='left', valign='middle', text_size=(self.width, None))
        self.ids.msgs.add_widget(lbl)

    def on_receive(self, text):
        self.display_message("Remote: " + text)

    def on_status(self, status):
        self.display_message("[status] " + status)

    def on_send(self):
        txt = self.ids.message_input.text.strip()
        if not txt:
            return
        self.display_message("Me: " + txt)
        Thread(target=self.bt.send, args=(txt,), daemon=True).start()
        self.ids.message_input.text = ''

    def on_scan_connect(self):
        Thread(target=self.bt.scan_and_connect, daemon=True).start()

    def disconnect(self):
        self.bt.disconnect()

class ArbchatApp(App):
    def build(self):
        return MainUI()

if __name__ == '__main__':
    ArbchatApp().run()