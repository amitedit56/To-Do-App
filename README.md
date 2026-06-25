# ✦ Taskflow — Focus & Ship

A clean, minimal To-Do app built with **Python + Streamlit**, featuring a sharp dark UI with custom CSS styling, priority badges, and real-time task filtering.

## 🔗 Live Demo

<img width="947" height="731" alt="image" src="https://github.com/user-attachments/assets/5077d3ba-e74d-43f1-b18f-902d53e2818d" />

> 🚀 **Live URL:** [https://to-do-app-amit.streamlit.app](https://to-do-app-amit.streamlit.app/)

---

## ✨ Features

- ✦ **Custom Dark UI** — Minimal `#0f0f11` dark theme with DM Sans + DM Mono typography
- 📊 **Live Stats Bar** — Pending / Completed / Total counts update instantly
- 🔴 **3 Priority Levels** — High, Medium, Low with color-coded badges
- 🔍 **Filter Tabs** — Switch between All, Pending, and Done views
- ✅ **Mark Done / Undo** — Toggle task completion per task
- 🗑️ **Bulk Clear** — Remove all completed tasks in one click
- 🕐 **Timestamps** — Each task shows time of creation
- 💬 **Empty States** — Contextual messages per filter view

---

## 📁 Project Structure

```
taskflow/
├── app.py              # Main Streamlit application
├── main.py             # main console based file
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
streamlit>=1.30.0
```

### 2. Run locally

```bash
streamlit run app.py
```

Opens at → **http://localhost:8501**

---

## 🖥️ App Overview

```
┌─────────────────────────────────────┐
│  ✦ Taskflow          FOCUS & SHIP   │
├──────────────┬──────────┬───────────┤
│  3 Pending   │ 2 Done   │ 5 Total   │
├─────────────────────────────────────┤
│  [ Task name... ] [Priority] [Add]  │
├─────────────────────────────────────┤
│  All | Pending | Done    [Clear 2]  │
│  ─────────────────────────────────  │
│  ● Buy groceries       Medium  ...  │
│  ● Fix login bug    🔴 High    ...  │
│  ✓ Write report     🟢 Low     ...  │
└─────────────────────────────────────┘
```

---

## 📖 How to Use

| Action | Steps |
|---|---|
| **Add a task** | Type in the input → select priority → click **Add** |
| **Complete a task** | Click **Done** button next to the task |
| **Undo completion** | Click **Undo** on a completed task |
| **Delete a task** | Click **✕** on any task |
| **Filter tasks** | Click **All / Pending / Done** tabs |
| **Clear completed** | Click **Clear N done** button |

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| Python 3.8+ | Language |
| Streamlit | Web framework |
| CSS3 | Custom dark theme & components |
| Google Fonts | DM Sans + DM Mono |


## 📄 License

MIT — free to use and modify.
