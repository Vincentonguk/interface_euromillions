import streamlit as st
import time

st.set_page_config(page_title="Quantum Avatar Bot", page_icon="🤖", layout="centered")

# Estados possíveis
states = {
    "thinking": {"bg": "#222222", "color": "#00ffff", "text": "🤔 Thinking..."},
    "responding": {"bg": "#222222", "color": "#00ff00", "text": "💬 Responding..."},
    "learning": {"bg": "#222222", "color": "#ffcc00", "text": "📚 Learning..."},
    "idle": {"bg": "#222222", "color": "#888888", "text": "💤 Idle..."}
}

# Inicializa estado da sessão
if "state" not in st.session_state:
    st.session_state.state = "idle"
if "last_user_msg" not in st.session_state:
    st.session_state.last_user_msg = ""

st.markdown(
    """
    <style>
    .avatar {
        animation: pulse 2s infinite;
        width: 300px;
        height: auto;
    }

    @keyframes pulse {
      0% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.05); opacity: 0.7; }
      100% { transform: scale(1); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🧠 Quantum Avatar Bot")

# Campo de mensagem
user_msg = st.text_input("Digite sua mensagem:")
if st.button("Enviar") and user_msg:
    st.session_state.last_user_msg = user_msg
    st.session_state.state = "thinking"
    st.experimental_rerun()

if st.session_state.state == "thinking":
    st.markdown(
        f"""
        <div style="background-color: {states['thinking']['bg']}; padding: 20px; border-radius: 10px; text-align: center;">
            <img src="assets/avatar.png" class="avatar"><br>
            <span style="color: {states['thinking']['color']}; font-size: 24px;">{states['thinking']['text']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    time.sleep(2)
    st.session_state.state = "responding"
    st.experimental_rerun()

elif st.session_state.state == "responding":
    resposta = f"Você disse: {st.session_state.last_user_msg}. Aqui está minha resposta!"
    st.markdown(
        f"""
        <div style="background-color: {states['responding']['bg']}; padding: 20px; border-radius: 10px; text-align: center;">
            <img src="assets/avatar.png" class="avatar"><br>
            <span style="color: {states['responding']['color']}; font-size: 24px;">{states['responding']['text']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.success(resposta)
    st.session_state.state = "idle"

elif st.session_state.state == "idle":
    st.markdown(
        f"""
        <div style="background-color: {states['idle']['bg']}; padding: 20px; border-radius: 10px; text-align: center;">
            <img src="assets/avatar.png" class="avatar"><br>
            <span style="color: {states['idle']['color']}; font-size: 24px;">{states['idle']['text']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.info("Digite uma mensagem e clique em Enviar para interagir com o avatar.")
