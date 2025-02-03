import hashlib
import requests
import string
import tkinter as tk
from tkinter import messagebox

# HIBP API URL
HIBP_API_URL = "https://api.pwnedpasswords.com/range/"

def check_password_strength(password):
    """Analyzes password strength based on length, complexity, and common weaknesses."""
    score = 0
    feedback = []

    # Length check (Max: 4 points)
    if len(password) >= 12:
        score += 4
    elif len(password) >= 8:
        score += 2
    else:
        feedback.append("⚠️ Password is too short. Use at least 12 characters.")

    # Complexity check (Max: 4 points)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    complexity_score = sum([has_upper, has_lower, has_digit, has_special])
    if complexity_score == 4:
        score += 4
    elif complexity_score == 3:
        score += 2
    elif complexity_score == 2:
        score += 1
    else:
        feedback.append("⚠️ Use a mix of uppercase, lowercase, numbers, and symbols.")

    # Common password check (-4 penalty if common)
    common_passwords = {"password", "123456", "qwerty", "letmein", "welcome"}
    if password.lower() in common_passwords:
        feedback.append("⚠️ This is a commonly used password. Choose a stronger one.")
        score -= 4

    # Ensure the score is between 0 and 10
    score = max(0, min(score, 10))

    return score, feedback

def check_password_breach(password):
    """Checks if the password has been exposed in data breaches using HIBP API."""
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    
    try:
        response = requests.get(HIBP_API_URL + prefix)
        if response.status_code != 200:
            return "❌ Error checking password breach. Try again later."

        hashes = (line.split(":") for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return f"⚠️ WARNING: This password has been found in {count} breaches!"

        return "✅ This password has NOT been found in known breaches."
    
    except requests.exceptions.RequestException:
        return "❌ Network error! Check your internet connection."

def analyze_password():
    """Handles the password analysis when button is clicked."""
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Input Error", "Please enter a password to analyze.")
        return

    # Strength check
    score, feedback = check_password_strength(password)
    strength_label.config(text=f"Strength Score: {score}/10", fg="green" if score >= 7 else "red")

    # Display feedback
    feedback_text.config(state=tk.NORMAL)
    feedback_text.delete("1.0", tk.END)
    for msg in feedback:
        feedback_text.insert(tk.END, msg + "\n", "warning")
    feedback_text.config(state=tk.DISABLED)

    # Breach check
    breach_result = check_password_breach(password)
    breach_label.config(text=breach_result, fg="green" if "NOT" in breach_result else "red")

# GUI Setup
root = tk.Tk()
root.title("MusclePass - Password Analyzer")
root.geometry("450x400")
root.resizable(False, False)

# Header
header_label = tk.Label(root, text="💪 MusclePass - Password Analyzer 🔒", font=("Arial", 14, "bold"))
header_label.pack(pady=10)

# Password Input (Plaintext)
password_label = tk.Label(root, text="Enter a password:")
password_label.pack()
password_entry = tk.Entry(root, width=40)  # Now in plaintext mode
password_entry.pack()

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Password", command=analyze_password, bg="blue", fg="white")
analyze_button.pack(pady=10)

# Strength Output
strength_label = tk.Label(root, text="Strength Score: --", font=("Arial", 10, "bold"))
strength_label.pack()

# Feedback Output
feedback_text = tk.Text(root, height=4, width=50, wrap=tk.WORD, state=tk.DISABLED)
feedback_text.tag_config("warning", foreground="red")
feedback_text.pack(pady=5)

# Breach Check Output
breach_label = tk.Label(root, text="Breach Check: --", font=("Arial", 10, "bold"))
breach_label.pack()

# Run the GUI
root.mainloop()
