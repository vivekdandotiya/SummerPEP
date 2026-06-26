import json
import re

def main():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()
        
        # Find the DAYS array definition inside the script
        days_match = re.search(r'"DAYS":\s*(\[.*?\])\s*\n\s*\]', html, re.DOTALL)
        if not days_match:
            # Try a simpler regex that matches "DAYS": [ ... ]
            days_match = re.search(r'"DAYS":\s*(\[.*?\}\s*\])', html, re.DOTALL)
            
        if days_match:
            days_json = days_match.group(1)
            # Safe parsing using json.loads
            try:
                days = json.loads(days_json)
            except Exception:
                # Fallback to eval since dict keys/values are double-quoted and syntax is python-compatible
                days = eval(days_json)
        else:
            print("Could not parse DAYS array directly from index.html.")
            return

        # Add Days 51-70
        for d in range(51, 71):
            days.append({
                "d": d,
                "topic": "Spare / Optional Review",
                "objectives": "Additional review or project work as time allows.",
                "handsOn": "Continue practice or take breaks.",
                "interview": "N/A",
                "subject": "support"
            })

        # Write formatted details to my.txt
        with open("my.txt", "w", encoding="utf-8") as out:
            out.write("========================================================================\n")
            out.write("                  L2/DEVOPS 70-DAY PLACEMENT STUDY PLAN                 \n")
            out.write("========================================================================\n\n")
            for day in days:
                out.write(f"DAY {day['d']}: {day['topic']}\n")
                out.write(f"Subject: {day.get('subject', 'N/A').upper()}\n")
                out.write(f"Learning Objectives: {day.get('objectives', 'N/A')}\n")
                out.write(f"Hands-on Tasks: {day.get('handsOn', 'N/A')}\n")
                out.write(f"Interview Prep: {day.get('interview', 'N/A')}\n")
                out.write("-" * 80 + "\n\n")
        
        print(f"Successfully processed {len(days)} days and wrote to my.txt")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()