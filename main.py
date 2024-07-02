"""
键盘监听程序
"""
import logging
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
    logging.info("Hotkey ctrl + win + a was pressed")
    print("Hotkey ctrl + win + a was pressed")

    # 从剪贴板中获取所有文本保存到question_input变量中
    # 从剪贴板中获取所有文本保存到question_input变量中
    question_input = pyperclip.paste()
    logging.info("Text from clipboard: %s", question_input)
    print(f"Text from clipboard: {question_input}")

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


# 监听快捷键 ctrl + win + a，并执行回调函数
keyboard.add_hotkey("ctrl+win+a", consolidate_responses)

# 保持程序运行
print("键盘监听已启动。按下 ESC 键退出。")
keyboard.wait("esc")
print("程序已退出。")
