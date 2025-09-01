-- -----------------------------------------------------
-- LANsight - Inicialización de Base de Datos
-- Tabla: devices
-- Descripción: Inventario de dispositivos conectados a la LAN
-- Fecha: 2025-08-31
-- -----------------------------------------------------

-- Crear tabla devices
CREATE TABLE IF NOT EXISTS devices (
    id SERIAL PRIMARY KEY,
    ip VARCHAR(50) UNIQUE NOT NULL,
    mac VARCHAR(50) UNIQUE NOT NULL,
    hostname VARCHAR(100),
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    suspicious BOOLEAN DEFAULT FALSE
);

-- Insertar registros de ejemplo
INSERT INTO devices (ip, mac, hostname, suspicious) VALUES
('192.168.1.1', 'AA:BB:CC:DD:EE:01', 'Router', FALSE),
('192.168.1.101', 'AA:BB:CC:DD:EE:02', 'PC-Estudiante', FALSE),
('192.168.1.102', 'AA:BB:CC:DD:EE:03', 'Laptop-Profesor', FALSE),
('192.168.1.150', 'AA:BB:CC:DD:EE:04', 'Impresora', FALSE),
('192.168.1.200', 'AA:BB:CC:DD:EE:05', 'CCTV-Camara', TRUE);
