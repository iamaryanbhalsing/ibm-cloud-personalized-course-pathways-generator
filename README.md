# LearnMate – Agentic AI for Personalized Course Pathways

LearnMate is an **agentic AI learning coach** that helps students pick the right online learning path based on their interests, current skill level, and long‑term goals.  
It is built only on **IBM Cloud** using **IBM watsonx.ai (llama models)**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

> Live At : https://ibm-cloud-personalized-course-pathways-generator.streamlit.app

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" alt="" style="max-width: 100%; display: inline-block;" data-target="animated-image.originalImage">

## 🎯 Problem & Solution

### ❓Problem

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
personalized-course-pathways/
├── assets/
│   └── styles.css
├── data/
│   ├── courses.csv
│   └── roadmap_templates.json
├── src/
│   ├── model_client.py
│   ├── recommender.py
│   ├── roadmap_builder.py
│   ├── storage.py
│   └── utils.py
├── .env
├── app.py
└── requirements.txt
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
   streamlit
   ibm-watsonx-ai==1.5.14
   python-dotenv
   pandas
   ```

3. Install dependencies:

   ```bash
   cd personalized-course-pathways/
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

You should see something like:

```text
* Running on http://127.0.0.1:5000
```

Live Demo of Running Locally :

<a href="https://ibb.co/s9c3vxn8"><img src="https://i.ibb.co/m5dzCZkf/Recording-2026-07-11-101752-1.gif" alt="Recording-2026-07-11-101752-1" border="0"></a>

---

## 🧠 Agentic AI Aspect

LearnMate is **agentic** because:

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
I Kɴᴏᴡ Yᴏᴜ Aʀᴇ Iᴍᴘʀᴇꜱꜱᴇᴅ Nᴏᴡ Vɪꜱɪᴛ Mʏ Pʀᴏꜰɪʟᴇ Aɴᴅ Exᴘʟᴏʀᴇ Mᴏʀᴇ Pʀᴏᴊᴇᴄᴛꜱ
</b> </div>
