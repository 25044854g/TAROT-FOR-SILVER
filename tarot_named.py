# -*- coding: utf-8 -*-

# 大阿尔克那（22 张）
MAJOR_ARCANA = {
    "YR": "The Fool",
    "MS": "The Magician",
    "JS": "The High Priestess",  # 女祭司
    "NH": "The Empress",
    "HD": "The Emperor",
    "JH": "The Hierophant",
    "LR": "The Lovers",
    "ZC": "The Chariot",
    "LL": "Strength",
    "YS": "The Hermit",          # 隐者
    "MY": "Wheel of Fortune",
    "ZY": "Justice",
    "DJ": "The Hanged Man",
    "SS": "Death",               # 死神
    "JZ": "Temperance",
    "EM": "The Devil",
    "GT": "The Tower",
    "XX": "The Star",
    "YL": "The Moon",
    "TY": "The Sun",
    "SP": "Judgement",
    "SJ": "The World"
}

# 小阿尔克那（56 张）
MINOR_ARCANA = {
    # 权杖 Wands
    **{f"Q{i}": f"Wands {i}" for i in range(1, 11)},
    "QP": "Page of Wands",
    "QN": "Knight of Wands",
    "QQ": "Queen of Wands",
    "QK": "King of Wands",

    # 圣杯 Cups
    **{f"C{i}": f"Cups {i}" for i in range(1, 10+1)},
    "CP": "Page of Cups",
    "CN": "Knight of Cups",
    "CQ": "Queen of Cups",
    "CK": "King of Cups",

    # 宝剑 Swords
    **{f"J{i}": f"Swords {i}" for i in range(1, 10+1)},
    "JP": "Page of Swords",
    "JN": "Knight of Swords",
    "JQ": "Queen of Swords",
    "JK": "King of Swords",

    # 星币 Pentacles
    **{f"B{i}": f"Pentacles {i}" for i in range(1, 10+1)},
    "BP": "Page of Pentacles",
    "BN": "Knight of Pentacles",
    "BQ": "Queen of Pentacles",
    "BK": "King of Pentacles"
}


# 合并所有牌
tarot_cards = {**MAJOR_ARCANA, **MINOR_ARCANA}

ORIENTATION_UPRIGHT = 1
ORIENTATION_REVERSED = 0

ORIENTATION_NAMES = {
    ORIENTATION_UPRIGHT: "Upright",
    ORIENTATION_REVERSED: "Reversed",
}


def get_card_name(card_code):
    if card_code not in tarot_cards:
        raise ValueError(f"未知的牌编码: {card_code}")
    return tarot_cards[card_code]


def get_card_display_name(card_code, orientation=None):
    card_name = get_card_name(card_code)
    if orientation is None:
        return f"{card_code} {card_name}"

    if orientation not in ORIENTATION_NAMES:
        raise ValueError(f"未知的正逆位编码: {orientation}")

    return f"{card_code} {card_name} ({ORIENTATION_NAMES[orientation]})"

def encode_card(card_code, orientation):
    """
    card_code: str, 塔罗牌缩写编码 (如 'YR', 'Q6', 'CQ')
    orientation: int, 1=正位, 0=逆位
    return: list [card_code, orientation]
    """
    if card_code not in tarot_cards:
        raise ValueError(f"未知的牌编码: {card_code}")
    if orientation not in ORIENTATION_NAMES:
        raise ValueError(f"未知的正逆位编码: {orientation}")
    return [card_code, orientation]
