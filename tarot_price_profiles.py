# -*- coding: utf-8 -*-

QUALITATIVE_STRENGTH = {
    "强": 0.85,
    "中": 0.60,
    "弱": 0.35,
}

QUALITATIVE_VOLATILITY = {
    "极高": 0.95,
    "高": 0.75,
    "中": 0.50,
    "低": 0.25,
}

QUALITATIVE_PERSISTENCE = {
    "强": 0.85,
    "中": 0.60,
    "弱": 0.35,
}

COMBINED_MODEL_BLEND = {
    "nine_card_weight": 0.5,
    "fifteen_card_weight": 0.5,
}

DIRECTION_RULES = {
    "↗ 上涨": {"direction": "bullish", "pattern": "uptrend", "direction_score": 1.0},
    "↗ 反弹": {"direction": "bullish", "pattern": "rebound", "direction_score": 0.7},
    "↗ 大涨": {"direction": "bullish", "pattern": "surge", "direction_score": 1.2},
    "→ 震荡": {"direction": "neutral", "pattern": "consolidation", "direction_score": 0.0},
    "→ 震荡偏上": {"direction": "neutral", "pattern": "consolidation_up", "direction_score": 0.3},
    "→ 震荡偏下": {"direction": "neutral", "pattern": "consolidation_down", "direction_score": -0.3},
    "↘ 下跌": {"direction": "bearish", "pattern": "downtrend", "direction_score": -1.0},
    "↘ 暴跌": {"direction": "bearish", "pattern": "crash", "direction_score": -1.3},
}


def build_profile(direction_label, strength_label, volatility_label, persistence_label):
    rule = DIRECTION_RULES[direction_label]
    return {
        "direction_label": direction_label,
        "direction": rule["direction"],
        "pattern": rule["pattern"],
        "direction_score": rule["direction_score"],
        "strength_label": strength_label,
        "strength": QUALITATIVE_STRENGTH[strength_label],
        "volatility_label": volatility_label,
        "volatility": QUALITATIVE_VOLATILITY[volatility_label],
        "persistence_label": persistence_label,
        "persistence": QUALITATIVE_PERSISTENCE[persistence_label],
    }


