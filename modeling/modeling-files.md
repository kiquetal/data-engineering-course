# Database Normalization Illustrated

Database normalization is the process of structuring a database according to a series of normal forms to reduce data redundancy and improve data integrity. This document uses Mermaid diagrams to visualize the transformation of database schemas through the normalization process.

## Example: Online Bookstore Database

Let's start with an unnormalized table for an online bookstore and see how normalization improves its structure.

### Unnormalized Form

```mermaid
erDiagram
    ORDERS {
        int order_id
        date order_date
        string customer_name
        string customer_email
        string customer_address
        string book_title
        string book_author
        decimal book_price
        int quantity
        decimal total_price
        string shipping_method
        string payment_method
    }
```

### First Normal Form (1NF)
- Eliminate repeating groups
- Create separate tables for each set of related data
- Identify each set of related data with a primary key

```mermaid
erDiagram
    ORDERS {
        int order_id PK
        date order_date
        int customer_id FK
        decimal total_price
        string shipping_method
        string payment_method
    }
    
    CUSTOMERS {
        int customer_id PK
        string customer_name
        string customer_email
        string customer_address
    }
    
    ORDER_ITEMS {
        int order_item_id PK
        int order_id FK
        int book_id FK
        int quantity
        decimal item_price
    }
    
    BOOKS {
        int book_id PK
        string book_title
        string book_author
        decimal book_price
    }
    
    ORDERS ||--o{ ORDER_ITEMS : contains
    CUSTOMERS ||--o{ ORDERS : places
    BOOKS ||--o{ ORDER_ITEMS : includes
```

### Second Normal Form (2NF)
- Meet all requirements of 1NF
- Remove subsets of data that apply to multiple rows of a table and place them in separate tables
- Create relationships between these new tables and their predecessors through foreign keys

```mermaid
erDiagram
    ORDERS {
        int order_id PK
        date order_date
        int customer_id FK
        decimal total_price
        int shipping_method_id FK
        int payment_method_id FK
    }
    
    CUSTOMERS {
        int customer_id PK
        string customer_name
        string customer_email
    }
    
    CUSTOMER_ADDRESSES {
        int address_id PK
        int customer_id FK
        string street
        string city
        string state
        string postal_code
        string country
    }
    
    ORDER_ITEMS {
        int order_item_id PK
        int order_id FK
        int book_id FK
        int quantity
        decimal item_price
    }
    
    BOOKS {
        int book_id PK
        string book_title
        int author_id FK
        decimal book_price
    }
    
    AUTHORS {
        int author_id PK
        string author_name
        date birth_date
        string bio
    }
    
    SHIPPING_METHODS {
        int shipping_method_id PK
        string method_name
        decimal base_cost
        int estimated_days
    }
    
    PAYMENT_METHODS {
        int payment_method_id PK
        string method_name
    }
    
    ORDERS ||--o{ ORDER_ITEMS : contains
    CUSTOMERS ||--o{ ORDERS : places
    CUSTOMERS ||--o{ CUSTOMER_ADDRESSES : has
    BOOKS ||--o{ ORDER_ITEMS : includes
    AUTHORS ||--o{ BOOKS : writes
    SHIPPING_METHODS ||--o{ ORDERS : uses
    PAYMENT_METHODS ||--o{ ORDERS : paid_with
```

### Third Normal Form (3NF)
- Meet all requirements of 2NF
- Remove columns that are not dependent on the primary key

```mermaid
erDiagram
    ORDERS {
        int order_id PK
        date order_date
        int customer_id FK
        int shipping_method_id FK
        int payment_method_id FK
    }
    
    ORDER_TOTALS {
        int order_id PK, FK
        decimal subtotal
        decimal tax
        decimal shipping_cost
        decimal total_price
    }
    
    CUSTOMERS {
        int customer_id PK
        string customer_name
        string customer_email
    }
    
    CUSTOMER_ADDRESSES {
        int address_id PK
        int customer_id FK
        string street
        string city
        int state_id FK
        string postal_code
        int country_id FK
    }
    
    STATES {
        int state_id PK
        string state_name
        string state_code
    }
    
    COUNTRIES {
        int country_id PK
        string country_name
        string country_code
    }
    
    ORDER_ITEMS {
        int order_item_id PK
        int order_id FK
        int book_id FK
        int quantity
        decimal item_price
    }
    
    BOOKS {
        int book_id PK
        string book_title
        int author_id FK
        decimal base_price
    }
    
    BOOK_CATEGORIES {
        int book_category_id PK
        int book_id FK
        int category_id FK
    }
    
    CATEGORIES {
        int category_id PK
        string category_name
    }
    
    AUTHORS {
        int author_id PK
        string author_name
        date birth_date
        string bio
    }
    
    SHIPPING_METHODS {
        int shipping_method_id PK
        string method_name
        decimal base_cost
        int estimated_days
    }
    
    PAYMENT_METHODS {
        int payment_method_id PK
        string method_name
    }
    
    ORDERS ||--|| ORDER_TOTALS : has
    ORDERS ||--o{ ORDER_ITEMS : contains
    CUSTOMERS ||--o{ ORDERS : places
    CUSTOMERS ||--o{ CUSTOMER_ADDRESSES : has
    STATES ||--o{ CUSTOMER_ADDRESSES : located_in
    COUNTRIES ||--o{ CUSTOMER_ADDRESSES : located_in
    BOOKS ||--o{ ORDER_ITEMS : includes
    AUTHORS ||--o{ BOOKS : writes
    BOOKS ||--o{ BOOK_CATEGORIES : belongs_to
    CATEGORIES ||--o{ BOOK_CATEGORIES : contains
    SHIPPING_METHODS ||--o{ ORDERS : uses
    PAYMENT_METHODS ||--o{ ORDERS : paid_with
```

## Benefits of Normalization

1. **Minimizes Redundancy**: Less duplicate data means less storage space required.
2. **Improves Data Integrity**: Reduces the risk of data inconsistencies.
3. **Better Query Performance**: For complex queries and updates.
4. **More Flexible Database Design**: Makes it easier to extend the database structure.
5. **Reduces Update Anomalies**: Prevents errors when inserting, updating, or deleting data.

## Drawbacks to Consider

1. **Increased Complexity**: More tables mean more joins in queries.
2. **Performance Impact**: Excessive normalization can negatively impact read performance for some operations.
3. **Development Overhead**: More tables can increase development time and complexity.

Remember that normalization is a guideline, not a strict rule. In real-world applications, controlled denormalization might be applied for performance optimization.
