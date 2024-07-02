"""
键盘监听程序
"""
import logging
import time
from datetime import datetime
import keyboard
import pyperclip

# 获取当前时间，并格式化为字符串
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 配置日志记录
logging.basicConfig(
    filename=f"logs/{current_time}.log",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

# 监听快捷键 ctrl + win + a，并执行回调函数
def consolidate_responses():
    """
    当快捷键 ctrl + win + a 被按下时执行的回调函数
    """
    logging.info("热键 ctrl + win + a 被按下")
    print("热键 ctrl + win + a 被按下")

    # 从剪贴板中获取所有文本保存到question_input变量中
    # 从剪贴板中获取所有文本保存到question_input变量中
    question_input = pyperclip.paste()
    logging.info("从剪贴板中获取文字: %s", question_input)
    print(f"从剪贴板中获取文字: {question_input}")

    text0 = """
    给定三份关于同一主题的文本,每份文本都可能包含一些事实错误或表述不清的地方。
    请仔细阅读这三份文本,通过交叉对比和验证信息,识别出最准确的内容。然后,使用简洁、
    严谨而又流畅的语言,将这些内容整合成一份全面、准确、逻辑清晰的文本。在整合过程中,
    请注意以下几点:
    1. 消除事实性错误,确保最终文本中的每一个信息都是正确的。
    2. 去除冗余和重复的内容,使文本更加简洁，但也要有一定的细节。
    3. 调整语言表述,使文本更加正式和专业。
    4. 优化文本结构,确保信息的逻辑流畅,易于理解。
    5. 尽可能保留原文中的关键信息和观点,不要过度改变原意。
    6. 请提供综合后的文本,并解释你在整合过程中所做的主要改动。

    问题：
    """

    # text0 = """
    # 下面是三个根据大纲生成的对的问题，每个回答都有各自的不合适的地方，可能是过多偏向某个领域，
    # 不够均衡，可能问题的针对性不够。请综合三份问题清单，整合出一份更加合适的包含十个问题的
    # 问题清单，使得问题更加均衡有针对性。
    # """

    ask_once(question_input, "https://poe.com/Assistant")


def wait_for_keys_release(keys):
    "等待所有按键是否都已经松开"
    while any(keyboard.is_pressed(key) for key in keys):
        logging.info('等待所有按键被释放')
        time.sleep(0.1)

def press_keys_with_logging(keys, log_message, delay=0):
    "按下按键并记录日志"
    keyboard.press_and_release(keys)
    logging.info(log_message)
    if delay > 0:
        time.sleep(delay)

def copy_to_clipboard(text, log_message):
    "将文本复制到剪贴板并记录日志"
    pyperclip.copy(text)
    logging.info(log_message)

def ask_once(text, link):
    """
    模拟按键操作函数
    :param text: 提问的文本
    :param link: 链接
    """
    logging.info("函数 ask_once 被执行")

    wait_for_keys_release(keyboard.all_modifiers)

    press_keys_with_logging('ctrl+l', '按下 Ctrl+L', delay=1)

    copy_to_clipboard(link, '复制链接到剪贴板')
    press_keys_with_logging('ctrl+v', '从剪贴板中粘贴链接')
    press_keys_with_logging('enter', '按下回车', delay=3)

    press_keys_with_logging('tab', '按下 Tab')
    press_keys_with_logging('shift+tab', '按下 Shift+Tab', delay=1)

    copy_to_clipboard(text, '将问题文本复制到剪贴板')
    press_keys_with_logging('ctrl+v', '从剪贴板中粘贴问题文本', delay=1)

    for _ in range(3):
        press_keys_with_logging('tab', '按下 Tab', delay=0.1)

    press_keys_with_logging('enter', '按下回车', delay=60)


# 监听快捷键 ctrl + win + a，并执行回调函数
keyboard.add_hotkey("ctrl+win+a", consolidate_responses)

# 保持程序运行
print("键盘监听已启动。按下 ESC 键退出。")
keyboard.wait("esc")
print("程序已退出。")
