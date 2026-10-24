import json, subprocess, sys, tempfile, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
from not_ai_core.gate import evaluate, POLICIES
class GateTests(unittest.TestCase):
    def test_all_18_genres_are_available(self): self.assertEqual(len(POLICIES),18)
    def test_empty_fails(self): self.assertFalse(evaluate("  ").passed)
    def test_protected_literal_passes(self): self.assertTrue(evaluate("Nagpur event",protected_terms=["Nagpur"]).passed)
    def test_missing_protected_literal_fails(self): self.assertFalse(evaluate("Event",protected_terms=["Nagpur"]).passed)
    def test_advisory_does_not_fail(self): self.assertTrue(evaluate("Moreover, this robust approach helps.").passed)
    def test_unicode_is_flagged_advisory(self): self.assertTrue(evaluate("token\u200bsplit").passed)
    def test_cli_json(self):
        p=subprocess.run([sys.executable,str(ROOT/"tools/gate.py"),"--stdin","--json"],input="Plain sentence.",text=True,capture_output=True)
        self.assertEqual(p.returncode,0); self.assertTrue(json.loads(p.stdout)["passed"])
if __name__=="__main__": unittest.main()
