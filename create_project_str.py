import os

folders_and_files = [
    "data/Reviews.csv",
    "notebooks/sentiment_model.ipynb",
    "model/model.pkl",
    "app/app.py",
    "app/templates/index.html",
    "app/requirements.txt",
    "docker/Dockerfile",
    "cicd/deploy.yml",
    "k8s/deployment.yaml",
    "README.md",
    ".gitignore"
]

for item in folders_and_files:
    path = os.path.join(os.getcwd(), item)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("")  # Create empty file

print("✅ Folder structure created successfully in:", os.getcwd())
