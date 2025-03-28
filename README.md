# Hall Permission Management System

A Django-based venue/hall permission management system for college use.

## 🚀 Setup Instructions

Follow these steps to run the project on your local machine:

### 1️⃣ Create a Virtual Environment
Run the following command:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Create a .env File

In the root directory, create a `.env` file and add the following details:

```ini
# Secret Key
SECRET_KEY=your-secret-key

# Debug mode (set to False in production)
DEBUG=True

# Database Configuration
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=5432

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

### 4️⃣ Apply Migrations and Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Your Django app should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/). 🎉