TAROT_CARD_PROFILES = {
    "YR": {"upright": build_profile("↗ 上涨", "中", "高", "弱"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "MS": {"upright": build_profile("↗ 上涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "JS": {"upright": build_profile("→ 震荡", "弱", "低", "中"), "reversed": build_profile("→ 震荡偏下", "弱", "中", "弱")},
    "NH": {"upright": build_profile("↗ 上涨", "强", "低", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "中")},
    "HD": {"upright": build_profile("↗ 上涨", "强", "低", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "中")},
    "JH": {"upright": build_profile("→ 震荡", "中", "低", "强"), "reversed": build_profile("→ 震荡偏下", "弱", "中", "弱")},
    "LR": {"upright": build_profile("↗ 上涨", "中", "中", "中"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "ZC": {"upright": build_profile("↗ 上涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "LL": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "YS": {"upright": build_profile("→ 震荡", "弱", "低", "中"), "reversed": build_profile("→ 震荡偏下", "弱", "中", "弱")},
    "MY": {"upright": build_profile("↗ 上涨", "中", "高", "中"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "ZY": {"upright": build_profile("→ 震荡", "中", "低", "强"), "reversed": build_profile("→ 震荡偏下", "弱", "中", "弱")},
    "DJ": {"upright": build_profile("→ 震荡", "弱", "中", "弱"), "reversed": build_profile("↗ 反弹", "中", "高", "弱")},
    "SS": {"upright": build_profile("↘ 下跌", "强", "高", "强"), "reversed": build_profile("↗ 反弹", "中", "高", "弱")},
    "JZ": {"upright": build_profile("→ 震荡", "中", "低", "强"), "reversed": build_profile("→ 震荡偏下", "弱", "高", "弱")},
    "EM": {"upright": build_profile("↘ 下跌", "中", "高", "中"), "reversed": build_profile("↗ 反弹", "中", "高", "弱")},
    "GT": {"upright": build_profile("↘ 暴跌", "强", "极高", "强"), "reversed": build_profile("↗ 反弹", "中", "高", "弱")},
    "XX": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "YL": {"upright": build_profile("→ 震荡", "弱", "高", "弱"), "reversed": build_profile("→ 震荡偏上", "中", "中", "中")},
    "TY": {"upright": build_profile("↗ 大涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "中")},
    "SP": {"upright": build_profile("↗ 上涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "SJ": {"upright": build_profile("↗ 上涨", "强", "低", "强"), "reversed": build_profile("→ 震荡", "中", "中", "弱")},

    "Q1": {"upright": build_profile("↗ 上涨", "中", "中", "中"), "reversed": build_profile("→ 震荡", "弱", "高", "弱")},
    "Q2": {"upright": build_profile("↗ 上涨", "中", "中", "中"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "Q3": {"upright": build_profile("↗ 上涨", "中", "中", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "Q4": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "Q5": {"upright": build_profile("→ 震荡", "中", "高", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "Q6": {"upright": build_profile("↗ 上涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "弱")},
    "Q7": {"upright": build_profile("↗ 上涨", "中", "高", "中"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "Q8": {"upright": build_profile("↗ 上涨", "强", "高", "中"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "Q9": {"upright": build_profile("→ 震荡", "中", "中", "中"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "Q10": {"upright": build_profile("↘ 下跌", "中", "中", "中"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "QP": {"upright": build_profile("↗ 上涨", "弱", "高", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "QN": {"upright": build_profile("↗ 上涨", "强", "高", "中"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "QQ": {"upright": build_profile("↗ 上涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "弱")},
    "QK": {"upright": build_profile("↗ 上涨", "强", "中", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "弱")},

    "C1": {"upright": build_profile("↗ 上涨", "中", "低", "中"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "C2": {"upright": build_profile("↗ 上涨", "中", "低", "中"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "C3": {"upright": build_profile("↗ 上涨", "中", "中", "中"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "C4": {"upright": build_profile("→ 震荡", "弱", "低", "弱"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "C5": {"upright": build_profile("↘ 下跌", "中", "中", "弱"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "C6": {"upright": build_profile("↗ 上涨", "中", "低", "中"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "C7": {"upright": build_profile("→ 震荡", "弱", "高", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "C8": {"upright": build_profile("↘ 下跌", "中", "中", "中"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "C9": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "C10": {"upright": build_profile("↗ 上涨", "强", "低", "强"), "reversed": build_profile("→ 震荡", "中", "中", "弱")},
    "CP": {"upright": build_profile("↗ 上涨", "弱", "中", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "CN": {"upright": build_profile("↗ 上涨", "中", "中", "中"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "CQ": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "CK": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},

    "J1": {"upright": build_profile("↗ 上涨", "中", "高", "中"), "reversed": build_profile("↘ 下跌", "中", "高", "弱")},
    "J2": {"upright": build_profile("→ 震荡", "弱", "低", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "J3": {"upright": build_profile("↘ 下跌", "中", "高", "中"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "J4": {"upright": build_profile("→ 震荡", "弱", "低", "弱"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "J5": {"upright": build_profile("↘ 下跌", "中", "高", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "J6": {"upright": build_profile("→ 震荡", "中", "中", "中"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "J7": {"upright": build_profile("→ 震荡", "弱", "高", "弱"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "J8": {"upright": build_profile("→ 震荡", "弱", "中", "弱"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "J9": {"upright": build_profile("↘ 下跌", "中", "高", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "J10": {"upright": build_profile("↘ 暴跌", "强", "极高", "强"), "reversed": build_profile("↗ 反弹", "中", "高", "弱")},
    "JP": {"upright": build_profile("→ 震荡", "弱", "高", "弱"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "JN": {"upright": build_profile("↘ 下跌", "强", "高", "中"), "reversed": build_profile("↗ 反弹", "中", "高", "弱")},
    "JQ": {"upright": build_profile("↘ 下跌", "中", "中", "中"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "JK": {"upright": build_profile("→ 震荡", "中", "低", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "弱")},

    "B1": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "B2": {"upright": build_profile("→ 震荡", "中", "中", "中"), "reversed": build_profile("→ 震荡", "弱", "高", "弱")},
    "B3": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "B4": {"upright": build_profile("→ 震荡", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "B5": {"upright": build_profile("↘ 下跌", "中", "中", "中"), "reversed": build_profile("↗ 反弹", "弱", "中", "弱")},
    "B6": {"upright": build_profile("↗ 上涨", "中", "低", "中"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "B7": {"upright": build_profile("→ 震荡", "中", "低", "中"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "B8": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "B9": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "B10": {"upright": build_profile("↗ 上涨", "强", "低", "强"), "reversed": build_profile("→ 震荡", "中", "中", "弱")},
    "BP": {"upright": build_profile("↗ 上涨", "弱", "中", "弱"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "BN": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("↘ 下跌", "弱", "中", "弱")},
    "BQ": {"upright": build_profile("↗ 上涨", "中", "低", "强"), "reversed": build_profile("→ 震荡", "弱", "中", "弱")},
    "BK": {"upright": build_profile("↗ 上涨", "强", "低", "强"), "reversed": build_profile("↘ 下跌", "中", "中", "弱")},
}

TAROT_PRICE_SEMANTICS = {
    code: profiles["upright"].copy()
    for code, profiles in TAROT_CARD_PROFILES.items()
}