# Token Authentication using Flask

## 👤 Student Details

* **Name:** Om Kumar Jha
* **UID:** 23BCC70012

---

## 📌 Experiment Title

Implement Authentication using Tokens

---

## 🚀 Features

* Authentication using **Authorization Header (Basic Auth)**
* Authentication using **Custom Headers**
* Authentication using **JWT (JSON Web Tokens)**
* Protected API route using JWT
* Tested using Postman
* Ready for deployment (Render)

---

## 🛠️ Tech Stack

* Python
* Flask
* PyJWT
* Postman

---

## 📂 Project Structure

```
token-auth-flask/
│── app.py
│── requirements.txt
│── Procfile
│── runtime.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/omkumarjha1/FSD-2.git
cd token-auth-flask
```

### 2. Create Virtual Environment

```
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python app.py
```

Server runs on:

```
http://127.0.0.1:5000
```

---

## 🔌 API Endpoints

### 1. Authorization Header

* **URL:** `/auth-header`
* **Method:** POST
* **Auth:** Basic Auth
* **Username:** admin
* **Password:** 1234

---

### 2. Custom Header

* **URL:** `/custom-header`
* **Method:** POST
* **Headers:**

```
X-Username: admin
X-Password: 1234
```

---

### 3. JWT Authentication

#### 🔹 Login (Generate Token)

* **URL:** `/login`
* **Method:** POST
* **Body (JSON):**

```
{
  "username": "admin",
  "password": "1234"
}
```

#### 🔹 Access Protected Route

* **URL:** `/protected`
* **Method:** GET
* **Header:**

```
Authorization: Bearer <token>
```

---

## 🧪 Testing

* All APIs tested using Postman
* Screenshots included in submission

---

## 🌐 Deployment

* Deployed on Render platform
* Live URL: *(Add your deployed link here)*

---

## 📚 Learning Outcomes

* Understood token-based authentication
* Learned how JWT works
* Implemented secure API endpoints
* Gained experience with Postman testing
* Learned basic cloud deployment

---

## 📎 Notes

* Do not upload `venv/` folder to GitHub
* Use `.gitignore` to exclude unnecessary files

---

## ✅ Conclusion

This experiment demonstrates how different authentication mechanisms can be implemented in a Flask-based backend and how JWT provides a secure and scalable way to manage user sessions.
