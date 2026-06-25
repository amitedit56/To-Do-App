import streamlit as st
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Taskflow",
    page_icon="✦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font import ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&family=DM+Mono:wght@400;500&display=swap');

/* ── Reset & base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stApp"] {
    background: #0f0f11 !important;
    color: #e8e6e3 !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: #0f0f11 !important;
}

[data-testid="stHeader"] { display: none !important; }

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }

/* ── App shell ── */
.block-container {
    max-width: 680px !important;
    padding: 3rem 1.5rem 4rem !important;
    margin: 0 auto !important;
}

/* ── Wordmark header ── */
.app-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 2.5rem;
}
.app-logo {
    width: 34px; height: 34px;
    background: #c8f135;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 700; color: #0f0f11;
    flex-shrink: 0;
}
.app-title {
    font-size: 1.35rem;
    font-weight: 600;
    letter-spacing: -0.02em;
    color: #f0ede9;
}
.app-subtitle {
    font-size: 0.78rem;
    color: #5a5a60;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-left: auto;
}

/* ── Stats row ── */
.stats-row {
    display: flex;
    gap: 12px;
    margin-bottom: 2rem;
}
.stat-card {
    flex: 1;
    background: #1a1a1e;
    border: 1px solid #27272d;
    border-radius: 12px;
    padding: 1rem 1.2rem;
}
.stat-number {
    font-size: 1.9rem;
    font-weight: 600;
    color: #f0ede9;
    line-height: 1;
    letter-spacing: -0.03em;
}
.stat-label {
    font-size: 0.73rem;
    color: #5a5a60;
    margin-top: 4px;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.stat-card.accent .stat-number { color: #c8f135; }

/* ── Section labels ── */
.section-label {
    font-size: 0.72rem;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #5a5a60;
    margin-bottom: 0.6rem;
}

/* ── Input area ── */
[data-testid="stTextInput"] input {
    background: #1a1a1e !important;
    border: 1px solid #27272d !important;
    border-radius: 10px !important;
    color: #e8e6e3 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    padding: 0.7rem 1rem !important;
    transition: border-color .2s;
}
[data-testid="stTextInput"] input:focus {
    border-color: #c8f135 !important;
    box-shadow: 0 0 0 3px rgba(200, 241, 53, 0.08) !important;
    outline: none !important;
}
[data-testid="stTextInput"] label { display: none !important; }

/* ── Primary button ── */
[data-testid="stButton"] > button {
    background: #c8f135 !important;
    color: #0f0f11 !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.65rem 1.4rem !important;
    cursor: pointer !important;
    transition: opacity .15s, transform .1s !important;
    white-space: nowrap !important;
}
[data-testid="stButton"] > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}
[data-testid="stButton"] > button:active { transform: translateY(0) !important; }

/* ── Danger (delete) buttons ── */
[data-testid="stButton"].delete-btn > button,
button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid #2e2e35 !important;
    color: #5a5a60 !important;
}
[data-testid="stButton"].delete-btn > button:hover { border-color: #ff4d4f !important; color: #ff4d4f !important; }

/* ── Task cards ── */
.task-card {
    background: #1a1a1e;
    border: 1px solid #27272d;
    border-radius: 12px;
    padding: 0.9rem 1.1rem;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: border-color .2s;
}
.task-card:hover { border-color: #3a3a42; }
.task-card.done {
    opacity: 0.45;
    background: #131315;
}
.task-bullet {
    width: 8px; height: 8px;
    background: #c8f135;
    border-radius: 50%;
    flex-shrink: 0;
}
.task-card.done .task-bullet {
    background: #3a3a42;
}
.task-text {
    flex: 1;
    font-size: 0.92rem;
    color: #d4d2cf;
    line-height: 1.4;
}
.task-card.done .task-text {
    text-decoration: line-through;
    color: #4a4a50;
}
.task-meta {
    font-size: 0.7rem;
    color: #3a3a42;
    font-family: 'DM Mono', monospace;
    flex-shrink: 0;
}

/* ── Priority badge ── */
.badge {
    display: inline-block;
    font-size: 0.65rem;
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 2px 7px;
    border-radius: 4px;
    flex-shrink: 0;
}
.badge-high   { background: rgba(255,77,79,.15);  color: #ff7875; }
.badge-medium { background: rgba(255,167,38,.12); color: #ffa940; }
.badge-low    { background: rgba(82,196,26,.12);  color: #73d13d; }

/* ── Filter tabs ── */
[data-testid="stRadio"] {
    background: #1a1a1e !important;
    border: 1px solid #27272d !important;
    border-radius: 10px !important;
    padding: 4px !important;
    display: inline-flex !important;
}
[data-testid="stRadio"] label {
    font-size: 0.8rem !important;
    color: #5a5a60 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stRadio"] [data-testid="stMarkdownContainer"] p { color: #5a5a60 !important; }

/* ── Select box ── */
[data-testid="stSelectbox"] > div > div {
    background: #1a1a1e !important;
    border: 1px solid #27272d !important;
    border-radius: 10px !important;
    color: #e8e6e3 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
}
[data-testid="stSelectbox"] label { display: none !important; }

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 3rem 1rem;
    color: #3a3a42;
}
.empty-icon { font-size: 2rem; margin-bottom: 0.8rem; }
.empty-text { font-size: 0.88rem; line-height: 1.6; }

/* ── Toast-style alerts ── */
[data-testid="stSuccess"], [data-testid="stError"], [data-testid="stInfo"] {
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.88rem !important;
    border: none !important;
}

/* ── Divider ── */
hr { border: none; border-top: 1px solid #1e1e23; margin: 1.5rem 0; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2e2e35; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────────────────────
if "tasks" not in st.session_state:
    st.session_state.tasks = []       # list of dicts
if "input_key" not in st.session_state:
    st.session_state.input_key = 0   # bump to clear input


def add_task(text: str, priority: str):
    st.session_state.tasks.append({
        "id": datetime.now().timestamp(),
        "text": text.strip(),
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%b %d, %H:%M"),
    })


def toggle_task(task_id):
    for t in st.session_state.tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            break


def delete_task(task_id):
    st.session_state.tasks = [t for t in st.session_state.tasks if t["id"] != task_id]


def clear_done():
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]


# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="app-logo">✦</div>
    <div class="app-title">Taskflow</div>
    <div class="app-subtitle">Focus &amp; Ship</div>
</div>
""", unsafe_allow_html=True)

# ── Stats ────────────────────────────────────────────────────────────────────
total   = len(st.session_state.tasks)
done    = sum(1 for t in st.session_state.tasks if t["done"])
pending = total - done

st.markdown(f"""
<div class="stats-row">
    <div class="stat-card accent">
        <div class="stat-number">{pending}</div>
        <div class="stat-label">Pending</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{done}</div>
        <div class="stat-label">Completed</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">{total}</div>
        <div class="stat-label">Total tasks</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Add task ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">New task</div>', unsafe_allow_html=True)

col_input, col_pri, col_btn = st.columns([4, 2, 1.4])

with col_input:
    new_task = st.text_input(
        "task",
        placeholder="What needs to be done?",
        key=f"task_input_{st.session_state.input_key}",
        label_visibility="collapsed",
    )

with col_pri:
    priority = st.selectbox(
        "priority",
        ["🔴 High", "🟡 Medium", "🟢 Low"],
        index=1,
        label_visibility="collapsed",
    )

with col_btn:
    add_clicked = st.button("Add", use_container_width=True)

if add_clicked:
    if new_task.strip():
        pri_map = {"🔴 High": "high", "🟡 Medium": "medium", "🟢 Low": "low"}
        add_task(new_task, pri_map[priority])
        st.session_state.input_key += 1
        st.rerun()
    else:
        st.error("Type a task name first.")

st.markdown("<hr>", unsafe_allow_html=True)

# ── Filter & clear ────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Tasks</div>', unsafe_allow_html=True)

col_filter, col_clear = st.columns([4, 2])

with col_filter:
    view = st.radio(
        "filter",
        ["All", "Pending", "Done"],
        horizontal=True,
        label_visibility="collapsed",
    )

with col_clear:
    if done > 0:
        if st.button(f"Clear {done} done", use_container_width=True):
            clear_done()
            st.rerun()

# ── Task list ─────────────────────────────────────────────────────────────────
tasks = st.session_state.tasks

if view == "Pending":
    filtered = [t for t in tasks if not t["done"]]
elif view == "Done":
    filtered = [t for t in tasks if t["done"]]
else:
    filtered = tasks

badge_cls  = {"high": "badge-high", "medium": "badge-medium", "low": "badge-low"}
badge_text = {"high": "High",       "medium": "Medium",       "low": "Low"}

if not filtered:
    label = "Nothing here yet — add your first task above." if view == "All" else \
            "No pending tasks. Nice work!" if view == "Pending" else \
            "No completed tasks yet."
    st.markdown(f"""
    <div class="empty-state">
        <div class="empty-icon">{"✦" if view == "All" else "🎯" if view == "Pending" else "✅"}</div>
        <div class="empty-text">{label}</div>
    </div>
    """, unsafe_allow_html=True)
else:
    for task in reversed(filtered):
        done_cls = "done" if task["done"] else ""
        bcls     = badge_cls[task["priority"]]
        btxt     = badge_text[task["priority"]]

        col_card, col_toggle, col_del = st.columns([8, 1.5, 1.2])

        with col_card:
            st.markdown(f"""
            <div class="task-card {done_cls}">
                <div class="task-bullet"></div>
                <div class="task-text">{task['text']}</div>
                <span class="badge {bcls}">{btxt}</span>
                <div class="task-meta">{task['created']}</div>
            </div>
            """, unsafe_allow_html=True)

        with col_toggle:
            label = "Undo" if task["done"] else "Done"
            if st.button(label, key=f"tog_{task['id']}", use_container_width=True):
                toggle_task(task["id"])
                st.rerun()

        with col_del:
            if st.button("✕", key=f"del_{task['id']}", use_container_width=True):
                delete_task(task["id"])
                st.rerun()