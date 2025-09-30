import os

# === Repo structure ===
folders = ["docs", "scripts", "configs", "community"]
files = {
    "README.md": """# 🌐 NodeBuilder-X Community

> 🚀 Build nodes. Grow networks. Empower communities.  

## ⚡ Mission
We don’t just run nodes – we **build decentralized ecosystems**.
Every validator, guardian, miner, or indexer is a key piece of the Web3 future.
""",
    "CONTRIBUTING.md": """# 🤝 Contributing Guide

- Fork this repo
- Create your branch (`git checkout -b feature/foo`)
- Commit your changes (`git commit -m "Add foo"`)
- Push to the branch (`git push origin feature/foo`)
- Open a Pull Request
"""
}

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))  # thư mục chứa file py
    
    # Tạo folders
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"📂 Created folder: {path}")
    
    # Tạo files
    for fname, content in files.items():
        path = os.path.join(base_path, fname)
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(content.strip() + "\n")
            print(f"📄 Created file: {path}")
        else:
            print(f"⚠️ File already exists: {path}")

if __name__ == "__main__":
    main()
