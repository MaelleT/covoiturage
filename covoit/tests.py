from django.test import TestCase
from covoit.models import OffrePermanente, TypeOffre, Lieu, Jour
from posix import unlink
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.test.client import Client

# Create your tests here.
class OffrePermanenteMethodTests(TestCase):

    def setUp(self):
        TestCase.setUp(self)
        self.unLieu = Lieu(libelle='Nantes - Nantes Nord')
        self.unType=TypeOffre(libelle = 'Départ')
        self.unJour=Jour('lundi')
        self.unUser=User.objects.create_user('test', 'test@test.com', 'test1234')
        self.OffrePermanenteDep=OffrePermanente(lieu=self.unLieu,type=self.unType,jour=self.unJour,auteur=self.unUser)
        
    def tearDown(self):
        TestCase.tearDown(self)
        
    def test_isDepart_offre(self):
        """
        test_isDepart_offre doit retourner True pour les questions de type Départ
        """
        self.assertEqual(self.OffrePermanenteDep.isDepart(),True,"Erreur : Offre de type départ") 
    
def create_offre(unLieu,unType,unJour,unUser):
    '''
    Creates a question with the given question_text and published givne number of days
    '''
    return OffrePermanente.objects.create(lieu=unLieu,type=unType,jour=unJour,auteur=unUser)
    
class TestMesOffresView(TestCase):
    """ Test la vue MesOffres"""
    def setUp(self):
        TestCase.setUp(self)
        unLieu = Lieu(libelle='Nantes - Nantes Nord')
        unLieu.save()
        unType=TypeOffre(libelle = 'Départ')
        unType.save()
        unJour=Jour(libelle='lundi')
        unJour.save()
        unUser=User.objects.create_user('test', 'test@test.com', 'test1234')
        unUser.save()
        
        create_offre(unLieu,unType,unJour,unUser)
        
    def tearDown(self):
        TestCase.tearDown(self)
    
    def testMesOffresWithoutConnexion(self):
        '''
        Teste l'accès à mes offres sans connexion : erreur 302 attendue
        ''' 
        response = self.client.get(reverse('covoit:mesOffres'))
        self.assertEqual(response.status_code, 302)
        
    def testMesOffresWithConnexion(self):
        '''
        Teste l'accès à mes offres avec connexion utilisateur auteur des offres
  
        ''' 
        self.client.login(username='test', password='test1234')
        response = self.client.get(reverse('covoit:mesOffres'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].username,'test')
        
        self.assertEqual(len(response.context['offres_user']),1)
        
    def testMesOffresWithConnexionOtherUser(self):
        '''
        Teste l'accès à mes offres avec connexion d'un autre utilisateur 
  
        ''' 
        unUser1=User.objects.create_user('test1', 'test1@test.com', 'test1234')
        unUser1.save()
        self.client.login(username='test1', password='test1234')
        
        response = self.client.get(reverse('covoit:mesOffres'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["user"].username,'test1')
        
        self.assertEqual(len(response.context['offres_user']),0)
