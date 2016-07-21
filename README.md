# raccoongang.com
Raccoon Gang corporate site

Clone project form GitHub:

    git clone https://github.com/raccoongang/raccoongang.com.git

Install dependencies

    pip install -r requirements.txt

Make migrations

    python manage.py migrate
    
Remove djangocms-blog additional menu

go to *<virtualenv dir>/lib/python2.7/site-packages/djangocms_blog/cms_app.py*
and comment or remove string 

    menus = [BlogCategoryMenu]

Start site

    python manage.py
