"""
键盘监听程序
"""

import logging
import os
import time
from datetime import datetime

import keyboard
import pyperclip

# 获取当前时间，并格式化为字符串
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 创建logs文件夹（如果不存在）
os.makedirs("logs", exist_ok=True)

# 配置日志记录
logging.basicConfig(
    filename=f"logs/{current_time}.log",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)


def consolidate_responses_knowledge():
    """
    当快捷键 ctrl + win + a 被按下时执行的回调函数
    """
    logging.info("热键 ctrl + win + a 被按下")
    print("热键 ctrl + win + a 被按下")

    # 从剪贴板中获取所有文本保存到question_input变量中
    question_input = pyperclip.paste()
    logging.info("从剪贴板中获取文字: %s", question_input)
    print(f"从剪贴板中获取文字: {question_input}")

    text0 = """
    下面是三份关于同一主题的文本,每份文本都可能包含一些事实错误或表述不清的地方。
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

    multi_query_handler(question_input, text0, 60)


def consolidate_responses_question():
    """
    当快捷键 ctrl + win + b 被按下时执行的回调函数
    """
    logging.info("热键 ctrl + win + b 被按下")
    print("热键 ctrl + win + b 被按下")

    # 从剪贴板中获取所有文本保存到question_input变量中
    question_input = pyperclip.paste()
    logging.info("从剪贴板中获取文字: %s", question_input)
    print(f"从剪贴板中获取文字: {question_input}")

    text0 = """
    下面是三个根据大纲生成的对的问题，每个回答都有各自的不合适的地方，可能是过多偏向某个领域，
    不够均衡，可能问题的针对性不够。请综合三份问题清单，整合出一份更加合适的包含十个问题的
    问题清单，使得问题更加均衡有针对性。
    """

    multi_query_handler(question_input, text0, 60)


def consolidate_responses_fast():
    """
    当快捷键 ctrl + win + c 被按下时执行的回调函数
    """
    logging.info("热键 ctrl + win + c 被按下")
    print("热键 ctrl + win + c 被按下")

    # 从剪贴板中获取所有文本保存到question_input变量中
    question_input = pyperclip.paste()
    logging.info("从剪贴板中获取文字: %s", question_input)
    print(f"从剪贴板中获取文字: {question_input}")

    text0 = """
    下面是两份关于同一主题的文本,每份文本都可能包含一些事实错误或表述不清的地方。
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

    multi_query_handler_fast(question_input, text0, 25)


def multi_query_handler(question_input, text0, wait_time):
    """
    执行多次提问并获取生成的文本
    """
    ask_once(question_input, "https://poe.com/GPT-4-Turbo", wait_time)
    text_1 = get_text()
    ask_once(question_input, "https://poe.com/GPT-4-Turbo", wait_time)
    text_2 = get_text()
    ask_once(question_input, "https://poe.com/Claude-3-Opus", wait_time)
    text_3 = get_text()

    final_question = (
        text0
        + "\n"
        + question_input
        + "\n 回答1 \n"
        + text_1
        + "\n 回答2 \n"
        + text_2
        + "\n 回答3 \n"
        + text_3
    )

    ask_once(final_question, "https://poe.com/Claude-3-Opus", wait_time)


def multi_query_handler_fast(question_input, text0, wait_time):
    """
    执行多次提问并获取生成的文本
    """
    ask_once(question_input, "https://poe.com/GPT-4o", wait_time)
    text_1 = get_text()
    ask_once(question_input, "https://poe.com/GPT-4-Turbo", 60)
    text_2 = get_text()
    final_question = (
        text0 + "\n" + question_input + "\n 回答1 \n" + text_1 + "\n 回答2 \n" + text_2
    )

    ask_once(final_question, "https://poe.com/GPT-4o", wait_time)


def wait_for_keys_release(keys):
    "等待所有按键是否都已经松开"
    # while any(keyboard.is_pressed(key) for key in keys):
    #     logging.info("等待所有按键被释放")
    #     time.sleep(0.1)
    time.sleep(1)


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


def ask_once(text, link, wait_time):
    """
    模拟按键操作函数
    :param text: 提问的文本
    :param link: 链接
    """
    logging.info("函数 ask_once 被执行")
    print("开始提问")

    wait_for_keys_release(keyboard.all_modifiers)

    press_keys_with_logging("ctrl+l", "按下 Ctrl+L", delay=1)

    copy_to_clipboard(link, "复制链接到剪贴板")
    press_keys_with_logging("ctrl+v", "从剪贴板中粘贴链接", delay=0.1)
    press_keys_with_logging("enter", "按下回车", delay=3)

    press_keys_with_logging("tab", "按下 Tab")
    press_keys_with_logging("shift+tab", "按下 Shift+Tab", delay=1)

    copy_to_clipboard(text, "将问题文本复制到剪贴板")
    press_keys_with_logging("ctrl+v", "从剪贴板中粘贴问题文本", delay=1)

    for _ in range(3):
        press_keys_with_logging("tab", "按下 Tab", delay=0.1)

    print("等待生成中...")
    press_keys_with_logging("enter", "按下回车", delay=wait_time)
    print("等待结束。")


def get_text():
    """
    获取生成的文本
    """
    press_keys_with_logging("shift+tab", "按下 Shift+Tab", delay=1)
    press_keys_with_logging("ctrl+a", "全选", delay=1)
    press_keys_with_logging("ctrl+c", "复制生成的全部内容", delay=1)
    str_origin = pyperclip.paste()
    logging.info("复制文本：\n%s", str_origin)

    char_start_flag_1 = "\nPoe"
    char_end_flag = "\n分享"
    pos_start_flag_1 = str_origin.rfind(char_start_flag_1) + len(char_start_flag_1)
    logging.info(
        "char_start_flag_1 '%s' 最后一次出现的位置: %s",
        char_start_flag_1,
        pos_start_flag_1,
    )

    pos_end_flag = str_origin.rfind(char_end_flag)
    logging.info(
        "char_end_flag '%s' 最后一次出现的位置: %s", char_end_flag, pos_end_flag
    )

    extracted_text = str_origin[pos_start_flag_1:pos_end_flag]
    logging.info("提取的文本: %s", extracted_text)
    print(f"获取到文本：\n{extracted_text}")

    return extracted_text


# 监听快捷键 ctrl + win + a，并执行回调函数
keyboard.add_hotkey("shift+alt+a", consolidate_responses_knowledge)

# 生成问题
keyboard.add_hotkey("shift+alt+b", consolidate_responses_question)

# 使用 gpt-4o 快速提问
keyboard.add_hotkey("shift+alt+c", consolidate_responses_fast)


# 保持程序运行
print("键盘监听已启动。按下 ESC 键退出。")
keyboard.wait("esc")
print("程序已退出。")
