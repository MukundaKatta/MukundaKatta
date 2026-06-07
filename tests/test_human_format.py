"""Tests for ``refresh_stats._human``, the badge number formatter.

``_human`` feeds the ``message`` field of the shields.io endpoint JSON in
``.stats/*.json``, so its output is rendered verbatim on the public profile
badges. These are pure, offline assertions and run with the standard library:

    python3 -m unittest discover -s tests
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import refresh_stats as rs  # noqa: E402


class HumanFormatTests(unittest.TestCase):
    def test_below_thousand_is_plain_integer(self) -> None:
        self.assertEqual(rs._human(0), "0")
        self.assertEqual(rs._human(5), "5")
        self.assertEqual(rs._human(999), "999")

    def test_thousands_get_k_suffix(self) -> None:
        self.assertEqual(rs._human(1_000), "1.0k")
        self.assertEqual(rs._human(1_500), "1.5k")
        self.assertEqual(rs._human(23_400), "23.4k")

    def test_millions_get_m_suffix(self) -> None:
        self.assertEqual(rs._human(1_000_000), "1.0M")
        self.assertEqual(rs._human(2_500_000), "2.5M")

    def test_rounding_carries_into_next_unit(self) -> None:
        # Regression: 999_999 used to render the nonsensical "1000.0k" because
        # the magnitude check ran before rounding. It must round up to "1.0M".
        self.assertEqual(rs._human(999_999), "1.0M")
        self.assertEqual(rs._human(999_950), "1.0M")
        # Just below the carry threshold stays in the k unit.
        self.assertEqual(rs._human(999_949), "999.9k")

    def test_never_emits_overflowed_mantissa(self) -> None:
        # No formatted value should ever read ">= 1000" within its own unit.
        for n in (999, 1_000, 999_949, 999_950, 999_999, 1_000_000, 9_999_500):
            rendered = rs._human(n)
            mantissa = rendered.rstrip("kM")
            if mantissa != rendered:  # had a k/M suffix
                self.assertLess(float(mantissa), 1000.0, f"overflow for {n}: {rendered}")


if __name__ == "__main__":
    unittest.main()
