"""Tests for tools/check_readme_sync.py.

Run from the repository root with:

    python -m unittest discover -s tools/tests -v
"""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import check_readme_sync as sync  # noqa: E402


SOURCE = """\
### reBot Arm B601 DM

| Ecosystem | Status | Notes |
| :--- | :---: | :--- |
| **Motors** | \u2705 Completed | basic control |
| **ROS2** | \u2705 Completed | controller |
| **Isaac Sim** | \u2705 Completed | USD models |
| **Courses** | \u23F3 Planned | later |

## Specifications

| Parameter | B601-DM | B601-RS |
| :--- | :--- | :--- |
| **Payload** | 1.5kg | 2.5kg |
| **Max Reach** | 767 mm | 754 mm |
| **Supply Voltage** | DC 24V | DC 48V |
"""

# Same facts, different language and phrasing, comma decimal separator.
GOOD_TRANSLATION = """\
### reBot Arm B601 DM

| \u00c9cosyst\u00e8me | Statut | Notes |
| :--- | :---: | :--- |
| **Moteurs** | \u2705 Termin\u00e9 | contr\u00f4le de base |
| **ROS2** | \u2705 Termin\u00e9 | contr\u00f4leur |
| **Simulation Isaac Sim** | \u2705 Termin\u00e9 | mod\u00e8les USD |
| **Cours** | \u23F3 Pr\u00e9vu | plus tard |

## Sp\u00e9cifications

| Param\u00e8tre | B601-DM | B601-RS |
| :--- | :--- | :--- |
| **Charge utile** | 1,5 kg | 2,5 kg |
| **Port\u00e9e maximale** | 767 mm | 754 mm |
| **Tension d'alimentation** | DC 24V | DC 48V |
"""


class SyncCheckTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        self.write(sync.SOURCE, SOURCE)
        for name in sync.TRANSLATIONS:
            self.write(name, GOOD_TRANSLATION)

    def write(self, name, text):
        with open(os.path.join(self.root, name), "w", encoding="utf-8") as handle:
            handle.write(text)

    def test_translations_that_agree_pass(self):
        self.assertEqual(sync.check(self.root), [])

    def test_differing_decimal_separator_is_not_a_difference(self):
        """1,5 kg and 1.5kg are the same payload written two ways."""
        self.assertEqual(sync.check(self.root), [])

    def test_stale_status_is_caught(self):
        """The real bug: Isaac Sim shipped, a translation still says planned."""
        stale = GOOD_TRANSLATION.replace(
            "| **Simulation Isaac Sim** | \u2705 Termin\u00e9 |",
            "| **Simulation Isaac Sim** | \u23F3 Pr\u00e9vu |",
        )
        self.write("README_Fr.md", stale)
        problems = sync.check(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("README_Fr.md", problems[0])
        self.assertIn("row 3", problems[0])

    def test_missing_row_is_caught(self):
        """A feature row added to English but never to a translation."""
        short = GOOD_TRANSLATION.replace(
            "| **Simulation Isaac Sim** | \u2705 Termin\u00e9 | mod\u00e8les USD |\n", ""
        )
        self.write("README_zh.md", short)
        problems = sync.check(self.root)
        self.assertTrue(any("3 rows" in p and "README_zh.md" in p for p in problems))

    def test_superseded_specification_is_caught(self):
        """The real bug: README_zh kept 650 mm after English moved to 767 mm."""
        old = GOOD_TRANSLATION.replace("| 767 mm |", "| 650 mm |")
        self.write("README_zh.md", old)
        problems = sync.check(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("reach", problems[0])
        self.assertIn("650", problems[0])

    def test_missing_specification_row_is_caught(self):
        without = GOOD_TRANSLATION.replace(
            "| **Port\u00e9e maximale** | 767 mm | 754 mm |\n", ""
        )
        self.write("README_JP.md", without)
        problems = sync.check(self.root)
        self.assertTrue(any("no reach row" in p for p in problems))

    def test_missing_file_is_reported_not_crashed_on(self):
        os.remove(os.path.join(self.root, "README_es.md"))
        problems = sync.check(self.root)
        self.assertTrue(any("is missing" in p for p in problems))

    def test_extra_table_is_caught(self):
        extra = GOOD_TRANSLATION + (
            "\n| Extra | Statut |\n| :--- | :---: |\n| **Bonus** | \u2705 Termin\u00e9 |\n"
        )
        self.write("README_es.md", extra)
        problems = sync.check(self.root)
        self.assertTrue(any("roadmap tables" in p for p in problems))

    def test_missing_github_link_is_caught(self):
        """A community project added to English but missing from a translation."""
        url = "https://github.com/example/community-project"
        self.write(sync.SOURCE, SOURCE + f"\n- [Project]({url})\n")
        for name in sync.TRANSLATIONS:
            suffix = f"\n- [Projet]({url})\n" if name != "README_zh.md" else ""
            self.write(name, GOOD_TRANSLATION + suffix)
        problems = sync.check(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("README_zh.md", problems[0])
        self.assertIn("missing GitHub link", problems[0])
        self.assertIn(url, problems[0])

    def test_extra_github_link_is_caught(self):
        """A stale GitHub link left in a translation after removal from English."""
        url = "https://github.com/example/removed-project"
        self.write("README_JP.md", GOOD_TRANSLATION + f"\n- [Old]({url})\n")
        problems = sync.check(self.root)
        self.assertEqual(len(problems), 1)
        self.assertIn("README_JP.md", problems[0])
        self.assertIn("extra GitHub link", problems[0])
        self.assertIn(url, problems[0])


class RepositoryTest(unittest.TestCase):
    """The real files in this repository must agree."""

    def test_repository_readmes_are_in_sync(self):
        root = os.path.join(os.path.dirname(__file__), "..", "..")
        problems = sync.check(root)
        self.assertEqual(problems, [], "\n".join(problems))


if __name__ == "__main__":
    unittest.main()
