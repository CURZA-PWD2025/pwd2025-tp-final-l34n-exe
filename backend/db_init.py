import mysql.connector
from mysql.connector import Error, errorcode
import os
from dotenv import load_dotenv


load_dotenv()
DB_NAME = os.getenv("DB_NAME")

DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'port': os.getenv("DB_PORT"),
    'raise_on_warnings': True,
}

TABLES = {}
SEEDS = {}

# Proveedores de productos #
TABLES['proveedores'] = (
    "CREATE TABLE `proveedores` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `nombre` VARCHAR(100) NOT NULL,"
    "  `telefono` VARCHAR(15),"
    "  `email` VARCHAR(100),"
    "  PRIMARY KEY (`id`)"
    ")"
)

# Categorias para sabores y productos #
TABLES['categoria'] = (
    "CREATE TABLE `categoria` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `nombre` VARCHAR(100) NOT NULL,"
    "  `tipo` ENUM('Sabor', 'Producto') NOT NULL,"
    "  `descripcion` VARCHAR(255) DEFAULT NULL,"
    "  PRIMARY KEY (`id`)"
    ")"
)

# Productos (Helados, Paletas, Tortas, Batidos, Bebidas) #
TABLES['productos'] = (
    "CREATE TABLE `productos` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `nombre` VARCHAR(100) NOT NULL,"
    "  `precio` DECIMAL(10,2) NOT NULL,"
    "  `stock` INT NOT NULL CHECK (stock >= 0),"
    "  `max_sabores` INT NOT NULL DEFAULT 1,"
    "  `id_proveedor` INT NOT NULL,"
    "  `id_categoria` INT NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_proveedor`) REFERENCES `proveedores`(`id`),"
    "  FOREIGN KEY (`id_categoria`) REFERENCES `categoria`(`id`)"
    ")"
)

# Sabores de helado #
TABLES['sabores'] = (
    "CREATE TABLE `sabores` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `nombre` VARCHAR(100) NOT NULL,"
    "  `stock` INT NOT NULL CHECK (stock >= 0),"
    "  `disponible` TINYINT NOT NULL DEFAULT 1,"
    "  `id_categoria` INT NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_categoria`) REFERENCES `categoria`(`id`)"
    ")"
)


# Empleados #
TABLES['empleados'] = (
    "CREATE TABLE `empleados` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `nombre` VARCHAR(100) NOT NULL,"
    "  `apellido` VARCHAR(100) NOT NULL,"
    "  `telefono` VARCHAR(15),"
    "  `email` VARCHAR(100),"
    "  `puesto` ENUM('Cajero', 'Limpieza', 'Gerente') NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")"
)

# Clientes #
TABLES['clientes'] = (
    "CREATE TABLE `clientes` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `nombre` VARCHAR(100) NOT NULL,"
    "  `apellido` VARCHAR(100) NOT NULL,"
    "  `telefono` VARCHAR(15) NOT NULL,"
    "  `direccion` VARCHAR(255) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")"
)

# Ventas realizadas #
TABLES['ventas'] = (
    "CREATE TABLE `ventas` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "  `total` DECIMAL(10,2) NOT NULL,"
    "  `id_cliente` INT NOT NULL,"
    "  `id_empleado` INT NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`), "
    "  FOREIGN KEY (`id_empleado`) REFERENCES `empleados`(`id`) "
    ")"
)

# Items dentro de una venta #
TABLES['items_ventas'] = (
    "CREATE TABLE `items_ventas` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `id_venta` INT NOT NULL,"
    "  `id_producto` INT NOT NULL,"
    "  `cantidad` INT NOT NULL CHECK (cantidad > 0),"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (`id_venta`) REFERENCES `ventas`(`id`) ON DELETE CASCADE,"
    "  FOREIGN KEY (`id_producto`) REFERENCES `productos`(`id`)"
    ")"
)

