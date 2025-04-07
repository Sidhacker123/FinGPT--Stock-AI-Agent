
#!/bin/bash

echo "🚀 Starting Agentic AI GPU Setup..."

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv -y

python3 -m venv agentic_env
source agentic_env/bin/activate

pip install --upgrade pip
pip install fastapi uvicorn httpx toml streamlit torch pandas scikit-learn matplotlib seaborn

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

echo "✅ Environment ready!"
echo "➡️ Run FastAPI: uvicorn main:app --reload"
echo "➡️ Run Streamlit: streamlit run app.py"
