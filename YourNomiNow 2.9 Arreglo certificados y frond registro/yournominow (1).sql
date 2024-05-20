-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-03-2024 a las 21:17:08
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `yournominow`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add cargo', 7, 'add_cargo'),
(26, 'Can change cargo', 7, 'change_cargo'),
(27, 'Can delete cargo', 7, 'delete_cargo'),
(28, 'Can view cargo', 7, 'view_cargo'),
(29, 'Can add rol', 8, 'add_rol'),
(30, 'Can change rol', 8, 'change_rol'),
(31, 'Can delete rol', 8, 'delete_rol'),
(32, 'Can view rol', 8, 'view_rol'),
(33, 'Can add usuario', 9, 'add_usuario'),
(34, 'Can change usuario', 9, 'change_usuario'),
(35, 'Can delete usuario', 9, 'delete_usuario'),
(36, 'Can view usuario', 9, 'view_usuario'),
(37, 'Can add descuento', 10, 'add_descuento'),
(38, 'Can change descuento', 10, 'change_descuento'),
(39, 'Can delete descuento', 10, 'delete_descuento'),
(40, 'Can view descuento', 10, 'view_descuento'),
(41, 'Can add devengado', 11, 'add_devengado'),
(42, 'Can change devengado', 11, 'change_devengado'),
(43, 'Can delete devengado', 11, 'delete_devengado'),
(44, 'Can view devengado', 11, 'view_devengado'),
(45, 'Can add nomina', 12, 'add_nomina'),
(46, 'Can change nomina', 12, 'change_nomina'),
(47, 'Can delete nomina', 12, 'delete_nomina'),
(48, 'Can view nomina', 12, 'view_nomina');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desprendible_descuento`
--

CREATE TABLE `desprendible_descuento` (
  `desc_id` int(11) NOT NULL,
  `desc_creditos_libranza` int(11) NOT NULL,
  `desc_cuotas_sindicales` int(11) NOT NULL,
  `desc_embargos_judiciales` int(11) NOT NULL,
  `desc_periodo_pago` date NOT NULL,
  `desc_cedula_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desprendible_devengado`
--

CREATE TABLE `desprendible_devengado` (
  `deveng_id` int(11) NOT NULL,
  `deveng_subs_trans` int(11) NOT NULL,
  `deveng_subs_alim` int(11) NOT NULL,
  `deveng_horas_extra_diur` int(11) NOT NULL,
  `deveng_horas_extra_noct` int(11) NOT NULL,
  `deveng_horas_extra_diur_domfest` int(11) NOT NULL,
  `deveng_horas_extra_noct_domfest` int(11) NOT NULL,
  `deveng_bonificacion` int(11) NOT NULL,
  `deveng_periodo_pago` date NOT NULL,
  `deveng_cedula_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `desprendible_devengado`
--