# Sabores elegidos por cada item (N:M entre items_venta y sabores) #
TABLES['items_venta_sabores'] = (
    "CREATE TABLE `items_venta_sabores` ("
    "  `id` INT NOT NULL AUTO_INCREMENT,"
    "  `id_item` INT NOT NULL,"
    "  `id_sabor` INT NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  UNIQUE KEY `ux_item_sabor` (`id_item`, `id_sabor`),"
    "  FOREIGN KEY (`id_item`) REFERENCES `items_ventas`(`id`) ON DELETE CASCADE,"
    "  FOREIGN KEY (`id_sabor`) REFERENCES `sabores`(`id`)"
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
    "INSERT INTO `productos` (nombre, precio, stock, max_sabores, id_proveedor, id_categoria) VALUES "
    # Helados
    "('Pote 1/4 kg', 1500.00, 100, 2, 1, 4),"
    "('Pote 1/2 kg', 2500.00, 80, 3, 2, 4),"
    "('Pote 1 kg', 4200.00, 60, 4, 3, 4),"
    "('Cucurucho simple', 900.00, 150, 1, 1, 3),"
    "('Cucurucho doble', 1300.00, 120, 2, 2, 3),"
    "('Vaso chico', 850.00, 140, 1, 1, 6),"
    "('Vaso grande', 1200.00, 120, 2, 2, 6),"
    # Paletas
    "('Paleta de agua', 600.00, 90, 2, 5, 5),"
    "('Paleta de crema', 750.00, 80, 2, 5, 5),"
    "('Paleta rellena', 900.00, 70, 2, 5, 5),"
    # Tortas
    "('Torta helada vainilla y frutilla', 2800.00, 30, 2, 3, 1),"
    "('Torta helada chocolate y dulce de leche', 3000.00, 25, 2, 3, 1),"
    "('Torta helada americana y chocolate', 3200.00, 20, 3, 3, 1),"
    # Bebidas
    "('Batido', 1800.00, 40, 1, 1, 7),"
    "('Yogur helado', 1700.00, 50, 2, 4, 2);"
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
    "INSERT INTO `clientes` (nombre, apellido, telefono, direccion) VALUES "
    "('Juan', 'Perez', '2920123456', 'Calle 123'),"
    "('Maria', 'Gomez', '2920987654', 'Avenida Siempre Viva 456'),"
    "('Carlos', 'Lopez', '2920555666', 'Boulevard Central 789');"
)

SEEDS['ventas'] = (
    "INSERT INTO `ventas` (fecha, total, id_cliente, id_empleado) VALUES "
    "('2025-10-01 11:00:00', 4600.00, 1, 1),"  # Juan compra varios helados y lo atiende Ana
    "('2025-10-02 16:30:00', 3400.00, 2, 3),"  # María compra cucuruchos y batido, la atiende Sofía
    "('2025-10-03 19:45:00', 5600.00, 3, 2),"  # Carlos compra potes y bebidas, lo atiende Luis
    "('2025-10-04 15:10:00', 2800.00, 1, 4);"  # Juan compra mas productos, lo atiende Miguel
)


SEEDS['items_ventas'] = (
    "INSERT INTO `items_ventas` (id_venta, id_producto, cantidad) VALUES "
    "(1, 2, 1),"   # 1 pote 1/2 kg
    "(1, 5, 2),"   # 2 cucuruchos dobles
    "(2, 6, 1),"   # 1 vaso chico
    "(2, 13, 1),"  # 1 batido
    "(3, 3, 1),"   # 1 pote 1 kg
    "(3, 15, 2),"  # 2 yogures
    "(4, 8, 2);"   # 2 paletas de agua
)


SEEDS['items_venta_sabores'] = (
    "INSERT INTO `items_venta_sabores` (id_item, id_sabor) VALUES "
    "(1, 1),"   # Vainilla
    "(1, 2),"   # Chocolate
    "(2, 3),"   # Dulce de Leche
    "(2, 10),"  # Granizado
    "(3, 4),"   # Menta Granizada
    "(4, 5),"   # Frutilla
    "(5, 2),"   # Chocolate
    "(5, 3),"   # Dulce de Leche
    "(5, 1),"   # Vainilla
    "(6, 5),"   # Frutilla
    "(6, 9),"   # Naranja
    "(7, 6),"   # Limón
    "(7, 9);"   # Naranja
)

def create_database(cursor):
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` DEFAULT CHARACTER SET 'utf8'")
        print(f"Database {DB_NAME} created successfully.")
    except Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print(f"Database {DB_NAME} already exists.")
        else:
            print(err)

def create_tables(tables, cursor):
    for name, ddl in tables.items():
        try:
            print(f"Creating table {name}: ", end="")
            cursor.execute(ddl)
            print("OK")
        except Error as err:
            print(f"Error: {err.msg}")

def seed_tables(seeds, cursor):
    for name, sql in seeds.items():
        try:
            print(f"Seeding table {name}: ", end="")
            cursor.execute(f"DELETE FROM {name}")
            cursor.execute(sql)
            print("OK")
        except Error as err:
            print(f"Error: {err.msg}")


try:
    cxn = mysql.connector.connect(**DB_CONFIG)
    cursor = cxn.cursor()
    create_database(cursor)
    cursor.close()
    cxn.close()

    CONF_DB = DB_CONFIG.copy()
    CONF_DB['database'] = DB_NAME
    cxn = mysql.connector.connect(**CONF_DB)
    cursor = cxn.cursor()

    create_tables(TABLES, cursor)
    seed_tables(SEEDS, cursor)

    cxn.commit()
    print("\nBase de datos inicializada correctamente.")
except Error as e:
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    if cxn:
        cxn.close()



