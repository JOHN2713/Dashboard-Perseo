import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Facturito | Perseo",
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

# Mostrar logo en el header
logo_base64 = get_image_base64("perseo-logo-negro.png")
if logo_base64:
    st.markdown(
        f"""
        <style>
            .logo-container {{
                text-align: center;
                padding: 1rem 0 1rem 0;
            }}
            .logo-container img {{
                max-width: 180px;
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
st.title("📊 Dashboard Facturito")
st.markdown("---")

# Cargar datos con cache
@st.cache_data(ttl=3600)
def cargar_datos():
    """Carga datos desde Google Drive o archivo local con fallback"""
    import gdown
    import os
    
    # Intentar cargar desde Google Drive (para Streamlit Cloud)
    file_id = "1fforhn03rynmhUva0SaN1SawnxmEm5dV"
    
    try:
        st.sidebar.info("📡 Descargando datos desde Google Drive...")
        
        # Descargar archivo temporalmente
        temp_file = "temp_facturito.xlsx"
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, temp_file, quiet=False)
        
        # Leer el archivo descargado
        df = pd.read_excel(temp_file, engine='openpyxl')
        
        # Limpiar archivo temporal
        if os.path.exists(temp_file):
            os.remove(temp_file)
        
        st.sidebar.success("✅ Datos cargados desde Google Drive")
        
    except Exception as e:
        st.sidebar.warning(f"⚠️ Google Drive falló: {str(e)[:50]}...")
        # Intentar cargar desde archivo local
        try:
            st.sidebar.info("💾 Intentando cargar desde archivo local...")
            df = pd.read_excel('BASE FACTURITO OL.xlsx')
            st.sidebar.success("✅ Datos cargados desde archivo local")
        except Exception as e2:
            st.error(f"❌ Error al cargar datos: {str(e2)}")
            st.error("Por favor verifica que los archivos estén disponibles.")
            st.stop()
    
    # Asegurar que las fechas estén en formato correcto
    df['Inicio'] = pd.to_datetime(df['Inicio'], errors='coerce')
    df['Vence'] = pd.to_datetime(df['Vence'], errors='coerce')
    df['Fecha Ultimo Pago'] = pd.to_datetime(df['Fecha Ultimo Pago'], errors='coerce')
    return df

# Cargar datos
try:
    df = cargar_datos()
    st.sidebar.success(f"✅ Datos cargados: {len(df):,} registros")
except Exception as e:
    st.error(f"Error al cargar datos: {e}")
    st.stop()

st.sidebar.markdown("---")

# ============================================
# SIDEBAR - FILTROS
# ============================================
st.sidebar.header("🔍 Filtros")

# Filtro 1: Estado
estados_disponibles = ['Todos'] + sorted(df['Estado'].unique().tolist())
filtro_estado = st.sidebar.multiselect(
    "Estado",
    options=estados_disponibles[1:],
    default=estados_disponibles[1:]
)

# Filtro 2: Producto
productos_disponibles = ['Todos'] + sorted(df['Producto'].unique().tolist())
filtro_producto = st.sidebar.multiselect(
    "Producto",
    options=productos_disponibles[1:],
    default=productos_disponibles[1:]
)

# Filtro 3: Ciudad
ciudades_disponibles = sorted(df['CIUDAD'].unique().tolist())
filtro_ciudad = st.sidebar.multiselect(
    "Ciudad",
    options=ciudades_disponibles,
    default=ciudades_disponibles
)

# Filtro 4: Distribuidor
distribuidores_disponibles = sorted(df['Distribuidor'].unique().tolist())
filtro_distribuidor = st.sidebar.multiselect(
    "Distribuidor",
    options=distribuidores_disponibles,
    default=distribuidores_disponibles
)

# Filtro 5: Año Inicio
años_disponibles = sorted(df['Año Inicio'].unique().tolist())
filtro_año = st.sidebar.multiselect(
    "Año Inicio",
    options=años_disponibles,
    default=años_disponibles
)

# ============================================
# FILTRO DE PALABRAS CLAVE
# ============================================
st.sidebar.markdown("---")
with st.sidebar.expander("🔑 Filtro de Palabras Clave", expanded=False):
    st.markdown("**Buscar palabras clave en nombres de empresas**")
    
    # Palabras clave predefinidas sugeridas
    palabras_sugeridas = ["mecánica", "cevicheria", "ferretería", "restaurante", 
                          "farmacia", "tienda", "consultorio", "hotel", "panadería"]
    
    # Input para agregar palabras clave personalizadas
    palabras_personalizadas = st.text_input(
        "Agregar palabras clave (separadas por coma):",
        placeholder="Ej: mecánica, cevicheria, ferretería"
    )
    
    # Combinar palabras sugeridas y personalizadas
    if palabras_personalizadas:
        palabras_ingresadas = [p.strip().lower() for p in palabras_personalizadas.split(',') if p.strip()]
    else:
        palabras_ingresadas = []
    
    # Multiselect con palabras sugeridas
    palabras_seleccionadas_sugeridas = st.multiselect(
        "O selecciona palabras sugeridas:",
        options=palabras_sugeridas,
        default=[]
    )
    
    # Combinar todas las palabras clave
    todas_palabras_clave = palabras_ingresadas + palabras_seleccionadas_sugeridas

# ============================================
# APLICAR FILTROS
# ============================================
df_filtrado = df.copy()

if filtro_estado:
    df_filtrado = df_filtrado[df_filtrado['Estado'].isin(filtro_estado)]

if filtro_producto:
    df_filtrado = df_filtrado[df_filtrado['Producto'].isin(filtro_producto)]

if filtro_ciudad:
    df_filtrado = df_filtrado[df_filtrado['CIUDAD'].isin(filtro_ciudad)]

if filtro_distribuidor:
    df_filtrado = df_filtrado[df_filtrado['Distribuidor'].isin(filtro_distribuidor)]

if filtro_año:
    df_filtrado = df_filtrado[df_filtrado['Año Inicio'].isin(filtro_año)]

# Mostrar cantidad de registros filtrados
st.sidebar.markdown("---")
st.sidebar.metric("Registros filtrados", f"{len(df_filtrado):,}")

# ============================================
# ANÁLISIS DE PALABRAS CLAVE
# ============================================
if todas_palabras_clave:
    st.header("🔑 Análisis de Palabras Clave en Empresas")
    
    # Función para contar palabras clave
    def contar_palabra_clave(df, palabra):
        """Cuenta cuántas empresas contienen una palabra clave"""
        if 'EMPRESAS' in df.columns:
            # Convertir a string y minúsculas, manejar valores nulos
            empresas_str = df['EMPRESAS'].fillna('').astype(str).str.lower()
            return empresas_str.str.contains(palabra.lower(), na=False).sum()
        return 0
    
    # Crear diccionario de contadores
    contadores_palabras = {}
    for palabra in todas_palabras_clave:
        contadores_palabras[palabra] = contar_palabra_clave(df_filtrado, palabra)
    
    # Mostrar métricas en columnas
    st.subheader("📊 Contador de Palabras Clave")
    
    # Crear columnas dinámicas según la cantidad de palabras
    num_palabras = len(todas_palabras_clave)
    cols_por_fila = 4
    
    # Dividir en filas de columnas
    for i in range(0, num_palabras, cols_por_fila):
        cols = st.columns(cols_por_fila)
        palabras_fila = list(todas_palabras_clave)[i:i+cols_por_fila]
        
        for idx, palabra in enumerate(palabras_fila):
            with cols[idx]:
                st.metric(
                    label=f"🏢 {palabra.capitalize()}",
                    value=f"{contadores_palabras[palabra]} empresas"
                )
    
    # Gráfico de barras de palabras clave
    if contadores_palabras:
        st.subheader("📈 Distribución de Palabras Clave")
        
        # Crear DataFrame para el gráfico
        df_palabras = pd.DataFrame(
            list(contadores_palabras.items()),
            columns=['Palabra Clave', 'Cantidad']
        ).sort_values('Cantidad', ascending=True)
        
        fig_palabras = px.bar(
            df_palabras,
            x='Cantidad',
            y='Palabra Clave',
            orientation='h',
            title='Empresas que contienen cada palabra clave',
            labels={'Cantidad': 'Número de Empresas', 'Palabra Clave': 'Palabra Clave'},
            color='Cantidad',
            color_continuous_scale='Blues',
            text='Cantidad'
        )
        fig_palabras.update_traces(textposition='outside')
        fig_palabras.update_layout(height=max(300, len(df_palabras) * 50), showlegend=False)
        st.plotly_chart(fig_palabras, use_container_width=True)
    
    st.markdown("---")

# ============================================
# KPIs / TARJETAS
# ============================================
st.header("📈 Indicadores Clave (KPIs)")

# Calcular KPIs
total_clientes = len(df_filtrado)
clientes_activos = len(df_filtrado[df_filtrado['Estado'] == 'Activo'])
# mrr = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual'].sum()  # OCULTO TEMPORALMENTE
# arr = mrr * 12  # OCULTO TEMPORALMENTE
# ticket_promedio = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual'].mean()  # OCULTO TEMPORALMENTE

# Calcular Churn (clientes terminados + inactivos)
clientes_churn = len(df_filtrado[df_filtrado['Estado'].isin(['Terminado', 'Inactivo'])])
tasa_churn = (clientes_churn / total_clientes * 100) if total_clientes > 0 else 0
tasa_retencion = 100 - tasa_churn

# Mostrar KPIs en columnas
col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="👥 Total Clientes",
        value=f"{total_clientes:,}"
    )

with col2:
    st.metric(
        label="✅ Clientes Activos",
        value=f"{clientes_activos:,}",
        delta=f"{(clientes_activos/total_clientes*100):.1f}%" if total_clientes > 0 else "0%"
    )

# with col3:  # OCULTO TEMPORALMENTE
#     st.metric(
#         label="💰 MRR",
#         value=f"${mrr:,.2f}"
#     )

# with col4:  # OCULTO TEMPORALMENTE
#     st.metric(
#         label="💎 ARR",
#         value=f"${arr:,.2f}"
#     )

col5, col6 = st.columns(2)

# with col5:  # OCULTO TEMPORALMENTE
#     st.metric(
#         label="🎯 Ticket Promedio",
#         value=f"${ticket_promedio:,.2f}" if pd.notna(ticket_promedio) else "$0.00"
#     )

with col5:
    st.metric(
        label="📉 Tasa Churn",
        value=f"{tasa_churn:.2f}%",
        delta=f"-{clientes_churn} clientes",
        delta_color="inverse"
    )

with col6:
    st.metric(
        label="📈 % Tasa de Retención",
        value=f"{tasa_retencion:.2f}%",
        delta=f"{clientes_activos} activos"
    )

st.markdown("---")

# ============================================
# GRÁFICOS
# ============================================
st.header("📊 Visualizaciones")

# # Gráfico 1: Ingreso Mensual por Producto (Barras) - OCULTO TEMPORALMENTE
# st.subheader("💵 Ingreso Mensual por Producto")
# ingreso_producto = df_filtrado.groupby('Producto')['Ingreso Mensual'].sum().reset_index()
# ingreso_producto = ingreso_producto.sort_values('Ingreso Mensual', ascending=True)

# fig1 = px.bar(
#     ingreso_producto,
#     x='Ingreso Mensual',
#     y='Producto',
#     orientation='h',
#     title='Ingreso Mensual por Producto',
#     labels={'Ingreso Mensual': 'Ingreso Mensual ($)', 'Producto': 'Producto'},
#     color='Ingreso Mensual',
#     color_continuous_scale='Blues'
# )
# fig1.update_layout(height=400, showlegend=False)
# st.plotly_chart(fig1, width='stretch')

# st.markdown("---")

# # Gráfico 2: Ingreso Mensual por Distribuidor (Barras) - OCULTO TEMPORALMENTE
# st.subheader("🏢 Ingreso Mensual por Distribuidor")
# ingreso_distribuidor = df_filtrado.groupby('Distribuidor')['Ingreso Mensual'].sum().reset_index()
# ingreso_distribuidor = ingreso_distribuidor.sort_values('Ingreso Mensual', ascending=True)

# fig2 = px.bar(
#     ingreso_distribuidor,
#     x='Ingreso Mensual',
#     y='Distribuidor',
#     orientation='h',
#     title='Ingreso Mensual por Distribuidor',
#     labels={'Ingreso Mensual': 'Ingreso Mensual ($)', 'Distribuidor': 'Distribuidor'},
#     color='Ingreso Mensual',
#     color_continuous_scale='Greens'
# )
# fig2.update_layout(height=400, showlegend=False)
# st.plotly_chart(fig2, width='stretch')

# st.markdown("---")

# Fila de gráficos 3 y 4
col_left, col_right = st.columns(2)

with col_left:
    # Gráfico 3: Cliente por Estado (Dona)
    st.subheader("🎯 Clientes por Estado")
    clientes_estado = df_filtrado['Estado'].value_counts().reset_index()
    clientes_estado.columns = ['Estado', 'Cantidad']
    
    fig3 = px.pie(
        clientes_estado,
        values='Cantidad',
        names='Estado',
        title='Distribución de Clientes por Estado',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig3.update_traces(textposition='inside', textinfo='percent+label')
    fig3.update_layout(height=400)
    st.plotly_chart(fig3, width='stretch')

with col_right:
    # Gráfico 4: Recuento de Clientes por Ciudad (Barras)
    st.subheader("🌆 Clientes por Ciudad (Top 10)")
    clientes_ciudad = df_filtrado['CIUDAD'].value_counts().head(10).reset_index()
    clientes_ciudad.columns = ['Ciudad', 'Cantidad']
    clientes_ciudad = clientes_ciudad.sort_values('Cantidad', ascending=True)
    
    fig4 = px.bar(
        clientes_ciudad,
        x='Cantidad',
        y='Ciudad',
        orientation='h',
        title='Top 10 Ciudades por Número de Clientes',
        labels={'Cantidad': 'Número de Clientes', 'Ciudad': 'Ciudad'},
        color='Cantidad',
        color_continuous_scale='Oranges'
    )
    fig4.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig4, width='stretch')

st.markdown("---")

# Fila de gráficos 5 y 6
col_left2, col_right2 = st.columns(2)

with col_left2:
    # Gráfico 5: Ingreso Activo por Producto (Dona)
    st.subheader("💰 Ingreso Activo por Producto")
    df_activos = df_filtrado[df_filtrado['Estado'] == 'Activo']
    ingreso_activo_producto = df_activos.groupby('Producto')['Ingreso Mensual'].sum().reset_index()
    
    fig5 = px.pie(
        ingreso_activo_producto,
        values='Ingreso Mensual',
        names='Producto',
        title='Distribución de Ingresos Activos por Producto',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig5.update_traces(textposition='inside', textinfo='percent+label')
    fig5.update_layout(height=400)
    st.plotly_chart(fig5, width='stretch')

with col_right2:
    # # Gráfico 6: Recuento de Producto por Distribuidor y Estado (Barras Apiladas) - OCULTO TEMPORALMENTE
    # st.subheader("📦 Productos por Distribuidor y Estado")
    # producto_dist_estado = df_filtrado.groupby(['Distribuidor', 'Estado', 'Producto']).size().reset_index(name='Cantidad')
    
    # fig6 = px.bar(
    #     producto_dist_estado,
    #     x='Distribuidor',
    #     y='Cantidad',
    #     color='Estado',
    #     title='Recuento de Productos por Distribuidor y Estado',
    #     labels={'Cantidad': 'Cantidad de Productos', 'Distribuidor': 'Distribuidor'},
    #     barmode='stack',
    #     color_discrete_sequence=px.colors.qualitative.Set2
    # )
    # fig6.update_layout(height=400, xaxis_tickangle=-45)
    # st.plotly_chart(fig6, width='stretch')
    pass

st.markdown("---")

# ============================================
# TABLA DE DATOS
# ============================================
st.header("📋 Datos Detallados")

# Selector de columnas a mostrar
columnas_importantes = [
    'EMPRESAS', 'Producto', 'Estado', 'CIUDAD', 'Distribuidor',
    'Ingreso Mensual', 'Inicio', 'Vence', 'Estado Vencimiento',
    'Año Inicio', 'Antigüedad Meses', 'Segmento Precio'
]

columnas_seleccionadas = st.multiselect(
    "Selecciona las columnas a mostrar:",
    options=columnas_importantes,
    default=columnas_importantes[:6]
)

if columnas_seleccionadas:
    st.dataframe(
        df_filtrado[columnas_seleccionadas].head(100),
        width='stretch',
        height=400
    )
    
    # Botón de descarga
    csv = df_filtrado[columnas_seleccionadas].to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar datos filtrados (CSV)",
        data=csv,
        file_name=f'facturito_filtrado_{datetime.now().strftime("%Y%m%d")}.csv',
        mime='text/csv'
    )
else:
    st.warning("⚠️ Selecciona al menos una columna para mostrar los datos")

# Footer
st.markdown("---")
logo_footer_base64 = get_image_base64("perseo-logo-negro.png")

footer_html = f"""
<div style='text-align: center; padding: 2rem 0;'>
    <img src="data:image/png;base64,{logo_footer_base64}" alt="Perseo" style="max-width: 120px; margin-bottom: 1rem;">
    <p style='color: gray; margin: 0;'>Dashboard Facturito - Análisis de Clientes y Suscripciones</p>
    <p style='color: gray; font-size: 0.9rem;'>Desarrollado con Streamlit | © 2026 Perseo</p>
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
