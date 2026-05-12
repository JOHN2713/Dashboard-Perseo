---
name: dashboard-perseo-analisis-estrategico
description: Analiza archivos Excel y crea dashboards interactivos con Streamlit, incluyendo depuración de datos, creación de columnas estratégicas y visualizaciones avanzadas
version: 1.0
tags: [excel, dashboard, streamlit, analytics, data-cleaning, kpis]
author: Equipo de Análisis de Datos
date: 2026-04-28
---

# Dashboard Excel - Análisis y Visualización Estratégica

## Descripción

Este skill automatiza el proceso completo de análisis de datos desde archivos Excel, incluyendo:
- Depuración y limpieza de datos
- Creación de columnas estratégicas y KPIs
- Generación de dashboards interactivos con Streamlit
- Análisis de métricas de negocio (retención, churn, LTV, etc.)

## Cuándo usar este skill

Usa este skill cuando el usuario:
- Proporcione un archivo Excel con datos de clientes/suscripciones/ventas
- Solicite crear un dashboard o análisis de datos
- Pida análisis de KPIs, métricas o tendencias
- Necesite identificar oportunidades de negocio en datos

## Flujo de trabajo (3 pasos)

### PASO 1: Análisis y Depuración de Datos

1. **Cargar y analizar el archivo Excel**
   - Leer el archivo con pandas
   - Mostrar estructura: dimensiones, columnas, tipos de datos
   - Identificar valores nulos y duplicados
   - Generar estadísticas descriptivas

2. **Identificar columnas útiles**
   - Columnas de identificación (ID, nombre, empresa)
   - Columnas de ubicación (ciudad, barrio, país)
   - Columnas de producto/servicio
   - Columnas de fechas (inicio, vencimiento, pagos)
   - Columnas de estado (activo, suspendido, etc.)
   - Columnas financieras (precio, ingresos)
   - Columnas de contacto (vendedor, origen)

3. **Depurar datos**
   - Eliminar columnas duplicadas
   - Eliminar columnas innecesarias (datos personales sensibles, IDs redundantes)
   - Convertir fechas a formato datetime
   - Limpiar valores nulos (rellenar o marcar como "SIN ESPECIFICAR")
   - Crear columnas calculadas básicas:
     * Estado de suscripción
     * Categoría de precio
     * Ingreso anualizado
     * Tipo de cliente
     * Mes/Año de inicio y vencimiento
     * Duración del contrato

4. **Guardar datos depurados**
   - Formato Excel (.xlsx)
   - Formato CSV (.csv) para mayor compatibilidad

**Archivo de salida:** `{NOMBRE}_DEPURADO.xlsx`

---

### PASO 2: Dashboard Básico

1. **Crear dashboard con Streamlit**
   - Configuración de página (wide layout, sidebar colapsable)
   - Cargar datos con cache (@st.cache_data)

2. **Implementar KPIs principales**
   - Total de clientes
   - Ingresos totales
   - Ticket promedio
   - Clientes activos
   - Otras métricas relevantes

3. **Gráficos principales solicitados**
   - Gráfico de barras por ubicación (ciudad/región)
   - Gráfico de pastel por producto/categoría
   - Distribución de estados
   - Análisis temporal

4. **Filtros interactivos (sidebar)**
   - Estado (activo, suspendido, etc.)
   - Producto/Servicio
   - Ubicación
   - Período de tiempo

5. **Tabla de datos**
   - Mostrar primeros 100 registros
   - Selector de columnas
   - Botón de descarga en CSV

**Archivo de salida:** `dashboard.py`
**Puerto:** 8501

---

### PASO 3: Análisis Estratégico y Columnas Avanzadas

1. **Analizar oportunidades**
   - Análisis temporal y tendencias
   - Análisis de retención y churn
   - Análisis geográfico
   - Rendimiento comercial
   - Mix de productos
   - Análisis de canales

