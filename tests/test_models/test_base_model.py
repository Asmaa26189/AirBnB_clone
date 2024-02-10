#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instance(unittest.TestCase):
    """Unittest BaseModel class."""

    def test_base_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uniqueIds(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_diff_created_at(self):
        model1 = BaseModel()
        sleep(1)
        model2 = BaseModel()
        self.assertLess(model1.created_at, model2.created_at)

    def test_diff_updated_at(self):
        model1 = BaseModel()
        sleep(1)
        model2 = BaseModel()
        self.assertLess(model1.updated_at, model2.updated_at)

    def test_storage_new(self):
        self.assertIn(BaseModel(), models.storage.all().values())


class TestBaseModel_save(unittest.TestCase):
    """Unittests save BaseModel class."""

    def test_save(self):
        model = BaseModel()
        sleep(1)
        first_updated_at = model.updated_at
        model.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_more_saves(self):
        model1 = BaseModel()
        sleep(1)
        updated_at1 = model1.updated_at
        model2.save()
        updated_at2 = model2.updated_at
        self.assertLess(updated_at1, updated_at2)
        sleep(1)
        bm.save()
        self.assertLess(updated_at2, model1.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests to_dict BaseModel class."""

    def test_to_dict_type(self):
        model = BaseModel()
        self.assertTrue(dict, type(model.to_dict()))

    def test_to_dict_correct_data(self):
        model = BaseModel()
        self.assertIn("id", model.to_dict())
        self.assertIn("created_at", model.to_dict())
        self.assertIn("updated_at", model.to_dict())
        self.assertIn("__class__", model.to_dict())


if __name__ == "__main__":
    unittest.main()
