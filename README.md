# IT Department Lab & Server Energy Telemetry Monitor

A full-stack Python telemetry and power monitoring dashboard built to audit, detect surges, and track energy usage across IT Department infrastructure (Server Rooms, AI Labs, Networking racks, and Software Labs).

---

## 📌 Syllabus Coverage (ITL Laboratory)
- **Unit I (Python Basics & CLI):** Command-line telemetry ingestion using `sys.argv` in `seed_cli.py`.
- **Unit II (Data Structures & Exceptions):** Dictionaries, list comprehensions, and defensive `try-except` error handling.
- **Unit III & VI (Databases & Django Framework):** Relational database persistence using Django ORM and MVT (Model-View-Template) architecture.
- **Unit IV (NumPy Numerical Operations):** Array transformation, mean power draw calculations, and threshold filtering (`> 50 kWh`) for anomaly detection.
- **Unit V (Pandas & Matplotlib Visualization):** Group-by aggregations and summary statistics via Pandas DataFrame; real-time horizontal bar chart generation rendered as in-memory Base64 strings.

---

## 📋 Agile Development (Kanban Board)

| Backlog | To Do | In Progress | Testing / Review | Done |
| :--- | :--- | :--- | :--- | :--- |
| Email surge alerts | Unit tests for power spikes | Responsive mobile layout | CLI parameter validation | Virtualenv & Django setup |
| PDF report export | Add multi-user login (HOD/Admin) | Dynamic chart palette | SQLite schema migrations | Database model (`ITLabEnergy`) |
| IoT sensor webhook | Automated weekly cron jobs | Aggregation queries | Exception handling audit | NumPy/Pandas analytics engine |
| Multi-building tracking | Data export to Excel/CSV | — | Browser dashboard verification | Matplotlib Base64 visual dashboard |

---

## 🚀 How to Run
1. Activate virtual environment:
   ```bash
   source env/bin/activate