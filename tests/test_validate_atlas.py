import unittest
import tempfile
from pathlib import Path
import sys

# Add scripts to path
sys.path.append(str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_atlas import validate_catalog

class TestValidateAtlas(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        
        # Create minimal required structure
        (self.root / "CATALOG.md").touch()
        (self.root / "skills").mkdir()
        
    def tearDown(self):
        self.temp_dir.cleanup()

    def test_valid_links_and_anchors(self):
        (self.root / "doc1.md").write_text("# Doc 1\n\nLink to [doc2](doc2.md#section-2) and [itself](#doc-1).")
        (self.root / "doc2.md").write_text("# Doc 2\n\n## Section 2")
        
        errors = validate_catalog(self.root)
        self.assertEqual(errors, [])
        
    def test_missing_file(self):
        (self.root / "doc1.md").write_text("[broken](missing.md)")
        
        errors = validate_catalog(self.root)
        self.assertTrue(any("Missing file" in e for e in errors))
        
    def test_missing_anchor(self):
        (self.root / "doc1.md").write_text("[broken](doc2.md#missing-section)")
        (self.root / "doc2.md").write_text("# Doc 2")
        
        errors = validate_catalog(self.root)
        self.assertTrue(any("Missing anchor" in e for e in errors))
        
if __name__ == "__main__":
    unittest.main()
