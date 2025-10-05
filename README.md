# Análisis de Cohortes para la Optimización del Lifetime Value (LTV) 

## Resumen Ejecutivo y Conclusiones de Negocio

Este análisis de **retención de clientes (Churn)** a través del **Mapa de Calor de Cohortes** revela patrones de comportamiento críticos para la estrategia de negocio.

El hallazgo central es la existencia de una **fuga masiva de clientes (más del 70%) del Mes 0 al Mes 1**. Esto subraya una falla crítica en la activación post-adquisición. A pesar de esta fuga inicial, los clientes que **sobreviven al Mes 1** demuestran ser un subgrupo de alto valor, manteniendo tasas de retención estables.

[**Resumen Ejecutivo**]()

**Recomendación:** La empresa debe **priorizar la inversión en *onboarding*** (activación inicial) para reducir la caída del primer mes y, simultáneamente, enfocar los **programas de lealtad (CRM)** en el segmento de clientes que ya demostró compromiso para maximizar su LTV.

## Objetivo y Pregunta de Negocio 

El objetivo principal es analizar la **retención de clientes (Churn)** a lo largo del tiempo utilizando la metodología de **Análisis de Cohortes**. El resultado es un mapa de calor dinámico que permite identificar la **fuga masiva de clientes** y optimizar las inversiones en CRM para maximizar el Valor de Tiempo de Vida (LTV).

  * **Pregunta Central:** ¿Cuándo y por qué abandonan nuestros clientes después de su primera compra, y qué cohortes son inherentemente más leales?

## Hallazgos Clave y Recomendaciones Estratégicas

El análisis del Mapa de Calor revela patrones críticos para la toma de decisiones:

| Etapa/Área | Conclusión de Negocio | Recomendación Estratégica (Acción) |
| :--- | :--- | :--- |
| **A. Fuga Crítica e Inmediata** | La retención cae bruscamente del **Mes 0 al Mes 1**, con una fuga promedio de más del $70\%$ de los nuevos clientes. Esto es una **falla en el *onboarding***. | El equipo de Marketing debe lanzar una **Campaña de Incentivo a la Segunda Compra** dentro de las primeras 3 semanas para romper la barrera del Mes 1. |
| **B. Calidad de la Retención** | Los clientes que **sobreviven al Mes 1** son altamente leales, manteniendo tasas de retención estables en el rango de $20\%$ a $35\%$ en meses posteriores. | La inversión en **programas de lealtad y CRM** debe enfocarse en este segmento de clientes valiosos para maximizar su valor. |

## Metodología y Entregables Técnicos

Se empleó Python (Pandas) para la ingeniería de datos y la creación de la matriz de cohortes, y Power BI para la visualización de alto impacto, asegurando la precisión de los datos visualizados.

| Etapa | Herramienta | Acción Clave | Entregable |
| :--- | :--- | :--- | :--- |
| **1. Transformación de Datos** | Python (Pandas) | Creación de la matriz de retención, identificación del mes de adquisición y cálculo del índice de mes (Month Index). | `cohort_retention_matrix.csv` |
| **2. Preparación de Visualización** | Power Query / DAX | Anulación de dinamización (*Unpivot*) de la matriz. **Corrección de escala en DAX** para garantizar que el Mes 0 = $100.00$. | Medida DAX final (`Tasa Retención Final`) |
| **3. Visualización** | Power BI (Matriz) | Aplicación de formato condicional por reglas para crear un **Mapa de Calor** visualmente intuitivo (Mes 0 neutral, gradiente Negro-Gris). | Dashboard: "Mapa de Calor de Retención" |

El dashboard fue construido en Power BI para comunicar de forma visual y numérica los hallazgos.

![(**Dashboard:**)]()

## Instrucciones de Reproducción

1.  **Entorno:** Python 3.x, librerías `pandas`, Power BI Desktop.
2.  **Ejecución del Script:**
      * Ejecutar el *script* de Python para generar la matriz de retención:
        ```bash
        python src/run_cohort_analysis.py
        ```
      * El resultado se guarda en: `deliverables/cohort_retention_matrix.csv`