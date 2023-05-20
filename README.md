# Template of a e-shop (FastAPI+SQLAlchemy)

Production-ready backend template for a b2b e-shop. Includes auth, e-mail notifications, basic items management for business (suppliers) and customers (sellers). 

Start the project:

```shell
make build
make migrations
make population
make application
```

To run the project locally:

```shell
python3 app/main.py
```

You can find OpenAPI schema at http://localhost/docs

You can log in as a seller or a supplier with `supplier@mail.ru` and `seller@mail.ru` respectively. Password -
`Password1!`

**Architecture**

You might be overwhelmed by the amount of custom elements in the project. But let me reassure you that it’s quite
easy to use once you get the gist.

SQLAlchemy models defined at `app/orm`. Notice that a lot of commonly used types are already defined:
`bool_true`, `decimal_10_2`, `moscow_datetime_timezone` etc. Feel free to add new.

Look at `app/core/app/crud/__init__.py`. It’s where main class for CRUD operations is defined:

```python
class _CRUD:
    admins: CRUD[AdminModel] = CRUD(AdminModel)
    categories: CRUD[CategoryModel] = CRUD(CategoryModel)
    companies: CRUD[CompanyModel] = CRUD(CompanyModel)
    ...
```

As you can see it contains all the models. What is more it provides interface for all base SQL operations. You can find them
at `app/core/app/crud/operations`. It’s possible to do joins, grouping, ordering etc. just by passing args to functions:

```python
from corecrud import Limit, Offset, Options, OrderBy, Where
from core.app import crud
from orm import ProductModel, ProductPriceModel, SupplierModel

await crud.products.select.many(
    Where(
        ProductModel.is_active.is_(True),
        ProductModel.category_id == filters.category_id if filters.category_id else None,
    ),
    Options(
        selectinload(ProductModel.prices),
        selectinload(ProductModel.images),
        selectinload(ProductModel.supplier).joinedload(SupplierModel.user),
    ),
    Offset(pagination.offset),
    Limit(pagination.limit),
    OrderBy(filters.sort_type.by.asc() if filters.ascending else filters.sort_type.by.desc()),
    session=session,
)
```

All inputs and outputs of any endpoint should be typed. You can
find schemas at app/schemas. Feel free to add new schemas but examine existing ones first.

All common functions (*auth*, *session*, *AWS interfaces*) are kept at app/core/depends. Before writing new piece of
code
make sure it has not been written yet ;)

