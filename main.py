import time
from aliengripperapi import AlienGripper
import sys
import signal

flag = True

def task(alien: AlienGripper):
    while flag:
        alien.hold()
        time.sleep(0.01)
        alien.release()
        time.sleep(0.01)
        alien.disable()
        time.sleep(0.01)
        data = alien.getData()
        print(f"id: {data['id']}, Sensors: {data['sensors']}")

def handle_exit(sig, frame):
    print("กำลังปิดโปรแกรม...")
    alien.disable()
    flag = False
    alien.stop()
    print("โปรแกรมถูกปิดเรียบร้อย")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)

if __name__ == "__main__":
    alien = AlienGripper("192.168.83.184", "81", "ws")
    task(alien)

