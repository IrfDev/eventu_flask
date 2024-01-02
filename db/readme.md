# Models

Entities in the database

## Catalog

Products and references

### Product

- name
- description
- price
- discount
- Category:
  - This come from the category table
  - Array of categories
- Images:
  Array of medias type images
- Feature image:
  Id of one of the images array
- Product type:
  - Simple
  - Variable
- Brand:
  - Brand id
- Variables:
  - Stock id
  - Count
  - Image

### Variable

- Name
- Description

### Category

- Name
- Feature image
- Description

### Brand

- Name
- Feature image
- Description

## Transactions

User interactions

### Product reference

- Product id
- Count

### Order

- User id
- Products:
  - Array of references of product references
- Total amount
- Status: status id

### Status

- Name
- Description

### Shipping

- Type:
  - Region
- Amount
- Region
- Min amount

### Cart

- User id
- Products:
  - Array of references of product references
- Coupon

### Coupon

- Code
- Type:
  - Total
  - Category
- Amount

## Content

### Media

- Url
- Name
- Type
- Size

## User Management

### User type

- Buyer
- Seller
