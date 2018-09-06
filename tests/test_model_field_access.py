from unittest import TestCase
from better_leancloud_storage.storage import models, fields


class TestModelCreation(TestCase):

    def test_simple_access(self):
        class ModelA(models.Model):
            name = fields.Field()

        model = ModelA.create(name='my name')
        self.assertEqual(model.name, 'my name')

    def test_inherit_field_access(self):
        class BaseModel(models.Model):
            name = fields.Field()

        class ModelA(BaseModel):
            pass

        class ModelB(BaseModel):
            age = fields.Field()

        a = ModelA.create(name='my name')
        self.assertEqual(a.name, 'my name')
        b = ModelB.create(name='my name', age=18)
        self.assertEqual(b.name, 'my name')
        self.assertEqual(b.age, 18)

    def test_multi_inherit_overwrite_field(self):
        class BaseA(models.Model):
            name = fields.Field()

        class BaseB(models.Model):
            name = fields.Field()

        class ModelA(BaseA):
            name = fields.Field()

        class ModelB(BaseA, BaseB):
            name = fields.Field()

        class ModelC(BaseA, BaseB):
            age = fields.Field()

        a = ModelA.create(name='hello')
        self.assertEqual(a.name, 'hello')
        b = ModelB.create(name='world')
        self.assertEqual(b.name, 'world')
        c = ModelC.create(name='!', age=10)
        self.assertEqual(c.name, '!')
        self.assertEqual(c.age, 10)
