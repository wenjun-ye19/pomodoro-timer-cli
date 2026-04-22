import time
import os
import sys

# --- Configuration (Constants) ---
WORK_TIME = 25 * 60  # 25 minutes in seconds
BREAK_TIME = 5 * 60  # 5 minutes in seconds
MESSAGE_WORK = "🍅 Focus Time! Work hard."
MESSAGE_BREAK = "☕ Break Time! Relax and breathe."

def clear_screen():
    """Clears the terminal screen for a fresh display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_time(seconds):
    """Converts seconds into MM:SS format."""
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02d}:{secs:02d}"

def countdown(duration, label):
    """Runs the countdown timer with a clean UI update."""
    total_seconds = duration
    
    while total_seconds > 0:
        clear_screen()
        print(f"\n{label}")
        print(f"Time remaining: {format_time(total_seconds)}")
        print("-" * 30)
        print("Press Ctrl+C to stop early.")
        
        time.sleep(1)
        total_seconds -= 1
    
    # Timer finished
    clear_screen()
    print(f"\n✅ {label} Complete!")
    print("\a") # Plays a system beep sound (optional)

def main():
    print("👋 Welcome to Wenjun's Stoic Pomodoro Timer - CLI version")
    print("Focus on what you can control: the present moment.")
    
    try:
        while True:
            # 1. Work Session
            countdown(WORK_TIME, MESSAGE_WORK)
            
            # 2. Break Session
            input("\nPress Enter to start your break...")
            countdown(BREAK_TIME, MESSAGE_BREAK)
            
            # 3. Loop Back
            choice = input("\nStart another session? (y/n): ").lower()
            if choice != 'y':
                print("\n🙏 Great work today. Rest well.")
                break
                
    except KeyboardInterrupt:
        print("\n\n⏹️ Timer stopped by user. Stay focused!")
        sys.exit(0)

if __name__ == "__main__":
    main()