2. **Crear columnas estratégicas**

   **A. Valor de Cliente (5 columnas):**
   - `Antiguedad_Cliente_Dias` / `_Meses`: Tiempo desde la primera compra
   - `LTV_Estimado`: Lifetime Value (valor de vida del cliente)
   - `Riesgo_Churn`: Clasificación de riesgo de abandono (Crítico/Alto/Medio/Bajo/Muy Bajo)
   - `Valor_Estrategico`: Segmentación VIP/Valioso/Estándar/En Riesgo

   **B. Temporales Estratégicas (5 columnas):**
   - `Dias_Activo`: Días que lleva activa la relación
   - `Trimestre_Inicio` / `_Vence`: Q1, Q2, Q3, Q4
   - `Alerta_Renovacion`: Urgente/Próxima/Normal
   - `Semanas_Hasta_Vencer`: Semanas para vencimiento

   **C. Rendimiento (3 columnas):**
   - `Contribucion_Ingreso_Pct`: % de ingreso que representa cada cliente
   - `Rentabilidad_Ciudad_Promedio`: Ingreso promedio por ubicación
   - `Performance_Vendedor_Score`: Score de efectividad del vendedor

   **D. Segmentación (4 columnas):**
   - `Potencial_Upselling`: Oportunidad de upgrade
   - `Categoria_Geografica`: Alta/Media/Baja densidad
   - `Score_Engagement`: Puntuación 0-100 de compromiso
   - `Nivel_Engagement`: Bajo/Medio/Alto/Excelente

   **E. Financieras (3 columnas):**
   - `Ingreso_Mensual_Real`: Ingreso mensual normalizado
   - `Proyeccion_12_Meses`: Proyección de ingresos
   - `Margen_Contribucion_Pct` / `_Valor`: Margen de ganancia

   **F. Alertas y Acción (3 columnas):**
   - `Prioridad_Contacto`: Urgente/Alta/Media/Baja
   - `Accion_Recomendada`: Acción sugerida para el cliente
   - `Probabilidad_Renovacion_Pct`: % de probabilidad de renovación

   **G. Adicionales (3 columnas):**
   - `Dias_Desde_Ultimo_Pago`: Días desde el último pago
   - `Es_Cliente_Nuevo`: Boolean (< 3 meses)
   - `Clientes_En_Barrio`: Densidad en la zona

3. **Crear Dashboard Estratégico**

   **Componentes:**
   - **Alertas Críticas** (3 cards superiores):
     * Contactos urgentes
     * Riesgo crítico de churn
     * Renovaciones próximas

   - **KPIs Financieros** (6 métricas):
     * Ingreso Mensual Recurrente (MRR)
     * Ingreso Anual Recurrente (ARR)
     * Ingreso Promedio por Cliente (ARPU)
     * Valor de Vida Promedio (LTV)
     * Proyección 12 meses
     * Margen total

   - **Gráficos Estratégicos** (10+):
     * Top 15 ubicaciones con más clientes
     * Distribución por producto (pastel)
     * Segmentación por valor estratégico
     * Distribución de riesgo de churn
     * Score de engagement
     * Oportunidades de upselling
     * Clientes por trimestre
     * Alertas de renovación
     * Plan de acción estratégico
     * Top vendedores por ingreso
     * Categoría geográfica
     * Rendimiento comercial

   - **Tabla de Clientes Prioritarios**:
     * Lista filtrada por prioridad Urgente/Alta
     * Ordenada por probabilidad de renovación
     * Descargable en CSV

   - **Resumen Ejecutivo** (expandible):
     * Métricas financieras consolidadas
     * Indicadores de retención
     * Oportunidades de negocio

   - **Filtros Avanzados** (sidebar colapsable):
     * Filtros básicos: Estado, Producto, Ubicación
     * Filtros estratégicos: Riesgo, Valor, Prioridad

**Archivos de salida:**
- `{NOMBRE}_ENRIQUECIDO.xlsx` (datos con columnas adicionales)
- `dashboard_estrategico.py` (dashboard avanzado)
- Puerto: 8502

4. **Documentación**
   - Crear `GUIA_METRICAS.md` con explicación detallada de cada métrica
   - Crear `README.md` con documentación completa del proyecto

---

## Plantillas de Código

### Script de Depuración (depurar_datos.py)

