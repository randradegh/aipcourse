import streamlit as st

# Configuración de página
st.set_page_config(
    page_title="Curso ChatGPT",
    page_icon="🤖",
    layout="wide"
)


# Título y descripción

st.image("images/encabezado_curso_ai_02.jpg", width=800, use_column_width=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/768px-ChatGPT_logo.svg.png', width=150, use_column_width=False)
    
st.title("Clase Gratuita: ChatGPT, explorando sus posibilidades")
"""
## **¡Descubre el Poder de las Peticiones para ChatGPT!**

¿Quieres llevar tus habilidades al siguiente nivel en educación, negocios y análisis de datos? ¡Entonces, nuestra clase gratuita es perfecta para ti!

En esta experiencia única, te sumergirás en el fascinante mundo de las peticiones para ChatGPT, aprendiendo a crear interacciones inteligentes y efectivas. Imagina la capacidad de formular preguntas que despierten respuestas precisas y útiles de una IA avanzada.

### ✨ **¿Qué Aprenderás?**

1. **Educación Transformada:** Descubre cómo optimizar la enseñanza y el aprendizaje con peticiones inteligentes. Desde la creación de contenido educativo hasta la asistencia personalizada, las posibilidades son infinitas.

2. **Impulsa tus Negocios:** Aprende a utilizar peticiones para ChatGPT para mejorar la comunicación con clientes, generar ideas creativas y potenciar la eficiencia empresarial. ¡Impulsa tu empresa con conversaciones inteligentes!

3. **Análisis de Datos Sin Esfuerzo:** Explora cómo las peticiones bien formuladas pueden simplificar el análisis de datos. Desde la generación de informes hasta la interpretación de resultados, descubre cómo ChatGPT puede ser tu aliado en el mundo del análisis.

### **Beneficios Exclusivos:**

- ✔️ **Curso Gratuito de una Hora:** Sumérgete en una sesión interactiva y práctica que transformará tu enfoque hacia las peticiones para ChatGPT.
  
- 🎓 **Ejemplos de peticiones:** Obtendrás un archivo con los ejemplos de las peticiones que usaremos en la clase gratuita.

- 💰 **Descuento:** Un descuento especial sobre un pŕoximo curso de varias horas de duración.

¡No pierdas la oportunidad de introducirte en el arte de las peticiones y desbloquear un mundo de posibilidades con ChatGPT! 

**Regístrate ahora y prepárate para una experiencia educativa como ninguna otra.**


¡Te esperamos para descubrir juntos el futuro emocionante de las peticiones para ChatGPT!

"""

st.header("Temas de la Clase")
col1, col2, col3 = st.columns(3)
# Secciones para cada tema
with col1:
    st.subheader("📝 Educación ")
    st.write("Aprende cómo utilizar ChatGPT para mejorar la enseñanza y el aprendizaje en el ámbito educativo.")

with col2:
    st.subheader("💼 Negocios ")
    st.write("Explora cómo integrar ChatGPT en tu estrategia comercial para mejorar la comunicación y la interacción con los clientes.")

with col3:
    st.subheader("📊 Análisis de Datos ")
    st.write("Descubre cómo ChatGPT puede ser una herramienta valiosa en el análisis de datos y la generación de informes.")

# Invitación al curso
st.header("¡Únete a Nosotros!")
st.write("Este curso de una hora te proporcionará insights sobre las bondades y limitaciones de ChatGPT en diversos contextos.")

st.info("## ¡Te esperamos el **4 de enero de 2024 a las 18 horas**!")

"""
Envía un correo a randradedev@gmail.com con la siguiente información

- Nombre completo.
- Grado de estudios.
- Ocupación principal.
- ¿En qué áreas usarás tus conocimientos sobre las peticiones (*prompts*) a ChatGPT y otras AIG?
- ¿Ya tienes una cuenta para usar ChatGPT 3.5?

## Requisitos
- Conexión internet.
- Conocimientos básicos de manejo de un navegador en Windows, Mac o Linux.
- Poseer una cuenta de ChatGPT 3.5 o superior. 🔗 [Sitio de ChatGPT](https://chat.openai.com/)
- Manejo de Google Meet.
"""

# Pie de página
st.markdown("---")
st.write("© 2023 Curso ChatGPT. Todos los derechos reservados.")
