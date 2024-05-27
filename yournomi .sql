-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-05-2024 a las 02:13:50
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
-- Base de datos: `yournomi`
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
(48, 'Can view nomina', 12, 'view_nomina'),
(49, 'Can add valores_fijos', 13, 'add_valores_fijos'),
(50, 'Can change valores_fijos', 13, 'change_valores_fijos'),
(51, 'Can delete valores_fijos', 13, 'delete_valores_fijos'),
(52, 'Can view valores_fijos', 13, 'view_valores_fijos');

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
  `desc_tipo_descuento` longtext NOT NULL,
  `desc_precio` int(11) NOT NULL,
  `desc_fecha_des` date NOT NULL,
  `desc_cedula_id` int(11) NOT NULL,
  `des_time_retardo` int(11) NOT NULL,
  `total_descuentos` int(11) DEFAULT NULL
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
  `deveng_fecha` date NOT NULL,
  `deveng_cedula_id` int(11) NOT NULL,
  `total_devengados` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `nom_cedula_id` int(11) NOT NULL,
  `total_neto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desprendible_valores_fijos`
--

CREATE TABLE `desprendible_valores_fijos` (
  `valor_id` int(11) NOT NULL,
  `valor_trasporte` int(11) NOT NULL,
  `valor_alimentacion` int(11) NOT NULL,
  `valor_aport_salud` double NOT NULL,
  `valor_aport_pension` double NOT NULL,
  `valor_aport_sena` double NOT NULL,
  `valor_aport_icbf` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `desprendible_valores_fijos`
--

INSERT INTO `desprendible_valores_fijos` (`valor_id`, `valor_trasporte`, `valor_alimentacion`, `valor_aport_salud`, `valor_aport_pension`, `valor_aport_sena`, `valor_aport_icbf`) VALUES
(1, 160000, 60000, 0.04, 0.04, 0.04, 0.04);

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
(13, 'desprendible', 'valores_fijos'),
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
(1, 'contenttypes', '0001_initial', '2024-05-26 23:51:38.864566'),
(2, 'auth', '0001_initial', '2024-05-26 23:51:39.210340'),
(3, 'admin', '0001_initial', '2024-05-26 23:51:39.300881'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-05-26 23:51:39.306107'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-26 23:51:39.319091'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-05-26 23:51:39.374296'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-05-26 23:51:39.410195'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-05-26 23:51:39.426561'),
(9, 'auth', '0004_alter_user_username_opts', '2024-05-26 23:51:39.433164'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-05-26 23:51:39.471974'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-05-26 23:51:39.473306'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-26 23:51:39.482533'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-05-26 23:51:39.495872'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-26 23:51:39.509810'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-05-26 23:51:39.522834'),
(16, 'auth', '0011_update_proxy_permissions', '2024-05-26 23:51:39.531228'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-26 23:51:39.544613'),
(18, 'usuario', '0001_initial', '2024-05-26 23:51:39.655840'),
(19, 'usuario', '0002_remove_usuario_usu_antiguedad_and_more', '2024-05-26 23:51:39.938254'),
(20, 'usuario', '0003_alter_usuario_usu_id_rol', '2024-05-26 23:51:40.173356'),
(21, 'usuario', '0004_alter_usuario_usu_id_rol', '2024-05-26 23:51:40.409017'),
(22, 'usuario', '0005_alter_usuario_usu_estado', '2024-05-26 23:51:40.411624'),
(23, 'usuario', '0006_alter_usuario_usu_telefono', '2024-05-26 23:51:40.418933'),
(24, 'usuario', '0007_usuario_last_login', '2024-05-26 23:51:40.429108'),
(25, 'usuario', '0008_rename_usu_cedula_usuario_cedula_and_more', '2024-05-26 23:51:40.444900'),
(26, 'usuario', '0009_alter_usuario_usu_id_rol', '2024-05-26 23:51:40.824117'),
(27, 'usuario', '0010_alter_usuario_usu_telefono', '2024-05-26 23:51:40.829989'),
(28, 'usuario', '0011_usuario_image', '2024-05-26 23:51:40.846923'),
(29, 'desprendible', '0001_initial', '2024-05-26 23:51:40.849223'),
(30, 'desprendible', '0002_initial', '2024-05-26 23:51:40.852403'),
(31, 'desprendible', '0003_initial', '2024-05-26 23:51:41.027427'),
(32, 'desprendible', '0004_remove_descuento_desc_total_parcial_des', '2024-05-26 23:51:41.038329'),
(33, 'desprendible', '0005_descuento_des_time_retardo', '2024-05-26 23:51:41.057413'),
(34, 'desprendible', '0006_valores_fijos', '2024-05-26 23:51:41.067025'),
(35, 'desprendible', '0007_alter_valores_fijos_valor_aport_icbf_and_more', '2024-05-26 23:51:41.162344'),
(36, 'desprendible', '0008_devengado_total_devengados', '2024-05-26 23:51:41.180326'),
(37, 'desprendible', '0009_descuento_total_descuentos_nomina_total_neto', '2024-05-26 23:51:41.210737'),
(38, 'desprendible', '0010_alter_descuento_total_descuentos_and_more', '2024-05-26 23:51:41.350740'),
(39, 'sessions', '0001_initial', '2024-05-26 23:51:41.384262');

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
('qwgbn5a8mi5a87kkns2te1wo0aq0bl41', '.eJyrVopPLC3JiC8tTi2Kz0xRslIyVNJBFktKTM5OzQNJ5OSnZ-bpQfnFes6pKaU5iU5QaRQ9GYnFGUANSrUANMohUQ:1sBNkZ:_bpjXurNyqBk9_Ng8GUJjI8Iv-BiFU_ovNv1nkiJAnE', '2024-06-09 23:58:03.606795');

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
(1, 123, 'Nicolas Martinez', 'nicolasmartinezf137@gmail.com', 123123, 'pbkdf2_sha256$720000$Y0C5D34eGZxj5ehaV8AheC$Sy7qx2MAnM8aBGMrrchE7Zlb5IGpAzKyo/wyFgAAv4M=', 'calle 123', '2024-05-26 23:51:42.289474', 'activo', 1, 1, '2024-05-26 23:58:03.603746', ''),
(2, 147, 'JHON DOE', 'django@gmail.com', 2147483647, 'pbkdf2_sha256$720000$1StoMS4NH2LqrEF7G3V0He$yntc4Q4AMl/Rh43R3kD+BKX9dtU+jN5EoMSTqhmZ2+M=', 'calle 15', '2024-05-26 23:57:07.190769', 'activo', 3, 2, '2024-05-26 23:57:50.751544', '');

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
-- Indices de la tabla `desprendible_valores_fijos`
--
ALTER TABLE `desprendible_valores_fijos`
  ADD PRIMARY KEY (`valor_id`);

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

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
  MODIFY `desc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `desprendible_devengado`
--
ALTER TABLE `desprendible_devengado`
  MODIFY `deveng_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `desprendible_nomina`
--
ALTER TABLE `desprendible_nomina`
  MODIFY `nom_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `desprendible_valores_fijos`
--
ALTER TABLE `desprendible_valores_fijos`
  MODIFY `valor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

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
  MODIFY `usu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
