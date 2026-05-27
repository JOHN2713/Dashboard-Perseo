# 📊 Fórmulas de Métricas - Dashboards Perseo

Este documento contiene todas las fórmulas utilizadas para calcular las métricas clave en los dashboards de Perseo (Facturito, PC y WEB).

---

## 📈 Métricas Principales

### 1. MRR (Monthly Recurring Revenue) - Ingreso Recurrente Mensual

**Definición:** Suma total de los ingresos mensuales de todos los clientes activos.

**Fórmulas por Dashboard:**

#### Facturito:
```python
mrr = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual'].sum()
```

#### Perseo PC:
```python
mrr = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual Equiv'].sum()
```

#### Perseo WEB:
```python
mrr = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual Equiv'].sum()
```

**Explicación:**
- Se filtran únicamente los clientes con `Estado = 'Activo'`
- Se suman todos los valores de la columna de ingreso mensual
- El resultado representa el ingreso mensual recurrente total

---

### 2. ARR (Annual Recurring Revenue) - Ingreso Recurrente Anual

**Definición:** Proyección anual del MRR multiplicado por 12 meses.

**Fórmula (Todos los dashboards):**
```python
arr = mrr * 12
```

**Explicación:**
- Se multiplica el MRR por 12 para obtener la proyección anual
- Asume que el ingreso mensual se mantendrá constante durante el año
- Es una métrica clave para evaluar el valor anual del negocio

---

### 3. Ticket Promedio

**Definición:** Ingreso mensual promedio por cliente activo.

**Fórmulas por Dashboard:**

#### Facturito:
```python
ticket_promedio = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual'].mean()
```

#### Perseo PC:
```python
ticket_promedio = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual Equiv'].mean()
```

#### Perseo WEB:
```python
ticket_promedio = df_filtrado[df_filtrado['Estado'] == 'Activo']['Ingreso Mensual Equiv'].mean()
```

**Explicación:**
- Se filtran únicamente los clientes con `Estado = 'Activo'`
- Se calcula el promedio (media) de los ingresos mensuales
- Indica cuánto paga en promedio cada cliente activo

---

### 4. Tasa de Churn

**Definición:** Porcentaje de clientes que han abandonado el servicio (perdidos).

**Fórmula (Todos los dashboards):**
```python
# Primero se calcula el número de clientes en churn
clientes_churn = len(df_filtrado[df_filtrado['Estado'].isin(['Terminado', 'Inactivo'])])

# Luego se calcula el porcentaje
tasa_churn = (clientes_churn / total_clientes * 100) if total_clientes > 0 else 0
```

**Explicación:**
- Se cuentan los clientes con estado `'Terminado'` o `'Inactivo'`
- Se divide entre el total de clientes y se multiplica por 100 para obtener el porcentaje
- Si no hay clientes, la tasa es 0% para evitar división por cero
- Una tasa de churn alta indica que se están perdiendo muchos clientes

**Ejemplo de cálculo:**
```
Total Clientes: 100
Clientes en Churn: 15
Tasa de Churn = (15 / 100) * 100 = 15%
```

---

### 5. Tasa de Retención

**Definición:** Porcentaje de clientes que se mantienen activos (contrario al churn).

**Fórmula (Todos los dashboards):**
```python
tasa_retencion = 100 - tasa_churn
```

**Explicación:**
- Es el complemento de la tasa de churn
- Si la tasa de churn es 15%, la tasa de retención es 85%
- Una tasa de retención alta indica que los clientes se quedan con el servicio
- Es una métrica clave para evaluar la satisfacción y lealtad del cliente

**Ejemplo de cálculo:**
```
Tasa de Churn: 15%
Tasa de Retención = 100 - 15 = 85%
```

---

## 📋 Variables Auxiliares

### Total de Clientes
```python
total_clientes = len(df_filtrado)
```
Cuenta el número total de registros (clientes) después de aplicar filtros.

### Clientes Activos
```python
clientes_activos = len(df_filtrado[df_filtrado['Estado'] == 'Activo'])
```
Cuenta únicamente los clientes con estado `'Activo'`.

### Clientes en Churn
```python
clientes_churn = len(df_filtrado[df_filtrado['Estado'].isin(['Terminado', 'Inactivo'])])
```
Cuenta los clientes con estado `'Terminado'` o `'Inactivo'`.

---

## 🔍 Columnas de Ingreso por Dashboard

| Dashboard | Columna de Ingreso Mensual |
|-----------|---------------------------|
| **Facturito** | `Ingreso Mensual` |
| **Perseo PC** | `Ingreso Mensual Equiv` |
| **Perseo WEB** | `Ingreso Mensual Equiv` |

---

## 📝 Notas Importantes

1. **Filtros aplicados:** Todas las fórmulas se calculan sobre `df_filtrado`, que es el dataframe después de aplicar los filtros seleccionados por el usuario (estado, producto, ciudad, distribuidor, año).

2. **Manejo de valores nulos:** Se recomienda usar `pd.notna()` al mostrar valores para evitar errores con datos faltantes.

3. **Estados considerados:**
   - **Activo:** Cliente que paga y usa el servicio
   - **Terminado:** Cliente que canceló el servicio
   - **Inactivo:** Cliente que no está usando el servicio actualmente

4. **Formato de visualización:**
   ```python
   # Para montos
   f"${valor:,.2f}"  # Ej: $1,234.56
   
   # Para porcentajes
   f"{valor:.2f}%"   # Ej: 85.50%
   
   # Para cantidades
   f"{valor:,}"      # Ej: 1,234
   ```

---

## 📊 Relaciones entre Métricas

```
MRR = Suma(Ingresos Mensuales de Clientes Activos)
ARR = MRR × 12
Ticket Promedio = MRR ÷ Número de Clientes Activos
Tasa de Churn = (Clientes Perdidos ÷ Total Clientes) × 100
Tasa de Retención = 100 - Tasa de Churn
```

---

**Última actualización:** Mayo 2026  
**Dashboards:** Facturito, Perseo PC, Perseo WEB  
**Plataforma:** Streamlit + Python + Pandas
