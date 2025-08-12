"""
Simplified Bluetooth service — simulation only.

This keeps the app simple so it builds in Colab without extra native recipes.
"""
import threading, time

class BluetoothService:
    def __init__(self, on_receive=None, on_status=None):
        self.on_receive = on_receive or (lambda msg: None)
        self.on_status = on_status or (lambda s: None)
        self._running = False
        self._connected = False
        self.on_status("Bluetooth service: simulation mode")

    def scan_and_connect(self):
        self.on_status("Scanning (simulated)...")
        time.sleep(1)
        self._connected = True
        self.on_status("Connected (simulated)")

    def start_receiving(self):
        if self._running:
            return
        self._running = True
        t = threading.Thread(target=self._loop, daemon=True)
        t.start()

    def _loop(self):
        while self._running:
            time.sleep(5)
            if self._connected:
                self.on_receive("simulated reply at " + time.strftime("%H:%M:%S"))

    def send(self, text):
        # echo back after delay
        time.sleep(0.3)
        self.on_receive(text + " (echo)")

    def disconnect(self):
        self._running = False
        self._connected = False
        self.on_status("Disconnected (simulated)")