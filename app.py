import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# 🎨 ESTILOS DANY OCEAN
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #020617, #0c4a6e);
    color: #e0f2fe;
}

/* Banner */
.banner {
    background: linear-gradient(90deg, #0284c7, #38bdf8);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0px 5px 25px rgba(0,0,0,0.4);
}

/* Botones */
.stButton > button {
    background: linear-gradient(90deg, #0ea5e9, #0369a1);
    color: white;
    border-radius: 14px;
    padding: 12px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.07);
    background: linear-gradient(90deg, #0284c7, #075985);
}
</style>
""", unsafe_allow_html=True)

# 🐋 Banner
st.markdown("""
<div class="banner">
    <h1>🐋 MQTT Control - Dany 🌊</h1>
    <p>FIND US IN THE WAVES 💙</p>
</div>
""", unsafe_allow_html=True)

st.write("🐍 Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):
    print("el dato ha sido publicado")

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write("📩 Mensaje recibido:", message_received)

broker="157.230.214.127"
port=1883
client1= paho.Client("BALLENITA06")
client1.on_message = on_message

st.subheader("🎛️ Control Digital")

# 🔵 ON (CORREGIDO EL TOPIC)
if st.button('🔵 Encender'):
    act1="ON"
    client1= paho.Client("BALLENITA06")
    client1.on_publish = on_publish
    client1.connect(broker,port)
    message =json.dumps({"Act1":act1})
    client1.publish("cmqtt_amotorcito", message)  # ✅ CORREGIDO

# ⚫ OFF
if st.button('⚫ Apagar'):
    act1="OFF"
    client1= paho.Client("BALLENITA06")
    client1.on_publish = on_publish
    client1.connect(broker,port)
    message =json.dumps({"Act1":act1})
    client1.publish("cmqtt_amotorcito", message)

st.divider()

st.subheader("🎚️ Control Analógico")

values = st.slider('🌊 Nivel de intensidad',0.0, 100.0)
st.write('Valor:', values)

if st.button('✨ Enviar valor'):
    client1= paho.Client("BALLENITA06")
    client1.on_publish = on_publish
    client1.connect(broker,port)
    message =json.dumps({"Analog": float(values)})
    client1.publish("cmqtt_slucecita", message)



