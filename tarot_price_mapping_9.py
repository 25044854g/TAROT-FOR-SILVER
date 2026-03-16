# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

# ==================== 塔罗牌价格特征映射 ====================

TAROT_PRICE_SEMANTICS = {
    # 大阿尔克那（22张）
    "YR": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.4, "strength": 0.5},  # 愚者
    "MS": {"direction": "bullish", "pattern": "breakout", "volatility": 0.5, "strength": 0.8},  # 魔术师
    "JS": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.6},  # 女祭司
    "NH": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.7},  # 皇后
    "HD": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.5, "strength": 0.8},  # 皇帝
    "JH": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.6},  # 教皇
    "LR": {"direction": "neutral", "pattern": "reversal", "volatility": 0.6, "strength": 0.7},  # 恋人
    "ZC": {"direction": "bullish", "pattern": "breakout", "volatility": 0.5, "strength": 0.85},  # 战车
    "LL": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.75},  # 力量
    "YS": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.2, "strength": 0.5},  # 隐者
    "MY": {"direction": "neutral", "pattern": "reversal", "volatility": 0.7, "strength": 0.6},  # 幸运之轮
    "ZY": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.4, "strength": 0.7},  # 正义
    "DJ": {"direction": "bearish", "pattern": "consolidation", "volatility": 0.5, "strength": 0.6},  # 吊人
    "SS": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.6, "strength": 0.85},  # 死神
    "JZ": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.4, "strength": 0.6},  # 节制
    "EM": {"direction": "volatile", "pattern": "zigzag", "volatility": 0.85, "strength": 0.8},  # 恶魔
    "GT": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.9, "strength": 0.95},  # 塔
    "XX": {"direction": "bullish", "pattern": "recovery", "volatility": 0.3, "strength": 0.8},  # 星星
    "YL": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.6, "strength": 0.7},  # 月亮
    "TY": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.9},  # 太阳
    "SP": {"direction": "bullish", "pattern": "reversal", "volatility": 0.5, "strength": 0.85},  # 审判
    "SJ": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.9},  # 世界

    # 小阿尔克那 - 权杖（Wands）
    "Q1": {"direction": "bullish", "pattern": "breakout", "volatility": 0.6, "strength": 0.7},
    "Q2": {"direction": "volatile", "pattern": "zigzag", "volatility": 0.7, "strength": 0.6},
    "Q3": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.5, "strength": 0.75},
    "Q4": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.5},
    "Q5": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.6, "strength": 0.7},
    "Q6": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.8},
    "Q7": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.5, "strength": 0.75},
    "Q8": {"direction": "bullish", "pattern": "breakout", "volatility": 0.6, "strength": 0.8},
    "Q9": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.85},
    "Q10": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.9},
    "QP": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.4, "strength": 0.5},
    "QN": {"direction": "bullish", "pattern": "breakout", "volatility": 0.5, "strength": 0.7},
    "QQ": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.8},
    "QK": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.85},

    # 小阿尔克那 - 圣杯（Cups）
    "S1": {"direction": "bullish", "pattern": "recovery", "volatility": 0.3, "strength": 0.8},
    "S2": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.2, "strength": 0.4},
    "S3": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.7},
    "S4": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.5},
    "S5": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.5, "strength": 0.6},
    "S6": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.2, "strength": 0.4},
    "S7": {"direction": "neutral", "pattern": "reversal", "volatility": 0.6, "strength": 0.6},
    "S8": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.4, "strength": 0.5},
    "S9": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.2, "strength": 0.75},
    "S10": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.85},
    "SP": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.5},
    "SN": {"direction": "neutral", "pattern": "reversal", "volatility": 0.5, "strength": 0.6},
    "SQ": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.8},
    "SK": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.2, "strength": 0.85},

    # 小阿尔克那 - 宝剑（Swords）
    "B1": {"direction": "bullish", "pattern": "breakout", "volatility": 0.6, "strength": 0.7},
    "B2": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.4, "strength": 0.5},
    "B3": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.7, "strength": 0.75},
    "B4": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.5, "strength": 0.6},
    "B5": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.6, "strength": 0.7},
    "B6": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.4, "strength": 0.6},
    "B7": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.5, "strength": 0.5},
    "B8": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.7, "strength": 0.8},
    "B9": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.8, "strength": 0.9},
    "B10": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.9, "strength": 0.95},
    "BP": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.4, "strength": 0.5},
    "BN": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.6, "strength": 0.7},
    "BQ": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.5, "strength": 0.75},
    "BK": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.4, "strength": 0.7},

    # 小阿尔克那 - 钱币（Pentacles）
    "J1": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.8},
    "J2": {"direction": "volatile", "pattern": "zigzag", "volatility": 0.7, "strength": 0.6},
    "J3": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.7},
    "J4": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.2, "strength": 0.5},
    "J5": {"direction": "bearish", "pattern": "downtrend", "volatility": 0.6, "strength": 0.7},
    "J6": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.5},
    "J7": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.5, "strength": 0.6},
    "J8": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.75},
    "J9": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.85},
    "J10": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.2, "strength": 0.9},
    "JP": {"direction": "neutral", "pattern": "consolidation", "volatility": 0.3, "strength": 0.5},
    "JN": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.4, "strength": 0.7},
    "JQ": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.3, "strength": 0.8},
    "JK": {"direction": "bullish", "pattern": "uptrend", "volatility": 0.2, "strength": 0.85},
}

