import streamlit as st

st.set_page_config(
    page_title="Spike Distorter - Theory",
    page_icon="📚"
)

# Page Header
st.title("🧠 Neuroscience Behind Spike Distortion")
st.markdown("""
    *Understanding how neural systems handle noisy signals*
""")

# Theory Section
with st.expander("🔍 Core Concepts", expanded=True):
    st.markdown("""
    ### 1. Neural Spikes (Action Potentials)
    Neurons communicate via brief electrical impulses called *action potentials* or *spikes*:
    - **Binary nature**: All-or-none events (1=spike, 0=silence)
    - **Timing matters**: Information encoded in spike timing patterns
    
    ```python
    # Your simulation approximates this with binary arrays
    signal = [1, 0, 1, 1, 0]  # Spike train
    ```
    """)

    # Labster image with responsive sizing
    st.image("https://images.my.labster.com/1e5dcd3b-327e-44c4-8b0a-ceb4cc58b784/SMV_ActionPotential.en.x512.png",
             width=500,  # Optimal width for Streamlit
             caption="Action potential phases (Source: Labster)")
    

with st.expander("📊 Noise in Biological Systems"):
    st.markdown("""
    ### 2. Sources of Neural Noise
    | Source | Effect | Simulation Equivalent |
    |--------|--------|-----------------------|
    | Ion channel variability | Random spike timing | `np.random.random() < noise_level` |
    | Synaptic unreliability | Dropped spikes | Bit flips in your code |
    | Network crosstalk | Added false spikes | Extra 1s in output |
    
    **Why noise isn't always bad**:
    - Improves generalization (like dropout in neural networks)
    - Enables stochastic resonance
    """)

# References Section
st.divider()
st.header("📚 Academic References")
st.markdown("""
1. **Carandini & Heeger (2012)**  
   *Normalization as a canonical neural computation*  
   [Nature Reviews Neuroscience](https://www.nature.com/articles/nrn3353)  
   - Key paper on noise in cortical circuits

2. **Faisal et al. (2008)**  
   *Noise in the nervous system*  
   [Nature Reviews Neuroscience](https://www.nature.com/articles/nrn2258)  
   - Comprehensive review of neural noise sources

3. **Stein et al. (2005)**  
   *Neuronal variability: noise or part of the computation?*  
   [Nature Neuroscience](https://www.nature.com/articles/nn0705_811)  
   - How brains exploit noise
""")

# Link back to main app
st.markdown("""
---
🔧 **Ready to experiment?** [Go to the Spike Distorter demo →](/)
""")