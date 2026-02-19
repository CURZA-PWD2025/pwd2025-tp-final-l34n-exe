import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "raise_on_warnings": False,
}

TABLES = {}
SEEDS = {}

TABLES["proveedores"] = (
    "CREATE TABLE IF NOT EXISTS proveedores ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "nombre VARCHAR(100) NOT NULL,"
    "telefono VARCHAR(15),"
    "email VARCHAR(100)"
    ")"
)

TABLES["categoria"] = (
    "CREATE TABLE IF NOT EXISTS categoria ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "nombre VARCHAR(100) NOT NULL,"
    "tipo ENUM('Sabor','Producto') NOT NULL,"
    "descripcion VARCHAR(255)"
    ")"
)

TABLES["productos"] = (
    "CREATE TABLE IF NOT EXISTS productos ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "nombre VARCHAR(100) NOT NULL,"
    "precio DECIMAL(10,2) NOT NULL,"
    "stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),"
    "max_sabores INT NOT NULL DEFAULT 1,"
    "disponible TINYINT NOT NULL DEFAULT 1,"
    "id_proveedor INT NOT NULL,"
    "id_categoria INT NOT NULL,"
    "FOREIGN KEY (id_proveedor) REFERENCES proveedores(id),"
    "FOREIGN KEY (id_categoria) REFERENCES categoria(id)"
    ")"
)

TABLES["sabores"] = (
    "CREATE TABLE IF NOT EXISTS sabores ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "nombre VARCHAR(100) NOT NULL,"
    "stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),"
    "disponible TINYINT NOT NULL DEFAULT 1,"
    "id_categoria INT NOT NULL,"
    "FOREIGN KEY (id_categoria) REFERENCES categoria(id)"
    ")"
)

TABLES["empleados"] = (
    "CREATE TABLE IF NOT EXISTS empleados ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "nombre VARCHAR(100) NOT NULL,"
    "apellido VARCHAR(100) NOT NULL,"
    "telefono VARCHAR(15),"
    "email VARCHAR(100),"
    "puesto ENUM('Cajero','Limpieza','Gerente') NOT NULL"
    ")"
)

TABLES["clientes"] = (
    "CREATE TABLE IF NOT EXISTS clientes ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "nombre VARCHAR(100) NOT NULL,"
    "apellido VARCHAR(100) NOT NULL,"
    "telefono VARCHAR(15) NOT NULL,"
    "email VARCHAR(100),"
    "direccion VARCHAR(255) NOT NULL"
    ")"
)

TABLES["ventas"] = (
    "CREATE TABLE IF NOT EXISTS ventas ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "total DECIMAL(10,2) NOT NULL DEFAULT 0,"
    "estado ENUM('abierta','cerrada') DEFAULT 'abierta',"
    "id_cliente INT NOT NULL,"
    "id_empleado INT NOT NULL,"
    "FOREIGN KEY (id_cliente) REFERENCES clientes(id),"
    "FOREIGN KEY (id_empleado) REFERENCES empleados(id)"
    ")"
)

TABLES["items_ventas"] = (
    "CREATE TABLE IF NOT EXISTS items_ventas ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "id_venta INT NOT NULL,"
    "id_producto INT NOT NULL,"
    "cantidad INT NOT NULL,"
    "subtotal DECIMAL(10,2) NOT NULL DEFAULT 0,"
    "FOREIGN KEY (id_venta) REFERENCES ventas(id) ON DELETE CASCADE,"
    "FOREIGN KEY (id_producto) REFERENCES productos(id)"
    ")"
)

TABLES["items_venta_sabores"] = (
    "CREATE TABLE IF NOT EXISTS items_venta_sabores ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "id_item INT NOT NULL,"
    "id_sabor INT NOT NULL,"
    "UNIQUE KEY ux_item_sabor (id_item, id_sabor),"
    "FOREIGN KEY (id_item) REFERENCES items_ventas(id) ON DELETE CASCADE,"
    "FOREIGN KEY (id_sabor) REFERENCES sabores(id)"
    ")"
)

SEEDS['proveedores'] = (
    "INSERT INTO `proveedores` (nombre, telefono, email) VALUES "
    "('ICE', '2920552210', 'ice@gmail.com'),"
    "('Grido', '2920552211', 'grido@outlook.com'),"
    "('La Montevideana', '2920552212', 'lamontevideana@gmail.com'),"
    "('Freddo', '2920552213', 'freddo@outlook.com'),"
    "('Frigor', '2920444555', 'frigor@gmail.com');"
)