# ==================== 时间段定义 ====================

TIME_SEGMENTS = {
    1: {"start": "6:00", "end": "8:20", "group": 1},
    2: {"start": "8:20", "end": "10:40", "group": 1},
    3: {"start": "10:40", "end": "16:00", "group": 1},
    4: {"start": "15:30", "end": "17:37", "group": 2},
    5: {"start": "17:37", "end": "19:45", "group": 2},
    6: {"start": "19:45", "end": "1:00", "group": 2},  # 次日1:00
    7: {"start": "21:30", "end": "22:58", "group": 3},
    8: {"start": "22:58", "end": "0:26", "group": 3},  # 次日0:26
    9: {"start": "0:26", "end": "5:00", "group": 3},   # 次日5:00
}

# ==================== 重叠时段定义 ====================

OVERLAP_SEGMENTS = [
    {"start": "15:30", "end": "16:00", "cards": (3, 4), "description": "牌3 + 牌4"},
    {"start": "21:30", "end": "22:00", "cards": (6, 7), "description": "牌6 + 牌7"},
    {"start": "23:30", "end": "1:00", "cards": (6, 8), "description": "牌6 + 牌8"},
]

# ==================== 核心函数 ====================

def get_card_meaning(card_code, orientation):
    """
    获取牌的含义
    
    参数：
        card_code: str，塔罗牌缩写编码 (如 'YR', 'Q6', 'SQ')
        orientation: int，0=正位，1=逆位
    
    返回：
        dict，牌的价格特征
    """
    if card_code not in TAROT_PRICE_SEMANTICS:
        raise ValueError(f"未知的牌编码: {card_code}")
    
    meaning = TAROT_PRICE_SEMANTICS[card_code].copy()
    
    # 逆位处理
    if orientation == 1:
        if meaning["direction"] == "bullish":
            meaning["direction"] = "bearish"
        elif meaning["direction"] == "bearish":
            meaning["direction"] = "bullish"
        # volatile 和 neutral 保持不变
        meaning["strength"] *= 0.7  # 逆位强度降低30%
    
    return meaning


def get_time_segment(position):
    """
    根据位置获取时间段
    
    参数：
        position: int，牌的位置 (1-9)
    
    返回：
        dict，时间段信息
    """
    if position < 1 or position > 9:
        raise ValueError("位置必须在1-9之间")
    
    return TIME_SEGMENTS[position]


def get_overlap_segments_for_card(position):
    """
    获取该牌涉及的重叠时段
    
    参数：
        position: int，牌的位置 (1-9)
    
    返回：
        list，所有包含该牌的重叠时段
    """
    overlaps = []
    for overlap in OVERLAP_SEGMENTS:
        if position in overlap["cards"]:
            overlaps.append(overlap)
    return overlaps


def merge_signals(signal1, signal2):
    """
    融合两个牌的信号
    
    参数：
        signal1: dict，第一个牌的信号
        signal2: dict���第二个牌的信号
    
    返回：
        dict，融合后的综合信号
    """
    # 方向融合逻辑
    direction_mapping = {
        ("bullish", "bullish"): "bullish",
        ("bearish", "bearish"): "bearish",
        ("bullish", "bearish"): "volatile",
        ("bearish", "bullish"): "volatile",
        ("bullish", "neutral"): "bullish",
        ("bearish", "neutral"): "bearish",
        ("neutral", "bullish"): "bullish",
        ("neutral", "bearish"): "bearish",
        ("neutral", "neutral"): "neutral",
        ("volatile", "volatile"): "volatile",
        ("bullish", "volatile"): "volatile",
        ("bearish", "volatile"): "volatile",
        ("volatile", "bullish"): "volatile",
        ("volatile", "bearish"): "volatile",
        ("volatile", "neutral"): "volatile",
        ("neutral", "volatile"): "volatile",
    }
    
    key = (signal1["direction"], signal2["direction"])
    merged_direction = direction_mapping.get(key, "neutral")
    
    # 其他属性平均值
    merged_volatility = (signal1["volatility"] + signal2["volatility"]) / 2
    merged_strength = (signal1["strength"] + signal2["strength"]) / 2
    
    # 模式融合
    merged_pattern = f"{signal1['pattern']} + {signal2['pattern']}"
    
    return {
        "direction": merged_direction,
        "pattern": merged_pattern,
        "volatility": merged_volatility,
        "strength": merged_strength,
    }


