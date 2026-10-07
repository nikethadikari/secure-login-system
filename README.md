# 🔐 Secure Login System

A beginner-friendly **Python authentication and user management system** built to practice **Object-Oriented Programming (OOP)** and fundamental cybersecurity concepts.

This project simulates a simple login system with **user registration, authentication, account lockout, password management, and role-based access control**.

---

## 🚀 Version 1.0

Version 1 focuses on building the core authentication and authorization logic using Python classes, objects, methods, and dictionaries.

### ✨ Features

* 👤 User registration
* 🔑 User login
* 🚫 Failed login attempt tracking
* 🔒 Account lockout after 3 failed attempts
* 🔄 Password changing
* 🗑️ User deletion
* 📋 User information display
* 🛡️ Role-based access control
* 👑 Administrator-controlled role changes
* 👥 `user` and `administrator` roles
* 🔎 Username uniqueness checking

---

## 🧠 Concepts Practiced

This project was created while learning Python Object-Oriented Programming and includes:

* Classes and Objects
* `__init__()` constructors
* Instance attributes
* Methods
* `self`
* Dictionaries
* Object references
* Conditional statements
* Return values
* State management
* Authentication
* Authorization
* Role-Based Access Control (RBAC)

---

## 🏗️ Project Structure

```text
secure-login-system/
│
├── main.py
├── README.md
└── .gitignore
```

---

## 👥 Roles

The system currently supports two roles:

| Role            | Permissions                   |
| --------------- | ----------------------------- |
| `user`          | Basic account operations      |
| `administrator` | Can change other users' roles |

Only an **administrator** can change the role of another user.

---

## 🔐 Authentication Flow

The basic login process works like this:

```text
User
 │
 ▼
Enter Username & Password
 │
 ▼
Find User
 │
 ├── User Not Found
 │
 ▼
Verify Password
 │
 ├── Invalid Password
 │       │
 │       ▼
 │   Failed Attempts +1
 │
 └── Correct Password
         │
         ▼
    Login Successful
```

After **3 failed login attempts**, the account becomes locked.

---

## ⚠️ Security Note

This is an **educational project** created to practice Python programming, Object-Oriented Programming, and basic cybersecurity concepts.

> **Version 1 is not intended for production use.**

Passwords are currently stored in plaintext for simplicity while learning the core authentication logic.

Future versions will introduce proper password hashing and additional security controls.

---

## 🛠️ Planned Improvements

Future versions may include:

* 🔐 Secure password hashing
* 📏 Password strength requirements
* 🛡️ Improved brute-force protection
* 📝 Security and audit logging
* 🎫 Session management
* 🔑 More detailed role-based permissions
* 💾 Persistent user storage
* 🧪 Automated unit tests
* ⚙️ Improved error handling

---

## 🎯 Purpose

The main goal of this project is not to build a production-ready authentication system, but to **learn by building**.

It is part of my journey in learning:

**Python → Object-Oriented Programming → Cybersecurity → Secure Application Development**

---

## 📌 Project Status

**Current Version:** `v1.0`
**Status:** 🚧 Learning Project

More security-focused features will be added in future versions.

---

## 👨‍💻 Author

Built as a personal learning project while studying **Python, Object-Oriented Programming, Cybersecurity, and secure application development**.

