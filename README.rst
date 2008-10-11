================
SCOFIELD-PROJECT
================

In my need to provide my clients with a 'simple' shopping cart that's agile enough to customize quickly and pluggable enough to add to existing Django projects I have started the Scofield Project.  To stick with the Jazz theme the Scofield Project is appropriately named after the Master Jazz Guitarist John Scofield.

**Features**

- Nested Categories
- Manufacturers
- Multiple images per product with thumbnails and effects using sorl-thumbnail
- Wishlist
- Tagging
- Threaded Comments for products
- Products model is a abstract class allowing you to easily extend the fields

**Dependencies**

- Django-Tagging
- Django-ThreadedComments
- Sorl-thumbnail
- Django-Debug_toolbar (optional)

**TODO:**

- Add simple checkout
- Rethink the cart (whether or not to use generic relations and/or sessions)
- Add views for Wishlist
- Add tests

**References**

-  20seven_
-  John Scofield_
  
_20seven: http://20seven.org
_Scofield: http://johnscofield.com