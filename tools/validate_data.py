import json, csv, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def fail(msg):
    print(msg)
    sys.exit(1)

def ok(msg):
    print(msg)

def load_json(p):
    return json.loads(p.read_text(encoding="utf-8"))

def check_speedup_constants():
    p = DATA / "speedup_constants.json"
    j = load_json(p)
    if j["official_speedup_range_euclidean_vs_he"]["min"] != 21.0 or j["official_speedup_range_euclidean_vs_he"]["max"] != 46.0:
        fail("Official Euclidean vs HE range must be 21–46.")
    if j["official_speedup_range_dijkstra_vs_he"]["min"] != 2.0 or j["official_speedup_range_dijkstra_vs_he"]["max"] != 6.0:
        fail("Official Dijkstra vs HE range must be 2–6.")
    me = j["measured_speedup_range_euclidean_vs_he"]
    md = j["measured_speedup_range_dijkstra_vs_he"]
    if me["min"] < 21.0:
        fail("Measured Euclidean min must be >= 21.")
    if md["min"] < 2.0:
        fail("Measured Dijkstra min must be >= 2.")
    ok("Speedup constants validated.")

def check_visual_compare():
    p = DATA / "visual_compare_summary.csv"
    with p.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            for k in ["dataset","N","time_HE","time_E","time_D","h_star","speedup_E_over_HE","speedup_D_over_HE","sha256"]:
                if row.get(k, "") in ("", None):
                    fail(f"Missing field {k} in visual_compare_summary.")
    ok("Visual compare summary validated.")

def check_he_only():
    p = DATA / "he_only_summary.csv"
    with p.open("r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            for k in ["dataset","N","time_HE","h_max_HE","h_star","gap_HE","kappa","lambda_geo","K","R","sha256"]:
                if row.get(k, "") in ("", None):
                    fail(f"Missing field {k} in he_only_summary.")
    ok("HE-only summary validated.")

def main():
    check_speedup_constants()
    check_visual_compare()
    check_he_only()
    ok("All validations passed.")

if __name__ == "__main__":
    main()
