# 🔐 Password Leak Checker

Ever wonder if your passwords are floating around the dark corners of the internet? This tool checks if any of your passwords have been compromised — quickly, safely, and using k-anonymity to protect your data.

Built with Python, it leverages the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords) to verify password integrity without ever exposing your full password.

---

## 🚀 Why this project matters

- 💥 **Real-world utility:** Password security is not optional — it’s critical.
- 🛡️ **Privacy first:** Uses SHA-1 hashing and k-anonymity, so your actual passwords are never sent over the internet.
- 🔍 **Recruiter-ready demo:** Clean, efficient code with solid error handling and a real-world API integration.
- 📈 **Scalable design:** Easily extendable for GUI interfaces, batch automation, or CI/CD pipelines.

---

## 🧠 How it works

1. Takes a list of passwords from a `.txt` file.
2. Hashes each password using SHA-1.
3. Sends only the **first 5 characters** of the hash to the API.
4. Compares the rest of the hash locally against the API response.
5. Reports if a password has been found in previous leaks — and how many times.

---

## 📸 Example Output

```
Password bhjgvjdhsuifeh has no leaks.
Password RabbitCarrot@ has no leaks.
Password CorrecthorseStablerider has no leaks.
Password 987password has 9 times leaks.
Done!
```

---

## 🛠️ How to Run

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/password-leak-checker.git
cd password-leak-checker
```

2. **Create your password file**

A `.txt` file with one password per line. Example:

```
bhjgvjdhsuifeh
RabbitCarrot@
CorrecthorseStablerider
987password
```

3. **Run the script**

```bash
python checkpassword.py stored_passwords.txt
```

---

## 🧪 Tech Stack

- Python 3
- `hashlib` for SHA-1 hashing
- `requests` for API calls
- Have I Been Pwned Public API

---

## 🔮 Future Improvements

- 🔐 Integration with password managers (1Password, Bitwarden, etc.)
- 🖥️ GUI using Tkinter or PyQt
- ☁️ Deploy as a serverless AWS Lambda or REST API
- 🧪 Unit tests and CI/CD integration
- 📊 Export results to CSV/JSON for auditing

---

## 🤝 Let's connect

I'm Liz — an aspiring AI developer passionate about building secure, scalable tools that actually help people.

- 🌐 [LinkedIn](https://www.linkedin.com/in/elizabeth-challenger)
- 🧠 [ZTM Graduate - AI Developer Path](https://zerotomastery.io/)
- 🏞️ Outdoor explorer & Mexican food enthusiast 🌮

---

> “A strong password is your digital seatbelt — this project helps you check if yours has already been cut.”\
> — Liz, future AI security ninja 🥷

---

