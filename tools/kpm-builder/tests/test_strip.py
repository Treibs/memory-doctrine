"""Tests for kpm_builder.strip helpers."""


# ── belief-state promotion (#5 / EFF-2, Builder side) ──────────────────────────


class TestApplyBeliefStatus:
    def _idea(self, bucket):
        from kpm_builder.schema import ScoredIdea, SourceTier
        from kpm_builder.snapshot import Snapshot, SpanRef

        return ScoredIdea(
            statement="s",
            source_ref="https://ex.com/a",
            span=SpanRef(sha256="x", start=0, end=1, text="t"),
            source_tier=SourceTier.UNKNOWN,
            access_level="public",
            confidence=bucket,
            generativity=3,
        )

    def test_buckets_map_to_statuses(self):
        from kpm_builder.schema import ConfidenceBucket
        from kpm_builder.strip import apply_belief_status

        class _Ax:
            status = "candidate"

        axioms = [_Ax(), _Ax(), _Ax()]
        ideas = [
            self._idea(ConfidenceBucket.SUPPORTED),
            self._idea(ConfidenceBucket.PARTIAL),
            self._idea(ConfidenceBucket.UNVERIFIED),
        ]
        apply_belief_status(axioms, ideas)
        assert [a.status for a in axioms] == ["locked", "provisional", "candidate"]

    def test_misalignment_raises(self):
        import pytest as _pytest

        from kpm_builder.strip import apply_belief_status

        with _pytest.raises(ValueError):
            apply_belief_status([], [self._idea(None)])