```python
import pandas as pd
import numpy as np
from datetime import datetime

# Cargar datos
df = pd.read_excel('ARCHIVO.xlsx')

# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Eliminar columnas innecesarias
columnas_eliminar = ['ID_DUPLICADO', 'DATOS_SENSIBLES', ...]
df = df.drop(columns=columnas_eliminar)

# Convertir fechas
columnas_fecha = ['Fecha_Inicio', 'Fecha_Vence', ...]
for col in columnas_fecha:
    df[col] = pd.to_datetime(df[col], format='%d-%m-%Y', errors='coerce')

# Limpiar nulos
df['Ciudad'] = df['Ciudad'].fillna('SIN ESPECIFICAR')

# Crear columnas calculadas
df['Ingreso_Anualizado'] = df.apply(calcular_ingreso_anual, axis=1)
df['Categoria_Precio'] = df['Precio'].apply(categorizar_precio)

# Guardar
df.to_excel('ARCHIVO_DEPURADO.xlsx', index=False)
df.to_csv('ARCHIVO_DEPURADO.csv', index=False, encoding='utf-8-sig')
```

### Script de Columnas Estratégicas (crear_columnas_estrategicas.py)

```python
import pandas as pd
from datetime import datetime

df = pd.read_excel('ARCHIVO_DEPURADO.xlsx')
fecha_actual = datetime.now()

# Valor de Cliente
df['Antiguedad_Cliente_Dias'] = (fecha_actual - df['Fecha_Inicio']).dt.days
df['LTV_Estimado'] = df['Ingreso_Anualizado'] * (df['Antiguedad_Cliente_Dias'] / 365 + 1)
df['Riesgo_Churn'] = df.apply(calcular_riesgo_churn, axis=1)
df['Valor_Estrategico'] = df.apply(clasificar_valor_estrategico, axis=1)

# Temporales
df['Trimestre_Inicio'] = df['Fecha_Inicio'].dt.quarter.apply(lambda x: f'Q{x}')
df['Alerta_Renovacion'] = df['Dias_Hasta_Vencer'].apply(clasificar_alerta)

# Rendimiento
ingreso_total = df['Ingreso_Anualizado'].sum()
df['Contribucion_Ingreso_Pct'] = (df['Ingreso_Anualizado'] / ingreso_total * 100)

# Segmentación
df['Score_Engagement'] = df.apply(calcular_engagement, axis=1)
df['Potencial_Upselling'] = df.apply(evaluar_upselling, axis=1)

# Financieras
df['Ingreso_Mensual_Real'] = df.apply(calcular_ingreso_mensual, axis=1)
df['Margen_Contribucion_Pct'] = df['Producto'].map(margen_producto)

# Alertas
df['Prioridad_Contacto'] = df.apply(definir_prioridad, axis=1)
df['Accion_Recomendada'] = df.apply(recomendar_accion, axis=1)
df['Probabilidad_Renovacion_Pct'] = df.apply(calcular_prob_renovacion, axis=1)

# Guardar
df.to_excel('ARCHIVO_ENRIQUECIDO.xlsx', index=False)
```

### Dashboard Estratégico (dashboard_estrategico.py)

```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dashboard Estratégico",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def cargar_datos():
    df = pd.read_excel('ARCHIVO_ENRIQUECIDO.xlsx')
    df['Fecha_Inicio'] = pd.to_datetime(df['Fecha_Inicio'])
    return df

df = cargar_datos()

# Sidebar con filtros
with st.sidebar:
    st.header("🔍 Filtros")
    estado = st.selectbox("Estado", ['Todos'] + list(df['Estado'].unique()))
    producto = st.selectbox("Producto", ['Todos'] + list(df['Producto'].unique()))

# Aplicar filtros
df_filtrado = df.copy()
if estado != 'Todos':
    df_filtrado = df_filtrado[df_filtrado['Estado'] == estado]

# Alertas críticas
col1, col2, col3 = st.columns(3)
with col1:
    urgentes = len(df_filtrado[df_filtrado['Prioridad_Contacto'] == 'Urgente'])
    st.metric("🚨 Contactos Urgentes", urgentes)

# KPIs Financieros
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    mrr = df_filtrado['Ingreso_Mensual_Real'].sum()
    st.metric("Ingreso Mensual Recurrente", f"${mrr:,.0f}")
with col2:
    arr = df_filtrado['Ingreso_Anualizado'].sum()
    st.metric("Ingreso Anual Recurrente", f"${arr:,.0f}")

# Gráficos
fig = px.bar(df_filtrado['Ciudad'].value_counts().head(15))
st.plotly_chart(fig)
```

