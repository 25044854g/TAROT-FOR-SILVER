# -*- coding: utf-8 -*-

# 假设 tarot_cards 字典已在其他模块定义并导入
from tarot_dict import tarot_cards

def encode_card(card_code, orientation):
    """
    单张牌编码
    card_code: str, 塔罗牌缩写编码 (如 'YR', 'Q6', 'SQ')
    orientation: int, 0=正位, 1=逆位
    return: list [card_code, orientation]
    """
    if card_code not in tarot_cards:
        raise ValueError(f"未知的牌编码: {card_code}")
    return [card_code, orientation]

def encode_batch_9(cards):
    """
    批量处理9张牌
    cards: list of tuples [(card_code, orientation), ...] 长度必须为9
    return: list of lists [[card_code, orientation], ...]
    """
    if len(cards) != 9:
        raise ValueError("必须输入9张牌")
    return [encode_card(code, orient) for code, orient in cards]

# 示例
if __name__ == "__main__":
    cards_9 = [
        ("YR", 0), ("MS", 1), ("Q6", 0),
        ("SQ", 1), ("SS", 0), ("B3", 1),
        ("J1", 0), ("QQ", 0), ("SK", 1)
    ]
    print(encode_batch_9(cards_9))
