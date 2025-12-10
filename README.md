# MyProject - Django Todo Application

A simple Django-based todo application with user authentication, allowing users to manage their tasks.

## Features

- User registration and login
- Create, view, and manage todo tasks
- Task descriptions, due dates, and times
- Admin panel for managing users and tasks
- Responsive templates

## Technologies Used

- Django 4.x
- Python 3.x
- SQLite (default database)
- HTML/CSS (Bootstrap for styling)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mentachaitanya/myproject.git
   cd myproject
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional for admin access):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Register a new account or login with existing credentials.
- Navigate to the Todo section to add, view, and manage your tasks.
- Use the admin panel at `/admin/` with superuser credentials to manage users and tasks.

## Project Structure

- `accounts/`: User authentication app
- `home/`: Home page app
- `todo/`: Todo management app
- `myproject/`: Main Django project settings

## Contributing

Feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the MIT License.
