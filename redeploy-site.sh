#!/bin/bash
tmux kill-server
cd ~/Portfolio-Site
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s portfolio "cd ~/Portfolio-Site && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"


