<<<<<<< HEAD

```markdown
# BharatFD Internship Test - Backend Solution

This repository contains the backend solution for the BharatFD internship test. It includes a Django-based REST API for managing FAQs with multilingual support, WYSIWYG editor integration, and Redis caching.

---

## **Features**
- **FAQ Management**: Create, read, update, and delete FAQs.
- **Multilingual Support**: FAQs can be translated into multiple languages (e.g., Hindi, Bengali).
- **WYSIWYG Editor**: Rich text formatting for FAQ answers using `django-ckeditor`.
- **Caching**: Redis is used to cache translations for improved performance.
- **REST API**: Supports language-specific FAQ retrieval via query parameters.

---

## **Installation**

### **Prerequisites**
- Python 3.8+
- Redis (for caching)
- Docker (optional, for deployment)

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/bharatfd_internship.git
   cd bharatfd_internship
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run migrations:
=======
# BharatFD Internship Test Project

This project is a backend implementation for managing FAQs with multilingual support, built using Django and Django REST Framework. It includes features like:

- **Multilingual FAQ Management**: Supports English, Hindi, and Bengali.
- **WYSIWYG Editor**: Integrated with CKEditor 5 for rich text editing.
- **Caching**: Uses Redis for efficient caching of FAQ responses.
- **REST API**: Provides endpoints to fetch FAQs in different languages.

---

## Table of Contents

1. [Installation](#installation)
2. [Running the Project](#running-the-project)
3. [API Usage](#api-usage)
4. [Caching](#caching)
5. [Multilingual Support](#multilingual-support)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Contributing](#contributing)

---

## Installation

### Prerequisites

- Python 3.11 or later
- Redis (for caching)
- Google Cloud Translation API (for translations)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add the following:
   ```env
   GOOGLE_APPLICATION_CREDENTIALS=path/to/your/google-cloud-credentials.json
   ```

6. **Run Migrations**:
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
   ```bash
   python manage.py migrate
   ```

<<<<<<< HEAD
4. Start the Redis server:
   - On macOS/Linux: `redis-server`
   - On Windows: Start the Redis server using the Redis installer.

5. Run the Django development server:
=======
7. **Start Redis**:
   - Ensure Redis is installed and running. For Windows, download Redis from [here](https://github.com/tporadowski/redis/releases).
   - Start the Redis server:
     ```bash
     redis-server
     ```

---

## Running the Project

1. **Start the Development Server**:
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
   ```bash
   python manage.py runserver
   ```

<<<<<<< HEAD
---

## **API Usage**

### **Endpoints**
- **Fetch FAQs in English (Default)**:
  ```bash
  GET /api/faqs/
=======
2. **Access the Admin Panel**:
   - Go to `http://localhost:8000/admin/`.
   - Log in with your superuser credentials (create one using `python manage.py createsuperuser` if needed).

3. **Add FAQs**:
   - Use the admin panel to add FAQs with questions and answers in English.
   - The system will automatically translate them into Hindi and Bengali.

---

## API Usage

### Fetch FAQs

- **Fetch FAQs in English**:
  ```bash
  curl http://localhost:8000/api/faqs/
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
  ```

- **Fetch FAQs in Hindi**:
  ```bash
<<<<<<< HEAD
  GET /api/faqs/?lang=hi
=======
  curl http://localhost:8000/api/faqs/?lang=hi
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
  ```

- **Fetch FAQs in Bengali**:
  ```bash
<<<<<<< HEAD
  GET /api/faqs/?lang=bn
  ```

### **Example**
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

---

## **Testing**

Run the test suite using:
=======
  curl http://localhost:8000/api/faqs/?lang=bn
  ```

---

## Caching

- The project uses **Redis** to cache FAQ responses for 15 minutes.
- To clear the cache, restart the Redis server or manually delete the cache keys.

---

## Multilingual Support

- The project supports **English**, **Hindi**, and **Bengali**.
- Translations are handled using the **Google Cloud Translation API**.
- If a translation fails, the system falls back to the original English text.

---

## Testing

To run the tests, use the following command:
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
```bash
python manage.py test
```

---

<<<<<<< HEAD
## **Deployment**

### **Using Docker**
1. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

2. Access the API at `http://localhost:8000/api/faqs/`.

---

## **Technologies Used**
- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default), Redis (caching)
- **WYSIWYG Editor**: django-ckeditor
- **Translation**: googletrans
- **Containerization**: Docker

---

## **Code Structure**
```
bharatfd_internship/
├── faqs/
│   ├── migrations/       # Database migrations
│   ├── models.py         # FAQ model
│   ├── serializers.py    # FAQ serializer
│   ├── views.py          # FAQ API views
│   ├── tests.py          # Unit tests
│   └── admin.py          # Django admin configuration
├── bharatfd_internship/
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI configuration
├── .gitignore            # Specifies files and directories to ignore in Git
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── README.md             # Project documentation
└── manage.py             # Django command-line utility
```

---

## **Contributing**
1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Commit your changes: `git commit -m "Add your feature"`.
4. Push to the branch: `git push origin feature/your-feature-name`.
=======
## Deployment

### Docker

1. **Build the Docker Image**:
   ```bash
   docker-compose build
   ```

2. **Run the Application**:
   ```bash
   docker-compose up
   ```

### Heroku

1. **Install the Heroku CLI**:
   Follow the instructions [here](https://devcenter.heroku.com/articles/heroku-cli).

2. **Deploy the Application**:
   ```bash
   heroku create
   git push heroku main
   heroku run python manage.py migrate
   heroku open
   ```

---

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
5. Open a pull request.

---

<<<<<<< HEAD
## **License**
This project is licensed under the MIT License.

## **Contact**
For questions or feedback, please open an issue in the repository or contact  [Harish Yadav](https://www.linkedin.com/in/v-harish-yadav-b2bb52241).

## **Acknowledgments**
- [Django](https://www.djangoproject.com/) for the web framework.
- [Django REST Framework](https://www.django-rest-framework.org/) for building the API.
- [Redis](https://redis.io/) for caching.
- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) for rich text editing.

---
=======
## License

This project is licensed under the MIT License.

---

## Contact
For any questions or issues, please contact [Harish Yadav](https://www.linkedin.com/in/v-harish-yadav-b2bb52241).
>>>>>>> e927071f71d4b16b1469db545f98dba4ec869209
