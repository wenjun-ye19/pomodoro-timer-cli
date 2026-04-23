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

def play_alert_sound():
    """Plays a sound alert cross-platform."""
    try:
        # Windows: Use built-in winsound module
        import winsound
        # Frequency (Hz), Duration (ms) - A pleasant chime
        winsound.Beep(600, 500) 
        winsound.Beep(800, 500)
    except ImportError:
        # Linux/macOS: Fallback to terminal bell (might not sound on all terminals)
        print("\a")

def countdown(duration, label):
    """Runs the countdown timer with a clean UI update."""
    total_seconds = duration
    
    while total_seconds > 0:
        clear_screen()
        print(f"\n{label}")
        print(f"Time remaining: {format_time(total_seconds)}")
        print("-" * 30)
        print("Press Ctrl+C to stop...for emergency only!")
        
        time.sleep(1)
        total_seconds -= 1
    
    # Timer finished
    clear_screen()
    print(f"\n✅ {label} Complete!")
    play_alert_sound()
    
    # Show Visual Alert regardless of software sound capabilities
    print("\n🔔 DING DING! Time's up!") 

def main():
    clear_screen()
    print("👋 Welcome to Wenjun's Stoic Pomodoro Timer - CLI version")
    print("Focus on what you can control: the present moment.")
    print("-" * 40)
    
    try:
        while True:
            # 1. Start Work Session (Wait for user confirmation)
            input("\n⏳ Press Enter to start your 25-min Focus Session...")
            countdown(WORK_TIME, MESSAGE_WORK)
            
            # 2. Start Break Session (Wait for user confirmation)
            input("\n☕ Press Enter to start your 5-min Break...")
            countdown(BREAK_TIME, MESSAGE_BREAK)
            
            # 3. Loop Back
            choice = input("\n🔄 Start another session? (Press Enter for Yes, type 'n' to quit): ").lower().strip()
            if choice == 'n':
                print("\n🙏 Great work today. Rest well.")
                break
                
    except KeyboardInterrupt:
        print("\n\n⏹️ Timer stopped by user. Stay focused!")
        sys.exit(0)

if __name__ == "__main__":
    main()