INSERT INTO `desprendible_devengado` (`deveng_id`, `deveng_subs_trans`, `deveng_subs_alim`, `deveng_horas_extra_diur`, `deveng_horas_extra_noct`, `deveng_horas_extra_diur_domfest`, `deveng_horas_extra_noct_domfest`, `deveng_bonificacion`, `deveng_periodo_pago`, `deveng_cedula_id`) VALUES
(6, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-26', 12),
(9, 162000, 84173, 0, 10, 30, 0, 0, '2024-07-30', 12),
(11, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 12),
(12, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 14),
(14, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 12323),
(15, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 23),
(16, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 1023),
(17, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 102332),
(18, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 23213),
(19, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 123123),
(20, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-31', 323),
(21, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 12),
(22, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 14),
(23, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 12323),
(24, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 23),
(25, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 1023),
(26, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 102332),
(27, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 23213),
(28, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 123123),
(29, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-30', 323),
(30, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 12),
(31, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 14),
(32, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 12323),
(33, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 23),
(34, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 1023),
(35, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 102332),
(36, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 23213),
(37, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 123123),
(38, 162000, 84173, 0, 10, 30, 0, 0, '2024-04-16', 323),
(39, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 12),
(40, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 14),
(41, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 12323),
(42, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 23),
(43, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 1023),
(44, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 102332),
(45, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 23213),
(46, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 123123),
(47, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-05', 323),
(48, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 12),
(49, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 14),
(50, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 12323),
(51, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 23),
(52, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 1023),
(53, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 102332),
(54, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 23213),
(55, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 123123),
(56, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-10', 323),
(57, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 12),
(58, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 14),
(59, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 12323),
(60, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 23),
(61, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 1023),
(62, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 102332),
(63, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 23213),
(64, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 123123),
(65, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 323),
(66, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-24', 123233),
(67, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 12),
(68, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 14),
(69, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 12323),
(70, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 23),
(71, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 1023),
(72, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 102332),
(73, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 23213),
(74, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 123123),
(75, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 323),
(76, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-11', 123233),
(77, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 12),
(78, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 14),
(79, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 12323),
(80, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 23),
(81, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 1023),
(82, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 102332),
(83, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 23213),
(84, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 123123),
(85, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 323),
(86, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 123233),
(87, 162000, 84173, 0, 10, 30, 0, 0, '2024-03-14', 123312);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desprendible_nomina`
--

CREATE TABLE `desprendible_nomina` (
  `nom_id` int(11) NOT NULL,
  `nom_fecha_creacion` date NOT NULL,
  `nom_tipo_pago` varchar(200) NOT NULL,
  `nom_periodo_pago` date NOT NULL,
  `nom_dias_trabajados` int(11) NOT NULL,
  `nom_cedula_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `desprendible_nomina`
--

INSERT INTO `desprendible_nomina` (`nom_id`, `nom_fecha_creacion`, `nom_tipo_pago`, `nom_periodo_pago`, `nom_dias_trabajados`, `nom_cedula_id`) VALUES
(11, '2024-03-26', 'Electronico', '2024-03-31', 30, 12),
(12, '2024-03-26', 'Electronico', '2024-03-31', 30, 14),
(14, '2024-03-26', 'Electronico', '2024-03-31', 30, 12323),
(15, '2024-03-26', 'Electronico', '2024-03-31', 30, 23),
(16, '2024-03-26', 'Electronico', '2024-03-31', 30, 1023),
(17, '2024-03-26', 'Electronico', '2024-03-31', 30, 102332),
(18, '2024-03-26', 'Electronico', '2024-03-31', 30, 23213),
(19, '2024-03-26', 'Electronico', '2024-03-31', 30, 123123),
(20, '2024-03-26', 'Electronico', '2024-03-31', 30, 323),
(21, '2024-03-26', 'Electronico', '2024-04-30', 30, 12),
(22, '2024-03-26', 'Electronico', '2024-04-30', 30, 14),
(23, '2024-03-26', 'Electronico', '2024-04-30', 30, 12323),
(24, '2024-03-26', 'Electronico', '2024-04-30', 30, 23),
(25, '2024-03-26', 'Electronico', '2024-04-30', 30, 1023),
(26, '2024-03-26', 'Electronico', '2024-04-30', 30, 102332),
(27, '2024-03-26', 'Electronico', '2024-04-30', 30, 23213),
(28, '2024-03-26', 'Electronico', '2024-04-30', 30, 123123),
(29, '2024-03-26', 'Electronico', '2024-04-30', 30, 323),
(30, '2024-03-26', 'Electronico', '2024-04-16', 30, 12),
(31, '2024-03-26', 'Electronico', '2024-04-16', 30, 14),
(32, '2024-03-26', 'Electronico', '2024-04-16', 30, 12323),
(33, '2024-03-26', 'Electronico', '2024-04-16', 30, 23),
(34, '2024-03-26', 'Electronico', '2024-04-16', 30, 1023),
(35, '2024-03-26', 'Electronico', '2024-04-16', 30, 102332),
(36, '2024-03-26', 'Electronico', '2024-04-16', 30, 23213),
(37, '2024-03-26', 'Electronico', '2024-04-16', 30, 123123),
(38, '2024-03-26', 'Electronico', '2024-04-16', 30, 323),
(39, '2024-03-26', 'Electronico', '2024-03-05', 30, 12),
(40, '2024-03-26', 'Electronico', '2024-03-05', 30, 14),
(41, '2024-03-26', 'Electronico', '2024-03-05', 30, 12323),
(42, '2024-03-26', 'Electronico', '2024-03-05', 30, 23),
(43, '2024-03-26', 'Electronico', '2024-03-05', 30, 1023),
(44, '2024-03-26', 'Electronico', '2024-03-05', 30, 102332),
(45, '2024-03-26', 'Electronico', '2024-03-05', 30, 23213),
(46, '2024-03-26', 'Electronico', '2024-03-05', 30, 123123),
(47, '2024-03-26', 'Electronico', '2024-03-05', 30, 323),
(48, '2024-03-26', 'Electronico', '2024-03-10', 30, 12),
(49, '2024-03-26', 'Electronico', '2024-03-10', 30, 14),
(50, '2024-03-26', 'Electronico', '2024-03-10', 30, 12323),
(51, '2024-03-26', 'Electronico', '2024-03-10', 30, 23),
(52, '2024-03-26', 'Electronico', '2024-03-10', 30, 1023),
(53, '2024-03-26', 'Electronico', '2024-03-10', 30, 102332),
(54, '2024-03-26', 'Electronico', '2024-03-10', 30, 23213),
(55, '2024-03-26', 'Electronico', '2024-03-10', 30, 123123),
(56, '2024-03-26', 'Electronico', '2024-03-10', 30, 323),
(57, '2024-03-27', 'Electronico', '2024-03-24', 30, 12),
(58, '2024-03-27', 'Electronico', '2024-03-24', 30, 14),
(59, '2024-03-27', 'Electronico', '2024-03-24', 30, 12323),
(60, '2024-03-27', 'Electronico', '2024-03-24', 30, 23),
(61, '2024-03-27', 'Electronico', '2024-03-24', 30, 1023),
(62, '2024-03-27', 'Electronico', '2024-03-24', 30, 102332),
(63, '2024-03-27', 'Electronico', '2024-03-24', 30, 23213),
(64, '2024-03-27', 'Electronico', '2024-03-24', 30, 123123),
(65, '2024-03-27', 'Electronico', '2024-03-24', 30, 323),
(66, '2024-03-27', 'Electronico', '2024-03-24', 30, 123233),
(67, '2024-03-27', 'Electronico', '2024-03-11', 30, 12),
(68, '2024-03-27', 'Electronico', '2024-03-11', 30, 14),
(69, '2024-03-27', 'Electronico', '2024-03-11', 30, 12323),
(70, '2024-03-27', 'Electronico', '2024-03-11', 30, 23),
(71, '2024-03-27', 'Electronico', '2024-03-11', 30, 1023),
(72, '2024-03-27', 'Electronico', '2024-03-11', 30, 102332),
(73, '2024-03-27', 'Electronico', '2024-03-11', 30, 23213),
(74, '2024-03-27', 'Electronico', '2024-03-11', 30, 123123),
(75, '2024-03-27', 'Electronico', '2024-03-11', 30, 323),
(76, '2024-03-27', 'Electronico', '2024-03-11', 30, 123233),
(77, '2024-03-27', 'Electronico', '2024-03-14', 30, 12),
(78, '2024-03-27', 'Electronico', '2024-03-14', 30, 14),
(79, '2024-03-27', 'Electronico', '2024-03-14', 30, 12323),
(80, '2024-03-27', 'Electronico', '2024-03-14', 30, 23),
(81, '2024-03-27', 'Electronico', '2024-03-14', 30, 1023),
(82, '2024-03-27', 'Electronico', '2024-03-14', 30, 102332),
(83, '2024-03-27', 'Electronico', '2024-03-14', 30, 23213),
(84, '2024-03-27', 'Electronico', '2024-03-14', 30, 123123),
(85, '2024-03-27', 'Electronico', '2024-03-14', 30, 323),
(86, '2024-03-27', 'Electronico', '2024-03-14', 30, 123233),
(87, '2024-03-27', 'Electronico', '2024-03-14', 30, 123312);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'desprendible', 'descuento'),
(11, 'desprendible', 'devengado'),
(12, 'desprendible', 'nomina'),
(6, 'sessions', 'session'),
(7, 'usuario', 'cargo'),
(8, 'usuario', 'rol'),
(9, 'usuario', 'usuario');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-03-22 00:14:27.398191'),
(2, 'auth', '0001_initial', '2024-03-22 00:14:27.946468'),
(3, 'admin', '0001_initial', '2024-03-22 00:14:28.123666'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-03-22 00:14:28.138672'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-03-22 00:14:28.166164'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-03-22 00:14:28.214587'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-03-22 00:14:28.274036'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-03-22 00:14:28.289493'),
(9, 'auth', '0004_alter_user_username_opts', '2024-03-22 00:14:28.300548'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-03-22 00:14:28.336514'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-03-22 00:14:28.340175'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-03-22 00:14:28.347830'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-03-22 00:14:28.362103'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-03-22 00:14:28.387701'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-03-22 00:14:28.401131'),
(16, 'auth', '0011_update_proxy_permissions', '2024-03-22 00:14:28.410525'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-03-22 00:14:28.424547'),
(18, 'usuario', '0001_initial', '2024-03-22 00:14:28.592017'),
(19, 'usuario', '0002_remove_usuario_usu_antiguedad_and_more', '2024-03-22 00:14:29.687143'),
(20, 'usuario', '0003_alter_usuario_usu_id_rol', '2024-03-22 00:14:30.040141'),
(21, 'usuario', '0004_alter_usuario_usu_id_rol', '2024-03-22 00:14:30.398035'),
(22, 'usuario', '0005_alter_usuario_usu_estado', '2024-03-22 00:14:30.414983'),
(23, 'usuario', '0006_alter_usuario_usu_telefono', '2024-03-22 00:14:30.423246'),
(24, 'usuario', '0007_usuario_last_login', '2024-03-22 00:14:30.437243'),
(25, 'usuario', '0008_rename_usu_cedula_usuario_cedula_and_more', '2024-03-22 00:14:30.456357'),
(26, 'usuario', '0009_alter_usuario_usu_id_rol', '2024-03-22 00:14:30.791647'),
(27, 'usuario', '0010_alter_usuario_usu_telefono', '2024-03-22 00:14:30.798666'),
(28, 'desprendible', '0001_initial', '2024-03-22 00:14:30.802306'),
(29, 'desprendible', '0002_initial', '2024-03-22 00:14:30.805665'),
(30, 'desprendible', '0003_initial', '2024-03-22 00:14:31.108250'),
(31, 'sessions', '0001_initial', '2024-03-22 00:14:31.154369'),
(32, 'usuario', '0011_usuario_image', '2024-03-27 19:30:48.449775');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('h1vxyezyos86jdjakxzsadv6uokfneew', '.eJyrVopPLC3JiC8tTi2Kz0xRslIyVdJBFktKTM5OzQNJ5OSnZ-bpQfnFes6pKaU5iU5QaRQ9GYnFGUANSrUANfohVQ:1rpZgh:5CBOzbPPED5xw3aanYtw90JHs426TBtSOj6AqXRM1kw', '2024-04-10 20:15:55.430593');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_cargo`
--

CREATE TABLE `usuario_cargo` (
  `cargo_id` int(11) NOT NULL,
  `cargo_nombre` varchar(200) NOT NULL,
  `cargo_sueldo_basico` int(11) NOT NULL,
  `cargo_empresa` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_cargo`
--

INSERT INTO `usuario_cargo` (`cargo_id`, `cargo_nombre`, `cargo_sueldo_basico`, `cargo_empresa`) VALUES
(1, 'CEO', 3000000, 'Globant'),
(2, 'Senior', 5000000, 'Globant'),
(3, 'Junior', 4000000, 'Globant'),
(4, 'Gerente', 2000000, 'Globant');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_rol`
--

CREATE TABLE `usuario_rol` (
  `rol_id` int(11) NOT NULL,
  `rol_nombre` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_rol`
--

INSERT INTO `usuario_rol` (`rol_id`, `rol_nombre`) VALUES
(1, 'Administrador'),
(2, 'Empleado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario_usuario`
--

CREATE TABLE `usuario_usuario` (
  `usu_id` int(11) NOT NULL,
  `cedula` int(11) NOT NULL,
  `usu_nombre` varchar(200) NOT NULL,
  `usu_correo` varchar(200) NOT NULL,
  `usu_telefono` int(11) NOT NULL,
  `password` varchar(200) NOT NULL,
  `usu_direccion` varchar(200) NOT NULL,
  `usu_fecha_ingreso` datetime(6) NOT NULL,
  `usu_estado` varchar(200) NOT NULL,
  `usu_id_cargo_id` int(11) NOT NULL,
  `usu_id_rol_id` int(11) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario_usuario`
--

INSERT INTO `usuario_usuario` (`usu_id`, `cedula`, `usu_nombre`, `usu_correo`, `usu_telefono`, `password`, `usu_direccion`, `usu_fecha_ingreso`, `usu_estado`, `usu_id_cargo_id`, `usu_id_rol_id`, `last_login`, `image`) VALUES
(5, 12, 'juan pedro perez', 'juanovalle2022123@gmail.com', 2147483647, 'pbkdf2_sha256$720000$AYWnnq5q7Hg3eGHohRaZN7$T7BQmlkdyzRevehocsXa36uYIhaVVkg1rCjG2itw3Ng=', 'calle 12547', '2024-03-24 19:38:01.117913', 'activo', 1, 1, '2024-03-27 20:15:55.427864', 'images/Screenshot_2024-03-22_150020_2rAoIkA.png'),
(8, 14, '212', 'juan@gmail.com', 12, 'pbkdf2_sha256$720000$xm5a8ax8oJEdrhq8i1TVsh$efqR6p82ZFE61d/XgT/S1I/1q80o+dexmhAoW7krw10=', 'no me acuerdp', '2024-03-26 00:36:39.670945', 'activo', 1, 2, '2024-03-26 14:49:16.203517', NULL),
(16, 12323, 'juan pedro perez', '3424@gmail.com', 2147483647, 'pbkdf2_sha256$720000$GziZXIsc70kanvYFQ5VRCx$TqJvuVBJ7D7WmTAuy8JMPXX34oDPhJTmGYxsosOeWGo=', 'calle 23', '2024-03-26 17:15:19.933802', 'activo', 2, 1, NULL, NULL),
(17, 23, '32212', 'employee1321@gmail.com', 35454, 'pbkdf2_sha256$720000$VUzrWmPHrSUX3hEllnjg4z$PBP3PeB5+62ZdsBUR5s3Wr078gNQ3pVpo8OadfF/+ks=', '12321', '2024-03-26 18:06:09.631198', 'activo', 1, 1, NULL, NULL),
(18, 1023, '21321', 'employee121321@gmail.com', 2131222121, 'pbkdf2_sha256$720000$IduLjaQMXGYGFafNOulzxk$Tb0LpxbdlFD4TtC4b8g9MxeT6dbp65c98bWcTRqDXuA=', '12321', '2024-03-26 18:08:41.348896', 'activo', 1, 1, NULL, NULL),
(20, 102332, '21321', 'emploe121321@gmail.com', 2132121, 'pbkdf2_sha256$720000$wTg7dukxjn6O9zcnX9x1Ch$unBWr3Rv+ZocBYCSOOrftejAGYr0+RaUJL94k50XMgg=', 'fr', '2024-03-26 18:11:01.382452', 'activo', 4, 1, NULL, NULL),
(40, 23213, '2321', '1232323@gmail.com', 3231323, 'pbkdf2_sha256$720000$eMIwpXW8c3tQpXyTGoSvkI$ECGDwxk8wbq9uUG428F3tkyxM5gim2Kf9CaNSHFl+To=', '23213', '2024-03-27 01:44:49.164687', 'activo', 1, 1, NULL, NULL),
(41, 123123, '3213', '3234@gmail.com', 213232121, 'pbkdf2_sha256$720000$mFxAM80m5v3KfvFzLm8oqv$wXp5V39eKjB7bQvvUjhnOnV0f7XHslqNUYnhJ4sTBeU=', '12321', '2024-03-27 01:45:47.696290', 'activo', 1, 1, NULL, NULL),
(44, 323, '3232', '323322232@gmail.com', 2147483647, 'pbkdf2_sha256$720000$CGH0IWvvCmBnFMaCtJwr23$MM97P50GcUmeHWOmoSpKnlGORUiOy2WOIHk9sKiD79M=', '323322', '2024-03-27 01:46:12.936062', 'activo', 1, 1, NULL, NULL),
(69, 123233, '2321', 'dfkmkf@gmail.com', 2147483647, 'pbkdf2_sha256$720000$yfajqmtaMVWzaiCDkmLdYl$SRCySMUJjk2qhb5m7dWNUvSIOPpCiXUgBqYKsd8eK74=', '23213', '2024-03-27 13:32:42.233738', 'activo', 2, 2, NULL, NULL),
(70, 123312, '3232', '3232232@gmail.com', 2147483647, 'pbkdf2_sha256$720000$Ztsxb5vTR2ZE9TO2qQL8vF$R34ekWQ1T8YiOth50ZoF0bUZxIuTsZTIgJ2e+mkys78=', '323322', '2024-03-27 16:48:27.847560', 'activo', 1, 1, NULL, NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `desprendible_descuento`
--
ALTER TABLE `desprendible_descuento`
  ADD PRIMARY KEY (`desc_id`),
  ADD KEY `desprendible_descuen_desc_cedula_id_338b042c_fk_usuario_u` (`desc_cedula_id`);

--
-- Indices de la tabla `desprendible_devengado`
--
ALTER TABLE `desprendible_devengado`
  ADD PRIMARY KEY (`deveng_id`),
  ADD KEY `desprendible_devenga_deveng_cedula_id_b43ba80a_fk_usuario_u` (`deveng_cedula_id`);

--
-- Indices de la tabla `desprendible_nomina`
--
ALTER TABLE `desprendible_nomina`
  ADD PRIMARY KEY (`nom_id`),
  ADD KEY `desprendible_nomina_nom_cedula_id_ec440cf9_fk_usuario_u` (`nom_cedula_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `usuario_cargo`
--
ALTER TABLE `usuario_cargo`
  ADD PRIMARY KEY (`cargo_id`);

--
-- Indices de la tabla `usuario_rol`
--
ALTER TABLE `usuario_rol`
  ADD PRIMARY KEY (`rol_id`);

--
-- Indices de la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  ADD PRIMARY KEY (`usu_id`),
  ADD UNIQUE KEY `usu_cedula` (`cedula`),
  ADD KEY `usuario_usuario_usu_id_cargo_id_66771502_fk_usuario_c` (`usu_id_cargo_id`),
  ADD KEY `usuario_usuario_usu_id_rol_id_633ea710_fk_usuario_rol_rol_id` (`usu_id_rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `desprendible_descuento`
--
ALTER TABLE `desprendible_descuento`
  MODIFY `desc_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `desprendible_devengado`
--
ALTER TABLE `desprendible_devengado`
  MODIFY `deveng_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT de la tabla `desprendible_nomina`
--
ALTER TABLE `desprendible_nomina`
  MODIFY `nom_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `usuario_cargo`
--
ALTER TABLE `usuario_cargo`
  MODIFY `cargo_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuario_rol`
--
ALTER TABLE `usuario_rol`
  MODIFY `rol_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  MODIFY `usu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `desprendible_descuento`
--
ALTER TABLE `desprendible_descuento`
  ADD CONSTRAINT `desprendible_descuen_desc_cedula_id_338b042c_fk_usuario_u` FOREIGN KEY (`desc_cedula_id`) REFERENCES `usuario_usuario` (`cedula`);

--
-- Filtros para la tabla `desprendible_devengado`
--
ALTER TABLE `desprendible_devengado`
  ADD CONSTRAINT `desprendible_devenga_deveng_cedula_id_b43ba80a_fk_usuario_u` FOREIGN KEY (`deveng_cedula_id`) REFERENCES `usuario_usuario` (`cedula`);

--
-- Filtros para la tabla `desprendible_nomina`
--
ALTER TABLE `desprendible_nomina`
  ADD CONSTRAINT `desprendible_nomina_nom_cedula_id_ec440cf9_fk_usuario_u` FOREIGN KEY (`nom_cedula_id`) REFERENCES `usuario_usuario` (`cedula`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `usuario_usuario`
--
ALTER TABLE `usuario_usuario`
  ADD CONSTRAINT `usuario_usuario_usu_id_cargo_id_66771502_fk_usuario_c` FOREIGN KEY (`usu_id_cargo_id`) REFERENCES `usuario_cargo` (`cargo_id`),
  ADD CONSTRAINT `usuario_usuario_usu_id_rol_id_633ea710_fk_usuario_rol_rol_id` FOREIGN KEY (`usu_id_rol_id`) REFERENCES `usuario_rol` (`rol_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
