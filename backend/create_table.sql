CREATE TABLE `productos`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `tipo` VARCHAR(50) NOT NULL,
    `precio` DECIMAL(10,2) NOT NULL,
    `stock` INT NOT NULL,
    `fechaVcto` DATETIME NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `sabores`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `id_categoria` BIGINT UNSIGNED NOT NULL,
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

CREATE TABLE `empleados`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    `apellido` VARCHAR(50) NOT NULL,
    `puesto` VARCHAR(50) NOT NULL,
    `salario` DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `categorias`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`)
);

CREATE TABLE `productos_sabores`(
    `id_producto` BIGINT UNSIGNED NOT NULL,
    `id_sabor` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (`id_producto`, `id_sabor`),
    CONSTRAINT `fk_productos_sabores_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos`(`id`),
    CONSTRAINT `fk_productos_sabores_sabor` FOREIGN KEY (`id_sabor`) REFERENCES `sabores`(`id`)
);

CREATE TABLE `ventas`(
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `total` DECIMAL(10,2) NOT NULL,
    `fecha` DATETIME NOT NULL,
    `id_producto` BIGINT UNSIGNED NOT NULL,
    `id_cliente` BIGINT UNSIGNED NOT NULL,
    `id_empleado` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_ventas_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos`(`id`),
    CONSTRAINT `fk_ventas_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `clientes`(`id`),
    CONSTRAINT `fk_ventas_empleado` FOREIGN KEY (`id_empleado`) REFERENCES `empleados`(`id`)
);