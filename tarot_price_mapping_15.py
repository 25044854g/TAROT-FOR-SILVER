# -*- coding: utf-8 -*-

import random
from datetime import datetime, timedelta
from tarot_price_mapping_9 import get_card_meaning


def generate_15_card_price_trend(start_price, trend_cards, amplitude_cards, hours=23):
    """
    根据15张塔罗牌生成价格趋势。

    参数：
        start_price: float，起始价格
        trend_cards: list[tuple[str, int]]，12张趋势塔罗
        amplitude_cards: list[tuple[str, int]]，3张幅度塔罗
        hours: int，默认从06:00到次日05:00
    """
    if len(trend_cards) != 12:
        raise ValueError("15张模型中的趋势塔罗必须输入12张牌")
    if len(amplitude_cards) != 3:
        raise ValueError("15张模型中的幅度塔罗必须输入3张牌")

    all_cards = list(trend_cards) + list(amplitude_cards)

    trend_strength = 0
    trend_persistence = 0
    trend_direction_score = 0
    for card_code, orientation in trend_cards:
        semantics = get_card_meaning(card_code, orientation)
        trend_strength += semantics["strength"]
        trend_persistence += semantics["persistence"]
        trend_direction_score += semantics["direction_score"]

    amplitude_volatility = 0
    amplitude_strength = 0
    for card_code, orientation in amplitude_cards:
        semantics = get_card_meaning(card_code, orientation)
        amplitude_volatility += semantics["volatility"]
        amplitude_strength += semantics["strength"]

    total_volatility = 0
    for card_code, orientation in all_cards:
        semantics = get_card_meaning(card_code, orientation)
        total_volatility += semantics["volatility"]

    avg_strength = (trend_strength / len(trend_cards)) * 0.75 + (amplitude_strength / len(amplitude_cards)) * 0.25
    avg_volatility = (total_volatility / len(all_cards)) * 0.7 + (amplitude_volatility / len(amplitude_cards)) * 0.3
    avg_persistence = trend_persistence / len(trend_cards)
    avg_direction_score = trend_direction_score / len(trend_cards)

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
        "model": "15-card",
        "cards": list(all_cards),
        "trend_cards": list(trend_cards),
        "amplitude_cards": list(amplitude_cards),
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
