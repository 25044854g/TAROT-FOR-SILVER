# -*- coding: utf-8 -*-

import sys
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, HourLocator
from tarot_price_mapping_9 import (
    ORIENTATION_REVERSED,
    ORIENTATION_UPRIGHT,
    TAROT_PRICE_SEMANTICS,
    generate_9_card_price_trend,
)
from tarot_price_mapping_15 import generate_15_card_price_trend
from tarot_named import get_card_display_name, tarot_cards

def parse_card_with_orientation(card_str):
    """
    解析卡牌代码和正逆位
    格式: "卡牌代码 方向" 或 "卡牌代码,方向"
    例如: "Q8 1" (正位) 或 "Q8 0" (逆位) 或 "Q8" (默认正位)
    
    返回: (卡牌代码, 方向) 其中方向 1=正位, 0=逆位
    """
    card_str = card_str.strip()
    
    # 支持空格和逗号分隔
    if ' ' in card_str or '，' in card_str or ',' in card_str:
        # 先替换中文逗号为英文逗号
        card_str = card_str.replace('，', ',')
        # 支持空格和逗号分隔
        if ' ' in card_str:
            parts = card_str.split()
        else:
            parts = card_str.split(',')
        
        if len(parts) == 2:
            code, direction = parts[0].strip(), parts[1].strip()
            try:
                direction = int(direction)
                if direction not in [ORIENTATION_REVERSED, ORIENTATION_UPRIGHT]:
                    raise ValueError("方向必须是 1 (正位) 或 0 (逆位)")
                return code, direction
            except ValueError:
                raise ValueError(f"无效的方向值: {parts[1]}")
    
    # 默认为正位（1）
    return card_str, ORIENTATION_UPRIGHT

def parse_card_batch(card_input):
    card_list = []
    for card_str in card_input.split(','):
        code, direction = parse_card_with_orientation(card_str)
        card_list.append((code, direction))

    invalid_cards = [code for code, _ in card_list if code not in tarot_cards or code not in TAROT_PRICE_SEMANTICS]
    if invalid_cards:
        raise ValueError(f"Invalid card codes: {', '.join(invalid_cards)}")

    return card_list


def print_result_summary(result, label):
    card_lines = [get_card_display_name(code, orientation) for code, orientation in result.get('cards', [])]
    print("\n" + "=" * 60)
    print(f"{label} Price Trend Analysis Report")
    print("=" * 60)
    if card_lines:
        print("Cards:")
        print(", ".join(card_lines))
    print(f"Starting Price: ${result['start_price']:.2f}")
    print(f"Predicted Final Price: ${result['final_price']:.2f}")
    print(f"Price Change: ${result['change']:+.2f} ({result['change_percent']:+.2f}%)")
    print(f"Trend Direction: {result['direction']}")
    print(f"Average Strength: {result['avg_strength']:.2f} (0-1)")
    print(f"Average Volatility: {result['avg_volatility']:.2f} (0-1)")
    print(f"Average Persistence: {result['avg_persistence']:.2f} (0-1)")
    print(f"Average Direction Score: {result['avg_direction_score']:+.2f}")
    print("=" * 60 + "\n")


def plot_prediction_result(result, title_label, line_color, fill_color, save_path=None, show_chart=True):
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(result["timestamps"], result["prices"], linewidth=2, marker="o", markersize=4, color=line_color)
    ax.fill_between(result["timestamps"], result["prices"], alpha=0.25, color=fill_color)
    plt.title(f"Tarot Silver Price Trend Prediction ({title_label})\n{result['direction']}", fontsize=14, fontweight="bold")
    fig.text(0.05, 0.98, f"Date: {result['timestamps'][0].strftime('%Y-%m-%d')}", fontsize=11, verticalalignment='top', transform=fig.transFigure)
    ax.xaxis.set_major_locator(HourLocator(interval=2))
    ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))
    ax.set_xlabel('Time (2-hour intervals)', fontsize=12)
    ax.set_ylabel('Price (USD/oz)', fontsize=12)
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')

    if show_chart:
        plt.show()

    return fig


def ask_save_path(default_prefix):
    save_option = input("\nSave chart to file? (y/n): ").lower().strip()
    if save_option != 'y':
        return None
    return f"{default_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

