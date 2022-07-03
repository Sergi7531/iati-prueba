# Technical test for IATI Seguros:
This test was entirely made by Sergio Domínguez and its main goal is to emulate a small shopping application backend.

## Getting started:

Assuming we are in a Linux environment, we install the dependencies:

    sudo apt install python3-pip
    pip install django
    
Now, we need to make sure we have the right database manager.
<br/>
We can ensure this by running the following command:
    
    sudo apt install mysql-server

Setting up the database will be easy:

    mysql -u root -p

    CREATE DATABASE catalog;

    exit

## Setup local environment:

Migrate the models to the MySQL database:

    python3 manage.py migrate

And load the products from the fixture:

    python3 manage.py loaddata products

After this, we can run the server and start the tests:

    python3 manage.py runserver

## Testing the endpoints:

#### Catalog (GET) `/catalog/`:

This endpoint will return the list of all products in the catalog.<br/>

(The catalog is based in 2 database tables: `shoppingcart_cap` and `shoppingcart_tshirt`)

The response should look like this:

<details closed>
<summary>Response</summary>

``` json
{
    "caps": [
        {
            "main_color": "Negro",
            "secondary_color": null,
            "brand": "Ralph Lauren",
            "catalog_inclusion_date": "2022-06-29T19:38:05Z",
            "image_url": "https://m.media-amazon.com/images/I/81lDs66F1pL._AC_UX522_.jpg",
            "description": "Gorra Ralph Lauren adulto",
            "id": 4,
            "logo_color": "Beige"
        },
        {
            "main_color": "Negro",
            "secondary_color": "Rojo",
            "brand": "Adidas",
            "catalog_inclusion_date": "2022-07-02T10:00:00Z",
            "image_url": "https://www.rekordsport.es/uploads/photo/image/4920/gallery_A02506_1.JPG",
            "description": "Gorra adidas con gráfico para niño",
            "id": 1,
            "logo_color": "Blanco"
        },
        {
            "main_color": "Blanco",
            "secondary_color": "Rojo",
            "brand": "FILA",
            "catalog_inclusion_date": "2022-07-02T11:00:00Z",
            "image_url": "https://deportesmoya.es/127801-large_default/gorra-fila-trucker-cap-blanco-azul.jpg",
            "description": "Gorra FILA Trucker",
            "id": 3,
            "logo_color": "Azul/Rojo"
        },
        {
            "main_color": "Rojo",
            "secondary_color": null,
            "brand": "Lacoste",
            "catalog_inclusion_date": "2022-07-02T23:00:00Z",
            "image_url": "https://http2.mlstatic.com/D_NQ_NP_730275-MLC45216814813_032021-W.jpg",
            "description": "Gorra Lacoste edición limitada 25 aniversario",
            "id": 5,
            "logo_color": "Verde con borde blanco"
        },
        {
            "main_color": "Negro",
            "secondary_color": null,
            "brand": "Nike",
            "catalog_inclusion_date": "2022-07-03T11:00:04Z",
            "image_url": "https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/ntdkudemnsoblgfhg17p/gorra-aerobill-classic-99-FjPlk8.png",
            "description": "Gorra Nike para adulto",
            "id": 2,
            "logo_color": "Blanco"
        }
    ],
    "t-shirts": [
        {
            "main_color": "Negro",
            "secondary_color": null,
            "brand": "Nike",
            "catalog_inclusion_date": "2022-07-01T10:00:00Z",
            "image_url": "https://cdn.idealo.com/folder/Product/201788/5/201788558/s11_produktbild_gross_4/nike-sportswear-t-shirt-dm4685.jpg",
            "description": "Nike Sportswear t-shirt",
            "id": 1,
            "size": "S",
            "fabric": "Poliéster",
            "gender": "Hombre",
            "sleeves": false
        },
        {
            "main_color": "Negro",
            "secondary_color": "Camel",
            "brand": "Guess",
            "catalog_inclusion_date": "2022-07-01T10:00:02Z",
            "image_url": "https://images.sportsdirect.com/images/products/65826303_l_a1.jpg",
            "description": "Guess lady \"NORAH\" t-shirt new collection",
            "id": 2,
            "size": "XS",
            "fabric": "Poliéster 100%",
            "gender": "Mujer",
            "sleeves": true
        },
        {
            "main_color": "Negro",
            "secondary_color": "Azul y Verde",
            "brand": "Hollister",
            "catalog_inclusion_date": "2022-07-01T10:00:04Z",
            "image_url": "https://img.hollisterco.com/is/image/anf/KIC_324-2083-1063-916_prod1?policy=product-medium&wid=350&hei=438",
            "description": "Hollister logo icon CREW T-shirt. Ombre coloring...",
            "id": 3,
            "size": "MAS",
            "fabric": "Poliéster 100%",
            "gender": "Hombre",
            "sleeves": false
        },
        {
            "main_color": "Blanco",
            "secondary_color": "Azul oscuro",
            "brand": "Tommy Hilfiger",
            "catalog_inclusion_date": "2022-07-01T10:00:06Z",
            "image_url": "https://tommy-europe.scene7.com/is/image/TommyEurope/KB0KB07286_YBR_main_listing?$listing$",
            "description": "Camiseta para niños de Tommy Hilfiger con gráfico en el centro.",
            "id": 4,
            "size": "L",
            "fabric": "Poliéster 90%",
            "gender": "Hombre",
            "sleeves": false
        },
        {
            "main_color": "Verde claro",
            "secondary_color": null,
            "brand": "Blue Banana",
            "catalog_inclusion_date": "2022-07-01T10:00:08Z",
            "image_url": "https://cdn.shopify.com/s/files/1/0122/2724/8185/products/LSClassicTeeMint2_300x.jpg?v=1647509794",
            "description": "Camiseta Blue Banana con gráfico en la parte superior derecha",
            "id": 5,
            "size": "XL",
            "fabric": "Poliéster 90%",
            "gender": "Unisex",
            "sleeves": true
        }
    ]
}
```
</details>

#### Cart (GET) `/cart/`:

This endpoint will return the cart and its' items.

The cart is updated daily, thus meaning you will have to add products to the cart in order to see changes.

This is how the cart would look like when some items are added to it:

![](https://imgur.com/0N0QP9a.png)

#### Cart (POST) `/addtocart/`:

This endpoint will add a product to the cart.

Has 2 parameters:

- type: The product type. It is either a 't-shirt' or a 'cap' (case insensitive)
- product_id: The ID of the product (in this test, it's up to 5 because there are 5 products of each type)

Postman screenshot on how a valid POST request to this endpoint would look like:
<br/><br/>
![here](https://imgur.com/J1dfyvJ.png)

#### Checkout (GET) `/checkout/`:

This endpoint will checkout the products in the cart.

As a consequence of requesting this endpoint an e-mail will be sent to the established e-mail address.<br/>

The e-mail address can be changed in line 146 of [views.py](./shoppingcart/views.py)

This is how the e-mail will look like:

![here](https://imgur.com/kOjoB1y.png)