SEEDS['categoria'] = (
    "INSERT INTO `categoria` (nombre, tipo, descripcion) VALUES "
    # CATEGORIAS DE PRODUCTOS
    "('Tortas', 'Producto', 'Tortas heladas de x sabor/es')," #1
    "('Yogures Helados', 'Producto', 'Yogures helados con toppings o sabores')," #2
    "('Cucuruchos', 'Producto', 'Helados servidos en cono')," #3
    "('Potes', 'Producto', 'Envases de 1/4, 1/2 o 1 kg')," #4
    "('Paletas', 'Producto', 'Helados de palito de crema o agua')," #5
    "('Vasos', 'Producto', 'Helado servido en vaso descartable')," #6
    "('Batidos', 'Producto', 'Helados licuados con leche o fruta')," #7
    # CATEGORIAS DE SABORES
    "('Chocolates', 'Sabor', 'Sabores basados en cacao'),"      #8
    "('Vainilla', 'Sabor', 'Sabores basados en vainilla'),"     #9
    "('Frutales', 'Sabor', 'Sabores de frutas naturales o artificiales')," #10
    "('Cremas', 'Sabor', 'Sabores de base láctea cremosa')," #11
    "('Agua', 'Sabor', 'Sabores sin base láctea')," #12
    "('Dulce de Leche', 'Sabor', 'Variantes de dulce de leche tradicional')," #13
    "('Menta', 'Sabor', 'Sabores refrescantes de menta o peperina');" #14
)


SEEDS['productos'] = (
    "INSERT INTO `productos` (nombre, precio, stock, max_sabores, disponible, id_proveedor, id_categoria) VALUES "
    # Potes
    "('Pote 1/4 kg', 9500.00, 100, 2, 1, 1, 4),"
    "('Pote 1/2 kg', 17000.00, 80, 3, 1, 2, 4),"
    "('Pote 1 kg', 27000.00, 60, 4, 1, 3, 4),"
    # Cucuruchos
    "('Cucurucho simple', 800.00, 150, 1, 1, 1, 3),"
    "('Cucurucho doble', 1400.00, 120, 2, 1, 2, 3),"
    # Vasos
    "('Vaso chico', 700.00, 140, 1, 1, 1, 6),"
    "('Vaso grande', 1200.00, 120, 2, 1, 2, 6),"
    # Paletas
    "('Paleta de agua', 1000.00, 90, 2, 1, 5, 5),"
    "('Paleta de crema', 1050.00, 80, 2, 1, 5, 5),"
    "('Paleta rellena', 1200.00, 70, 2, 1, 5, 5),"
    # Tortas
    "('Torta helada vainilla y frutilla', 28000.00, 30, 2, 1, 3, 1),"
    "('Torta helada chocolate y dulce de leche', 29000.00, 25, 2, 1, 3, 1),"
    "('Torta helada americana y chocolate', 31000.00, 20, 3, 1, 3, 1),"
    # Batidos y Yogures
    "('Batido', 9000.00, 40, 1, 1, 1, 7),"
    "('Yogur helado', 7000.00, 50, 2, 1, 4, 2);"
)

SEEDS['sabores'] = (
    "INSERT INTO `sabores` (nombre, stock, disponible, id_categoria) VALUES "
    "('Vainilla', 50, 1, 9),"
    "('Chocolate', 40, 1, 8),"
    "('Chocolate Blanco', 30, 1, 8),"
    "('Chocolate Amargo', 20, 1, 8),"
    "('Dulce de Leche', 60, 1, 13),"
    "('Dulce de Leche Granizado', 30, 1, 13),"
    "('Dulce de Leche con Nuez', 25, 1, 13),"
    "('Menta Granizada', 30, 1, 14),"
    "('Peperina', 20, 1, 14),"
    "('Café', 25, 1, 11),"
    "('Pistacho', 20, 1, 10),"
    "('Granizado', 50, 1, 11),"
    "('Banana Split', 40, 1, 11),"
    "('Crema Americana', 55, 1, 11),"
    "('Crema Rusa', 45, 1, 11),"
    "('Crema del Cielo', 35, 1, 11),"
    "('Frutilla', 45, 1, 10),"
    "('Limón', 35, 1, 10),"
    "('Coco', 35, 1, 10),"
    "('Maracuya', 25, 1, 10),"
    "('Naranja', 30, 1, 10),"
    "('Anana', 20, 1, 10);"
)

SEEDS['empleados'] = (
    "INSERT INTO `empleados` (nombre, apellido, telefono, email, puesto) VALUES "
    "('Luis', 'Rodriguez', '2920547896', 'luisrodriguez@outlook.com', 'Gerente'),"
    "('Ana', 'Martinez', '2920663322', 'anamartinez@gmail.com', 'Cajero'),"
    "('Sofia', 'Fernandez', '2920986321', 'sofiafernandez@gmail.com', 'Cajero'),"
    "('Miguel', 'Lopez', '2920222333', 'miguellopez@yahoo.com', 'Cajero'),"
    "('Diego', 'Gonzalez', '2920111222', 'diegogonzalez@protonmail.com', 'Limpieza');"
)

