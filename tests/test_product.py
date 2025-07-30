import unittest
from unittest.mock import patch
from product import Product

class TestProduct(unittest.TestCase):
  def test_positive_storage_avaliable(self):
    """Caso de teste para estoque disponível"""
    self.product = Product("Test", 10, 30)
    valueToCheck = 10

    self.assertTrue(self.product.storage_avaliable(valueToCheck))

  def test_negative_storage_avaliable(self):
    """Caso de teste para estoque indisponível"""
    self.product = Product("Test", 10, 30)
    valueToCheck = 40

    self.assertFalse(self.product.storage_avaliable(valueToCheck))

  def test_equal_storage_avaliable(self):
    """Caso de teste para estoque disponível igual à quantidade"""
    self.product = Product("Test", 10, 30)
    valueToCheck = 30

    self.assertTrue(self.product.storage_avaliable(valueToCheck))

  def test_increment_storage(self):
    """Caso de teste para incremento de estoque"""
    self.product = Product("Test", 10, 30)
    incoming = 20
    expectedQuantity = 50
    result = self.product.increment_storage(incoming)

    self.assertEqual(result, expectedQuantity)

  def test_decrement_storage_success(self):
    """Caso de teste positivo para decremento de estoque"""
    self.product = Product("Test", 10, 30)
    outcoming = 20
    expectedQuantity = 10
    result = self.product.decrement_storage(outcoming)

    self.assertEqual(result, expectedQuantity)

  def test_decrement_storage_error(self):
    """Caso de teste negativo para decremento de estoque"""
    self.product = Product("Test", 10, 30)
    outcoming = 40

    self.assertRaises(ValueError, self.product.decrement_storage, outcoming)

  def test_storage_report_critical_low(self):
    """Caso de teste para relatorio de estoque criticamente baixo"""
    self.product = Product("Test", 10, 5)
    result = self.product.storage_report()

    self.assertEqual(result, 'Storage is CRITICAL LOW')

  def test_storage_report_low(self):
    """Caso de teste para relatorio de estoque baixo"""
    self.product = Product("Test", 10, 20)
    result = self.product.storage_report()

    self.assertEqual(result, 'Storage is LOW')

  def test_storage_report_medium(self):
    """Caso de teste para relatorio de estoque médio"""
    self.product = Product("Test", 10, 45)
    result = self.product.storage_report()

    self.assertEqual(result, 'Storage is MEDIUM')

  def test_storage_report_ok(self):
    """Caso de teste para relatorio de estoque ok"""
    self.product = Product("Test", 10, 60)
    result = self.product.storage_report()

    self.assertEqual(result, 'Storage is OK')

  @patch('builtins.print')
  def test_show_tags_success(self, mock_print):
    """Caso de teste de sucesso para ver as tags do produto"""
    self.product = Product("Test", 10, 60, ['bom', 'barato', 'aprovado', 'popular'])
    tagsToShow = 3

    self.product.show_tags(tagsToShow)
    self.assertEqual(mock_print.call_count, tagsToShow)

  def test_show_tags_error(self):
    """Caso de teste de erro para ver as tags do produto"""
    self.product = Product("Test", 10, 60, ['bom', 'barato', 'aprovado', 'popular'])
    tagsToShow = 5

    self.assertRaises(ValueError, self.product.show_tags, tagsToShow)

  def test_positive_tag_is_in_position(self):
    """Caso de teste de tag na posição esperada"""
    self.product = Product("Test", 10, 60, ['bom', 'barato', 'aprovado', 'popular'])
    tag = 'barato'
    position = 1

    self.assertTrue(self.product.tag_is_in_position(tag, position))

  def test_negative_tag_is_in_position(self):
    """Caso de teste de tag na posição errada"""
    self.product = Product("Test", 10, 60, ['bom', 'barato', 'aprovado', 'popular'])
    tag = 'aprovado'
    position = 0

    self.assertFalse(self.product.tag_is_in_position(tag, position))

  def test_positive_change_tag(self):
    """Caso de teste positivo de troca de tag"""
    self.product = Product("Test", 10, 60, ['bom', 'barato', 'aprovado', 'popular'])
    oldTag = 'barato'
    newTag = 'caro'
    expected = ['bom', 'caro', 'aprovado', 'popular']
    result = self.product.change_tag(oldTag, newTag)

    self.assertEqual(result, expected)

  def test_negative_change_tag(self):
    """Caso de teste negativo de troca de tag"""
    self.product = Product("Test", 10, 60, ['bom', 'barato', 'aprovado', 'popular'])
    oldTag = 'certo'
    newTag = 'errado'
    expected = ['bom', 'barato', 'aprovado', 'popular']
    result = self.product.change_tag(oldTag, newTag)

    self.assertEqual(result, expected)

unittest.main(argv=[''], verbosity=2, exit=False)
