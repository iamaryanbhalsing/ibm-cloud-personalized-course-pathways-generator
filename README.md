# LearnMate – Agentic AI for Personalized Course Pathways

LearnMate is an **agentic AI learning coach** that helps students pick the right online learning path based on their interests, current skill level, and long‑term goals.  
It is built only on **IBM Cloud** using **IBM watsonx.ai (llama models)**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

> Live At : https://ibm-cloud-personalized-course-pathways-generator.streamlit.app

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

## 🎯 Problem & Solution

### Problem

Students are overwhelmed by thousands of online courses and don’t know:

- Which skill path fits their interests (Frontend, Cybersecurity, UI/UX, etc.).
- Where to start based on their current level.
- How to adjust the roadmap as they progress or change goals.

### ✅Solution

LearnMate:

- Chats with the student to understand interests and goals.
- Stores a simple **student profile** on IBM Cloud.
- Uses **IBM Granite** to generate a **personalized learning roadmap**.
- Provides an AI chat coach that adapts advice as the student’s profile evolves.

IBM’s Granite foundation models are decoder‑only language models optimized for predicting and generating text, which makes them suitable for this kind of coaching and roadmap generation .

---

## 🏗 Architecture Overview

All components run on IBM Cloud:

- **Frontend**: Simple HTML/CSS/JavaScript (static files). - StreamLit
- **Backend**: Python + Flask API.
- **AI Layer**: IBM watsonx.ai Runtime using an **IBM llama-3-3-70b-instruct model**.
- **Database**: IBM Cloudant (Lite plan) for storing student profiles.

IBM Cloud Lite plans allow you to try over 40 services, including foundation models and databases, for free within usage limits .

---

## 📂 Project Structure

```text
learnmate/
  backend/
    app.py
    requirements.txt
    .env
  frontend/
    index.html
    style.css
    app.js
```

---

## ⚙️ Prerequisites

Before running the project, you need:

1. **IBM Cloud account** (Lite / Free tier) .
2. **IBM watsonx.ai project** with:
   - A **Granite instruct model** (e.g., `llama-3-3-70b-instruct`).
   - A **Runtime** instance for text generation.
3. **IBM Cloudant** Lite instance for storing profiles.
4. Python 3.10+ installed locally.

---

## 🔑 IBM Cloud Setup

### 1. Create IBM Cloud account

- Go to the IBM Cloud Free Tier page and sign up for an account .

### 2. Create watsonx.ai project & Runtime

- Open **watsonx.ai** in IBM Cloud.
- Create a **Project** (note the **Project ID**).
- In the project, create a **Runtime** (Lite plan).
- Enable a Granite text model from the foundation model catalog (llama-3-3-70b-instruct family) .
- Generate an **API key** in IBM Cloud (IAM → API keys).

You will need:

- `WATSONX_APIKEY` – your IBM Cloud API key.
- `WATSONX_PROJECT_ID` – your watsonx.ai project ID.
- `WATSONX_URL` – usually `https://us-south.ml.cloud.ibm.com`.

### 3. Create Cloudant instance

- In IBM Cloud, create **Cloudant** (Lite).
- Go to **Service credentials**.
- Copy:
  - Cloudant URL (e.g. `https://xxxxx.cloudantnosqldb.appdomain.cloud`).
  - Cloudant API key.

You will need:

- `CLOUDANT_URL`
- `CLOUDANT_APIKEY`
- Any database name (e.g. `learnmate_students`); it will be created automatically.

---

## 🔧 Local Setup

### 1. Backend configuration

In the `backend` folder:

1. Create `.env`:

   ```env
   WATSONX_APIKEY=your_ibm_api_key_here
   WATSONX_PROJECT_ID=your_watsonx_project_id_here
   WATSONX_URL=https://us-south.ml.cloud.ibm.com
   WATSONX_MODEL_ID=meta-llama/llama-3-3-70b-instruct
   ```

2. Create `requirements.txt`:

   ```txt
   flask
   flask-cors
   requests
   python-dotenv
   ```

3. Install dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Run the backend:

   ```bash
   python app.py
   ```

You should see something like:

```text
* Running on http://127.0.0.1:5000
```

Flask allows returning dictionaries which are automatically serialized into JSON, making it simple to expose API endpoints consumed by the frontend

### 2. Frontend setup

