# 大阿尔克那（22 张）
major_arcana = {
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
minor_arcana = {
    # 权杖 Wands
    **{f"Q{i}": f"Wands {i}" for i in range(1, 11)},
    "QP": "Page of Wands",
    "QN": "Knight of Wands",
    "QQ": "Queen of Wands",
    "QK": "King of Wands",

    # 圣杯 Cups
    **{f"S{i}": f"Cups {i}" for i in range(1, 10+1)},
    "SP": "Page of Cups",
    "SN": "Knight of Cups",
    "SQ": "Queen of Cups",
    "SK": "King of Cups",

    # 宝剑 Swords
    **{f"B{i}": f"Swords {i}" for i in range(1, 10+1)},
    "BP": "Page of Swords",
    "BN": "Knight of Swords",
    "BQ": "Queen of Swords",
    "BK": "King of Swords",

    # 钱币 Pentacles
    **{f"J{i}": f"Pentacles {i}" for i in range(1, 10+1)},
    "JP": "Page of Pentacles",
    "JN": "Knight of Pentacles",
    "JQ": "Queen of Pentacles",
    "JK": "King of Pentacles"
}

# 合并所有牌
tarot_cards = {**major_arcana, **minor_arcana}

def encode_card(card_code, orientation):
    """
    card_code: str, 塔罗牌缩写编码 (如 'YR', 'Q6', 'SQ')
    orientation: int, 0=正位, 1=逆位
    return: list [card_code, orientation]
    """
    if card_code not in tarot_cards:
        raise ValueError(f"未知的牌编码: {card_code}")
    return [card_code, orientation]

# 示例
print(encode_card("YR", 0))   # ['YR', 0] 愚者正位
print(encode_card("SS", 1))   # ['SS', 1] 死神逆位
print(encode_card("Q6", 0))   # ['Q6', 0] 权杖6正位
print(encode_card("SQ", 1))   # ['SQ', 1] 圣杯皇后逆位
