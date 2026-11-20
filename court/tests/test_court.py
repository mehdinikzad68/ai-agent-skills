"""Tests for the Artemis adaptation of court.py.

Adapted from the upstream test suite by Alex Chen (MIT,
https://github.com/alexyc9381/court-skill). Changes: 14-seat juror pool,
6-juror default, --full = 12, Persian verdict headings, Jev advisory render.
"""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..")
sys.path.insert(0, SKILL)
import court  # noqa: E402


class CourtTest(unittest.TestCase):
    def setUp(self):
        self.old = os.getcwd()
        self.tmp = tempfile.mkdtemp()
        os.chdir(self.tmp)
        os.makedirs(".court")
        with open(".court/case.md", "w") as f:
            f.write("Quit my job to sell candles on Etsy full time\n\nI have $8,000 saved.\n")

    def tearDown(self):
        os.chdir(self.old)
        shutil.rmtree(self.tmp)

    def open_trial(self, *extra):
        court.main(["init", "--case-file", ".court/case.md", "--seed", "7"] + list(extra))
        return court.load_state()

    def write_all(self, state, phase, text):
        for j in court.jobs(state, phase):
            with open(j["output"], "w") as f:
                f.write(text)

    def test_juror_pool_is_14_and_distinct(self):
        jurors = court.load_jurors()
        self.assertEqual(len(jurors), 14)
        self.assertEqual(len({j["name"] for j in jurors}), 14)
        names = {j["name"] for j in jurors}
        self.assertIn("The Iran Regulator", names)
        self.assertIn("The Iranian Customer", names)

    def test_default_jury_is_six(self):
        state = self.open_trial()
        self.assertEqual(len(state["jury"]), 6)

    def test_quick_jury_is_six_distinct(self):
        state = self.open_trial("--quick")
        self.assertEqual(len(state["jury"]), 6)
        self.assertEqual(len({j["name"] for j in state["jury"]}), 6)

    def test_full_jury_is_twelve(self):
        state = self.open_trial("--full")
        self.assertEqual(len(state["jury"]), 12)

    def test_jury_can_use_whole_pool(self):
        state = self.open_trial("--jury", "14")
        self.assertEqual(len(state["jury"]), 14)

    def test_briefs_name_their_output_and_the_record(self):
        state = self.open_trial("--jury", "3")
        court.main(["prompts", "jury"])
        j = court.jobs(state, "jury")[0]
        with open(j["brief"]) as f:
            text = f.read()
        self.assertIn(j["output"], text)
        self.assertIn("VOTE: GUILTY or NOT GUILTY", text)
        self.assertIn(os.path.abspath(os.path.join(state["dir"], "rebuttal", "defense.md")), text)

    def test_parse_vote_variants(self):
        v = court.parse_vote("VOTE: NOT GUILTY\nREASON: it pays.\nDECIDING FACT: $8,000\nWOULD FLIP IF: no savings")
        self.assertEqual(v["vote"], "NOT GUILTY")
        self.assertEqual(v["flip"], "no savings")
        self.assertEqual(court.parse_vote("**VOTE:** guilty\nREASON: x")["vote"], "GUILTY")
        self.assertIsNone(court.parse_vote("NO VOTE"))

    def test_full_trial_tally_and_render(self):
        state = self.open_trial("--jury", "5")
        self.write_all(state, "opening", "1. point")
        self.write_all(state, "rebuttal", "1. answer")
        votes = ["GUILTY", "GUILTY", "NOT GUILTY", "GUILTY", "NO VOTE"]
        for j, v in zip(court.jobs(state, "jury"), votes):
            with open(j["output"], "w") as f:
                f.write("NO VOTE" if v == "NO VOTE" else "VOTE: %s\nREASON: because | pipes\n" % v)
        t = court.tally(state)
        self.assertEqual((t["verdict"], t["guilty"], t["not_guilty"], t["no_vote"]), ("GUILTY", 3, 1, 1))
        self.assertEqual(court.verdict_line(t), "GUILTY, 3 to 1")
        self.write_all(state, "judge", "## The sentence\nKeep the job for now.")
        text = court.render(state)
        self.assertIn("# حکم دادگاه: GUILTY, 3 to 1", text)
        self.assertIn("Quit my job to sell candles", text)
        self.assertIn("because / pipes", text)
        self.assertIn("## The sentence", text)
        self.assertTrue(text.rstrip().endswith(court.ADAPT_CREDIT))
        self.assertIn(court.CREDIT, text)

    def test_jev_advisory_renders_but_is_not_a_vote(self):
        state = self.open_trial("--jury", "3")
        self.write_all(state, "opening", "1. point")
        self.write_all(state, "rebuttal", "1. answer")
        for j in court.jobs(state, "jury"):
            with open(j["output"], "w") as f:
                f.write("VOTE: NOT GUILTY\nREASON: fine\n")
        self.write_all(state, "judge", "## The sentence\nGo.")
        with open(os.path.join(state["dir"], "jev.md"), "w") as f:
            f.write("Jev risk score: 0.42 (below the 0.65 review threshold).")
        text = court.render(state)
        self.assertIn("## نظر مشورتی Jev (رأی نیست)", text)
        self.assertIn("0.42", text)
        self.assertIn("NOT GUILTY, 3 to 0", text)

    def test_hung_jury(self):
        state = self.open_trial("--jury", "4")
        for j, v in zip(court.jobs(state, "jury"), ["GUILTY", "NOT GUILTY", "GUILTY", "NOT GUILTY"]):
            with open(j["output"], "w") as f:
                f.write("VOTE: %s\n" % v)
        self.assertEqual(court.verdict_line(court.tally(state)), "HUNG JURY, 2 to 2")

    def test_next_walks_the_phases(self):
        state = self.open_trial("--jury", "3")
        self.assertTrue(court.missing(state, "opening"))
        self.write_all(state, "opening", "x")
        self.assertFalse(court.missing(state, "opening"))
        self.assertTrue(court.missing(state, "rebuttal"))


if __name__ == "__main__":
    unittest.main()
