"""
🏠 Dashboard Perseo - Página Principal
Sistema de Análisis de Clientes y Suscripciones
"""
import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Perseo | Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Función para cargar imagen como base64
def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Mostrar logo
logo_base64 = get_image_base64("perseo-logo-negro.png")
if logo_base64:
    st.markdown(
        f"""
        <style>
            .logo-container {{
                text-align: center;
                padding: 2rem 0 2rem 0;
            }}
            .logo-container img {{
                max-width: 250px;
                height: auto;
            }}
        </style>
        <div class="logo-container">
            <img src="data:image/png;base64,{logo_base64}" alt="Perseo Logo">
        </div>
        """,
        unsafe_allow_html=True
    )

# Título principal
st.title("🏠 Sistema de Dashboards Perseo")
st.markdown("### Bienvenido al análisis de clientes y suscripciones")
st.markdown("---")

# Instrucciones
st.markdown("""
👈 **Selecciona un dashboard en el menú lateral** para comenzar el análisis.

Cada dashboard incluye:
- 🔍 **5 Filtros interactivos** (Estado, Producto, Ciudad, Distribuidor, Año)
- 📊 **7 KPIs principales** (Clientes, MRR, ARR, Churn, Retención)
- 📈 **6 Visualizaciones** (Gráficos de barras, donas, apilados)
- 📥 **Exportación a CSV** de datos filtrados
""")

st.markdown("<br>", unsafe_allow_html=True)

# Cards de información
col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **📊 Facturito**
    
    Análisis de suscripciones de Facturito con métricas de retención y churn.
    
    📈 **2,462 clientes**
    """)

with col2:
    st.success("""
    **🌐 Perseo WEB**
    
    Dashboard para clientes de plataforma WEB con KPIs de negocio.
    
    📈 **1,033 clientes**
    """)

with col3:
    st.warning("""
    **💻 Perseo PC**
    
    Análisis de producto PC con métricas detalladas de uso.
    
    📈 **622 clientes**
    """)

st.markdown("---")

# Características
st.markdown("### ✨ Características Principales")

col_feat1, col_feat2 = st.columns(2)

with col_feat1:
    st.markdown("""
    **🎯 Análisis Completo**
    - Filtrado dinámico por múltiples criterios
    - KPIs actualizados en tiempo real
    - Visualizaciones interactivas con Plotly
    - Exportación de datos personalizados
    """)

with col_feat2:
    st.markdown("""
    **📊 Métricas de Negocio**
    - MRR y ARR calculados automáticamente
    - Tasa de Churn y Retención
    - Distribución geográfica de clientes
    - Análisis por distribuidor y producto
    """)

st.markdown("---")

# Información adicional
with st.expander("ℹ️ Información sobre los datos"):
    st.markdown("""
    **Fuente de datos**: Google Drive (actualización automática)
    
    **Última actualización**: Los datos se cargan en tiempo real desde Google Drive
    
    **Caché**: Los datos se cachean por 1 hora para mejor rendimiento
    
    **Privacidad**: Los datos están protegidos con permisos de solo lectura
    """)

# Footer
st.markdown("---")
logo_footer_base64 = get_image_base64("perseo-logo-negro.png")

footer_html = f"""
<div style='text-align: center; padding: 2rem 0;'>
    <img src="data:image/png;base64,{logo_footer_base64}" alt="Perseo" style="max-width: 120px; margin-bottom: 1rem;">
    <p style='color: gray; margin: 0;'>Sistema de Dashboards Perseo - Análisis de Clientes y Suscripciones</p>
    <p style='color: gray; font-size: 0.9rem;'>Desarrollado con Streamlit | © 2026 Perseo</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
