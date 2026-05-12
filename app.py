"""
Dashboard Principal Perseo
Punto de entrada para seleccionar el dashboard a visualizar
"""
import streamlit as st
import base64

# Configuración de la página
st.set_page_config(
    page_title="Dashboards Perseo | Selección",
    page_icon="📊",
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
st.title("📊 Sistema de Dashboards Perseo")
st.markdown("### Análisis de Clientes y Suscripciones")
st.markdown("---")

# Descripción
st.markdown("""
Bienvenido al sistema de análisis de datos de Perseo. Selecciona el dashboard que deseas visualizar:
""")

st.markdown("<br>", unsafe_allow_html=True)

# Crear tres columnas para los dashboards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='text-align: center; padding: 2rem; border: 2px solid #1E88E5; border-radius: 10px; height: 300px; display: flex; flex-direction: column; justify-content: center;'>
        <h2>📊 Facturito</h2>
        <p>Dashboard de análisis para clientes de Facturito con métricas de suscripción y retención</p>
        <p><strong>2,462 clientes</strong></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🚀 Ver Dashboard Facturito", "dashboard_facturito.py", use_container_width=True)

with col2:
    st.markdown("""
    <div style='text-align: center; padding: 2rem; border: 2px solid #4CAF50; border-radius: 10px; height: 300px; display: flex; flex-direction: column; justify-content: center;'>
        <h2>🌐 Perseo WEB</h2>
        <p>Dashboard de análisis para clientes de plataforma WEB con KPIs de negocio</p>
        <p><strong>1,033 clientes</strong></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🚀 Ver Dashboard WEB", "dashboard_web.py", use_container_width=True)

with col3:
    st.markdown("""
    <div style='text-align: center; padding: 2rem; border: 2px solid #FF9800; border-radius: 10px; height: 300px; display: flex; flex-direction: column; justify-content: center;'>
        <h2>💻 Perseo PC</h2>
        <p>Dashboard de análisis para clientes de producto PC con métricas detalladas</p>
        <p><strong>622 clientes</strong></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("🚀 Ver Dashboard PC", "dashboard_pc.py", use_container_width=True)

st.markdown("---")

# Características
st.markdown("### ✨ Características de los Dashboards")
col_feat1, col_feat2, col_feat3 = st.columns(3)

with col_feat1:
    st.markdown("""
    **🔍 Filtros Interactivos**
    - Estado
    - Producto
    - Ciudad
    - Distribuidor
    - Año Inicio
    """)

with col_feat2:
    st.markdown("""
    **📈 7 KPIs Principales**
    - Total Clientes
    - Clientes Activos
    - MRR / ARR
    - Ticket Promedio
    - Tasa Churn
    - % Retención
    """)

with col_feat3:
    st.markdown("""
    **📊 Visualizaciones**
    - Gráficos de barras
    - Gráficos de dona
    - Gráficos apilados
    - Tablas interactivas
    - Exportación CSV
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
