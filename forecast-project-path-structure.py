import os

# Nome da pasta raiz
root_dir = 'stock-forecast'

# Estrutura de diretórios
dirs = [
    os.path.join(root_dir, 'data', 'raw'),
    os.path.join(root_dir, 'data', 'processed'),
    os.path.join(root_dir, 'data', 'features'),
    os.path.join(root_dir, 'data', 'models'),
    os.path.join(root_dir, 'notebooks', 'exploration'),
    os.path.join(root_dir, 'notebooks', 'preprocessing'),
    os.path.join(root_dir, 'notebooks', 'modeling'),
    os.path.join(root_dir, 'notebooks', 'backtesting'),
    os.path.join(root_dir, 'src', 'data'),
    os.path.join(root_dir, 'src', 'features'),
    os.path.join(root_dir, 'src', 'models'),
    os.path.join(root_dir, 'src', 'utils'),
    os.path.join(root_dir, 'src', 'visualization'),
    os.path.join(root_dir, 'configs'),
    os.path.join(root_dir, 'reports', 'figures'),
    os.path.join(root_dir, 'logs'),
    os.path.join(root_dir, 'tests')
]

# Criação dos diretórios
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Criação de arquivos básicos
files = {
    os.path.join(root_dir, 'README.md'): "# Stock Forecast Project\n\nThis project is designed to forecast stock prices and analyze potential investment signals.",
    os.path.join(root_dir, 'requirements.txt'): "",
    os.path.join(root_dir, '.gitignore'): "*.csv\n*.log\n*.pkl\n__pycache__/\n.ipynb_checkpoints/",
    os.path.join(root_dir, 'configs', 'config.yaml'): "# Configuration file for Stock Forecast Project\n",
    os.path.join(root_dir, 'configs', 'secrets.yaml'): "# Secrets (API keys, etc.)\n",
    os.path.join(root_dir, 'reports', 'final_report.md'): "# Final Report\n\nSummary of the analysis and findings."
}

for file, content in files.items():
    with open(file, 'w') as f:
        f.write(content)

print(f"Project structure created successfully in '{root_dir}'")
