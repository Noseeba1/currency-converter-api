# استخدام Python 3.12
FROM python:3.12-slim

# منع إنشاء ملفات cache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# مجلد العمل داخل الكونتينر
WORKDIR /app

# نسخ ملف المكتبات
COPY requirements.txt .

# تثبيت المكتبات
RUN pip install --no-cache-dir -r requirements.txt

# نسخ بقية المشروع
COPY . .

# المنفذ الذي يعمل عليه التطبيق
EXPOSE 8000

# تشغيل FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]