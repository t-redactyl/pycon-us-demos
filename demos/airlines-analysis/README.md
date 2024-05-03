# PyCon US Jupyter notebook demo

## This README contains two sections:
* Set up
* Demo instructions

## Set up for PyCharm demo (2024.1)
1. Start Docker Desktop
2. Disable **Settings | Tools | AI Assistant | Enable automatic inline code completion as you type** to avoid [these known issues](https://youtrack.jetbrains.com/issue/PY-64470/LLM-Make-multiline-completion-work-in-Jupyter-Notebooks#focus=Comments-27-8909363.0-0) during the demo.
3. In new terminal window:
   * cd databases 
   * `docker-compose up`
4. In PyCharm:
   * Open Database tool window 
   * Data Source > PostgreSQL 
     * Host: localhost 
     * Port: 5432 
     * User: pycharm 
     * Password: pycharm 
     * Database: demo 
     * Download the missing driver files
5. In PyCharm:
   * Open databases/insert_airlines_into_postgres_db.py 
   * Run 
   * In Database tool window: Refresh 
   * Check that table has appeared
6. Open `airport-exploration.ipynb` for the demo notebook.

The instructions of how to work through this demo are here: https://gist.github.com/t-redactyl/7501e450d4822c3eafc2e354973a6027


