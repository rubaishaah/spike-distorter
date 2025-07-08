import streamlit as st
import numpy as np
import plotly.graph_objects as go
from streamlit.components.v1 import html
import sounddevice as sd

# --- App Config ---
st.set_page_config(
    page_title="Spike Distorter", 
    page_icon="🧠",
    layout="wide"
)

# --- CSS Animation ---
st.markdown("""
<style>
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}
.neuron-pulse {
    animation: pulse 2s infinite;
    display: inline-block;
    color: #4e54c8;
}
</style>
""", unsafe_allow_html=True)

# --- Header (Fixed) ---
st.markdown(
    """<h1 style='text-align: center;'>
     <span class='neuron-pulse'>Spike Distorter</span>
    </h1>""", 
    unsafe_allow_html=True
)

# --- Sidebar Controls ---
with st.sidebar:
    st.header("⚙️ Controls")
    user_input = st.text_input("**Binary Signal**", "101010", help="E.g., 1010 = beep-silence-beep-silence")
    noise_level = st.slider("**Noise Level**", 0.0, 1.0, 0.3, 0.01)
    if st.button("🎵 **Play Corrupted Signal**", type="primary"):
        st.session_state.play = True
    st.markdown("""
    **Explore Further:**
    - [📚 Theory Explanation](/Theory)
    - [GitHub Repo](https://github.com/your-repo)
    """)
    
# --- Signal Processing ---
try:
    signal = np.array([int(bit) for bit in user_input])
except:
    st.error("⚠️ Only 0s and 1s allowed!")
    st.stop()

# Add noise
noise_mask = np.random.random(len(signal)) < noise_level
corrupted_signal = np.where(noise_mask, 1 - signal, signal)

# --- Plotly Interactive Figure ---
fig = go.Figure()
# Plot corrupted signal FIRST (bottom layer)
fig.add_trace(go.Scatter(
    x=np.arange(len(corrupted_signal)),
    y=corrupted_signal,
    mode='markers+lines',
    name='Corrupted Signal',
    marker=dict(color='#ffffff', size=12, symbol='x-thin', line=dict(width=4)),
    line=dict(color='rgba(255,255,255,0.8)', width=2)
))

# Plot original signal LAST (top layer)
fig.add_trace(go.Scatter(
    x=np.arange(len(signal)),
    y=signal,
    mode='markers+lines',
    name='Original Signal',
    marker=dict(color='#4e54c8', size=10),
    line=dict(color='#4e54c8', width=3)
))


# Update layout for clarity
fig.update_layout(
    title="<b>Signal Corruption by Neural Noise</b>",
    xaxis_title="Time Step",
    yaxis_title="Spike (1) or Silence (0)",
    hovermode="x unified",
    template="plotly_white",
    height=400,
    showlegend=True
)

# --- Display Plotly ---
st.plotly_chart(fig, use_container_width=True)

# --- Audio Playback ---
def generate_beep(bit, duration=0.2, freq=880):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t) * bit

if 'play' in st.session_state:
    audio = np.concatenate([generate_beep(bit) for bit in corrupted_signal])
    sd.play(audio, samplerate=44100)
    st.success(f"🔊 Playing: {''.join(map(str, corrupted_signal))}")

# --- Stats Dashboard ---
col1, col2 = st.columns(2)
with col1:
    st.metric("**Error Rate**", f"{np.mean(signal != corrupted_signal):.0%}")
with col2:
    st.metric("**Surviving Spikes**", 
              f"{np.sum(corrupted_signal == 1)}/{np.sum(signal == 1)}",
              help="How many original spikes made it through")

# --- Footer ---
st.markdown("---")
st.caption("""
    *Built with ♥ using Streamlit + Plotly | [GitHub](https://github.com/)*  
    *Try hovering/zooming the chart!*
""")