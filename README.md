# 📊 Dashboard Perseo - Análisis de Clientes y Suscripciones

Sistema de dashboards interactivos desarrollados con Streamlit para analizar datos de clientes y suscripciones de los productos Perseo.

## 🌟 Características

- **3 Dashboards Especializados**: Facturito, Perseo WEB y Perseo PC
- **Filtros Interactivos**: Estado, Producto, Ciudad, Distribuidor, Año Inicio
- **7 KPIs en tiempo real**: Total Clientes, Clientes Activos, MRR, ARR, Ticket Promedio, Tasa Churn, Tasa de Retención
- **6 Visualizaciones por dashboard**: Gráficos de barras, donas y gráficos apilados
- **Exportación de datos**: Descarga de datos filtrados en formato CSV
- **Branding Perseo**: Logo corporativo integrado

## 📋 KPIs Disponibles

- 👥 **Total Clientes**: Cantidad total de clientes en el período
- ✅ **Clientes Activos**: Clientes con suscripción activa
- 💰 **MRR** (Monthly Recurring Revenue): Ingresos mensuales recurrentes
- 💎 **ARR** (Annual Recurring Revenue): Ingresos anuales recurrentes
- 🎯 **Ticket Promedio**: Valor promedio de ingreso por cliente
- 📉 **Tasa Churn**: Porcentaje de clientes perdidos
- 📈 **Tasa de Retención**: Porcentaje de clientes que permanecen activos

## 📊 Visualizaciones

1. **Barras**: Ingreso Mensual por Producto
2. **Barras**: Ingreso Mensual por Distribuidor
3. **Dona**: Distribución de Clientes por Estado
4. **Barras**: Top 10 Ciudades por Clientes
5. **Dona**: Ingreso Activo por Producto
6. **Barras Apiladas**: Productos por Distribuidor y Estado

## 🚀 Instalación Local

### Prerrequisitos

- Python 3.13 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. Clona este repositorio:
```bash
git clone https://github.com/JOHN2713/Dashboard-Perseo.git
cd Dashboard-Perseo
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. **Opción A - Usar archivos locales**:
   - Coloca los archivos Excel en la carpeta raíz:
     - `BASE FACTURITO OL.xlsx`
     - `BASE WEB OK (1).xlsx`
     - `BASE PRODUCTO PC.xlsx`

4. **Opción B - Cargar desde Google Drive** (automático):
   - Los dashboards están configurados para cargar desde Google Drive automáticamente
   - No necesitas los archivos Excel locales
   - Los datos se descargan al iniciar el dashboard

## ☁️ Despliegue en Streamlit Cloud

Este proyecto utiliza una **estructura multipage** que permite acceder a los 3 dashboards desde una sola aplicación desplegada.

### Pasos para desplegar:

1. Los datos se cargan automáticamente desde Google Drive
2. No necesitas subir archivos Excel a GitHub
3. Solo despliega **un archivo**: `Home.py`

### Configuración en Streamlit Cloud:

1. Ve a https://share.streamlit.io
2. Click en **"New app"**
3. Configuración:
   - **Repository**: `JOHN2713/Dashboard-Perseo`
   - **Branch**: `main`
   - **Main file path**: `Home.py` ⭐ **Importante**
4. Click en **"Deploy!"**

Una vez desplegado, tendrás acceso a los 3 dashboards desde el menú lateral de una sola aplicación.

**URL única**: `https://dashboard-perseo.streamlit.app`

### Archivos de datos en Google Drive

Los dashboards cargan los datos desde:
- **Facturito**: Google Drive (ID: 1fforhn03rynmhUva0SaN1SawnxmEm5dV)
- **Perseo WEB**: Google Drive (ID: 1wt2unhyUsXhKjQnjEXoB36tlP2eA5Jst)
- **Perseo PC**: Google Drive (ID: 168V0BCy0-LZDzeKQp-9sdJuXIbRQvOpd)

## 💻 Uso

### Opción 1: Multipage App (Recomendado)

Ejecuta la aplicación principal que incluye los 3 dashboards:

```bash
streamlit run Home.py
```

Esto abrirá la aplicación en http://localhost:8501 con un **menú lateral** que te permite navegar entre:
- 🏠 Home (página de bienvenida)
- 📊 Facturito
- 🌐 Perseo WEB
- 💻 Perseo PC

### Opción 2: Dashboards Individuales

