# Slot Antenna Predictor

A Django web application for predicting slot antenna parameters using a machine learning model.

## Features

- User authentication (login required)
- Form for inputting antenna parameters (supports 2-loop and 4-loop configurations)
- Robust backend validation and prediction
- Modern, responsive frontend UI
- Ready for deployment on Railway and GitHub

## Local Development

### Prerequisites

- Python 3.11+
- pip
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Setup

1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd slot_antenna_project
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser (for admin access):
   ```sh
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Deployment on Railway

1. Push your repository to GitHub.
2. Go to [Railway](https://railway.app/) and create a new project.
3. Connect your GitHub repository.
4. Set the following environment variables in Railway:
   - `DJANGO_SECRET_KEY` (generate a strong secret key)
   - `DEBUG` (set to `False` for production)
   - `ALLOWED_HOSTS` (set to your Railway domain)
5. Add a `requirements.txt` and `Procfile` if not present:
   - `requirements.txt`: List all Python dependencies.
   - `Procfile`:
     ```
     web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn slot_antenna_project.wsgi
     ```
6. Deploy the project. Railway will build and serve your Django app.

## Deployment on GitHub Pages

GitHub Pages does not support Django directly. For static frontend-only demos, export static HTML or use a static site generator. For full backend support, use Railway or another PaaS.

## Notes

- Ensure `model/multi_output_rf_model.pkl` and `model/scaler.pkl` are present in the `model/` directory.
- For any issues, check logs on Railway or run locally with `DEBUG=True`.

## License

MIT
