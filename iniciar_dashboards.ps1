# Script para iniciar todos los dashboards de Perseo
# Ejecutar con: .\iniciar_dashboards.ps1

Write-Host "=" -ForegroundColor Cyan
Write-Host "🚀 Iniciando Dashboards Perseo" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Verificar que Python está instalado
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python no está instalado o no está en el PATH" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Python encontrado: $(python --version)" -ForegroundColor Green
Write-Host ""

# Verificar que Streamlit está instalado
$streamlitInstalled = python -m pip list | Select-String "streamlit"
if (!$streamlitInstalled) {
    Write-Host "❌ Streamlit no está instalado" -ForegroundColor Red
    Write-Host "Instalando dependencias..." -ForegroundColor Yellow
    python -m pip install -r requirements.txt
}

Write-Host "✅ Streamlit instalado" -ForegroundColor Green
Write-Host ""

# Iniciar los 3 dashboards en diferentes puertos
Write-Host "📊 Iniciando Dashboard Facturito en puerto 8501..." -ForegroundColor Yellow
Start-Process -FilePath "python" -ArgumentList "-m streamlit run dashboard_facturito.py" -WindowStyle Normal

Start-Sleep -Seconds 3

Write-Host "🌐 Iniciando Dashboard Perseo WEB en puerto 8502..." -ForegroundColor Yellow
Start-Process -FilePath "python" -ArgumentList "-m streamlit run dashboard_web.py --server.port 8502" -WindowStyle Normal

Start-Sleep -Seconds 3

Write-Host "💻 Iniciando Dashboard Perseo PC en puerto 8503..." -ForegroundColor Yellow
Start-Process -FilePath "python" -ArgumentList "-m streamlit run dashboard_pc.py --server.port 8503" -WindowStyle Normal

Write-Host ""
Write-Host "================================" -ForegroundColor Green
Write-Host "✅ Todos los dashboards iniciados" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "📊 URLs de acceso:" -ForegroundColor Cyan
Write-Host "  - Facturito: http://localhost:8501" -ForegroundColor White
Write-Host "  - Perseo WEB: http://localhost:8502" -ForegroundColor White
Write-Host "  - Perseo PC: http://localhost:8503" -ForegroundColor White
Write-Host ""
Write-Host "Presiona Ctrl+C para detener todos los dashboards" -ForegroundColor Yellow
Write-Host ""

# Mantener el script ejecutándose
Read-Host "Presiona Enter para cerrar este mensaje..."