The frontend is pure static files, so there’s no build step.

## 💻 Frontend Behaviour

The frontend (`frontend/app.js`) does:

- `saveProfile()` – calls `/profile` to store the student’s data.
- `generateRoadmap()` – calls `/roadmap` and displays the generated roadmap JSON.
- `sendChat()` – calls `/chat` and shows LearnMate’s AI response.

All calls use `fetch` with `Content-Type: application/json` and talk to `http://127.0.0.1:5000`.

Flask‑CORS is enabled (`CORS(app)`) so browsers can call the API from a different origin without CORS issues, which is a common pattern for React/JS frontends talking to Flask backends.

---

## 🔍 Typical Usage Flow

1. Start the backend: `python app.py`.
2. Open the frontend: `frontend/index.html`.
3. Enter:
   - Student ID and name.
   - Interests (e.g., `frontend, cybersecurity`).
   - Level (beginner/intermediate/advanced).
   - Goal and time per day.
4. Click **Save Profile**.
5. Click **Generate Roadmap** – the roadmap appears as formatted JSON.
6. Use the **Chat** section to ask “How should I start?” or “Can you adjust my plan?”

---

## 🧠 Agentic AI Aspect

LearnMate is **agentic** because:

- It keeps a student profile in Cloudant.
- Uses Lamma Model from IBM to:
  - Analyse interests and skill level.
  - Plan a multi‑week roadmap.
  - Adapt answers based on stored data.
- It can be extended to:
  - Re‑generate roadmaps when progress is updated.
  - Integrate external course catalogs via additional tools.


---

## 🚀 Future Improvements

Ideas you can add later:

- Skill assessment quizzes before generating the roadmap.
- Progress tracking (completed topics, dates).
- Integration with IBM SkillsBuild or external course APIs.
- Role‑based flows (school admin vs student).
- More advanced agent orchestration with multi‑step planning.

---


## 🤝 Acknowledgements

- **IBM Cloud** Lite tier for free foundational services .
- **IBM watsonx.ai & lamma foundation models** for the AI coaching engine .

---

## 🤝 Thank you!!

## 💕 Special Thanks to EDUNET FOUNDATION AND IBM

---
### <img src="https://media.giphy.com/media/GFeFpm1jZZD0m4wlQ3/giphy.gif" width="50"> Cᴏɴᴛᴀᴄᴛ & Sᴏᴄɪᴀʟꜱ :

<p align="center">
  <a href="mailto:aryanbhalsing7090@gmail.com">
    <img src="https://img.shields.io/badge/Email-aryanbhalsing7090%40gmail.com-red?style=for-the-badge&logo=gmail" />
  </a>
  <a href="https://www.linkedin.com/in/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LinkedIn-iamaryanbhalsing-blue?style=for-the-badge&logo=linkedin" />
  </a>
  <a href="https://github.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/GitHub-iamaryanbhalsing-black?style=for-the-badge&logo=github" />
  </a>
  <a href="https://leetcode.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LeetCode-Profile-orange?style=for-the-badge&logo=leetcode" />
  </a>
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=iamaryanbhalsing&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</p>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

<div align="center">
  <img src="https://media.giphy.com/media/vXyIMuWbGTMtO/giphy.gif" width="500" alt="Anime GIF">
</div>

<div align="center"> <b>
Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Vɪꜱɪᴛɪɴɢ Mʏ Pʀᴏꜰɪʟᴇ! ✨  
Lᴇᴛ'ꜱ Bᴜɪʟᴅ Sᴏᴍᴇᴛʜɪɴɢ Iᴍᴘᴀᴄᴛꜰᴜʟ Tᴏɢᴇᴛʜᴇʀ.
</b> </div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

<div align="center"> <b>
Oʜʜ!! Tʜᴀᴛꜱ Nɪᴄᴇ Yᴏᴜ Rᴇᴀᴄʜᴇᴅ Hᴇʀᴇ !!
I Kɴᴏᴡ Yᴏᴜ Aʀᴇ Iᴍᴘʀᴇꜱꜱᴇᴅ Nᴏᴡ Vɪꜱɪᴛ Mʏ Pʀᴏꜰɪʟᴇ Aɴᴅ Exᴘʟᴏʀᴇ Mᴇ Pʀᴏᴊᴇᴄᴛꜱ
</b> </div>
