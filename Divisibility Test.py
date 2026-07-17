import sys
from typing import Dict, Any

class CompleteDivisibilityEngine:
    """Processes arbitrarily large string integers against all rules from 2 to 25 concurrently."""
    
    @staticmethod
    def test_2(n: str) -> Dict[str, Any]:
        last = int(n[-1])
        ok = last % 2 == 0
        return {"ok": ok, "txt": f"Ends in {last} ({'even' if ok else 'odd'})."}

    @staticmethod
    def test_3(n: str) -> Dict[str, Any]:
        digits = [int(d) for d in n]
        d_sum = sum(digits)
        ok = d_sum % 3 == 0
        return {"ok": ok, "txt": f"Digit sum: {'+'.join(n)} = {d_sum} ({'divisible' if ok else 'not divisible'} by 3)."}

    @staticmethod
    def test_4(n: str) -> Dict[str, Any]:
        last_two = int(n[-2:]) if len(n) >= 2 else int(n)
        ok = last_two % 4 == 0
        return {"ok": ok, "txt": f"Last 2 digits form {last_two:02d} ({'divisible' if ok else 'not divisible'} by 4)."}

    @staticmethod
    def test_5(n: str) -> Dict[str, Any]:
        last = n[-1]
        ok = last in ('0', '5')
        return {"ok": ok, "txt": f"Ends in {last} (must be 0 or 5)."}

    @staticmethod
    def test_6(n: str) -> Dict[str, Any]:
        t2 = CompleteDivisibilityEngine.test_2(n)["ok"]
        t3 = CompleteDivisibilityEngine.test_3(n)["ok"]
        return {"ok": t2 and t3, "txt": f"Divisible by 2: {t2} | Divisible by 3: {t3}."}

    @staticmethod
    def test_7(n: str) -> Dict[str, Any]:
        curr = n
        steps = []
        while len(curr) > 2:
            rest, last = int(curr[:-1]), int(curr[-1])
            diff = rest - (2 * last)
            steps.append(f"{rest}-(2*{last})={diff}")
            curr = str(diff)
        final_val = int(curr)
        ok = final_val % 7 == 0
        return {"ok": ok, "txt": f"Steps: {', '.join(steps)} -> Final: {final_val} % 7 == {final_val % 7}."}

    @staticmethod
    def test_8(n: str) -> Dict[str, Any]:
        last_three = int(n[-3:]) if len(n) >= 3 else int(n)
        ok = last_three % 8 == 0
        return {"ok": ok, "txt": f"Last 3 digits form {last_three} ({'divisible' if ok else 'not divisible'} by 8)."}

    @staticmethod
    def test_9(n: str) -> Dict[str, Any]:
        digits = [int(d) for d in n]
        d_sum = sum(digits)
        ok = d_sum % 9 == 0
        return {"ok": ok, "txt": f"Digit sum: {'+'.join(n)} = {d_sum} ({'divisible' if ok else 'not divisible'} by 9)."}

    @staticmethod
    def test_10(n: str) -> Dict[str, Any]:
        last = n[-1]
        ok = last == '0'
        return {"ok": ok, "txt": f"Ends in {last} (must be 0)."}

    @staticmethod
    def test_11(n: str) -> Dict[str, Any]:
        alt_sum = 0
        parts = []
        for i, digit in enumerate(reversed(n)):
            d = int(digit)
            if i % 2 == 0:
                alt_sum += d
                parts.append(f"+{d}")
            else:
                alt_sum -= d
                parts.append(f"-{d}")
        ok = alt_sum % 11 == 0
        return {"ok": ok, "txt": f"Alternating sum: {' '.join(reversed(parts))} = {alt_sum}."}

    @staticmethod
    def test_12(n: str) -> Dict[str, Any]:
        t3 = CompleteDivisibilityEngine.test_3(n)["ok"]
        t4 = CompleteDivisibilityEngine.test_4(n)["ok"]
        return {"ok": t3 and t4, "txt": f"Divisible by 3: {t3} | Divisible by 4: {t4}."}

    @staticmethod
    def test_13(n: str) -> Dict[str, Any]:
        curr = n
        steps = []
        while len(curr) > 3:
            rest, last = int(curr[:-1]), int(curr[-1])
            res = rest + (4 * last)
            steps.append(f"{rest}+(4*{last})={res}")
            curr = str(res)
        final_val = int(curr)
        ok = final_val % 13 == 0
        return {"ok": ok, "txt": f"Steps: {', '.join(steps)} -> Final: {final_val}."}

    @staticmethod
    def test_14(n: str) -> Dict[str, Any]:
        t2 = CompleteDivisibilityEngine.test_2(n)["ok"]
        t7 = CompleteDivisibilityEngine.test_7(n)["ok"]
        return {"ok": t2 and t7, "txt": f"Divisible by 2: {t2} | Divisible by 7: {t7}."}

    @staticmethod
    def test_15(n: str) -> Dict[str, Any]:
        t3 = CompleteDivisibilityEngine.test_3(n)["ok"]
        t5 = CompleteDivisibilityEngine.test_5(n)["ok"]
        return {"ok": t3 and t5, "txt": f"Divisible by 3: {t3} | Divisible by 5: {t5}."}

    @staticmethod
    def test_16(n: str) -> Dict[str, Any]:
        last_four = int(n[-4:]) if len(n) >= 4 else int(n)
        ok = last_four % 16 == 0
        return {"ok": ok, "txt": f"Last 4 digits form {last_four} ({'divisible' if ok else 'not divisible'} by 16)."}

    @staticmethod
    def test_17(n: str) -> Dict[str, Any]:
        curr = n
        steps = []
        while len(curr) > 3:
            rest, last = int(curr[:-1]), int(curr[-1])
            res = rest - (5 * last)
            steps.append(f"{rest}-(5*{last})={res}")
            curr = str(res)
        final_val = int(curr)
        ok = final_val % 17 == 0
        return {"ok": ok, "txt": f"Steps: {', '.join(steps)} -> Final: {final_val}."}

    @staticmethod
    def test_18(n: str) -> Dict[str, Any]:
        t2 = CompleteDivisibilityEngine.test_2(n)["ok"]
        t9 = CompleteDivisibilityEngine.test_9(n)["ok"]
        return {"ok": t2 and t9, "txt": f"Divisible by 2: {t2} | Divisible by 9: {t9}."}

    @staticmethod
    def test_19(n: str) -> Dict[str, Any]:
        curr = n
        steps = []
        while len(curr) > 3:
            rest, last = int(curr[:-1]), int(curr[-1])
            res = rest + (2 * last)
            steps.append(f"{rest}+(2*{last})={res}")
            curr = str(res)
        final_val = int(curr)
        ok = final_val % 19 == 0
        return {"ok": ok, "txt": f"Steps: {', '.join(steps)} -> Final: {final_val}."}

    @staticmethod
    def test_20(n: str) -> Dict[str, Any]:
        last_two = int(n[-2:]) if len(n) >= 2 else int(n)
        ok = last_two % 20 == 0
        return {"ok": ok, "txt": f"Ends in {last_two:02d} (must end in 00, 20, 40, 60, or 80)."}

    @staticmethod
    def test_21(n: str) -> Dict[str, Any]:
        t3 = CompleteDivisibilityEngine.test_3(n)["ok"]
        t7 = CompleteDivisibilityEngine.test_7(n)["ok"]
        return {"ok": t3 and t7, "txt": f"Divisible by 3: {t3} | Divisible by 7: {t7}."}

    @staticmethod
    def test_22(n: str) -> Dict[str, Any]:
        t2 = CompleteDivisibilityEngine.test_2(n)["ok"]
        t11 = CompleteDivisibilityEngine.test_11(n)["ok"]
        return {"ok": t2 and t11, "txt": f"Divisible by 2: {t2} | Divisible by 11: {t11}."}

    @staticmethod
    def test_23(n: str) -> Dict[str, Any]:
        curr = n
        steps = []
        while len(curr) > 3:
            rest, last = int(curr[:-1]), int(curr[-1])
            res = rest + (7 * last)
            steps.append(f"{rest}+(7*{last})={res}")
            curr = str(res)
        final_val = int(curr)
        ok = final_val % 23 == 0
        return {"ok": ok, "txt": f"Steps: {', '.join(steps)} -> Final: {final_val}."}

    @staticmethod
    def test_24(n: str) -> Dict[str, Any]:
        t3 = CompleteDivisibilityEngine.test_3(n)["ok"]
        t8 = CompleteDivisibilityEngine.test_8(n)["ok"]
        return {"ok": t3 and t8, "txt": f"Divisible by 3: {t3} | Divisible by 8: {t8}."}

    @staticmethod
    def test_25(n: str) -> Dict[str, Any]:
        last_two = int(n[-2:]) if len(n) >= 2 else int(n)
        ok = last_two in (0, 25, 50, 75)
        return {"ok": ok, "txt": f"Ends in {last_two:02d} (must end in 00, 25, 50, or 75)."}


def run_batch_app():
    print("=====================================================================")
    print("                COMPLETE BATCH DIVISIBILITY LAB (2-25)               ")
    print("=====================================================================\n")
    
    while True:
        try:
            raw_input = input("Enter a positive number to evaluate (or 'exit'): ").strip()
            if raw_input.lower() == 'exit':
                print("Goodbye!")
                sys.exit()
                
            if not raw_input.isdigit():
                print("❌ Error: Valid positive integers only.\n")
                continue
            
            print(f"\nAnalyzing number: {raw_input}")
            print(f"{'Divisor':<9} | {'Status':<8} | Breakdown & Proof String")
            print("-" * 75)
            
            # Execute every calculation method from 2 through 25 sequentially
            for divisor in range(2, 26):
                method = getattr(CompleteDivisibilityEngine, f"test_{divisor}")
                res = method(raw_input)
                
                status_str = "✅ PASS" if res["ok"] else "❌ FAIL"
                print(f"By {divisor:<6} | {status_str:<8} | {res['txt']}")
                
            print("-" * 75 + "\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run_batch_app()
