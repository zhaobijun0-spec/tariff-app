# 🚀 Deploy to Replit (No GitHub Needed!)

Replit is the easiest way to deploy - no setup, no commands, just upload and go!

## Step 1: Create Replit Account
- Go to [replit.com](https://replit.com)
- Sign up (takes 30 seconds)

## Step 2: Create a New Replit Project
- Click "Create Replit"
- Choose "Python" 
- Name it: `tariff-app`
- Click "Create"

## Step 3: Upload Your Files
In Replit:
1. Click the **folder icon** on the left
2. Click **"Upload file"** button
3. Upload all files from `/agent/home/tariff-app/`

Structure should be:
```
tariff-app/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── scraper.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── package.json
│   ├── App.jsx
│   ├── App.css
│   └── ...
└── replit.nix (special file)
```

## Step 4: Create replit.nix
Click "Create file" and paste this:

```nix
{ pkgs }: {
    deps = [
        pkgs.python311
        pkgs.python311Packages.pip
        pkgs.nodejs_20
    ];
    env = {
        PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
            pkgs.libuuid
        ];
        LANG = "en_US.UTF-8";
    };
}
```

## Step 5: Create .replit
Click "Create file" and paste this:

```
entrypoint = "backend/run.py"

[env]
PYTHONUNBUFFERED = "1"

[nix]
channel = "stable-22_11"

[unitTest]
language = "python3"

[debugger]
support = true

[debugger.interactive]
transport = "localhost:0"
startCommand = ["dap-python", "backend/run.py"]
```

## Step 6: Create backend/run.py
In Replit file manager, create `backend/run.py`:

```python
import os
import subprocess
import sys
from pathlib import Path

# Install Python dependencies
print("Installing Python dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"])

# Install frontend dependencies
print("Installing Node dependencies...")
os.chdir("frontend")
subprocess.check_call(["npm", "install"])
subprocess.check_call(["npm", "run", "build"])
os.chdir("..")

# Start backend
print("Starting backend...")
os.chdir("backend")
os.system("uvicorn main:app --host 0.0.0.0 --port 8000")
```

## Step 7: Run It!
- Click the green "Run" button at the top
- Wait 60 seconds for dependencies to install
- You'll see a preview panel on the right

## Step 8: Get Your Live URL
- Right-click the preview panel
- Copy the URL: `https://tariff-app-YOUR_NAME.replit.dev`
- That's your live dashboard! 🎉

## Step 9: View Your Dashboard
- The backend runs on port 8000
- The frontend runs on port 3000 (built as static)
- Your URL shows the frontend + connects to backend

## Stop/Restart
- Click "Stop" to stop the server
- Click "Run" to restart

## That's It!
Your dashboard is live and accessible to anyone with the URL!

### Your URLs:
- **Frontend**: `https://tariff-app-YOUR_NAME.replit.dev`
- **Backend API**: `https://tariff-app-YOUR_NAME.replit.dev/api/stats`
- **API Docs**: `https://tariff-app-YOUR_NAME.replit.dev/docs`

## Troubleshooting

**"Module not found"?**
- The first run takes longer (installing deps)
- Wait 2 minutes and refresh

**"Port already in use"?**
- Click Stop, then Run again

**"Build failed"?**
- Check the console output
- Usually means missing `package.json` or `requirements.txt`

## Customize Later
- Edit files directly in Replit
- Click "Run" again
- Changes live in seconds!

## Deploy to Real Server Later
Once working on Replit, you can easily move to:
- Render.com
- Railway.app
- Fly.io
- AWS
- Any cloud provider

---

**Your tariff dashboard will be live in 5 minutes!** 🚀
