Overview:
This project is a Multilingual FAQ Management System built using Django, designed to manage FAQs with language-specific translations. The system provides a REST API for retrieving FAQs in different languages, supports rich text formatting with a WYSIWYG editor, and uses caching for improved performance.

Features:
✅ Django-based FAQ Management: Store and manage FAQs efficiently.
✅ WYSIWYG Editor Support: Uses django-ckeditor for rich text formatting.
✅ Multi-language Translation: Automatically translates FAQs using Google Translate API or googletrans with a fallback to English.
✅ REST API: Retrieve FAQs in different languages using a ?lang= query parameter.
✅ Caching Mechanism: Uses Redis to store translations and improve response times.
✅ Admin Panel: Provides an easy-to-use interface for managing FAQs.
✅ Unit Testing & Code Quality: Implements pytest and follows PEP8 guidelines for clean, maintainable code.
✅ Git Best Practices: Uses atomic commits with proper commit messages.
✅ Deployment Ready: Supports Dockerization and can be deployed on Heroku or AWS.

Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/multilingual-faq-system.git
cd multilingual-faq-system

2. Create & Activate a Virtual Environment
python -m venv myenv
source myenv/Scripts/activate  # On Windows
# For macOS/Linux, use:
# source myenv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Create a Superuser (For Admin Panel Access)
python manage.py createsuperuser

6. Run the Server
python manage.py runserver

Using this we can translate the language from Hindi or Bengali to English.

