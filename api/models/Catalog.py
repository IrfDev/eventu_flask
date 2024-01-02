"""
Models for products and stock
"""
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import mapped_column

from ...db import db


class Prouct(db.Model):
    """Products"""

    id = mapped_column(Integer, primary_key=True)
    name = ""
    description = ""
    price = ""
    discount = ""
    category = ""
    images = ""
    feature_image = ""
    type = ""
    brand = ""
    variables = ""


class Product_Variable(db.Model):
    """Variables for products"""
