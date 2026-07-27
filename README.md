# Weather Dashboard

A modern, full-stack Python Django Weather Dashboard featuring user authentication, saved favorite locations, real-time weather metrics, and 24-hour/5-day forecasts via OpenWeatherMap, all wrapped in a stunning glassmorphism UI.

![Weather Dashboard Preview](docs/dashboard.png)

## About The Project
This project provides a personalized, fast, and visually appealing way for users to track weather across multiple cities simultaneously.
* **Personalized Experience:** Users can register accounts and manage their own list of favorite cities.
* **Real-Time Data:** Powered by the OpenWeatherMap API, the dashboard fetches live temperature, humidity, wind speed, and atmospheric conditions.
* **Forecasting:** Users can dive into specific locations to view granular 3-hour interval updates for the next 24 hours, as well as a 5-day outlook.
* **Robust Error Handling:** The backend Service layer intercepts API rate limits or invalid keys and handles them gracefully, ensuring the application never crashes.
* **Premium UI:** Designed without external CSS frameworks, using purely custom Vanilla CSS with a modern dark-mode glassmorphism aesthetic.

![Add Location Preview](docs/add_location.png)

## Demo Credentials
To test the application quickly without registering, you can use the default test account:
- **Username:** `admin`
- **Password:** `admin`


## Key Features
- **Object-Oriented Architecture**: Service layer separating external API logic from views.
- **Authentication & Authorization**: Built-in Django auth protecting personalized dashboards.
- **CRUD Operations**: Add, view, edit (nicknames), and delete favorite locations.
- **Exception Handling**: Graceful error handling for API failures (404, 429) using Django messages.
- **Modern UI**: Custom Vanilla CSS with a glassmorphism design.

## Prerequisites
- Python 3.10+
- OpenWeatherMap API Key (Free tier works perfectly)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ANAND-JATOTHU/kinetrexa-Weather-Dashboard.git
   cd kinetrexa-Weather-Dashboard
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory (where `manage.py` is located) and add your keys:
   ```env
   DJANGO_SECRET_KEY=your_secure_django_key
   DEBUG=True
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key_here
   ```

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000`.

## Generating the PDF Report
The project includes a standalone script to auto-generate the architecture and database schema report.
```bash
python generate_report.py
```
This will output `Project_Report.pdf` in the root directory.

## Testing
To run the automated test suite (if implemented):
```bash
python manage.py test
```

## Deployment
For deploying to platforms like Render or PythonAnywhere, you will need to:
1. Set `DEBUG=False` in `.env`.
2. Add the appropriate domain to `ALLOWED_HOSTS` in `settings.py`.
3. Configure static files using WhiteNoise or your web server's static file handler.
