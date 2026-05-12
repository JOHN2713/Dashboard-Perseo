# Comandos para subir el proyecto a GitHub

## 1. Inicializar Git (si no está inicializado)
```bash
git init
```

## 2. Agregar el remote de tu repositorio
```bash
git remote add origin https://github.com/JOHN2713/Dashboard-Perseo.git
```

## 3. Agregar todos los archivos (excepto los del .gitignore)
```bash
git add .
```

## 4. Hacer commit de los cambios
```bash
git commit -m "Initial commit: Dashboards Perseo con branding y KPIs"
```

## 5. Subir al repositorio
```bash
git push -u origin main
```

## Si ya tienes archivos en el repositorio, usa:
```bash
git pull origin main --rebase
git push origin main
```

---

## 📝 Notas Importantes

### Antes de subir a GitHub:

1. **Los archivos Excel NO se subirán** (están en .gitignore) por seguridad
2. **Los logos SÍ se subirán** (perseo-logo-negro.png y perseo-logo-blanco.png)
3. Todos los archivos Python (.py) se subirán
4. El archivo requirements.txt se subirá
5. La configuración de Streamlit (.streamlit/config.toml) se subirá

### Para desplegar en Streamlit Cloud:

1. Ve a https://share.streamlit.io
2. Inicia sesión con tu cuenta de GitHub
3. Click en "New app"
4. Selecciona tu repositorio: `JOHN2713/Dashboard-Perseo`
5. Branch: `main`
6. Main file path: Elige uno de estos:
   - `dashboard_facturito.py` para Dashboard Facturito
   - `dashboard_web.py` para Dashboard Perseo WEB
   - `dashboard_pc.py` para Dashboard Perseo PC
   - `app.py` para la página principal de selección

### Subir archivos Excel a Streamlit Cloud:

Como los archivos Excel no están en GitHub (por seguridad), necesitas:

1. **Opción A - Secrets Manager**: Subir los datos como secrets en Streamlit Cloud
2. **Opción B - URL Externa**: Alojar los Excel en Google Drive o similar y cargarlos por URL
3. **Opción C - Base de Datos**: Migrar los datos a una base de datos en la nube

### Recomendación para archivos Excel:

Agrega este código al inicio de cada dashboard para permitir cargar desde URL:

```python
# Si existe una URL en secrets, cargar desde ahí
if 'excel_url' in st.secrets:
    df = pd.read_excel(st.secrets['excel_url'])
else:
    # Cargar desde archivo local
    df = pd.read_excel('BASE FACTURITO OL.xlsx')
```

Y en Streamlit Cloud, en la sección "Secrets", agrega:
```toml
excel_url = "URL_DE_TU_ARCHIVO_EXCEL"
```
