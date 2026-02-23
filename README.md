<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/7aff82f6-15dd-4009-b92d-db34bd202bc0" />


# 📓 SmartNotes

SmartNotes is a user-based note management system built with Django.  
It includes a complete authentication system and a fully functional note CRUD architecture with additional features such as likes and visibility control.

The project demonstrates Django Class-Based Views, authentication workflows, secure user-based data filtering, form validation, and production-ready backend structuring.

---
# Mockup

<img width="1914" height="909" alt="Ekran görüntüsü 2026-02-24 011610" src="https://github.com/user-attachments/assets/5f9aebf0-afc6-4e40-859f-6913493ea0e6" />


<img width="1" height="1" alt="Ekran görüntüsü 2026-02-24 011729" src="https://github.com/user-attachments/assets/68a20269-a258-46d5-9e90-88be8fcbe16f" />


<img width="1915" height="922" alt="Ekran görüntüsü 2026-02-24 011739" src="https://github.com/user-attachments/assets/2d57b300-940d-4aa8-a687-14da65affa42" />


<img width="1915" height="916" alt="Ekran görüntüsü 2026-02-24 011759" src="https://github.com/user-attachments/assets/d4805ec9-33c2-4f72-94fe-733e30ecc15a" />


<img width="1917" height="912" alt="Ekran görüntüsü 2026-02-24 011813" src="https://github.com/user-attachments/assets/1bad66f6-2aa9-40ec-a8df-639649fe14f7" />


<img width="1916" height="910" alt="Ekran görüntüsü 2026-02-24 012018" src="https://github.com/user-attachments/assets/6556186b-fc59-46c1-86ca-e847dcc83a23" />


<img width="1916" height="914" alt="Ekran görüntüsü 2026-02-24 012119" src="https://github.com/user-attachments/assets/2e6b0c49-7afc-4755-865c-f826167b00e5" />


<img width="1912" height="916" alt="Ekran görüntüsü 2026-02-24 012125" src="https://github.com/user-attachments/assets/8b8842d0-234b-4082-bf52-025587f65e5b" />


<img width="1911" height="908" alt="Ekran görüntüsü 2026-02-24 012148" src="https://github.com/user-attachments/assets/8f7f6bb7-a5a9-44e9-897a-e7790bea2b3a" />


# 🚀 Features

## 🔐 Authentication System

- User Registration (Custom RegisterForm)
- Login / Logout
- Password Reset (Email-based)
- Automatic login after registration
- LoginRequiredMixin protection for restricted pages

### Authentication Routes

- `/login`
- `/logout`
- `/register`
- `/password-reset`
- `/password-reset/done`
- `/password-reset-confirm/<uidb64>/<token>`
- `/password-reset-complete`

---

## 📝 Notes System

### Core Functionalities

- Create Note
- List Notes (User-specific)
- View Note Detail
- Update Note
- Delete Note

### Additional Features

- Like System (POST-based secure increment)
- Public / Private visibility toggle
- Popular Notes filtering (likes ≥ 1)
- Notes ordered by newest first
- Users can only access their own notes

---

# 🧾 Forms & Validation

- Custom RegisterForm extending Django UserCreationForm
- Email field required during registration
- Model-based Note form implementation
- Title validation (minimum character requirement)
- Bootstrap-integrated form styling

---

# 🎨 UI & Templates

- Bootstrap-based responsive design
- List group display for notes
- Like counter badge
- Truncated preview text
- Delete confirmation page with CSRF protection
- Django date formatting filters

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/serkandemirtas/smartnotes.git
cd smartnotes
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

## 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

# 🔐 Create Superuser (Admin Panel Access)

```bash
python manage.py createsuperuser
```

Then visit:

```
http://127.0.0.1:8000/admin/
```

---

# 📧 Email Configuration (Required for Password Reset)

Since the project uses Django PasswordResetView, email backend configuration is required.

## Development (Console Backend)

Add to `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Emails will appear in the terminal.

---

## Gmail SMTP Setup

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourmail@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'
```

⚠ Gmail requires:
- 2FA enabled
- App Password generated from Google Account

For production, always use environment variables instead of hardcoding credentials.

---

# 🔒 Security

- CSRF Protection
- LoginRequiredMixin
- POST-only like & visibility operations
- Django password hashing
- User-based queryset filtering

---

# 🛠 Technologies Used

- Python
- Django
- Class-Based Views
- Django Authentication System
- SQLite
- Bootstrap

---

# 📈 Future Improvements

- Pagination
- AJAX-based Like system
- Comment system
- Tag system
- REST API (Django REST Framework)
- Docker deployment
- PostgreSQL production configuration
- AI-powered note summarization
- AI-based smart tagging system
- Semantic search using embeddings
- AI-driven personalized note recommendations
- Sentiment analysis for user notes
- Natural language query search (e.g., "Show me my productivity notes from last week")

---

# 📜 License

This project is licensed under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

The software is provided "as is", without warranty of any kind.

---

# 👨‍💻 Developer

Serkan Demirtaş  
Computer & Electrical-Electronics Engineering