def calculate_confidence(signal):
    """
    计算信号的可信度
    
    参数：
        signal: dict，价格信号
    
    返回：
        float，可信度百分比 (0-100)
    """
    confidence = 50  # 基础50%
    
    # 方向明确加分
    if signal["direction"] in ["bullish", "bearish"]:
        confidence += 15
    elif signal["direction"] == "volatile":
        confidence -= 20
    
    # 强度加分
    confidence += signal["strength"] * 20
    
    # 波动性扣分
    confidence -= signal["volatility"] * 15
    
    # 确保在0-100之间
    return max(0, min(100, confidence))


def analyze_9_cards(cards):
    """
    分析9张牌的完整信号
    
    参数：
        cards: list of tuples，[(card_code, orientation), ...] 长度必须为9
    
    返回：
        dict，包含所有时间段和重叠段的分析结果
    """
    if len(cards) != 9:
        raise ValueError("必须输入9张牌")
    
    results = {
        "cards": cards,
        "segments": {},
        "overlaps": {}
    }
    
    # 分析每张牌的信号
    card_signals = []
    for i, (card_code, orientation) in enumerate(cards, 1):
        signal = get_card_meaning(card_code, orientation)
        time_segment = get_time_segment(i)
        confidence = calculate_confidence(signal)
        
        card_signals.append(signal)
        results["segments"][i] = {
            "card": card_code,
            "orientation": "正位" if orientation == 0 else "逆位",
            "time": f"{time_segment['start']} - {time_segment['end']}",
            "signal": signal,
            "confidence": confidence
        }
    
    # 分析重叠时段
    for overlap in OVERLAP_SEGMENTS:
        pos1, pos2 = overlap["cards"]
        merged = merge_signals(card_signals[pos1-1], card_signals[pos2-1])
        confidence = calculate_confidence(merged)
        
        results["overlaps"][overlap["description"]] = {
            "time": f"{overlap['start']} - {overlap['end']}",
            "cards": (cards[pos1-1], cards[pos2-1]),
            "merged_signal": merged,
            "confidence": confidence
        }
    
    return results


# ==================== 示例 ====================

if __name__ == "__main__":
    # 示例：输入9张牌
    cards_9 = [
        ("TY", 0),   # 牌1：太阳正位
        ("XX", 0),   # 牌2：星星正位
        ("LL", 0),   # 牌3：力量正位
        ("MS", 0),   # 牌4：魔术师正位
        ("SJ", 0),   # 牌5：世界正位
        ("SP", 1),   # 牌6：审判逆位
        ("YR", 1),   # 牌7：愚者逆位
        ("MY", 1),   # 牌8：幸运之轮逆位
        ("S10", 0),  # 牌9：圣杯10正位
    ]
    
    results = analyze_9_cards(cards_9)
    
    print("=" * 60)
    print("塔罗9张牌分析结果")
    print("=" * 60)
    
    # 打印每张牌的分析
    print("\n【各时间段信号】")
    for pos, segment_info in results["segments"].items():
        print(f"\n牌{pos}: {segment_info['card']} ({segment_info['orientation']})")
        print(f"  时间段: {segment_info['time']}")
        print(f"  方向: {segment_info['signal']['direction']}")
        print(f"  模式: {segment_info['signal']['pattern']}")
        print(f"  波动: {segment_info['signal']['volatility']:.2f}")
        print(f"  强度: {segment_info['signal']['strength']:.2f}")
        print(f"  可信度: {segment_info['confidence']:.1f}%")
    
    # 打印重叠时段的融合信号
    print("\n\n【重叠时段融合信号】")
    for overlap_name, overlap_info in results["overlaps"].items():
        print(f"\n{overlap_name}")
        print(f"  时间段: {overlap_info['time']}")
        print(f"  融合方向: {overlap_info['merged_signal']['direction']}")
        print(f"  融合模式: {overlap_info['merged_signal']['pattern']}")
        print(f"  融合波动: {overlap_info['merged_signal']['volatility']:.2f}")
        print(f"  融合强度: {overlap_info['merged_signal']['strength']:.2f}")
        print(f"  融合可信度: {overlap_info['confidence']:.1f}%")
    
    print("\n" + "=" * 60)