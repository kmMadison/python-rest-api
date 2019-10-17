import app
import product
from marshmallow import Schema, fields, pprint

#Product Schema
class ProductSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

#init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)