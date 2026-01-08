
# 🚖 Online Driver Detector

Online Driver Detector — bu taksi haydovchilari va mijozlarni real vaqt rejimida bog‘lab beruvchi online xizmatdir.  
Mijozlar tezda haydovchi topishi, haydovchilar esa osonlik bilan yangi buyurtmalarni ko‘rishi uchun ishlab chiqilgan.

---

## 🚀 Texnologiyalar

Loyiha quyidagi stack asosida qurilgan:

| Texnologiya | Versiya |
|------------|---------|
| Python | 3.9 |
| Django | 5.1.4 |
| Django REST Framework | 3.16.1 |
| Channels | 4.3.2 |
| Daphne (ASGI server) | 4.0.0 |
| PostgreSQL | 16 |
| Redis | 7.1.0 |


---

# 🛠 Loyihani to‘liq sozlash va ishga tushirish

Quyidagi yo‘riqnoma orqali siz loyihani 0–dan ishlab ketadigan holatgacha ishga tushira olasiz.

---

## 1️⃣ Reponi clone qilib oling

git clone https://github.com/shamshod8052/online-driver-detection
cd online-driver-detector

---

## 2️⃣ .env faylni yaratish

Loyihada .env.example mavjud — uni .env ga ko‘chiring:

cp .env.example .env

So‘ng .env ichidagi qiymatlarni to‘ldiring:

---


## 8️⃣ Loyiha URL’lari

Local (Docker):

- Backend API → http://localhost:8005  
- Admin panel → http://localhost:8005/admin/  
- WebSocket server → ws://localhost:8005/ws/  

Production (Nginx bilan):

- Backend API → https://yourdomain.com  
- Admin panel → https://yourdomain.com/admin/  
- WebSocket → wss://yourdomain.com/ws/

---

## 9️⃣ WebSocket’ni test qilish

Browser console:
```code
let socket = new WebSocket("ws://localhost:8005/ws/test/");
socket.onopen = () => console.log("Connected");
socket.onmessage = (msg) => console.log("New:", msg.data);
```
---

# 📁 Loyiha tuzilmasi

online-driver-detection/
```
 ├── Admin/
 ├── config/
 ├── docker/
 ├── templates
 ├── Dockerfile
 ├── docker-compose.yml
 ├── manage.py
 ├── requirements.txt
 ├── .gitignore
 ├── .env.example
 └── README.md
```

## 📄 License

MIT License  
Copyright (c) 2025 Shamshod

Ushbu loyiha MIT litsenziyasi asosida tarqatiladi — foydalanish, o‘zgartirish va tarqatish erkin.

---

## 📬 Muallif

Shamshod Ramazonov

Loyiha bo‘yicha savol yoki mulohazalar bo‘lsa, bemalol bog‘laning! +998940048052