def main():
    print("\n" + "="*50)
    print("Tarot Silver Price Trend Prediction Tool")
    print("="*50 + "\n")
    
    # 获取用户输入
    try:
        print("Starting Price (USD/oz)")
        print("-" * 40)
        start_price = float(input("Enter price: "))
        
        print("\nSelect Tarot Card Mode")
        print("-" * 40)
        print("1. 9-Card Tarot")
        print("2. 15-Card Tarot (Trend + Amplitude)")
        print("3. Complete Set (9-Card + 15-Card)")
        print()
        choice = input("Select (1/2/3): ").strip()
        
        if choice not in ['1', '2', '3']:
            print("Error: Please enter 1, 2, or 3!")
            return
        
        # 根据选择获取卡牌
        if choice == '1':
            print("\n9-Card Tarot")
            print("-" * 40)
            print("Format: CARD CODE ORIENTATION (separated by space)")
            print("  Upright: 1 | Reversed: 0")
            print("  Example: Q8 1,MS 0,YR 1")
            print()
            tarot_input = input("Enter 9 Tarot codes: ").upper()

            if not tarot_input.strip():
                print("Error: Card codes cannot be empty!")
                return

            cards_9 = parse_card_batch(tarot_input)
            if len(cards_9) != 9:
                print("Error: 9-Card model requires exactly 9 cards!")
                return

            result = generate_9_card_price_trend(start_price, cards_9)
            print_result_summary(result, "9-Card")
            save_path = ask_save_path("tarot_trend_9")
            plot_prediction_result(result, "9-Card Tarot", "#1f77b4", "#93c5fd", save_path=save_path)

        elif choice == '2':
            # 15张塔罗 - 分两步输入
            print("\nTrend Tarot (12 cards)")
            print("-" * 40)
            print("Format: CARD CODE ORIENTATION (separated by space)")
            print("  Upright: 1 | Reversed: 0")
            print("  Example: Q8 1,MS 0,YR 1 (separate cards with comma)")
            print()
            trend_tarot = input("Enter 12 Trend Tarot codes: ").upper()
            
            if not trend_tarot.strip():
                print("Error: Card codes cannot be empty!")
                return
            
            print("\nAmplitude Tarot (3 cards)")
            print("-" * 40)
            amplitude_tarot = input("Enter 3 Amplitude Tarot codes: ").upper()
            
            if not amplitude_tarot.strip():
                print("Error: Card codes cannot be empty!")
                return

            trend_cards = parse_card_batch(trend_tarot)
            amplitude_cards = parse_card_batch(amplitude_tarot)
            if len(trend_cards) != 12:
                print("Error: 15-Card model requires exactly 12 trend cards!")
                return
            if len(amplitude_cards) != 3:
                print("Error: 15-Card model requires exactly 3 amplitude cards!")
                return

            result = generate_15_card_price_trend(start_price, trend_cards, amplitude_cards)
            print_result_summary(result, "15-Card")
            save_path = ask_save_path("tarot_trend_15")
            plot_prediction_result(result, "15-Card Tarot", "#d97706", "#fbbf24", save_path=save_path)

        else:
            print("\n9-Card Tarot")
            print("-" * 40)
            tarot_9_input = input("Enter 9 Tarot codes: ").upper()
            if not tarot_9_input.strip():
                print("Error: Card codes cannot be empty!")
                return

            print("\nTrend Tarot (12 cards)")
            print("-" * 40)
            trend_tarot = input("Enter 12 Trend Tarot codes: ").upper()
            if not trend_tarot.strip():
                print("Error: Card codes cannot be empty!")
                return

            print("\nAmplitude Tarot (3 cards)")
            print("-" * 40)
            amplitude_tarot = input("Enter 3 Amplitude Tarot codes: ").upper()
            if not amplitude_tarot.strip():
                print("Error: Card codes cannot be empty!")
                return

            cards_9 = parse_card_batch(tarot_9_input)
            trend_cards = parse_card_batch(trend_tarot)
            amplitude_cards = parse_card_batch(amplitude_tarot)

            if len(cards_9) != 9:
                print("Error: Complete mode requires exactly 9 cards for the 9-card model!")
                return
            if len(trend_cards) != 12 or len(amplitude_cards) != 3:
                print("Error: Complete mode requires 12 trend cards and 3 amplitude cards!")
                return

            result_9 = generate_9_card_price_trend(start_price, cards_9)
            result_15 = generate_15_card_price_trend(start_price, trend_cards, amplitude_cards)
            print_result_summary(result_9, "9-Card")
            print_result_summary(result_15, "15-Card")
            save_path_9 = ask_save_path("tarot_trend_9")
            plot_prediction_result(result_9, "9-Card Tarot", "#1f77b4", "#93c5fd", save_path=save_path_9)
            save_path_15 = ask_save_path("tarot_trend_15")
            plot_prediction_result(result_15, "15-Card Tarot", "#d97706", "#fbbf24", save_path=save_path_15)
    
    except ValueError:
        print("Error: Invalid price input. Please enter a number.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        try:
            start_price = float(sys.argv[1])
            tarot_cards = sys.argv[2] if len(sys.argv) > 2 else ""
            card_mode = sys.argv[3] if len(sys.argv) > 3 else "3"
            
            if not tarot_cards:
                print("Usage: python tarot_trend_generator.py <starting_price> <card_codes> [mode]")
                print("\nExamples:")
                print("  python tarot_trend_generator.py 30.5 'Q8 1,MS 0,YR 1' 3")
                print("  python tarot_trend_generator.py 30.5 Q8 3")
                print("\nFormat:")
                print("  • Upright: Q8 1 (or Q8, default upright)")
                print("  • Reversed: Q8 0")
                print("  • Mixed: Q8 1,MS 0,YR 1 (separate with comma)")
                print("\nOrientation: 1=Upright, 0=Reversed")
                print("Mode: 1=9-Card, 2=15-Card, 3=Complete(default)")
                sys.exit(1)
            cards = parse_card_batch(tarot_cards)
            if card_mode == "1":
                if len(cards) != 9:
                    raise ValueError("9-Card mode requires 9 cards")
                result = generate_9_card_price_trend(start_price, cards)
                print_result_summary(result, "9-Card")
                plot_prediction_result(result, "9-Card Tarot", "#1f77b4", "#93c5fd")
            elif card_mode == "2":
                if len(cards) != 15:
                    raise ValueError("15-Card mode requires 15 cards")
                result = generate_15_card_price_trend(start_price, cards[:12], cards[12:])
                print_result_summary(result, "15-Card")
                plot_prediction_result(result, "15-Card Tarot", "#d97706", "#fbbf24")
            else:
                raise ValueError("CLI complete mode is not supported. Please use interactive mode.")
        except ValueError:
            print("Error: Invalid parameter format")
            print("Usage: python tarot_trend_generator.py <starting_price> <card_codes> [mode]")
            sys.exit(1)
    else:
        # Interactive mode
        main()
