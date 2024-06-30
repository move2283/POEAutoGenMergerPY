"""
键盘监听程序
"""
import logging
import keyboard

# 配置日志记录
logging.basicConfig(
    filename="logs/key_log.log", level=logging.DEBUG, format="%(asctime)s: %(message)s"
)


def on_key_event(event):
    """
    键盘事件回调函数
    """
    # 记录按键事件
    logging.info("Key %s was %s", event.name, event.event_type)

# 启动键盘监听
keyboard.hook(on_key_event)

# 保持程序运行
print("键盘监听已启动。按下 ESC 键退出。")
keyboard.wait("esc")
print("程序已退出。")
