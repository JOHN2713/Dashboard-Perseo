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

3. Asegúrate de tener los archivos Excel en la carpeta raíz:
   - `BASE FACTURITO OL.xlsx`
   - `BASE WEB OK (1).xlsx`
   - `BASE PRODUCTO PC.xlsx`

## 💻 Uso

Ejecuta cada dashboard en puertos diferentes:

### Dashboard Facturito (Puerto 8501)
```bash
streamlit run dashboard_facturito.py
```

### Dashboard Perseo WEB (Puerto 8502)
```bash
streamlit run dashboard_web.py --server.port 8502
```

### Dashboard Perseo PC (Puerto 8503)
```bash
streamlit run dashboard_pc.py --server.port 8503
```

Los dashboards estarán disponibles en:
- Facturito: http://localhost:8501
- Perseo WEB: http://localhost:8502
- Perseo PC: http://localhost:8503

## 📦 Estructura del Proyecto

```
Dashboard-Perseo/
├── dashboard_facturito.py       # Dashboard para Facturito
├── dashboard_web.py             # Dashboard para Perseo WEB
├── dashboard_pc.py              # Dashboard para Perseo PC
├── requirements.txt             # Dependencias del proyecto
├── perseo-logo-negro.png        # Logo Perseo (fondo claro)
├── perseo-logo-blanco.png       # Logo Perseo (fondo oscuro)
├── .streamlit/
│   └── config.toml             # Configuración de Streamlit
├── BASE FACTURITO OL.xlsx      # Datos de Facturito
├── BASE WEB OK (1).xlsx        # Datos de Perseo WEB
├── BASE PRODUCTO PC.xlsx       # Datos de Perseo PC
└── README.md                   # Este archivo
```

## 🛠️ Tecnologías Utilizadas

- **Streamlit 1.40.0**: Framework para aplicaciones web interactivas
- **Pandas 2.2.0**: Análisis y manipulación de datos
- **Plotly 5.18.0**: Visualizaciones interactivas
- **OpenPyXL 3.1.2**: Lectura de archivos Excel

## 🌐 Despliegue en Streamlit Cloud

Este proyecto está preparado para ser desplegado en Streamlit Cloud:

1. Sube tu repositorio a GitHub
2. Ve a [share.streamlit.io](https://share.streamlit.io)
3. Conecta tu repositorio
4. Despliega cada dashboard seleccionando el archivo correspondiente

## 📊 Datos Requeridos

Los archivos Excel deben contener las siguientes columnas principales:

- **Identificación**: ID del cliente
- **EMPRESAS**: Nombre de la empresa
- **CIUDAD**: Ubicación del cliente
- **Producto**: Producto/Servicio contratado
- **Estado**: Estado de la suscripción (Activo, Suspendido, Terminado, Inactivo)
- **Distribuidor**: Distribuidor asignado
- **Ingreso Mensual**: Ingreso mensual del cliente
- **Año Inicio**: Año de inicio de la suscripción
- **Inicio/Vence**: Fechas de inicio y vencimiento

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

---

**Nota**: Este proyecto requiere archivos de datos Excel específicos que no están incluidos en el repositorio por motivos de confidencialidad. Contacta al administrador para obtener acceso a los datos.
