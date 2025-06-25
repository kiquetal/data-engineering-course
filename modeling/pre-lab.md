# Example SQL for fact_store

Below is an example SQL model for a fact table named `fact_store`, based on typical star schema conventions and the provided customer dimension structure. Adjust the fields and joins as needed for your actual schema and available tables.

```sql
-- models/star_schema/fact_store.sql

with sales as (
    select
        s.sale_id as store_sale_key,
        s.sale_date,
        s.store_id,
        s.customer_key,
        s.product_id,
        s.quantity,
        s.unit_price,
        s.total_amount
    from raw.sales s
)

select
    sales.store_sale_key,
    sales.sale_date,
    sales.store_id,
    sales.customer_key,
    sales.product_id,
    sales.quantity,
    sales.unit_price,
    sales.total_amount
from sales
```

- Replace `raw.sales` with your actual source table for sales transactions.
- Add or adjust columns as needed for your business logic.
- Place this SQL in `models/star_schema/fact_store.sql` in your dbt project.

# Example SQL for fact_order

Below is an example SQL model for a fact table named `fact_order`, following your specified columns and typical star schema conventions. This version includes joins to the dimension tables using the foreign keys.

```sql
-- models/star_schema/fact_order.sql

select
    o.order_id as fact_order_key,         -- Primary key
    c.customer_key,                       -- Foreign key to dim_customer
    e.employee_key,                       -- Foreign key to dim_employee
    f.office_key,                         -- Foreign key to dim_office
    p.product_key,                        -- Foreign key to dim_product
    o.order_date,                         -- Order date
    o.required_date as order_required_date,   -- Required date
    o.shipped_date as order_shipped_date,     -- Shipped date
    oi.quantity_ordered as quantity_order,    -- Quantity ordered
    oi.price_each as product_price            -- Product price
from raw.orders o
join raw.order_items oi on o.order_id = oi.order_id
join {{ ref('dim_customer') }} c on o.customer_id = c.customer_id
join {{ ref('dim_employee') }} e on o.employee_id = e.employee_id
join {{ ref('dim_office') }} f on o.office_id = f.office_id
join {{ ref('dim_product') }} p on oi.product_id = p.product_id
```

- Replace `raw.orders` and `raw.order_items` with your actual source tables if different.
- Place this SQL in `models/star_schema/fact_order.sql` in your dbt project.
- Adjust column names and joins as needed for your schema.

# Example SQL for dim_office

Below is an example SQL model for a dimension table named `dim_office`, using your specified columns and assuming a source table named `offices` exists.

```sql
-- models/star_schema/dim_office.sql

select
    o.office_code as office_key,   -- Surrogate or business key
    o.office_code,                 -- Foreign key for fact tables
    o.postal_code,
    o.city,
    o.state,
    o.country,
    o.territory
from raw.offices o
```

- Replace `raw.offices` with your actual source table if different.
- Place this SQL in `models/star_schema/dim_office.sql` in your dbt project.
- Adjust column names as needed for your schema.

# Example SQL for dim_employee

Below is an example SQL model for a dimension table named `dim_employee`, using your specified columns and assuming a source table named `employees` exists.

```sql
-- models/star_schema/dim_employee.sql

select
    e.employee_id as employee_key,         -- Surrogate or business key
    e.last_name as employee_last_name,
    e.job_title,
    e.email,
    e.first_name as employee_first_name
from raw.employees e
```

- Replace `raw.employees` with your actual source table if different.
- Place this SQL in `models/star_schema/dim_employee.sql` in your dbt project.
- Adjust column names as needed for your schema.

# Example SQL for dim_products

Below is an example SQL model for a dimension table named `dim_products`, using your specified columns and assuming source tables named `products` and `productLines` exist.

```sql
-- models/star_schema/dim_products.sql

select
    p.product_id as product_key,                -- Surrogate or business key
    p.product_name,
    p.product_line,
    p.product_scale,
    p.product_vendor,
    p.product_description,
    pl.text_description as product_line_description
from raw.products p
left join raw.productLines pl on p.product_line = pl.product_line
```

- Replace `raw.products` and `raw.productLines` with your actual source tables if different.
- Place this SQL in `models/star_schema/dim_products.sql` in your dbt project.
- Adjust column names as needed for your schema.
