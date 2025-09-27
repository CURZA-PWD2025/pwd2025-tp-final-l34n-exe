CREATE TABLE `categorias`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `productos`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `precio` DECIMAL(10,2) NOT NULL,
    `fechaVcto` DATE NOT NULL,
    `id_categoria` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_productos_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias`(`id`)
);

CREATE TABLE `sabores`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `clientes`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `apellido` VARCHAR(50) NOT NULL,
    `edad` INT NOT NULL,
    `direccion` VARCHAR(80) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `presentaciones`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `id_producto` BIGINT UNSIGNED NOT NULL,
    `id_sabor` BIGINT UNSIGNED NOT NULL,
    `stock` INT NOT NULL,
    PRIMARY KEY (`id`),
    CONSTRAINT `fk_presentaciones_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos`(`id`),
    CONSTRAINT `fk_presentaciones_sabor` FOREIGN KEY (`id_sabor`) REFERENCES `sabores`(`id`)
);

CREATE TABLE `ventas`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `total` DECIMAL(10,2) NOT NULL,
    `fecha` DATETIME NOT NULL,
    `id_cliente` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_ventas_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`)
);

CREATE TABLE `detalle_venta`(
    `id_venta` BIGINT UNSIGNED NOT NULL,
    `id_presentacion` BIGINT UNSIGNED NOT NULL,
    `cantidad` INT NOT NULL CHECK (cantidad > 0),
    `precio_unitario` DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
    PRIMARY KEY(`id_venta`, `id_presentacion`),
    CONSTRAINT `fk_detalle_venta_venta` FOREIGN KEY (`id_venta`) REFERENCES `ventas`(`id`),
    CONSTRAINT `fk_detalle_venta_presentacion` FOREIGN KEY (`id_presentacion`) REFERENCES `presentaciones`(`id`)
);
