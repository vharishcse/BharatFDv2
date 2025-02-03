Here’s an updated `README.md` file for your project, reflecting the changes we’ve made (including the switch to CKEditor 5 and Redis caching). You can customize it further as needed.

---

```markdown
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
   ```bash
   python manage.py migrate
   ```

7. **Start Redis**:
   - Ensure Redis is installed and running. For Windows, download Redis from [here](https://github.com/tporadowski/redis/releases).
   - Start the Redis server:
     ```bash
     redis-server
     ```

---

## Running the Project

1. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

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
  ```

- **Fetch FAQs in Hindi**:
  ```bash
  curl http://localhost:8000/api/faqs/?lang=hi
  ```

- **Fetch FAQs in Bengali**:
  ```bash
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
```bash
python manage.py test
```

---

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
5. Open a pull request.

---

## License

This project is licensed under the MIT License.

## Contact
For any questions or issues, please contact [Harish Yadav](https://www.linkedin.com/in/v-harish-yadav-b2bb52241).