---

## Funciones Auxiliares Comunes

### Cálculo de Riesgo de Churn

```python
def calcular_riesgo_churn(row):
    if row['Dias_Hasta_Vencer'] < 0:
        return 'Crítico'
    elif row['Dias_Hasta_Vencer'] <= 15:
        return 'Alto'
    elif row['Dias_Hasta_Vencer'] <= 30:
        return 'Medio'
    elif row['Dias_Hasta_Vencer'] <= 60:
        return 'Bajo'
    else:
        return 'Muy Bajo'
```

### Cálculo de Engagement

```python
def calcular_engagement(row):
    score = 0
    if row['Estado'] == 'Activo':
        score += 40
    if row['Dias_Activo'] > 365:
        score += 30
    elif row['Dias_Activo'] > 180:
        score += 20
    if row['Riesgo_Churn'] == 'Muy Bajo':
        score += 30
    elif row['Riesgo_Churn'] == 'Bajo':
        score += 20
    return min(score, 100)
```

### Evaluación de Upselling

```python
def evaluar_upselling(row):
    producto = row['Producto']
    if 'Gratis' in producto or producto == 'Gratis':
        return 'Alto - Puede subir a plan básico'
    elif 'Básico' in producto or 'Inicial' in producto:
        return 'Medio - Puede subir a plan pro'
    elif 'Pro' in producto:
        return 'Bajo - Puede subir a plan premium'
    else:
        return 'Ninguno - Ya está en el plan más alto'
```

### Cálculo de Ingreso Mensual Real

```python
def calcular_ingreso_mensual(row):
    if row['Periodo'] == 'Mensual':
        return row['Precio']
    elif row['Periodo'] in ['Anual', 'Pro', 'Premium']:
        return row['Precio'] / 12
    else:
        return row['Precio'] / 12
```

---

## Mejores Prácticas

### Columnas a Buscar en el Excel

1. **Identificación**: ID, Nombre, Empresa, Cliente
2. **Ubicación**: Ciudad, Barrio, País, Región, Zona
3. **Producto/Servicio**: Producto, Plan, Servicio, Categoría
4. **Fechas**: Fecha_Inicio, Fecha_Vencimiento, Fecha_Pago, Fecha_Renovación
5. **Estado**: Estado, Status, Condición
6. **Financiero**: Precio, Monto, Ingreso, Valor, Total
7. **Comercial**: Vendedor, Distribuidor, Canal, Origen
8. **Contacto**: Email, Teléfono, Celular (opcional para análisis)

### Columnas a Eliminar

- Datos personales sensibles: email detallado, teléfono, dirección exacta
- IDs redundantes o duplicados
- Columnas con un solo valor constante
- Columnas duplicadas (mismo contenido, diferente nombre)

### Adaptaciones por Tipo de Negocio

**SaaS / Suscripciones:**
- Foco en: MRR, ARR, Churn, LTV
- Columnas: Fecha_Inicio, Fecha_Vence, Plan, Periodo

**E-commerce:**
- Foco en: Ticket promedio, Frecuencia de compra, AOV
- Columnas: Fecha_Compra, Producto, Monto, Cantidad

**Servicios:**
- Foco en: Proyectos completados, Satisfacción, Retención
- Columnas: Fecha_Inicio_Proyecto, Fecha_Fin, Servicio, Estado

**B2B:**
- Foco en: Tamaño de cuenta, ARR por empresa, Pipeline
- Columnas: Empresa, Industria, Empleados, Contrato_Anual

---

## Checklist de Implementación

### Paso 1: Depuración ✅
- [ ] Archivo Excel cargado y analizado
- [ ] Estructura identificada (columnas, tipos, nulos)
- [ ] Columnas útiles identificadas
- [ ] Columnas innecesarias eliminadas
- [ ] Fechas convertidas a datetime
- [ ] Valores nulos gestionados
- [ ] Columnas calculadas básicas creadas
- [ ] Archivo depurado guardado (.xlsx y .csv)

