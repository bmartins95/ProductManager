## Product Manager App

### Description

This is just a example app to illustrate the creation of a web interface using Django. You can delete, create and visualize products listed in the database.

### Dependencies
These are the dependencies needed to run this project:

- [Django](https://pypi.org/project/Django/)

## Usage

Firstly you need to start the server,  go to **/product_manager** folder and run:

``` python
python3 manage.py runserver
```
After running the server, your terminal will output something like this:

``` bash
System check identified no issues (0 silenced).
March 19, 2021 - 12:32:31
Django version 3.1.7, using settings 'product_manager.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Open the http://127.0.0.1:8000/ on your browser, now you probably are seeing a list with the products currently available in the database:

<img src="https://github.com/bmartins95/ProductManager/blob/main/figures/product-list.png">

You can see details of a product by clicking is his name:

<img src="https://github.com/bmartins95/ProductManager/blob/main/figures/product-detail.png">

Now you can delete the product by clicking in the **Delete** link:

<img src="https://github.com/bmartins95/ProductManager/blob/main/figures/product-delete.png">

You can also add new products.  Go to the products list page by clicking on the products link, then click on the **Create new product** link:

<img src="https://github.com/bmartins95/ProductManager/blob/main/figures/product-create.png">

## References

- https://docs.djangoproject.com/en/3.1/
