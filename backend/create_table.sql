--Proveedores--
CREATE TABLE `proveedores`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `telefono` VARCHAR(50) NOT NULL,
    `email` VARCHAR(60) NOT NULL,
    PRIMARY KEY (`id`)
)

-- Productos (ejemplo: Helado, Paleta helada, Cucurucho, Torta helada)--
CREATE TABLE `productos` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `categoria` VARCHAR(50) NOT NULL, -- Ejemplos: Pote 1/4kg, Pote 1kg, Cucurucho simple, Cucurucho doble.--
    `precio` DECIMAL(10,2) NOT NULL CHECK (precio >= 0),
    `stock` INT NOT NULL CHECK (stock >= 0),
    `id_proveedor` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT fk_producto_proveedor FOREIGN KEY(id_proveedor) REFERENCES proveedores(`id`)
);

-- Sabores (ejemplo: Chocolate, Frutilla, Dulce de leche, etc) --
CREATE TABLE `sabores` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `stock` DECIMAL(10,2) NOT NULL CHECK (stock >= 0.0), -- kg disponibke por sabor --
    PRIMARY KEY (`id`)
);

-- Datos de clientes --
CREATE TABLE `clientes` (
  `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NOT NULL,
  `telefono` VARCHAR(50) NOT NULL,
  `direccion` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`)
);

-- Ventas --
CREATE TABLE `ventas` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `fecha` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `total` DECIMAL(10,2) NOT NULL,
    `id_cliente` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT fk_venta_cliente FOREIGN KEY(id_cliente) REFERENCES clientes(`id`)
);

-- Detalle de cada venta (cada fila es igual x unidades del mismo producto) --
CREATE TABLE `items_ventas` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `id_venta` BIGINT UNSIGNED NOT NULL,
    `id_producto` BIGINT UNSIGNED NOT NULL,
    `cantidad` INT NOT NULL CHECK (cantidad > 0),
    PRIMARY KEY (`id`),
    CONSTRAINT fk_items_venta FOREIGN KEY (`id_venta`) REFERENCES ventas(`id`),
    CONSTRAINT fk_items_producto FOREIGN KEY (`id_producto`) REFERENCES productos(`id`)
);

-- sabores elegidos por cada item (N:M entre items_venta y sabores)
CREATE TABLE `items_venta_sabores` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `id_item` BIGINT UNSIGNED NOT NULL,
    `id_sabor` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT fk_ivs_item FOREIGN KEY (`id_item`) REFERENCES items_ventas(`id`),
    CONSTRAINT fk_ivs_sabor FOREIGN KEY (`id_sabor`) REFERENCES sabores(`id`),
    UNIQUE (id_item, id_sabor)
);


