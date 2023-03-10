# Create a virtual env
python -m venv .venv

# Activate it
source .venv/bin/activate

# Upgrade pip and install pip-tools

pip install -U pip pip-tools

# Refresh lockfiles

make refresh-lockfiles 

# Sync to dev environment

make sync-to-env env=dev