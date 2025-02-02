# MusclePass - Password Analyzer 💪🔒

MusclePass is a Python-based password strength analyzer that evaluates password security and checks if it has been exposed in data breaches using the Have I Been Pwned (HIBP) API. This GUI application, built with Tkinter, provides real-time feedback and a detailed strength score out of 10 to help users create stronger, more secure passwords.
## 🔹 Features

✅ Password Strength Scoring (/10) – Rates passwords based on length, complexity, and common weaknesses.

✅ Data Breach Check – Uses the HIBP API to check if a password has been compromised.

✅ User-Friendly GUI – Built with Tkinter, making it easy to use without the command line.

✅ Instant Feedback – Color-coded feedback to guide users toward stronger passwords.

✅ Open-Source & Lightweight – No database needed, simple to set up and run.

## 📸 Screenshots

Coming soon!

## 🚀 Installation & Usage
### 🔧 Requirements

    Python 3.x
    Tkinter (built-in with Python)
    Requests library (pip install requests)

## 💻 Running the Application

    Clone the repository:

git clone https://github.com/JamesLorencee/MusclePass.git

    cd MusclePass

Install dependencies:

    pip install requests

Run the app:

    python musclepass_gui.py

## 🛠 How It Works

1️⃣ Enter a password in the text field.
2️⃣ Click "Analyze Password" to check strength and breach status.
3️⃣ See the results:

    Strength score (out of 10)
    Suggestions for improving password security
    Breach check status (safe or compromised)

## 📌 Example Outputs
Password	Score	Feedback	Breach Check
123456	0/10	"Common password. Choose a stronger one."	⚠️ Found in breaches!
Secure123	5/10	"Use a mix of uppercase, lowercase, numbers, and symbols."	✅ Not found
P@ssw0rd2024!	10/10	None (Perfect password)	✅ Not found

## 🛡️ Security & Privacy
🔒 Your password is **NEVER** sent over the internet.

✅ Only the first 5 characters of its SHA-1 hash are sent to the HIBP API for breach checking.

🔐 This method ensures secure and anonymous password verification.

## 🛠 Future Improvements
📊 Progress bar indicator for strength visualization.

🌍 Flask/Django web version for online password analysis.

🎨 Dark mode UI for better visual experience.

## 📜 License
This project is open-source and available under the MIT License.

## 👨‍💻 Contributing
Pull requests and suggestions are welcome! Feel free to fork the repo and contribute to MusclePass.
