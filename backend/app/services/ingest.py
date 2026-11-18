import json

from app.db import FIXTURES_DIR
from app.modules.dup_hop_quarantine import service as dup_svc


def run_batch() -> dict:
    """装载入口：读夹具后交由 dup_hop_quarantine 模块裁定 + 落库（失败闭）。"""
    path = FIXTURES_DIR / "ingest_batch.json"
    if not path.exists():
        return {"ok": False, "error": "缺少 ingest_batch.json"}
    payload = json.loads(path.read_text(encoding="utf-8"))
    return dup_svc.run_batch(
        payload.get("hops", []),
        batch_id=payload.get("batch_id"),
        cutoff_ts=payload.get("cutoff_ts"),
    )