### Paso 2: Dashboard Básico ✅
- [ ] Dashboard de Streamlit creado
- [ ] KPIs principales implementados
- [ ] Gráfico de barras por ubicación
- [ ] Gráfico de pastel por producto
- [ ] Filtros interactivos funcionando
- [ ] Tabla de datos con descarga
- [ ] Sidebar colapsable configurado
- [ ] Dashboard probado en http://localhost:8501

### Paso 3: Estratégico ✅
- [ ] Análisis de oportunidades completado
- [ ] 27 columnas estratégicas creadas:
  - [ ] 5 de Valor de Cliente
  - [ ] 5 Temporales
  - [ ] 3 de Rendimiento
  - [ ] 4 de Segmentación
  - [ ] 3 Financieras
  - [ ] 3 de Alertas
  - [ ] 3 Adicionales
- [ ] Dashboard estratégico creado
- [ ] Alertas críticas implementadas
- [ ] KPIs financieros (MRR, ARR, LTV, etc.)
- [ ] 10+ gráficos estratégicos
- [ ] Tabla de clientes prioritarios
- [ ] Filtros avanzados funcionando
- [ ] Dashboard probado en http://localhost:8502
- [ ] Guía de métricas documentada (GUIA_METRICAS.md)
- [ ] README.md completo

---

## Traducción de Términos

**Del inglés al español:**
- MRR → Ingreso Mensual Recurrente
- ARR → Ingreso Anual Recurrente
- ARPU → Ingreso Promedio por Cliente
- LTV → Valor de Vida del Cliente
- Churn → Tasa de Abandono / Deserción
- Engagement → Compromiso / Participación
- Upselling → Venta Ascendente / Mejora de Plan
- Score → Puntuación
- Performance → Rendimiento / Desempeño

---

## Archivos Generados

Al finalizar, el proyecto debe tener:

```
📁 Proyecto/
├── 📄 ARCHIVO_ORIGINAL.xlsx
├── 📄 ARCHIVO_DEPURADO.xlsx
├── 📄 ARCHIVO_DEPURADO.csv
├── 📄 ARCHIVO_ENRIQUECIDO.xlsx
├── 📄 ARCHIVO_ENRIQUECIDO.csv
├── 🐍 analizar_datos.py
├── 🐍 depurar_datos.py
├── 🐍 crear_columnas_estrategicas.py
├── 🐍 dashboard.py
├── 🐍 dashboard_estrategico.py
├── 📋 requirements.txt
├── 📖 README.md
├── 📖 GUIA_METRICAS.md
└── 📖 SKILL.md (este archivo)
```

---

## Ejemplo de Uso

**Usuario dice:**
> "Tengo un archivo Excel con datos de clientes, quiero crear un dashboard"

**Agente responde:**
1. Analiza el archivo Excel
2. Identifica las columnas relevantes
3. Presenta un plan de depuración
4. Solicita aprobación del usuario
5. Ejecuta depuración (Paso 1)
6. Crea dashboard básico (Paso 2)
7. Solicita aprobación para análisis avanzado
8. Crea columnas estratégicas (Paso 3)
9. Crea dashboard estratégico
10. Documenta todo en GUIA_METRICAS.md y README.md

---

## Métricas de Éxito

- ✅ Dataset depurado sin errores
- ✅ Dashboard básico funcionando en puerto 8501
- ✅ Dashboard estratégico funcionando en puerto 8502
- ✅ 27+ columnas estratégicas creadas
- ✅ 10+ gráficos estratégicos implementados
- ✅ Documentación completa generada
- ✅ Todos los términos en español
- ✅ Sidebar colapsable implementado

---

## Notas Importantes

1. **Siempre solicitar aprobación del usuario** antes de proceder a cada paso
2. **Adaptar las columnas estratégicas** según el tipo de negocio
3. **Traducir todos los términos técnicos** al español
4. **Mantener el sidebar colapsable** por defecto
5. **Generar documentación exhaustiva** de cada métrica
6. **Usar colores consistentes** en los gráficos (rojo=crítico, amarillo=advertencia, verde=bueno)
7. **Optimizar el rendimiento** con @st.cache_data
8. **Crear archivos tanto en .xlsx como .csv**

---

**Versión:** 1.0
**Fecha:** 2026-04-28
**Última actualización:** 2026-04-28
**Mantenedor:** Equipo de Análisis de Datos
