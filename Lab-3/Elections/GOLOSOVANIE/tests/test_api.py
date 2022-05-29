from rest_framework.test import APITestCase
import rest_framework.status as status
from django.urls import reverse_lazy


class GolosovanieApiTestCase(APITestCase):
    def test_index_page_get(self):
        url = reverse_lazy('index')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_elections_get(self):
        url = reverse_lazy('elections')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_candidates_get(self):
        url = reverse_lazy('my_candidates')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_slogan_get(self):
        url = reverse_lazy('add_slogan')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_batch_get(self):
        url = reverse_lazy('batch', args=(5,))
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    # def test_candidate_profile_get(self):
    #     pk = 3
    #     url = reverse_lazy('candidate', args=(pk,))
    #    # code = self.client.get(url).status_code
    #     print(self.client.get(url))
    #     # self.assertEqual(status.HTTP_200_OK, code)

    def test_add_candidate_get(self):
        url = reverse_lazy('add_candidate')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_302_FOUND, code)

    def test_registry_get(self):
        url = reverse_lazy('registry')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_add_registry_post(self):
        url = reverse_lazy('registry')
        code = self.client.post(url, {'username': 'oleg', 'nick_name': "aboba", 'email': 'user1@gmail.com',
                                      'password1': '123456', 'password2': '123456'}).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_login_get(self):
        url = reverse_lazy('login')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)

    def test_login_post(self):
        url = reverse_lazy('login')
       # self.client.User.create({'username': 'Kolya', 'password': 'kaba_baba'})
        code = self.client.post(url, {'id_username': 'Kolya', 'id_password': 'kaba_baba'}).status_code
        self.client.login(username='Kolya', password='kaba_baba')
        self.assertEqual(status.HTTP_200_OK, code)

    def test_add_slogan_get(self):
        url = reverse_lazy('add_slogan')
        code = self.client.get(url).status_code
        self.assertEqual(status.HTTP_200_OK, code)
