-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-12-2024 a las 10:07:04
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `paquetesbd`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(5) DEFAULT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `direccion`) VALUES
(54, 'Juan Zegarra', 'Av. Naciones Unidas Nro. 54'),
(55, 'María Flores', 'Calle Los Robles Nro. 456'),
(56, 'Carlos Rojas', 'Av. América Oeste Nro. 789'),
(57, 'Ana Sánchez', 'Calle 21 de Mayo Nro. 123'),
(58, 'Luis Gutiérrez', 'Av. Bolivia Nro. 456'),
(59, 'Sofía Mendoza', 'Calle del Sol Nro. 789'),
(60, 'Pedro Ramírez', 'Av. Colón Nro. 101'),
(61, 'Claudia Rivera', 'Calle Victoria Nro. 202'),
(62, 'Fernando Quiroga', 'Av. Libertador Nro. 303'),
(63, 'Patricia Vargas', 'Calle Sucre Nro. 404'),
(64, 'Jorge Salazar', 'Av. Las Palmas Nro. 505');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estadospaquete`
--

CREATE TABLE `estadospaquete` (
  `id` int(5) DEFAULT NULL,
  `nombre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estadospaquete`
--

INSERT INTO `estadospaquete` (`id`, `nombre`) VALUES
(86, 'Entregado'),
(87, 'En tránsito'),
(88, 'Pendiente de entrega'),
(89, 'Devuelto al remitent'),
(90, 'Extraviado'),
(91, 'En almacén regional'),
(92, 'En despacho'),
(93, 'En clasificación'),
(94, 'En proceso de entreg'),
(95, 'Retenido en aduana'),
(96, 'Preparado para envío');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movimientospaquete`
--

CREATE TABLE `movimientospaquete` (
  `id` int(5) DEFAULT NULL,
  `paquete_id` int(5) DEFAULT NULL,
  `ubicacion_actual` varchar(30) DEFAULT NULL,
  `fecha_movimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `movimientospaquete`
--

INSERT INTO `movimientospaquete` (`id`, `paquete_id`, `ubicacion_actual`, `fecha_movimiento`) VALUES
(22, 97, 'Oficina central', '2024-12-10'),
(22, 97, 'Oficina central', '2024-12-10'),
(23, 98, 'Centro de logística', '2024-12-11'),
(24, 99, 'Almacén regional', '2024-12-12'),
(25, 100, 'Sucursal principal', '2024-12-13'),
(26, 101, 'Punto de entrega', '2024-12-14'),
(27, 102, 'Centro de distribución', '2024-12-15'),
(28, 103, 'Almacén central', '2024-12-16'),
(29, 104, 'Plataforma de despacho', '2024-12-17'),
(30, 105, 'Oficina de recepción', '2024-12-18'),
(31, 106, 'Punto de recolección', '2024-12-19'),
(32, 107, 'Área de clasificación', '2024-12-20');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paquetes`
--

CREATE TABLE `paquetes` (
  `id` int(5) DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL,
  `cliente_id` int(5) DEFAULT NULL,
  `estado_id` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paquetes`
--

INSERT INTO `paquetes` (`id`, `descripcion`, `cliente_id`, `estado_id`) VALUES
(34, 'documento importante', 11, 32),
(34, 'documento importante', 11, 32),
(34, 'documento importante', 11, 32),
(35, 'Electrodomésticos', 12, 33),
(36, 'Ropa deportiva', 13, 34),
(37, 'Juguetes infantiles', 14, 35),
(38, 'Medicamentos', 15, 36),
(39, 'Material de oficina', 16, 37),
(40, 'Equipos electrónicos', 17, 38),
(41, 'Libros', 18, 39),
(42, 'Herramientas', 19, 40),
(43, 'Productos de limpieza', 20, 41),
(44, 'Alimentos no perecederos', 21, 42);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
