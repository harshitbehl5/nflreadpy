import os
import traceback

# =========================
# Create output directory
# =========================
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

# =========================
# Helper function
# =========================
def safe_export(name, func):
    """
    Runs a loader function and saves output to CSV.
    Continues even if one dataset fails.
    """
    try:
        print(f"Loading {name}...")
        df = func()
        path = f"{EXPORT_DIR}/{name}.csv"
        df.to_csv(path, index=False)
        print(f"✔ Saved {path}")
    except Exception as e:
        print(f"✖ Failed {name}")
        traceback.print_exc()


# =========================
# IMPORT LOADERS
# =========================
from load_pbp import load_pbp
from load_players import load_players
from load_teams import load_teams
from load_schedules import load_schedules
from load_rosters import load_rosters
from load_rosters_weekly import load_rosters_weekly
from load_depth_charts import load_depth_charts
from load_injuries import load_injuries
from load_snap_counts import load_snap_counts
from load_participation import load_participation
from load_stats import load_stats
from load_pfr_advstats import load_pfr_advstats
from load_nextgen_stats import load_nextgen_stats
from load_draft_picks import load_draft_picks
from load_trades import load_trades
from load_contracts import load_contracts
from load_officials import load_officials
from load_combine import load_combine
from load_ffverse import load_ffverse
from load_ftn_charting import load_ftn_charting

# datasets.py loaders
from datasets import (
    load_player_name_mapping,
    load_team_abbr_mapping
)

# =========================
# EXPORT EVERYTHING
# =========================
print("=== STARTING POWER BI EXPORT BUILD ===")

safe_export("pbp", load_pbp)
safe_export("players", load_players)
safe_export("teams", load_teams)
safe_export("schedules", load_schedules)

safe_export("rosters", load_rosters)
safe_export("rosters_weekly", load_rosters_weekly)
safe_export("depth_charts", load_depth_charts)
safe_export("injuries", load_injuries)

safe_export("snap_counts", load_snap_counts)
safe_export("participation", load_participation)
safe_export("stats", load_stats)
safe_export("pfr_advstats", load_pfr_advstats)
safe_export("nextgen_stats", load_nextgen_stats)

safe_export("draft_picks", load_draft_picks)
safe_export("trades", load_trades)
safe_export("contracts", load_contracts)
safe_export("officials", load_officials)
safe_export("combine", load_combine)

safe_export("ffverse", load_ffverse)
safe_export("ftn_charting", load_ftn_charting)

safe_export("player_name_mapping", load_player_name_mapping)
safe_export("team_abbr_mapping", load_team_abbr_mapping)

print("=== POWER BI EXPORT BUILD COMPLETE ===")
