import sys
from typing import List

from appdirs import AppDirs


def markup(text: str, style: str) -> str:
    ansi_codes = {"bold": "\033[1m", "red": "\033[31m", "green": "\033[32m",
                  "cyan": "\033[36m", "magenta": "\033[35m"}
    return ansi_codes[style] + text + "\033[0m"


def pre(text: str) -> str:
    if "```" in text:
        print(markup("Sending a message containing ``` is not supported with --pre.", "red"))
        sys.exit(1)
    return "```text\n" + text + "```"


def split_message(message: str, max_length: int) -> List[str]:
    """Split large message into smaller messages each smaller than the max_length."""
    ms = []
    while len(message) > max_length:
        ms.append(message[:max_length])
        message = message[max_length:]
    ms.append(message)
    return ms


def get_config_path():
    return AppDirs("telegram-send").user_config_dir + ".conf"
