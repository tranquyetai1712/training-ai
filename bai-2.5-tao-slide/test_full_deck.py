import os
import unittest
import zipfile
from pptx import Presentation
from generate_deck import create_deck

class TestFullDeck(unittest.TestCase):
    def test_create_deck_generates_valid_10_slide_pptx(self):
        output_file = create_deck()
        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 20000)

        # Kiểm tra qua Presentation
        prs = Presentation(output_file)
        self.assertEqual(len(prs.slides), 10)

        # Kiểm tra không có chữ "7 phút" trong toàn bộ XML
        with zipfile.ZipFile(output_file, 'r') as z:
            slide_xmls = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            self.assertEqual(len(slide_xmls), 10)
            for s in slide_xmls:
                xml_data = z.read(s).decode('utf-8')
                self.assertNotIn("7 PHÚT", xml_data.upper())

if __name__ == "__main__":
    unittest.main()
