python -m venv .venv
cmd /c ".venv\Scripts\activate.bat & pip install -r requirements.txt & python tests\unittests.py & .venv\Scripts\deactivate.bat & rmdir /s /q .venv"