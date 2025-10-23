# Healthcare Management System

A Django-based healthcare management system that enables patient and doctor user types with separate dashboards and profile management.

## Features

- **Multi-User Types**
  - Patient accounts
  - Doctor accounts
  - Role-specific dashboards

- **User Authentication**
  - Custom user model
  - Secure signup and login
  - Password reset functionality

- **Profile Management**
  - Profile picture upload
  - Personal information management
  - Address details

- **Responsive Dashboards**
  - Doctor dashboard with appointments and activity tracking
  - Patient dashboard with medical information
  - Quick actions and profile editing

## Technology Stack

- Python 3.8+
- Django 4.2
- SQLite3 (default database)
- Tailwind CSS for styling
- Pillow for image handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Praveen7-C/healthcare-user-auth.git
cd healthcare_project
```

2. Create a virtual environment and activate it:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Project Structure

```
healthcare_project/
├── healthcare_project/    # Project settings
├── users/                 # User management app
├── templates/            # Global templates
├── static/              # Static files
├── media/               # User-uploaded files
├── manage.py
└── requirements.txt
```

## User Types and Features

### Patient Features
- Personal dashboard
- Medical history view
- Appointment booking (coming soon)
- Profile management

### Doctor Features
- Professional dashboard
- Patient list view
- Appointment management
- Profile and credentials management

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

This project uses Django's built-in security features including:
- CSRF protection
- XSS prevention
- Secure password hashing
- User authentication

## Environment Variables

Create a `.env` file in the root directory with these variables:
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

* Django Documentation
* Tailwind CSS
* Django Crispy Forms
