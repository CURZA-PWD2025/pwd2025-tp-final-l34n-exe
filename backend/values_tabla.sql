INSERT INTO proveedores (nombre, telefono, email) VALUES
('Jauja', '299-1234567', 'contacto@jauja.com'),
('Grido', '299-9876543', 'ventas@grido.com'),
('Montevideana', '299-5551111', 'info@montevideana.com');

INSERT INTO sabores (nombre, stock) VALUES
('Chocolate', 20.5),
('Frutilla', 15.0),
('Dulce de leche', 18.7),
('Vainilla', 12.3),
('Menta granizada', 10.0);

INSERT INTO productos (nombre, categoria, precio, stock, id_proveedor) VALUES
('Helado 1/4kg', 'Pote 1/4kg', 1500.00, 50, 1),
('Helado 1kg', 'Pote 1kg', 4800.00, 30, 2),
('Cucurucho doble', 'Cucurucho doble', 2200.00, 40, 3),
('Torta helada', 'Torta familiar', 7500.00, 10, 1);

INSERT INTO clientes (nombre, telefono, direccion) VALUES
('Juan Pérez', '299-4441111', 'Av. Argentina 123'),
('María López', '299-5552222', 'San Martín 456'),
('Carlos Díaz', '299-6663333', 'Belgrano 789');

INSERT INTO ventas (fecha, total, id_cliente) VALUES
('2025-10-06 18:00:00', 3700.00, 1),
('2025-10-06 19:00:00', 4800.00, 2),
('2025-10-06 20:00:00', 9700.00, 3);

INSERT INTO items_ventas (id_venta, id_producto, cantidad) VALUES
(1, 1, 1), -- Juan compra un pote de 1/4kg
(1, 3, 1), -- Juan también compra un cucurucho doble
(2, 2, 1), -- María compra un pote de 1kg
(3, 4, 1), -- Carlos compra una torta helada
(3, 3, 2); -- Carlos también compra dos cucuruchos dobles


INSERT INTO items_venta_sabores (id_item, id_sabor) VALUES
(1, 1), (1, 3),          -- Helado 1/4kg de Chocolate y Dulce de leche
(2, 2), (2, 5),          -- Cucurucho doble de Frutilla y Menta
(3, 1), (3, 2), (3, 3),  -- Helado 1kg con tres sabores
(4, 3), (4, 4), (4, 5),  -- Torta con Dulce, Vainilla y Menta
(5, 1), (5, 2);          -- Cucuruchos de Chocolate y Frutilla

