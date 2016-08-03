from django.test import TestCase
from covoit.models import OffrePermanente, TypeOffre, Lieu, Jour
from posix import unlink

# Create your tests here.
class OffrePermanenteMethodTests(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.unLieu = Lieu(libelle='Nantes - Nantes Nord')
        self.unType=TypeOffre(libelle = 'Départ')
        self.unJour=Jour('lundi')
        self.OffrePermanenteDep=OffrePermanente(lieu=self.unLieu,type=self.unType,jour=self.unJour)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_isDepart_offre(self):
        """
        test_isDepart_offre doit retourner True pour les questions de type Départ
        """
        self.assertEqual(self.OffrePermanenteDep.isDepart(),True,"Erreur : Offre de type départ") 