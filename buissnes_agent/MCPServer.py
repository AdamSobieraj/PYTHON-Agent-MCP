from __future__ import annotations

import sys

from pathlib import Path

try:
    from .mcp_server import main
except ImportError:
    current_dir = Path(__file__).resolve().parent
    parent_dir = current_dir.parent
    if str(parent_dir) not in sys.path:
        sys.path.insert(0, str(parent_dir))
    from buissnes_agent.mcp_server import main


if __name__ == "__main__":
    main()
