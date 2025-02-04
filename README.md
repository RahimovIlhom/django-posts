# Django WebApp Loyihasi

Bu loyiha Python 3.10 yordamida ishlab chiqilgan va Django v5.0 bilan ishlaydi.

## Talablar

Loyihani ishga tushirishdan oldin quyidagi dasturlar o'rnatilganligiga ishonch hosil qiling:

- Python 3.10
- Docker va docker-compose

## O'rnatish va Ishga Tushirish

1. **Repository-ni klonlash yoki yuklab olish**:
   ```sh
   git clone https://github.com/RahimovIlhom/django-posts.git
   cd django-posts
   ```

2. **Virtual muhit yaratish va faollashtirish (ixtiyoriy, ammo tavsiya etiladi)**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # Linux yoki MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Loyihaga kerakli bog'liqliklarni o'rnatish**:
   ```sh
   pip install -r requirements.txt
   ```

4. **.env faylini yaratish va sozlash**:
   Loyiha muhit o'zgaruvchilarini saqlash uchun `.env` faylini loyihaning asosiy katalogida yarating:
   
   `.env` faylining namunasi:
   ```sh
   export SECRET_KEY=<your-secret-key>
   export DEBUG=True
   export ALLOWED_HOSTS=*  # Yoki o'zingizga kerakli hostlarni kiriting
   export CSRF_TRUSTED_ORIGINS=<your-allowed-origins>
   ```

   **SECRET_KEY yaratish:**
   SECRET_KEY ni yaratish uchun quyidagi Python buyruqlaridan foydalaning:
   ```sh
   python -c 'import secrets; print(secrets.token_urlsafe(50))'
   ```
   Hosil bo'lgan kalitni `.env` fayliga joylashtiring.

5. **Bazani migratsiya qilish**:
   ```sh
   python manage.py migrate
   ```

6. **Superuser yaratish (admin panelga kirish uchun)**:
   ```sh
   python manage.py createsuperuser
   ```
   So'rovga binoan foydalanuvchi nomi, email va parolni kiriting.

7. **Dastur serverini ishga tushirish**:
   ```sh
   python manage.py runserver
   ```

   Dastur localhostdagi 8000-portda ishga tushadi. Brauzerda quyidagi manzilga o'ting:
   ```
   http://127.0.0.1:8000/
   ```

Bu bilan Django loyihangiz ishga tushiriladi! 🎉

