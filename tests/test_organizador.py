import unittest
import os
import shutil
from organizador.organizador import organize_files

class TestOrganizador(unittest.TestCase):

    def setUp(self):
        # Cria uma pasta de teste
        self.test_dir = 'tests/temp_test_dir'
        os.makedirs(self.test_dir, exist_ok=True)

        # Cria arquivos com diferentes extensões
        open(os.path.join(self.test_dir, 'exemplo.txt'), 'w').close()
        open(os.path.join(self.test_dir, 'manual.pdf'), 'w').close()
        open(os.path.join(self.test_dir, 'script.bat'), 'w').close()

    def test_organiza_arquivos(self):
        organize_files(self.test_dir)

        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'TextFiles', 'txt', 'exemplo.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'PDFs', 'pdf', 'manual.pdf')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Comand', 'bat', 'script.bat')))

    def tearDown(self):
        # Apaga a pasta de teste
        shutil.rmtree(self.test_dir)

if __name__ == '__main__':
    unittest.main()
