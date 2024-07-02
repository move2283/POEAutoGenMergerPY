"""
键盘监听程序
"""
import logging
import keyboard

# 配置日志记录
logging.basicConfig(
    filename="logs/key_log.log", level=logging.DEBUG, format="%(asctime)s: %(message)s"
)

# 监听快捷键 ctrl + win + a，并执行回调函数
def consolidate_responses():
    """
    当快捷键 ctrl + win + a 被按下时执行的回调函数
    """
    logging.info("Hotkey ctrl + win + a was pressed")
    print("Hotkey ctrl + win + a was pressed")

# 监听快捷键 ctrl + win + a，并执行回调函数
keyboard.add_hotkey("ctrl+win+a", consolidate_responses)

# 保持程序运行
print("键盘监听已启动。按下 ESC 键退出。")
keyboard.wait("esc")
print("程序已退出。")
