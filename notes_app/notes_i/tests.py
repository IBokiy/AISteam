from django.test import TestCase
from django.urls import reverse
from .models import Notes, Category
from .forms import CreateNoteForm, UpdateNoteForm


class NotesAppTest(TestCase):
	@staticmethod
	def create_note(tittle='Test', text='Test'):
		return Notes.objects.create(tittle=tittle, text=text)

	@staticmethod
	def create_category(tittle='Test'):
		return Category.objects.create(tittle=tittle)

	def test_note_creation(self):
		test_note = self.create_note()
		self.assertTrue(isinstance(test_note, Notes))
		self.assertEqual(str(test_note), test_note.tittle)
		test_repr_note = f'Note object: {test_note.tittle}'
		self.assertEqual(repr(test_note), test_repr_note)

	def test_note_update(self):
		test_note = self.create_note()
		self.assertTrue(isinstance(test_note, Notes))
		self.assertEqual(str(test_note), test_note.tittle)
		test_updated_note = test_note.tittle = 'Test2'
		self.assertNotEqual(test_note, test_updated_note)

	def test_category_creation(self):
		test_category = self.create_category()
		self.assertTrue(isinstance(test_category, Category))
		self.assertEqual(str(test_category), test_category.tittle)
		test_repr_category = f'Category object: {test_category.tittle}'
		self.assertEqual(repr(test_category), test_repr_category)

	def test_index_view(self):
		test_note = self.create_note()
		url = reverse('index')
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		self.assertIn(test_note.tittle, resp.content.decode())

	def test_create_note_view(self):
		url = reverse('create_note')
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		self.assertIn('Create Note' and '<form', resp.content.decode())
		test_note = self.create_note()
		data = {
			'tittle': test_note.tittle,
			'text': test_note.text,
		}
		form = CreateNoteForm(data=data)
		self.assertTrue(form.is_valid())
		form.save()
		test_notes = Notes.objects.all()
		self.assertEqual(test_note.id, test_notes[0].id)
		self.assertEqual(self.client.post(path=url, data=data).status_code, 302)

	def test_update_note_view(self):
		test_note = self.create_note()
		test_note.save()
		url = reverse(viewname='update_note', args=[test_note.id])
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 200)
		self.assertIn('Update', resp.content.decode())
		data = {
			'tittle': "tittle1",
			'text': "text2",
		}
		self.assertEqual(self.client.post(path=url, data=data).status_code, 302)

	def test_delete_views(self):
		test_note = self.create_note()
		url = reverse(viewname='delete_note', args=[test_note.id])
		resp = self.client.get(url)
		self.assertEqual(resp.status_code, 302)

	def test_note_forms(self):
		test_note = self.create_note()
		valid_data = {
			'tittle': test_note.tittle,
			'text': test_note.text,
		}
		form = CreateNoteForm(data=valid_data)
		self.assertTrue(form.is_valid())
		form = UpdateNoteForm(data=valid_data)
		self.assertTrue(form.is_valid())
		invalid_data = {
			'tittle': "a" * 101,
			'text': '',
		}
		form = CreateNoteForm(data=invalid_data)
		self.assertFalse(form.is_valid())
