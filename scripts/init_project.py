# -*- coding: utf-8 -*-
"""
init_project.py — One-click Project Bootstrap Tool for Bolla-Agentic OS
"""
import argparse
import json
from pathlib import Path
from datetime import datetime

def bootstrap(project_name: str):
    root = Path(__file__).resolve().parent.parent
    print(f"🚀 Initializing Bolla-Agentic OS Living Memory for: {project_name}")

    # Reset ai_state.json
    state_file = root / "Root" / "ai_state.json"
    state = {
        "mode": "[ACTIVE_PROJECT_ORCHESTRATION]",
        "current_tag": f"[{project_name.upper()}_INIT]",
        "turn_count": 0,
        "git_commit": "HEAD",
        "egm_role": "ELEPHANT_ARCHITECT",
        "goldfish_review_verdict": "VERIFIED_PASS",
        "drift_check_status": "PASS_ZERO_DRIFT",
        "last_action": f"Bootstrapped new project workspace for {project_name}",
        "next_action": "Begin Phase 1 Requirements & Planning with AI Agent",
        "last_message_summary": f"Initialized {project_name} living memory kernel",
        "last_updated": datetime.now().isoformat()
    }
    state_file.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Reset Root/ai_state.json to Turn 0 for {project_name}")
    print("✅ System ready. Start pairing with your AI agent!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bootstrap a new project in Bolla-Agentic OS")
    parser.add_argument("--name", default="NewProject", help="Name of your project")
    args = parser.parse_args()
    bootstrap(args.name)
