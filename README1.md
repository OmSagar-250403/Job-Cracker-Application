# Job Cracker – Online Job Portal

**Job Cracker** is an online job portal built using Django that enables recruiters to post job openings and search for candidates. Job seekers can browse job listings, apply for jobs, and upload their resumes.

## 🚀 Features

### 🔹 **For Recruiters (HR)**
- Sign up and log in.
- Post job listings with details.
- View a list of applicants for each job.

### 🔹 **For Job Seekers**
- Browse available job listings.
- Apply for jobs without logging in.
- Upload resumes while applying.

### 🔹 **Admin Panel**
- Manage job postings.
- Manage recruiters.
- Oversee applications.

---

## 🛠 Technologies Used
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default), can be switched to PostgreSQL/MySQL

---

## 📌 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/OmSagar-250403/Job-Cracker-Application.git
cd job-cracker
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (for Admin Panel)
```bash
python manage.py createsuperuser
```
Follow the instructions to set up an admin account.

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to access the application.

---

## 🎯 Future Enhancements
- Email notifications for job applications.
- Advanced job search and filtering.
- Resume parsing and AI-based job matching.

---

## 📄 License
This project is licensed under the MIT License.
