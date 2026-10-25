# 🔐 Password Strength Checker in Python

A simple Python project that evaluates password strength based on length, uppercase letters, lowercase letters, digits, and special characters.

This project is designed for beginners learning Python programming, conditional statements, functions, regular expressions, and input handling.

## 📌 Features

- Checks password length (minimum 8 characters).
- Verifies the presence of uppercase letters.
- Verifies the presence of lowercase letters.
- Checks for numeric digits.
- Checks for special characters.
- Calculates a password strength score out of 5.
- Classifies passwords as Weak, Moderate, or Strong.
- Provides suggestions for improving password strength.
- Hides password input in the terminal using Python's `getpass` module.
- Runs locally without transmitting passwords to a server.

## 🛠️ Technologies Used

- **Language:** Python 3
- **Module:** `re` (Regular Expressions)
- **Module:** `getpass` (Hidden Password Input)

## 📂 Project Structure

```text
pass-strength/
├── password-checker.py
└── README.md
```

## ⚙️ Requirements

- Python 3 installed on your system.
- A terminal or command-line interface.

No external Python packages are required.

## 🚀 Installation and Usage

### 1. Clone the Repository

```bash
git clone <YOUR-REPOSITORY-URL>
```

Replace `<YOUR-REPOSITORY-URL>` with your actual GitHub repository URL.

### 2. Navigate to the Project Directory

```bash
cd pass-strength
```

### 3. Run the Program

```bash
python3 password-checker.py
```

### 4. Enter a Password

Enter the password when prompted. The characters will not appear on the terminal while you type.

The program will display the password strength, score, and suggestions for improvement.

## 📊 Password Scoring System

The program evaluates five criteria:

| Criterion | Points |
|---|---:|
| At least 8 characters | 1 |
| At least one uppercase letter | 1 |
| At least one lowercase letter | 1 |
| At least one digit | 1 |
| At least one special character | 1 |

### Strength Classification

| Score | Strength |
|---|---|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

**Note:** This is a basic educational scoring system. A high score does not guarantee that a password is secure.

## 💻 Example Output

```text
========================================
      PASSWORD STRENGTH CHECKER
========================================
Enter a password to check:

Password Strength: MODERATE
Score: 4/5

Suggestions for improvement:
- Add at least one special character.

Note: This is a basic educational checker.
```

The output shown above is an example. Actual results depend on the password entered.

## 🧠 Concepts Learned

This project demonstrates the use of:

- Python functions
- Conditional statements (`if`, `elif`, `else`)
- Regular expressions
- String handling
- Loops
- Variables and operators
- Return values
- Python modules
- Basic input validation

## 🔒 Privacy and Security

- The program checks passwords locally.
- It does not intentionally transmit passwords over the network.
- It does not save passwords to a file.
- Password input is hidden using `getpass`.

**Security disclaimer:** This project is intended for educational purposes. It is not a complete password-security auditing tool and should not be used as the sole method for evaluating password security.

## 🔮 Future Improvements

- Increase the recommended minimum password length.
- Detect common and predictable passwords.
- Identify repeated characters and simple patterns.
- Add automated unit tests.
- Develop a graphical user interface using Tkinter.
- Add a local password generator.

## 👨‍💻 Author

**Dhruv**

A beginner Python project created to practise programming fundamentals and explore basic password-strength evaluation.

## 📄 License

This project is available under the MIT License. If you intend to use that license, add a `LICENSE` file containing the MIT License text.
