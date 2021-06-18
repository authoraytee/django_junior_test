from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
 
from .models import Event
 
 
class EventTests(TestCase):
 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
 
        self.event = Event.objects.create(
            EventName='Name',
            PublicationDate=3,
            EventDate=3,
        )

    def test_string_representation(self):
        event = Event(EventName='Name')
        self.assertEqual(str(event), event.EventName)



    #---------------------------------------------------------------------
    def test_event_content(self):
        self.assertEqual(f'{self.event.EventName}', 'Name')
        self.assertEqual(f'{self.event.PublicationDate}', 3)

    #---------------------------------------------------------------------
    def test_event_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
 
    #---------------------------------------------------------------------
    def test_event_detail_view(self):
        response = self.client.get('/event/1/')
        no_response = self.client.get('/event/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Name')
        self.assertTemplateUsed(response, 'event_detail.html')