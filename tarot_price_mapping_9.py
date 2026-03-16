# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import random
from tarot_price_profiles import TAROT_CARD_PROFILES, TAROT_PRICE_SEMANTICS
from tarot_named import tarot_cards

# ==================== 统一表示方案 ====================

ORIENTATION_UPRIGHT = 1
ORIENTATION_REVERSED = 0

ORIENTATION_LABELS = {
    ORIENTATION_UPRIGHT: "正位",
    ORIENTATION_REVERSED: "逆位",
}


def normalize_orientation(orientation):
    """
    统一正逆位表示：1=正位，0=逆位。
    """
    if orientation not in (ORIENTATION_UPRIGHT, ORIENTATION_REVERSED):
        raise ValueError("orientation 必须是 1(正位) 或 0(逆位)")
    return orientation



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
        card_code: str，塔罗牌缩写编码 (如 'YR', 'Q6', 'CQ')
        orientation: int，1=正位，0=逆位
    
    返回：
        dict，牌的价格特征
    """
    if card_code not in tarot_cards or card_code not in TAROT_PRICE_SEMANTICS:
        raise ValueError(f"未知的牌编码: {card_code}")

    normalize_orientation(orientation)
    profile_key = "upright" if orientation == ORIENTATION_UPRIGHT else "reversed"
    return TAROT_CARD_PROFILES[card_code][profile_key].copy()


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
    merged_direction_score = (signal1["direction_score"] + signal2["direction_score"]) / 2
    if merged_direction_score > 0.2:
        merged_direction = "bullish"
    elif merged_direction_score < -0.2:
        merged_direction = "bearish"
    else:
        merged_direction = "neutral"

    merged_volatility = (signal1["volatility"] + signal2["volatility"]) / 2
    merged_strength = (signal1["strength"] + signal2["strength"]) / 2
    merged_persistence = (signal1["persistence"] + signal2["persistence"]) / 2
    
    merged_pattern = f"{signal1['pattern']} + {signal2['pattern']}"
    
    return {
        "direction_label": f"{signal1['direction_label']} + {signal2['direction_label']}",
        "direction": merged_direction,
        "pattern": merged_pattern,
        "direction_score": merged_direction_score,
        "strength_label": "中",
        "volatility": merged_volatility,
        "volatility_label": "中",
        "strength": merged_strength,
        "persistence": merged_persistence,
        "persistence_label": "中",
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
    elif signal["direction"] == "neutral":
        confidence -= 5
    
    # 强度加分
    confidence += signal["strength"] * 20

    # 持续性加分
    confidence += signal.get("persistence", 0.5) * 15
    
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
            "orientation": ORIENTATION_LABELS[normalize_orientation(orientation)],
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


def generate_9_card_price_trend(start_price, cards, hours=23):
    """
    根据9张塔罗牌生成价格趋势。

    参数：
        start_price: float，起始价格
        cards: list[tuple[str, int]]，9张牌 [(card_code, orientation), ...]
        hours: int，默认从 06:00 到次日 05:00，共 23 小时
    """
    if len(cards) != 9:
        raise ValueError("9张模型必须输入9张牌")

    total_strength = 0
    total_volatility = 0
    total_persistence = 0
    total_direction_score = 0

    for card_code, orientation in cards:
        semantics = get_card_meaning(card_code, orientation)
        total_strength += semantics["strength"]
        total_volatility += semantics["volatility"]
        total_persistence += semantics["persistence"]
        total_direction_score += semantics["direction_score"]

    avg_strength = total_strength / len(cards)
    avg_volatility = total_volatility / len(cards)
    avg_persistence = total_persistence / len(cards)
    avg_direction_score = total_direction_score / len(cards)

    if avg_direction_score > 0.2:
        overall_direction = "Bullish Trend"
    elif avg_direction_score < -0.2:
        overall_direction = "Bearish Trend"
    else:
        overall_direction = "Consolidation"

    current_time = datetime.now().replace(hour=6, minute=0, second=0, microsecond=0)
    current_price = start_price
    timestamps = []
    prices = []

    for i in range(hours + 1):
        timestamps.append(current_time + timedelta(hours=i))
        prices.append(current_price)

        if i < hours:
            trend_progress = 0.35 + avg_persistence * (i / hours)
            price_change_percent = avg_direction_score * avg_strength * trend_progress * 8
            volatility_factor = 1 + random.uniform(-avg_volatility, avg_volatility) * 0.08
            current_price = current_price * (1 + price_change_percent / 100) * volatility_factor

    final_price = prices[-1]
    price_change = final_price - start_price
    change_percent = (price_change / start_price) * 100

    return {
        "model": "9-card",
        "cards": list(cards),
        "start_price": start_price,
        "final_price": final_price,
        "change": price_change,
        "change_percent": change_percent,
        "direction": overall_direction,
        "avg_strength": avg_strength,
        "avg_volatility": avg_volatility,
        "avg_persistence": avg_persistence,
        "avg_direction_score": avg_direction_score,
        "timestamps": timestamps,
        "prices": prices,
    }


# ==================== 示例 ====================

if __name__ == "__main__":
    # 示例：输入9张牌
    cards_9 = [
        ("TY", 1),   # 牌1：太阳正位
        ("XX", 1),   # 牌2：星星正位
        ("LL", 1),   # 牌3：力量正位
        ("MS", 1),   # 牌4：魔术师正位
        ("SJ", 1),   # 牌5：世界正位
        ("SP", 0),   # 牌6：审判逆位
        ("YR", 0),   # 牌7：愚者逆位
        ("MY", 0),   # 牌8：幸运之轮逆位
        ("C10", 1),  # 牌9：圣杯10正位
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