# ☁️ AWS Data Engineering ETL Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Pipeline automatizado de extracción, transformación y carga (ETL) para el procesamiento de datos financieros y operativos orientados a arquitecturas Cloud.

---

### ⚙️ Arquitectura del Pipeline

1. **Extraction:** Consumo dinámico de datos mediante APIs REST en Python.
2. **Transformation:** Limpieza, tipado y estructuración de esquemas usando `Pandas`.
3. **Loading:** Persistencia de datos optimizada para Data Lakes (S3) y bases de datos relacionales (RDS PostgreSQL).

---

### 🚀 Ejecución Local

```bash
git clone [https://github.com/jocetapiadev/aws-etl-pipeline.git](https://github.com/jocetapiadev/aws-etl-pipeline.git)
pip install pandas requests
python etl_pipeline.py