Si prefieres ejecutar cada dashboard por separado:

#### Dashboard Facturito (Puerto 8501)
```bash
streamlit run dashboard_facturito.py
```

#### Dashboard Perseo WEB (Puerto 8502)
```bash
streamlit run dashboard_web.py --server.port 8502
```

#### Dashboard Perseo PC (Puerto 8503)
```bash
streamlit run dashboard_pc.py --server.port 8503
```

## 📦 Estructura del Proyecto

```
Dashboard-Perseo/
├── Home.py                          # 🏠 Página principal (punto de entrada)
├── pages/                           # 📁 Dashboards (multipage app)
│   ├── 1_📊_Facturito.py           # Dashboard para Facturito
│   ├── 2_🌐_Perseo_WEB.py          # Dashboard para Perseo WEB
│   └── 3_💻_Perseo_PC.py           # Dashboard para Perseo PC
├── dashboard_facturito.py           # Versión standalone de Facturito
├── dashboard_web.py                 # Versión standalone de WEB
├── dashboard_pc.py                  # Versión standalone de PC
├── requirements.txt                 # Dependencias del proyecto
├── perseo-logo-negro.png            # Logo Perseo (fondo claro)
├── perseo-logo-blanco.png           # Logo Perseo (fondo oscuro)
├── .streamlit/
│   └── config.toml                 # Configuración de Streamlit
├── test_google_drive.py            # Script de prueba de Google Drive
└── README.md                       # Este archivo
```

**Nota**: La estructura multipage permite acceder a los 3 dashboards desde una sola aplicación.

## 🛠️ Tecnologías Utilizadas

- **Streamlit 1.40.0**: Framework para aplicaciones web interactivas
- **Pandas 2.2.0**: Análisis y manipulación de datos
- **Plotly 5.18.0**: Visualizaciones interactivas
- **OpenPyXL 3.1.2**: Lectura de archivos Excel

## 📊 Datos Requeridos

Los dashboards cargan datos automáticamente desde Google Drive, por lo que no necesitas archivos locales para el despliegue en la nube.

Para uso local, los archivos Excel deben contener las siguientes columnas principales:

- **Identificación**: ID del cliente
- **EMPRESAS**: Nombre de la empresa
- **CIUDAD**: Ubicación del cliente
- **Producto**: Producto/Servicio contratado
- **Estado**: Estado de la suscripción (Activo, Suspendido, Terminado, Inactivo)
- **Distribuidor**: Distribuidor asignado
- **Ingreso Mensual**: Ingreso mensual del cliente
- **Año Inicio**: Año de inicio de la suscripción
- **Inicio/Vence**: Fechas de inicio y vencimiento

## 🔄 Carga de Datos Inteligente

Los dashboards implementan un sistema de carga dual:

1. **Primero**: Intentan cargar desde Google Drive (para Streamlit Cloud)
2. **Si falla**: Cargan desde archivo local (para desarrollo local)

Esto permite que funcionen tanto en producción como en desarrollo sin cambios de código.

## 🎨 Personalización

### Cambiar colores del tema

Edita el archivo `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1E88E5"        # Color principal
backgroundColor = "#FFFFFF"      # Fondo de la página
secondaryBackgroundColor = "#F0F2F6"  # Fondo secundario
textColor = "#262730"           # Color del texto
```

## 📝 Licencia

© 2026 Perseo. Todos los derechos reservados.

## 👥 Autor

Desarrollado por el equipo de análisis de datos de Perseo.

## 📧 Contacto

Para soporte o consultas sobre los dashboards, contacta al equipo de desarrollo de Perseo.

## 🔗 Enlaces Útiles

- **Repositorio GitHub**: https://github.com/JOHN2713/Dashboard-Perseo
- **Streamlit Cloud**: https://share.streamlit.io
- **Guía de Despliegue**: Ver [DEPLOY_GUIDE.md](DEPLOY_GUIDE.md)

## 📈 Próximas Mejoras

- [ ] Integración con base de datos en tiempo real
- [ ] Exportación de reportes en PDF
- [ ] Predicciones de churn con ML
- [ ] Dashboard consolidado con los 3 productos
- [ ] Notificaciones de alertas por email

---

**Nota**: Los datos se cargan desde Google Drive con permisos públicos de solo lectura. Para mayor seguridad en producción, considera migrar a una base de datos con autenticación.
