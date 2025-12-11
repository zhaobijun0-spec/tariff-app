#!/usr/bin/env python3
"""
Tariff Dashboard - Development Setup Script
Automatically sets up the development environment
"""

import os
import sys
import subprocess
from pathlib import Path

class Colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[1;33m'
    RED = '\033[0;31m'
    NC = '\033[0m'

def run_command(cmd, cwd=None):
    """Run a shell command"""
    try:
        subprocess.run(cmd, shell=True, cwd=cwd, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Colors.RED}Error: {e}{Colors.NC}")
        return False

def main():
    print(f"{Colors.BLUE}🚀 Tariff Dashboard Setup{Colors.NC}")
    print()
    
    project_root = Path(__file__).parent.parent
    backend_dir = project_root / "backend"
    frontend_dir = project_root / "frontend"
    
    # Setup backend
    print(f"{Colors.BLUE}📦 Setting up backend...{Colors.NC}")
    
    # Create virtual environment
    venv_path = backend_dir / "venv"
    if not venv_path.exists():
        print("Creating Python virtual environment...")
        run_command(f"{sys.executable} -m venv venv", cwd=backend_dir)
        print(f"{Colors.GREEN}✅ Virtual environment created{Colors.NC}")
    else:
        print(f"{Colors.GREEN}✅ Virtual environment already exists{Colors.NC}")
    
    # Install dependencies
    print("Installing Python dependencies...")
    requirements_file = backend_dir / "requirements.txt"
    if requirements_file.exists():
        run_command(f"{sys.executable} -m pip install -q -r requirements.txt", cwd=backend_dir)
        print(f"{Colors.GREEN}✅ Python dependencies installed{Colors.NC}")
    
    # Copy .env file
    env_file = backend_dir / ".env"
    env_example = backend_dir / ".env.example"
    if not env_file.exists() and env_example.exists():
        run_command(f"cp .env.example .env", cwd=backend_dir)
        print(f"{Colors.GREEN}✅ Created .env file{Colors.NC}")
    
    print()
    print(f"{Colors.BLUE}📦 Setting up frontend...{Colors.NC}")
    
    # Install npm dependencies
    print("Installing Node dependencies...")
    run_command("npm install -q", cwd=frontend_dir)
    print(f"{Colors.GREEN}✅ Node dependencies installed (including Recharts){Colors.NC}")
    
    # Copy .env file for frontend
    env_file = frontend_dir / ".env"
    if not env_file.exists():
        with open(env_file, 'w') as f:
            f.write("REACT_APP_API_URL=http://localhost:8000\n")
        print(f"{Colors.GREEN}✅ Created frontend .env file{Colors.NC}")
    
    print()
    print(f"{Colors.GREEN}✅ Setup complete!{Colors.NC}")
    print()
    print(f"{Colors.BLUE}🚀 Next steps:{Colors.NC}")
    print()
    print("Terminal 1 - Backend:")
    print("  cd tariff-app/backend")
    print("  source venv/bin/activate  # Windows: venv\\Scripts\\activate")
    print("  python -m uvicorn main:app --reload")
    print()
    print("Terminal 2 - Frontend:")
    print("  cd tariff-app/frontend")
    print("  npm start")
    print()
    print(f"Then open: {Colors.YELLOW}http://localhost:3000{Colors.NC}")
    print()

if __name__ == "__main__":
    main()
