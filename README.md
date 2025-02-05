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
   git clone https://github.com/vharishcse/BharatFDv2.git
   cd BharatFDv2
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the Redis server:
   - On macOS/Linux: `redis-server`
   - On Windows: Start the Redis server using the Redis installer.

5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

---

## **API Usage**

### **Endpoints**
- **Fetch FAQs in English (Default)**:
  ```bash
  GET /api/faqs/
  ```

- **Fetch FAQs in Hindi**:
  ```bash
  GET /api/faqs/?lang=hi
  ```

- **Fetch FAQs in Bengali**:
  ```bash
  GET /api/faqs/?lang=bn
  ```

### **Example**
```bash
curl http://localhost:8000/api/faqs/?lang=hi
```

---

## **Testing**

Run the test suite using:
```bash
python manage.py test
```

---

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
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License.
---

## **Contact**
For questions or feedback, please open an issue in the repository or contact me on GitHub:  
[Harish Yadav](https://github.com/vharishcse)

---

## **Acknowledgments**
- [Django](https://www.djangoproject.com/) for the web framework.
- [Django REST Framework](https://www.django-rest-framework.org/) for building the API.
- [Redis](https://redis.io/) for caching.
- [django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) for rich text editing.
