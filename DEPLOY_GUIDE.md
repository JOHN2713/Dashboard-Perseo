# 🚀 Guía de Despliegue en Streamlit Cloud

## ✅ Preparación Completada

Los dashboards ya están configurados para cargar datos desde Google Drive automáticamente cuando se despliegan en Streamlit Cloud.

## 📋 Enlaces de Google Drive Configurados

Los siguientes archivos están alojados en Google Drive con permisos públicos:

1. **BASE FACTURITO OL.xlsx**
   - File ID: `1fforhn03rynmhUva0SaN1SawnxmEm5dV`
   - URL: https://drive.google.com/uc?export=download&id=1fforhn03rynmhUva0SaN1SawnxmEm5dV

2. **BASE WEB OK (1).xlsx**
   - File ID: `1wt2unhyUsXhKjQnjEXoB36tlP2eA5Jst`
   - URL: https://drive.google.com/uc?export=download&id=1wt2unhyUsXhKjQnjEXoB36tlP2eA5Jst

3. **BASE PRODUCTO PC.xlsx**
   - File ID: `168V0BCy0-LZDzeKQp-9sdJuXIbRQvOpd`
   - URL: https://drive.google.com/uc?export=download&id=168V0BCy0-LZDzeKQp-9sdJuXIbRQvOpd

## 🌐 Pasos para Desplegar en Streamlit Cloud

### 1. Verificar que el código esté en GitHub

Asegúrate de que los cambios estén subidos:

```bash
git add .
git commit -m "Actualización: Carga de datos desde Google Drive para Streamlit Cloud"
git push origin main
```

### 2. Ir a Streamlit Cloud

1. Ve a: https://share.streamlit.io
2. Haz clic en **"New app"** (o **"Deploy an app"**)

### 3. Conectar el Repositorio

- **Repository**: `JOHN2713/Dashboard-Perseo`
- **Branch**: `main`
- **Main file path**: Selecciona uno de estos:
  - `dashboard_facturito.py` (Dashboard Facturito) ⭐ Recomendado para empezar
  - `dashboard_web.py` (Dashboard Perseo WEB)
  - `dashboard_pc.py` (Dashboard Perseo PC)
  - `app.py` (Página principal de selección)

### 4. Configuración Avanzada (Opcional)

En "Advanced settings":

- **Python version**: 3.13 (o la versión que uses localmente)
- **Main file path**: Confirma el archivo seleccionado

### 5. Deploy!

Haz clic en **"Deploy!"** y espera unos minutos mientras Streamlit Cloud:
- Instala las dependencias desde `requirements.txt`
- Descarga los datos desde Google Drive
- Inicia tu aplicación

### 6. Verificar el Despliegue

Una vez desplegado, verás:
- ✅ "📡 Datos cargados desde Google Drive" en el sidebar (confirmando que funciona)
- La URL pública de tu dashboard (ej: `https://dashboard-perseo.streamlit.app`)

## 🔄 Desplegar los 3 Dashboards

Si quieres tener los 3 dashboards en línea, repite el proceso 3 veces:

1. **Primera app**: `dashboard_facturito.py`
   - URL: https://dashboard-perseo-facturito.streamlit.app

2. **Segunda app**: `dashboard_web.py`
   - URL: https://dashboard-perseo-web.streamlit.app

3. **Tercera app**: `dashboard_pc.py`
   - URL: https://dashboard-perseo-pc.streamlit.app

## 📝 Notas Importantes

### Permisos de Google Drive

Los archivos deben tener permisos de **"Cualquier persona con el enlace"** con rol de **"Lector"**.

Para verificar:
1. Haz clic derecho en el archivo en Google Drive
2. "Compartir" → "Obtener enlace"
3. Cambia a "Cualquiera con el enlace puede ver"

### Comportamiento de la Carga de Datos

El código está configurado para:
1. **Primero**: Intentar cargar desde Google Drive
2. **Si falla**: Intentar cargar desde archivo local
3. **Si ambos fallan**: Mostrar error

Esto permite que funcione tanto en local como en la nube.

### Actualizar los Datos

Si actualizas los archivos en Google Drive:
1. Los datos se actualizarán automáticamente en los dashboards
2. Puede tardar hasta 5 minutos debido al caché de Streamlit
3. Puedes forzar la recarga presionando "C" en el dashboard → "Clear cache"

## 🎨 Personalización Post-Despliegue

Una vez desplegado, puedes:
- Cambiar el tema en Settings → Theme
- Configurar un dominio personalizado
- Agregar secrets si necesitas datos sensibles
- Configurar autenticación (plan Business)

## 🐛 Solución de Problemas

### Error: "Cannot download file from Google Drive"

**Causa**: Los permisos del archivo no son públicos.

**Solución**:
1. Ve al archivo en Google Drive
2. Compartir → "Cualquier persona con el enlace"
3. Rol: "Lector"

### Error: "Module not found"

**Causa**: Falta una dependencia en `requirements.txt`.

**Solución**:
1. Agrega el módulo faltante a `requirements.txt`
2. Commit y push:
   ```bash
   git add requirements.txt
   git commit -m "Actualizar dependencias"
   git push origin main
   ```
3. Streamlit Cloud se redesplegará automáticamente

### El dashboard es muy lento

**Causa**: Los archivos Excel son grandes y se cargan en cada visita.

**Solución**:
- Los datos se cachean con `@st.cache_data`
- Primera carga: lenta (descarga desde Google Drive)
- Siguientes cargas: rápidas (datos en caché)

## 📊 Monitoreo

En el panel de Streamlit Cloud puedes ver:
- **Logs**: Ver errores y mensajes de carga
- **Analytics**: Número de visitantes
- **Resources**: Uso de memoria y CPU

## 🔐 Seguridad

Los datos están en Google Drive con enlace público, pero:
- Solo personas con el enlace pueden acceder
- No se indexan en buscadores (si está configurado)
- Considera mover a una base de datos para mayor seguridad en producción

## ✨ ¡Listo para Desplegar!

Todos los dashboards están listos para funcionar en Streamlit Cloud. Solo sigue los pasos arriba y estarán en línea en minutos.