SEEDS['clientes'] = (
    "INSERT INTO `clientes` (nombre, apellido, telefono, email, direccion) VALUES "
    "('Juan', 'Perez', '2920123456', 'juanperez@gmail.com', 'Calle 123'),"
    "('Maria', 'Gomez', '2920987654', 'mariagomez@gmail.com', 'Avenida Siempre Viva 456'),"
    "('Carlos', 'Lopez', '2920555666', 'carloslopez@gmail.com', 'Boulevard Central 789');"
)

SEEDS['ventas'] = (
    "INSERT INTO `ventas` (fecha, total, estado, id_cliente, id_empleado) VALUES "
    "('2025-10-01 11:00:00', 4600.00, 'cerrada', 1, 1),"  # Juan compra varios helados y lo atiende Ana
    "('2025-10-02 16:30:00', 3400.00, 'cerrada', 2, 3),"  # María compra cucuruchos y batido, la atiende Sofía
    "('2025-10-03 19:45:00', 5600.00, 'cerrada', 3, 2),"  # Carlos compra potes y bebidas, lo atiende Luis
    "('2025-10-04 15:10:00', 2800.00, 'cerrada', 1, 4);"  # Juan compra mas productos, lo atiende Miguel
)


SEEDS["items_ventas"] = (
    "INSERT INTO items_ventas (id_venta, id_producto, cantidad, subtotal) "
    "SELECT 1, 2, 1, p.precio * 1 FROM productos p WHERE p.id = 2 "
    "UNION ALL "
    "SELECT 1, 5, 2, p.precio * 2 FROM productos p WHERE p.id = 5 "
    "UNION ALL "
    "SELECT 2, 6, 1, p.precio * 1 FROM productos p WHERE p.id = 6 "
    "UNION ALL "
    "SELECT 2, 13, 1, p.precio * 1 FROM productos p WHERE p.id = 13 "
    "UNION ALL "
    "SELECT 3, 3, 1, p.precio * 1 FROM productos p WHERE p.id = 3 "
    "UNION ALL "
    "SELECT 3, 15, 2, p.precio * 2 FROM productos p WHERE p.id = 15 "
    "UNION ALL "
    "SELECT 4, 8, 2, p.precio * 2 FROM productos p WHERE p.id = 8 "
    "UNION ALL "
    "SELECT 4, 9, 3, p.precio * 3 FROM productos p WHERE p.id = 9"
)

SEEDS['items_venta_sabores'] = (
    "INSERT INTO `items_venta_sabores` (id_item, id_sabor) VALUES "
    "(1, 1),"   # Pote 1/2 kg - Vainilla
    "(1, 2),"   # Pote 1/2 kg - Chocolate
    "(1, 5),"   # Pote 1/2 kg - Dulce de Leche
    "(2, 2),"   # Cucurucho doble - Chocolate
    "(2, 3),"   # Cucurucho doble - Dulce de Leche
    "(3, 4),"   # Vaso chico - Menta Granizada
    "(4, 11),"  # Yogur helado - Crema Americana
    "(4, 12),"  # Yogur helado - Crema Rusa
    "(5, 1),"   # Pote 1 kg - Vainilla
    "(5, 2),"   # Pote 1 kg - Chocolate
    "(5, 3),"   # Pote 1 kg - Dulce de Leche
    "(5, 5),"   # Pote 1 kg - Frutilla
    "(6, 6),"   # Batido - Limón
    "(6, 9),"   # Batido - Naranja
    "(7, 10),"  # Paleta de agua - Granizado
    "(8, 1),"   # Paleta de crema - Vainilla
    "(8, 2),"   # Paleta de crema - Chocolate
    "(8, 3)"    # Paleta de crema - Dulce de Leche
)

def create_database(cursor):
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
        "DEFAULT CHARACTER SET utf8mb4"
    )

def create_tables(cursor):
    for name, ddl in TABLES.items():
        print(f"Creating table {name}...", end=" ")
        cursor.execute(ddl)
        print("OK")

def seed_tables(cursor):
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

    for table in [
        "items_venta_sabores",
        "items_ventas",
        "ventas",
        "productos",
        "sabores",
        "clientes",
        "empleados",
        "categoria",
        "proveedores",
    ]:
        cursor.execute(f"TRUNCATE TABLE {table}")

    for name, sql in SEEDS.items():
        print(f"Seeding {name}...", end=" ")
        cursor.execute(sql)
        print("OK")

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

try:
    cxn = mysql.connector.connect(**DB_CONFIG)
    cursor = cxn.cursor()
    create_database(cursor)
    cursor.close()
    cxn.close()

    DB_CONFIG["database"] = DB_NAME
    cxn = mysql.connector.connect(**DB_CONFIG)
    cursor = cxn.cursor()

    create_tables(cursor)
    seed_tables(cursor)

    cxn.commit()
    print("\nBase de datos inicializada correctamente.")

except Error as e:
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if cxn:
        cxn.close()
