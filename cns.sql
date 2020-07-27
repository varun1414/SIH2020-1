-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 26, 2020 at 03:58 PM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cns`
--

-- --------------------------------------------------------

--
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
CREATE TABLE IF NOT EXISTS `airport` (
  `a_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `altitude` int(6) DEFAULT NULL,
  `area` float DEFAULT NULL,
  `dgm_id` int(5) DEFAULT NULL,
  `longitude` varchar(10) DEFAULT NULL,
  `latitude` varchar(10) DEFAULT NULL,
  `code` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`a_id`),
  UNIQUE KEY `dm_id` (`dgm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `airport`
--

INSERT INTO `airport` (`a_id`, `name`, `altitude`, `area`, `dgm_id`, `longitude`, `latitude`, `code`) VALUES
(1, 'Vadodara', 129, 149, 2102, '22.3325', '73.2171', 'BDQ'),
(2, 'Dabolim', 132, 121, 2121, '15.3803', '73.8350', 'GOI'),
(3, 'Sahar', 142, 125, 2111, '19.0896', '72.8656', 'BOM'),
(4, 'Delhi', 151, 120, 2131, '28.5562', '77.1000', 'DEL');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=249 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add airport', 1, 'add_airport'),
(2, 'Can change airport', 1, 'change_airport'),
(3, 'Can delete airport', 1, 'delete_airport'),
(4, 'Can view airport', 1, 'view_airport'),
(5, 'Can add cdvordaily', 2, 'add_cdvordaily'),
(6, 'Can change cdvordaily', 2, 'change_cdvordaily'),
(7, 'Can delete cdvordaily', 2, 'delete_cdvordaily'),
(8, 'Can view cdvordaily', 2, 'view_cdvordaily'),
(9, 'Can add cdvormonthly', 3, 'add_cdvormonthly'),
(10, 'Can change cdvormonthly', 3, 'change_cdvormonthly'),
(11, 'Can delete cdvormonthly', 3, 'delete_cdvormonthly'),
(12, 'Can view cdvormonthly', 3, 'view_cdvormonthly'),
(13, 'Can add cdvorweekly', 4, 'add_cdvorweekly'),
(14, 'Can change cdvorweekly', 4, 'change_cdvorweekly'),
(15, 'Can delete cdvorweekly', 4, 'delete_cdvorweekly'),
(16, 'Can view cdvorweekly', 4, 'view_cdvorweekly'),
(17, 'Can add communication', 5, 'add_communication'),
(18, 'Can change communication', 5, 'change_communication'),
(19, 'Can delete communication', 5, 'delete_communication'),
(20, 'Can view communication', 5, 'view_communication'),
(21, 'Can add datisdaily', 6, 'add_datisdaily'),
(22, 'Can change datisdaily', 6, 'change_datisdaily'),
(23, 'Can delete datisdaily', 6, 'delete_datisdaily'),
(24, 'Can view datisdaily', 6, 'view_datisdaily'),
(25, 'Can add datisweekly', 7, 'add_datisweekly'),
(26, 'Can change datisweekly', 7, 'change_datisweekly'),
(27, 'Can delete datisweekly', 7, 'delete_datisweekly'),
(28, 'Can view datisweekly', 7, 'view_datisweekly'),
(29, 'Can add dgm', 8, 'add_dgm'),
(30, 'Can change dgm', 8, 'change_dgm'),
(31, 'Can delete dgm', 8, 'delete_dgm'),
(32, 'Can view dgm', 8, 'view_dgm'),
(33, 'Can add dmedaily', 9, 'add_dmedaily'),
(34, 'Can change dmedaily', 9, 'change_dmedaily'),
(35, 'Can delete dmedaily', 9, 'delete_dmedaily'),
(36, 'Can view dmedaily', 9, 'view_dmedaily'),
(37, 'Can add dmemonthly', 10, 'add_dmemonthly'),
(38, 'Can change dmemonthly', 10, 'change_dmemonthly'),
(39, 'Can delete dmemonthly', 10, 'delete_dmemonthly'),
(40, 'Can view dmemonthly', 10, 'view_dmemonthly'),
(41, 'Can add dmeweekly', 11, 'add_dmeweekly'),
(42, 'Can change dmeweekly', 11, 'change_dmeweekly'),
(43, 'Can delete dmeweekly', 11, 'delete_dmeweekly'),
(44, 'Can view dmeweekly', 11, 'view_dmeweekly'),
(45, 'Can add dscndaily', 12, 'add_dscndaily'),
(46, 'Can change dscndaily', 12, 'change_dscndaily'),
(47, 'Can delete dscndaily', 12, 'delete_dscndaily'),
(48, 'Can view dscndaily', 12, 'view_dscndaily'),
(49, 'Can add dscnmonthly', 13, 'add_dscnmonthly'),
(50, 'Can change dscnmonthly', 13, 'change_dscnmonthly'),
(51, 'Can delete dscnmonthly', 13, 'delete_dscnmonthly'),
(52, 'Can view dscnmonthly', 13, 'view_dscnmonthly'),
(53, 'Can add dscnweekly', 14, 'add_dscnweekly'),
(54, 'Can change dscnweekly', 14, 'change_dscnweekly'),
(55, 'Can delete dscnweekly', 14, 'delete_dscnweekly'),
(56, 'Can view dscnweekly', 14, 'view_dscnweekly'),
(57, 'Can add engineer', 15, 'add_engineer'),
(58, 'Can change engineer', 15, 'change_engineer'),
(59, 'Can delete engineer', 15, 'delete_engineer'),
(60, 'Can view engineer', 15, 'view_engineer'),
(61, 'Can add head', 16, 'add_head'),
(62, 'Can change head', 16, 'change_head'),
(63, 'Can delete head', 16, 'delete_head'),
(64, 'Can view head', 16, 'view_head'),
(65, 'Can add issues', 17, 'add_issues'),
(66, 'Can change issues', 17, 'change_issues'),
(67, 'Can delete issues', 17, 'delete_issues'),
(68, 'Can view issues', 17, 'view_issues'),
(69, 'Can add navigation', 18, 'add_navigation'),
(70, 'Can change navigation', 18, 'change_navigation'),
(71, 'Can delete navigation', 18, 'delete_navigation'),
(72, 'Can view navigation', 18, 'view_navigation'),
(73, 'Can add ndbdaily', 19, 'add_ndbdaily'),
(74, 'Can change ndbdaily', 19, 'change_ndbdaily'),
(75, 'Can delete ndbdaily', 19, 'delete_ndbdaily'),
(76, 'Can view ndbdaily', 19, 'view_ndbdaily'),
(77, 'Can add ndbmonthly', 20, 'add_ndbmonthly'),
(78, 'Can change ndbmonthly', 20, 'change_ndbmonthly'),
(79, 'Can delete ndbmonthly', 20, 'delete_ndbmonthly'),
(80, 'Can view ndbmonthly', 20, 'view_ndbmonthly'),
(81, 'Can add ndbweekly', 21, 'add_ndbweekly'),
(82, 'Can change ndbweekly', 21, 'change_ndbweekly'),
(83, 'Can delete ndbweekly', 21, 'delete_ndbweekly'),
(84, 'Can view ndbweekly', 21, 'view_ndbweekly'),
(85, 'Can add scctvdaily', 22, 'add_scctvdaily'),
(86, 'Can change scctvdaily', 22, 'change_scctvdaily'),
(87, 'Can delete scctvdaily', 22, 'delete_scctvdaily'),
(88, 'Can view scctvdaily', 22, 'view_scctvdaily'),
(89, 'Can add scctvmonthly', 23, 'add_scctvmonthly'),
(90, 'Can change scctvmonthly', 23, 'change_scctvmonthly'),
(91, 'Can delete scctvmonthly', 23, 'delete_scctvmonthly'),
(92, 'Can view scctvmonthly', 23, 'view_scctvmonthly'),
(93, 'Can add scctvweekly', 24, 'add_scctvweekly'),
(94, 'Can change scctvweekly', 24, 'change_scctvweekly'),
(95, 'Can delete scctvweekly', 24, 'delete_scctvweekly'),
(96, 'Can view scctvweekly', 24, 'view_scctvweekly'),
(97, 'Can add supervisor', 25, 'add_supervisor'),
(98, 'Can change supervisor', 25, 'change_supervisor'),
(99, 'Can delete supervisor', 25, 'delete_supervisor'),
(100, 'Can view supervisor', 25, 'view_supervisor'),
(101, 'Can add surveillance', 26, 'add_surveillance'),
(102, 'Can change surveillance', 26, 'change_surveillance'),
(103, 'Can delete surveillance', 26, 'delete_surveillance'),
(104, 'Can view surveillance', 26, 'view_surveillance'),
(105, 'Can add vhfdaily', 27, 'add_vhfdaily'),
(106, 'Can change vhfdaily', 27, 'change_vhfdaily'),
(107, 'Can delete vhfdaily', 27, 'delete_vhfdaily'),
(108, 'Can view vhfdaily', 27, 'view_vhfdaily'),
(109, 'Can add vhfmonthly', 28, 'add_vhfmonthly'),
(110, 'Can change vhfmonthly', 28, 'change_vhfmonthly'),
(111, 'Can delete vhfmonthly', 28, 'delete_vhfmonthly'),
(112, 'Can view vhfmonthly', 28, 'view_vhfmonthly'),
(113, 'Can add vhfyearly', 29, 'add_vhfyearly'),
(114, 'Can change vhfyearly', 29, 'change_vhfyearly'),
(115, 'Can delete vhfyearly', 29, 'delete_vhfyearly'),
(116, 'Can view vhfyearly', 29, 'view_vhfyearly'),
(117, 'Can add log entry', 30, 'add_logentry'),
(118, 'Can change log entry', 30, 'change_logentry'),
(119, 'Can delete log entry', 30, 'delete_logentry'),
(120, 'Can view log entry', 30, 'view_logentry'),
(121, 'Can add permission', 31, 'add_permission'),
(122, 'Can change permission', 31, 'change_permission'),
(123, 'Can delete permission', 31, 'delete_permission'),
(124, 'Can view permission', 31, 'view_permission'),
(125, 'Can add group', 32, 'add_group'),
(126, 'Can change group', 32, 'change_group'),
(127, 'Can delete group', 32, 'delete_group'),
(128, 'Can view group', 32, 'view_group'),
(129, 'Can add user', 33, 'add_user'),
(130, 'Can change user', 33, 'change_user'),
(131, 'Can delete user', 33, 'delete_user'),
(132, 'Can view user', 33, 'view_user'),
(133, 'Can add content type', 34, 'add_contenttype'),
(134, 'Can change content type', 34, 'change_contenttype'),
(135, 'Can delete content type', 34, 'delete_contenttype'),
(136, 'Can view content type', 34, 'view_contenttype'),
(137, 'Can add session', 35, 'add_session'),
(138, 'Can change session', 35, 'change_session'),
(139, 'Can delete session', 35, 'delete_session'),
(140, 'Can view session', 35, 'view_session'),
(141, 'Can add auth group', 36, 'add_authgroup'),
(142, 'Can change auth group', 36, 'change_authgroup'),
(143, 'Can delete auth group', 36, 'delete_authgroup'),
(144, 'Can view auth group', 36, 'view_authgroup'),
(145, 'Can add auth group permissions', 37, 'add_authgrouppermissions'),
(146, 'Can change auth group permissions', 37, 'change_authgrouppermissions'),
(147, 'Can delete auth group permissions', 37, 'delete_authgrouppermissions'),
(148, 'Can view auth group permissions', 37, 'view_authgrouppermissions'),
(149, 'Can add auth permission', 38, 'add_authpermission'),
(150, 'Can change auth permission', 38, 'change_authpermission'),
(151, 'Can delete auth permission', 38, 'delete_authpermission'),
(152, 'Can view auth permission', 38, 'view_authpermission'),
(153, 'Can add auth user', 39, 'add_authuser'),
(154, 'Can change auth user', 39, 'change_authuser'),
(155, 'Can delete auth user', 39, 'delete_authuser'),
(156, 'Can view auth user', 39, 'view_authuser'),
(157, 'Can add auth user groups', 40, 'add_authusergroups'),
(158, 'Can change auth user groups', 40, 'change_authusergroups'),
(159, 'Can delete auth user groups', 40, 'delete_authusergroups'),
(160, 'Can view auth user groups', 40, 'view_authusergroups'),
(161, 'Can add auth user user permissions', 41, 'add_authuseruserpermissions'),
(162, 'Can change auth user user permissions', 41, 'change_authuseruserpermissions'),
(163, 'Can delete auth user user permissions', 41, 'delete_authuseruserpermissions'),
(164, 'Can view auth user user permissions', 41, 'view_authuseruserpermissions'),
(165, 'Can add django admin log', 42, 'add_djangoadminlog'),
(166, 'Can change django admin log', 42, 'change_djangoadminlog'),
(167, 'Can delete django admin log', 42, 'delete_djangoadminlog'),
(168, 'Can view django admin log', 42, 'view_djangoadminlog'),
(169, 'Can add django content type', 43, 'add_djangocontenttype'),
(170, 'Can change django content type', 43, 'change_djangocontenttype'),
(171, 'Can delete django content type', 43, 'delete_djangocontenttype'),
(172, 'Can view django content type', 43, 'view_djangocontenttype'),
(173, 'Can add django migrations', 44, 'add_djangomigrations'),
(174, 'Can change django migrations', 44, 'change_djangomigrations'),
(175, 'Can delete django migrations', 44, 'delete_djangomigrations'),
(176, 'Can view django migrations', 44, 'view_djangomigrations'),
(177, 'Can add django session', 45, 'add_djangosession'),
(178, 'Can change django session', 45, 'change_djangosession'),
(179, 'Can delete django session', 45, 'delete_djangosession'),
(180, 'Can view django session', 45, 'view_djangosession'),
(181, 'Can add datisdlogs', 46, 'add_datisdlogs'),
(182, 'Can change datisdlogs', 46, 'change_datisdlogs'),
(183, 'Can delete datisdlogs', 46, 'delete_datisdlogs'),
(184, 'Can view datisdlogs', 46, 'view_datisdlogs'),
(185, 'Can add datiswlogs', 47, 'add_datiswlogs'),
(186, 'Can change datiswlogs', 47, 'change_datiswlogs'),
(187, 'Can delete datiswlogs', 47, 'delete_datiswlogs'),
(188, 'Can view datiswlogs', 47, 'view_datiswlogs'),
(189, 'Can add dscndlogs', 48, 'add_dscndlogs'),
(190, 'Can change dscndlogs', 48, 'change_dscndlogs'),
(191, 'Can delete dscndlogs', 48, 'delete_dscndlogs'),
(192, 'Can view dscndlogs', 48, 'view_dscndlogs'),
(193, 'Can add vhfdlogs', 49, 'add_vhfdlogs'),
(194, 'Can change vhfdlogs', 49, 'change_vhfdlogs'),
(195, 'Can delete vhfdlogs', 49, 'delete_vhfdlogs'),
(196, 'Can view vhfdlogs', 49, 'view_vhfdlogs'),
(197, 'Can add vhfmlogs', 50, 'add_vhfmlogs'),
(198, 'Can change vhfmlogs', 50, 'change_vhfmlogs'),
(199, 'Can delete vhfmlogs', 50, 'delete_vhfmlogs'),
(200, 'Can view vhfmlogs', 50, 'view_vhfmlogs'),
(201, 'Can add vhfylogs', 51, 'add_vhfylogs'),
(202, 'Can change vhfylogs', 51, 'change_vhfylogs'),
(203, 'Can delete vhfylogs', 51, 'delete_vhfylogs'),
(204, 'Can view vhfylogs', 51, 'view_vhfylogs'),
(205, 'Can add employee', 52, 'add_employee'),
(206, 'Can change employee', 52, 'change_employee'),
(207, 'Can delete employee', 52, 'delete_employee'),
(208, 'Can view employee', 52, 'view_employee'),
(209, 'Can add mcdo', 53, 'add_mcdo'),
(210, 'Can change mcdo', 53, 'change_mcdo'),
(211, 'Can delete mcdo', 53, 'delete_mcdo'),
(212, 'Can view mcdo', 53, 'view_mcdo'),
(213, 'Can add cdvordlogs', 54, 'add_cdvordlogs'),
(214, 'Can change cdvordlogs', 54, 'change_cdvordlogs'),
(215, 'Can delete cdvordlogs', 54, 'delete_cdvordlogs'),
(216, 'Can view cdvordlogs', 54, 'view_cdvordlogs'),
(217, 'Can add cdvorwlogs', 55, 'add_cdvorwlogs'),
(218, 'Can change cdvorwlogs', 55, 'change_cdvorwlogs'),
(219, 'Can delete cdvorwlogs', 55, 'delete_cdvorwlogs'),
(220, 'Can view cdvorwlogs', 55, 'view_cdvorwlogs'),
(221, 'Can add dscnwlogs', 56, 'add_dscnwlogs'),
(222, 'Can change dscnwlogs', 56, 'change_dscnwlogs'),
(223, 'Can delete dscnwlogs', 56, 'delete_dscnwlogs'),
(224, 'Can view dscnwlogs', 56, 'view_dscnwlogs'),
(225, 'Can add dscnmlogs', 57, 'add_dscnmlogs'),
(226, 'Can change dscnmlogs', 57, 'change_dscnmlogs'),
(227, 'Can delete dscnmlogs', 57, 'delete_dscnmlogs'),
(228, 'Can view dscnmlogs', 57, 'view_dscnmlogs'),
(229, 'Can add cdvormlogs', 58, 'add_cdvormlogs'),
(230, 'Can change cdvormlogs', 58, 'change_cdvormlogs'),
(231, 'Can delete cdvormlogs', 58, 'delete_cdvormlogs'),
(232, 'Can view cdvormlogs', 58, 'view_cdvormlogs'),
(233, 'Can add scctvdlogs', 59, 'add_scctvdlogs'),
(234, 'Can change scctvdlogs', 59, 'change_scctvdlogs'),
(235, 'Can delete scctvdlogs', 59, 'delete_scctvdlogs'),
(236, 'Can view scctvdlogs', 59, 'view_scctvdlogs'),
(237, 'Can add scctvmlogs', 60, 'add_scctvmlogs'),
(238, 'Can change scctvmlogs', 60, 'change_scctvmlogs'),
(239, 'Can delete scctvmlogs', 60, 'delete_scctvmlogs'),
(240, 'Can view scctvmlogs', 60, 'view_scctvmlogs'),
(241, 'Can add scctvwlogs', 61, 'add_scctvwlogs'),
(242, 'Can change scctvwlogs', 61, 'change_scctvwlogs'),
(243, 'Can delete scctvwlogs', 61, 'delete_scctvwlogs'),
(244, 'Can view scctvwlogs', 61, 'view_scctvwlogs'),
(245, 'Can add dgm reports', 62, 'add_dgmreports'),
(246, 'Can change dgm reports', 62, 'change_dgmreports'),
(247, 'Can delete dgm reports', 62, 'delete_dgmreports'),
(248, 'Can view dgm reports', 62, 'view_dgmreports');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` int(11) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cdvordaily`
--

DROP TABLE IF EXISTS `cdvordaily`;
CREATE TABLE IF NOT EXISTS `cdvordaily` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time DEFAULT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'PENDING',
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) DEFAULT NULL,
  `Azimuth_angle` int(11) DEFAULT NULL,
  `30Hz_modulation` int(11) DEFAULT NULL,
  `9960Hz_modulation` int(11) DEFAULT NULL,
  `9960Hz_deviation` int(11) DEFAULT NULL,
  `field_intensity` int(11) DEFAULT NULL,
  `ident_modulation` int(11) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `emp_id` (`emp_id`),
  KEY `CDVORDaily_ibfk_1` (`a_id`),
  KEY `cdvordaily_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cdvordaily`
--

INSERT INTO `cdvordaily` (`p_id`, `date`, `time`, `status`, `a_id`, `emp_id`, `f_id`, `Azimuth_angle`, `30Hz_modulation`, `9960Hz_modulation`, `9960Hz_deviation`, `field_intensity`, `ident_modulation`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-04-18', '19:08:07', 'PENDING', 1, 4121, 1, 24, 30, 30, 16, 0, 10, NULL, NULL, NULL, NULL),
(2, '2020-04-23', '17:11:00', 'COMPLETED', 1, 4129, 1, 23, 28, 32, 17, 1, 11, NULL, 'YES', '2020-04-23', '13:04:07'),
(3, '2020-04-26', '13:12:36', 'COMPLETED', 1, 4123, 1, 24, 29, 30, 16, 1, NULL, NULL, 'YES', '2020-04-26', '09:05:00'),
(4, '2020-01-01', '01:38:34', 'PENDING', 1, 4123, 1, 23, 28, 26, 16, 1, NULL, NULL, NULL, NULL, NULL),
(5, '2020-04-28', '16:56:25', 'PENDING', 1, 4123, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(6, '2020-04-29', '17:26:41', 'PENDING', 1, 4123, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(7, '2020-04-30', '17:28:28', 'COMPLETED', 1, 4123, 1, 24, 28, 29, 16, 0, NULL, NULL, 'YES', '2020-04-30', '17:48:06'),
(8, '2020-05-01', '13:49:35', 'COMPLETED WITH ERRORS', 1, 4121, 1, 24, 28, 28, 18, 1, NULL, NULL, 'YES', '2020-05-01', '14:31:32'),
(9, '2020-05-02', '23:41:46', 'COMPLETED', 1, 4121, 1, 24, 28, 28, 15, 0, NULL, NULL, 'YES', '2020-05-02', '23:54:47'),
(10, '2020-05-03', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(11, '2020-05-04', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(12, '2020-05-05', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(13, '2020-05-06', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(14, '2020-05-07', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(15, '2020-05-08', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(16, '2020-05-09', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(17, '2020-05-10', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(18, '2020-05-11', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(19, '2020-05-12', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(20, '2020-05-13', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(21, '2020-05-14', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(22, '2020-05-15', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(23, '2020-05-16', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(24, '2020-05-17', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(25, '2020-05-18', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(26, '2020-05-19', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(27, '2020-05-20', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(28, '2020-05-21', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(29, '2020-05-22', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(30, '2020-05-23', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(31, '2020-05-24', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(32, '2020-05-25', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(33, '2020-05-26', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(34, '2020-05-27', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(35, '2020-05-28', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(36, '2020-05-29', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(37, '2020-05-30', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(38, '2020-05-31', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(39, '2020-06-01', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(40, '2020-06-02', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(41, '2020-06-03', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(42, '2020-06-04', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(43, '2020-06-05', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(44, '2020-06-06', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(45, '2020-06-07', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(46, '2020-06-08', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(47, '2020-06-09', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(48, '2020-06-10', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(49, '2020-06-11', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(50, '2020-06-12', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(51, '2020-06-13', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(52, '2020-06-14', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(53, '2020-06-15', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(54, '2020-06-16', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(55, '2020-06-17', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(56, '2020-06-18', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(57, '2020-06-19', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(58, '2020-06-20', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(59, '2020-06-21', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(60, '2020-06-22', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(61, '2020-06-23', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(62, '2020-06-24', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(63, '2020-06-25', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(64, '2020-06-26', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(65, '2020-06-27', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(66, '2020-06-28', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(67, '2020-06-29', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(68, '2020-06-30', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(69, '2020-07-01', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(70, '2020-07-02', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(71, '2020-07-03', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(72, '2020-07-04', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(73, '2020-07-05', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(74, '2020-07-06', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(75, '2020-07-07', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(76, '2020-07-08', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(77, '2020-07-09', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(78, '2020-07-10', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(79, '2020-07-11', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(80, '2020-07-12', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(81, '2020-07-13', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(82, '2020-07-14', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(83, '2020-07-15', '12:30:47', 'PENDING', 1, 4129, 2, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(84, '2020-07-16', '12:31:01', 'COMPLETED WITH ERRORS', 1, 4129, 1, 12, 234, 123, 123, 132234, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cdvordlogs`
--

DROP TABLE IF EXISTS `cdvordlogs`;
CREATE TABLE IF NOT EXISTS `cdvordlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cdvordlogs`
--

INSERT INTO `cdvordlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(1, 4123, 3, 'All parameters NORMAL', 'Parameters normal at the first submit!', '2020-07-04', '13:12:36'),
(7, 4123, 4, '26', 'Azimuth angle exceeds 25 degrees', '2020-04-27', '01:38:34'),
(8, 4123, 4, '32', '30Hz modulation not in specified range', '2020-04-27', '01:38:34'),
(9, 4123, 4, '28', 'Azimuth angle not normal(update)', '2020-04-27', '01:45:49'),
(10, 4123, 4, '-3', 'field intensity not normal(update)', '2020-04-27', '01:45:49'),
(20, 4123, 7, '27', '9960Hz modulation not in specified range', '2020-04-30', '17:28:28'),
(21, 4123, 7, 'hello', 'All parameters NORMAL', '2020-04-30', '17:28:47'),
(22, 4123, 7, 'bye', 'All parameters NORMAL', '2020-04-30', '17:45:59'),
(23, 4121, 8, '31', '30Hz modulation not in specified range', '2020-05-01', '13:49:35'),
(24, 4121, 8, '26', '9960Hz modulation not in specified range', '2020-05-01', '13:49:35'),
(25, 4121, 8, '18', '9960Hz modulation not in specified range', '2020-05-01', '13:49:35'),
(33, 4121, 8, 'FOLLOWED', 'Procedure Followed', '2020-05-01', '14:30:21'),
(34, 4121, 8, 'hello', 'Final submit with errors', '2020-05-01', '14:30:41'),
(35, 4121, 9, '26', 'Azimuth angle exceeds 25 degrees', '2020-05-02', '23:41:46'),
(38, 4121, 9, '18', '9960Hz modulation not in specified range', '2020-05-02', '23:41:46'),
(39, 4121, 9, '3', 'Field intensity not in specified range', '2020-05-02', '23:41:46'),
(40, 4121, 9, '18', '9960Hz deviation not normal(update)', '2020-05-02', '23:42:29'),
(41, 4121, 9, '3', 'field intensity not normal(update)', '2020-05-02', '23:42:29'),
(42, 4121, 9, 'hello', 'Procedure Followed', '2020-05-02', '23:42:29'),
(43, 4121, 9, '3', 'field intensity not normal(update)', '2020-05-02', '23:42:57'),
(44, 4121, 9, 'edit 2', 'Procedure Followed', '2020-05-02', '23:42:57'),
(45, 4121, 9, 'bye', 'Final submit with errors', '2020-05-02', '23:43:08'),
(46, 4121, 9, 'good', 'All parameters NORMAL', '2020-05-02', '23:47:06'),
(47, 4129, 84, '234', '30Hz modulation not in specified range', '2020-07-16', '12:31:01'),
(48, 4129, 84, '123', '9960Hz modulation not in specified range', '2020-07-16', '12:31:01'),
(49, 4129, 84, '123', '9960Hz modulation not in specified range', '2020-07-16', '12:31:01'),
(50, 4129, 84, '132234', 'Field intensity not in specified range', '2020-07-16', '12:31:01'),
(51, 4129, 84, 'umm\r\n', 'Final submit with errors', '2020-07-16', '12:31:09');

-- --------------------------------------------------------

--
-- Table structure for table `cdvormlogs`
--

DROP TABLE IF EXISTS `cdvormlogs`;
CREATE TABLE IF NOT EXISTS `cdvormlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(40) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cdvormlogs`
--

INSERT INTO `cdvormlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(3, 4123, 2, 'No Entry', 'Report not submitted', '2020-04-26', '12:51:16'),
(4, 4123, 2, 'No Entry', 'Report not submitted', '2020-04-27', '12:51:16'),
(5, 4123, 4, '31', 'Measured bearing 5 is deviating for more than 1', '2020-04-28', '12:52:39'),
(6, 4123, 4, 'bye', 'All parameters NORMAL', '2020-04-28', '12:53:32'),
(7, 4123, 5, '1', 'Measured bearing 1 is deviating for more than 1', '2020-05-01', '14:58:11'),
(8, 4123, 5, '16', 'Measured bearing 3 is deviating for more than 1', '2020-05-01', '14:58:11'),
(9, 4123, 5, '31', 'Measured bearing 5 is deviating for more than 1', '2020-05-01', '14:58:11'),
(10, 4123, 5, '0.8', 'Error spread found is greator than 0.5', '2020-05-01', '14:58:11'),
(11, 4123, 5, '1', 'Measured bearing 1 is deviating for more than 1(update)', '2020-05-01', '14:59:28'),
(12, 4123, 5, '31', 'Measured bearing 5 is deviating for more than 1(update)', '2020-05-01', '14:59:28'),
(13, 4123, 5, '0.6', 'Error spread found is >= 0.5(update)', '2020-05-01', '14:59:28'),
(14, 4123, 5, 'bye', 'Procedure Followed', '2020-05-01', '14:59:28'),
(15, 4123, 5, '31', 'Measured bearing 5 is deviating for more than 1(update)', '2020-05-01', '15:15:21'),
(16, 4123, 5, 'bye', 'Procedure Followed', '2020-05-01', '15:15:21'),
(17, 4123, 5, '5 normal', 'All parameters NORMAL', '2020-05-01', '15:25:43'),
(32, 4121, 7, '24', 'Measured bearing 4 is deviating for more than 1', '2020-05-03', '00:37:37'),
(33, 4121, 7, 'goodbye', 'Final submit with errors', '2020-05-03', '00:37:47'),
(34, 4121, 7, 'good', 'All parameters NORMAL', '2020-05-03', '00:51:32');

-- --------------------------------------------------------

--
-- Table structure for table `cdvormonthly`
--

DROP TABLE IF EXISTS `cdvormonthly`;
CREATE TABLE IF NOT EXISTS `cdvormonthly` (
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(30) NOT NULL,
  `measured_bearing_1` float DEFAULT NULL,
  `bearing_deviation_1` float DEFAULT NULL,
  `measured_bearing_2` float DEFAULT NULL,
  `bearing_deviation_2` float DEFAULT NULL,
  `measured_bearing_3` float DEFAULT NULL,
  `bearing_deviation_3` float DEFAULT NULL,
  `measured_bearing_4` float DEFAULT NULL,
  `bearing_deviation_4` float DEFAULT NULL,
  `measured_bearing_5` float DEFAULT NULL,
  `bearing_deviation_5` float DEFAULT NULL,
  `error_spread` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `emp_id` (`emp_id`),
  KEY `VHFMaily_ibfk_1` (`a_id`),
  KEY `cdvormonthly_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cdvormonthly`
--

INSERT INTO `cdvormonthly` (`date`, `time`, `a_id`, `emp_id`, `f_id`, `p_id`, `status`, `measured_bearing_1`, `bearing_deviation_1`, `measured_bearing_2`, `bearing_deviation_2`, `measured_bearing_3`, `bearing_deviation_3`, `measured_bearing_4`, `bearing_deviation_4`, `measured_bearing_5`, `bearing_deviation_5`, `error_spread`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
('2020-07-01', '11:06:06', 1, 4123, 1, 1, 'COMPLETED', 0, 0, 7.5, 0, 15, 0, 22.5, 0, 37.5, 0, 0, NULL, 'YES', '2020-02-27', '15:03:00'),
('2020-03-27', '00:00:00', 1, 4123, 2, 2, 'COMPLETED', 0, 0, 8, 0.5, 16, 1, 22.5, 0, 37.8, 0.3, 1.8, 'Error spread found of 1.8, which is nominal.', 'YES', '2020-03-27', '16:04:05'),
('2020-04-28', '12:52:39', 1, 4123, 1, 4, 'COMPLETED', 0, 0, 7.5, 0, 15, 0, 23, 0.5, 30, 0, 0.1, NULL, 'YES', '2020-05-01', '13:24:47'),
('2020-05-01', '14:58:11', 1, 4121, 1, 5, 'PENDING', 0, 0, 8, 0.5, 15, 0, 23, 0.5, 30, 0, 0.2, NULL, 'NO', '2020-05-03', '00:35:25'),
('2020-05-03', '00:37:37', 1, 4121, 1, 7, 'COMPLETED', 0, 0, 7.5, 0, 15, 0, 22.5, 0, 30, 0, 0, NULL, 'YES', '2020-05-03', '00:51:52');

-- --------------------------------------------------------

--
-- Table structure for table `cdvorweekly`
--

DROP TABLE IF EXISTS `cdvorweekly`;
CREATE TABLE IF NOT EXISTS `cdvorweekly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `status` varchar(30) NOT NULL,
  `PS_5V` float DEFAULT NULL,
  `PS_12V` float DEFAULT NULL,
  `PS_negative_12V` int(11) DEFAULT NULL,
  `PS_28V` int(11) DEFAULT NULL,
  `PS_48V` int(11) DEFAULT NULL,
  `outside_temp` int(11) DEFAULT NULL,
  `TX1_temp` int(11) DEFAULT NULL,
  `TX2_temp` int(11) DEFAULT NULL,
  `Out_temp_enabled` varchar(10) DEFAULT NULL,
  `AM` int(11) DEFAULT NULL,
  `FM` int(11) DEFAULT NULL,
  `sideband_frequency` int(11) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `cdvorweekly_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cdvorweekly`
--

INSERT INTO `cdvorweekly` (`p_id`, `date`, `time`, `a_id`, `emp_id`, `f_id`, `status`, `PS_5V`, `PS_12V`, `PS_negative_12V`, `PS_28V`, `PS_48V`, `outside_temp`, `TX1_temp`, `TX2_temp`, `Out_temp_enabled`, `AM`, `FM`, `sideband_frequency`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-04-12', '05:07:10', 1, 4129, 1, 'PENDING', 3, 10, -13, 29, 41, 79, 44, 49, 'FALSE', 30, 30, 10001, 'PS 5V,PS 12V,PS -12V, reading deviating too much. Issue no 519', NULL, NULL, NULL),
(2, '2020-04-21', '09:06:10', 1, 4123, 1, 'PENDING', 5, 5, 3, 56, 67, 45, 456, 67, '234', 546, 435, 345, 'xcg cgbxbvc', NULL, NULL, NULL),
(4, '2020-07-02', '11:52:19', 1, 4123, 1, 'COMPLETED', 7, 11.9, NULL, 28, NULL, 27, NULL, NULL, NULL, NULL, NULL, 10001, NULL, 'YES', '2020-04-28', '17:04:06'),
(5, '2020-02-01', '14:38:47', 1, 4121, 1, 'COMPLETED', 5.1, 12.4, NULL, 29, NULL, 34, NULL, NULL, NULL, NULL, NULL, 10001, NULL, 'YES', '2020-05-01', '14:45:50'),
(6, '2020-05-03', '00:13:58', 1, 4121, 1, 'COMPLETED', 5.1, 12.3, NULL, 28, NULL, 55, NULL, NULL, NULL, NULL, NULL, 10001, NULL, 'YES', '2020-05-03', '00:25:42'),
(7, '2020-07-16', '12:31:22', 1, 4129, 1, 'COMPLETED WITH ERRORS', 234, 234, NULL, 1243, NULL, 214, NULL, NULL, NULL, NULL, NULL, 123, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `cdvorwlogs`
--

DROP TABLE IF EXISTS `cdvorwlogs`;
CREATE TABLE IF NOT EXISTS `cdvorwlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cdvorwlogs`
--

INSERT INTO `cdvorwlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(3, 4123, 2, 'No Entry', 'Report not submitted', '2020-04-27', '11:33:59'),
(4, 4123, 4, '7', 'PS 5V not in range', '2020-04-28', '11:52:19'),
(5, 4129, 5, '2', 'PS 5V not in range', '2020-05-01', '14:38:47'),
(6, 4129, 5, '7', 'PS 12V not in range', '2020-05-01', '14:38:47'),
(7, 4129, 5, '31', 'PS 28V not in range', '2020-05-01', '14:38:47'),
(8, 4129, 5, '72', 'Outside temperature not in range', '2020-07-01', '14:38:47'),
(9, 4129, 5, '12', 'sideband frequency not equal to 10001 Hz', '2020-05-01', '14:38:47'),
(10, 4129, 5, '31', 'PS 28V value not in normal range(update)', '2020-05-01', '14:39:25'),
(11, 4129, 5, '72', 'Temperature not in range -25 to 70(update)', '2020-05-01', '14:39:25'),
(12, 4129, 5, '12', 'Sideband frequency not equal to 10001(update)', '2020-05-01', '14:39:25'),
(13, 4129, 5, 'followed', 'Procedure Followed', '2020-05-01', '14:39:25'),
(14, 4129, 5, '31', 'PS 28V value not in normal range(update)', '2020-05-01', '14:39:50'),
(15, 4129, 5, '12', 'Sideband frequency not equal to 10001(update)', '2020-05-01', '14:39:50'),
(16, 4129, 5, 'temp back to normal', 'Procedure Followed', '2020-05-01', '14:39:50'),
(17, 4129, 5, 'freq normal', 'All parameters NORMAL', '2020-05-01', '14:40:15'),
(22, 4121, 6, '5.3', 'PS 5V reading not correct (update)', '2020-05-03', '00:14:22'),
(27, 4121, 6, '72', 'Parameters normal at the first submit!', '2020-05-03', '00:14:38'),
(31, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-09', '12:30:47'),
(32, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-10', '12:30:47'),
(33, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-11', '12:30:47'),
(34, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-12', '12:30:47'),
(35, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-13', '12:30:47'),
(36, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-14', '12:30:47'),
(37, 4129, 6, 'No Entry', 'Report not submitted', '2020-07-15', '12:30:47'),
(38, 4129, 7, '234', 'PS 5V not in range', '2020-07-16', '12:31:22'),
(39, 4129, 7, '234', 'PS 12V not in range', '2020-07-16', '12:31:22'),
(40, 4129, 7, '1243', 'PS 28V not in range', '2020-07-16', '12:31:22'),
(41, 4129, 7, '214', 'Outside temperature not in range', '2020-07-16', '12:31:22'),
(42, 4129, 7, '123', 'sideband frequency not equal to 10001 Hz', '2020-07-16', '12:31:22'),
(43, 4129, 7, 'yes\r\n', 'Final submit with errors', '2020-07-16', '12:31:29');

-- --------------------------------------------------------

--
-- Table structure for table `communication`
--

DROP TABLE IF EXISTS `communication`;
CREATE TABLE IF NOT EXISTS `communication` (
  `f_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `facility` varchar(20) DEFAULT NULL,
  `make` varchar(20) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `DOI` date DEFAULT NULL,
  `DOC` date DEFAULT NULL,
  `location` varchar(20) DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT '3193',
  PRIMARY KEY (`f_id`,`a_id`),
  UNIQUE KEY `f_id` (`f_id`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`supervisor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `communication`
--

INSERT INTO `communication` (`f_id`, `a_id`, `facility`, `make`, `model`, `power`, `DOI`, `DOC`, `location`, `supervisor_id`) VALUES
(1, 1, 'VHF TX/RX', 'PAE', 'T6T', 50, '2009-06-15', '2009-06-20', 'E/ROOM', 3193),
(2, 1, 'DATIS', 'TERMA', '50209', NULL, '2008-11-01', '2009-01-01', 'E/ROOM', 3193),
(3, 1, 'DSCN', 'MEMOTEC', 'CX 800', NULL, '2020-01-07', '2020-02-29', 'COM CENTRE', 3193);

-- --------------------------------------------------------

--
-- Table structure for table `datisdaily`
--

DROP TABLE IF EXISTS `datisdaily`;
CREATE TABLE IF NOT EXISTS `datisdaily` (
  `p_id` int(10) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Status` varchar(40) NOT NULL,
  `f_id` int(11) DEFAULT NULL,
  `room_temp` int(11) DEFAULT NULL,
  `status_of_AC` varchar(10) DEFAULT NULL,
  `status_of_UPS` varchar(10) DEFAULT NULL,
  `status_of_serverA` varchar(10) DEFAULT NULL,
  `status_of_serverB` varchar(10) DEFAULT NULL,
  `datetime_of_servers_wrt_GPS_CLK` varchar(10) DEFAULT NULL,
  `status_of_Disk_array` varchar(10) DEFAULT NULL,
  `VHFTX_ATIS_status` varchar(10) DEFAULT NULL,
  `VHFRX_ATIS_status` varchar(10) DEFAULT NULL,
  `DATIS_update` varchar(10) DEFAULT NULL,
  `Audio_quality` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datisdaily`
--

INSERT INTO `datisdaily` (`p_id`, `date`, `time`, `a_id`, `emp_id`, `Status`, `f_id`, `room_temp`, `status_of_AC`, `status_of_UPS`, `status_of_serverA`, `status_of_serverB`, `datetime_of_servers_wrt_GPS_CLK`, `status_of_Disk_array`, `VHFTX_ATIS_status`, `VHFRX_ATIS_status`, `DATIS_update`, `Audio_quality`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-03-24', '15:14:07', 1, 4169, 'PENDING', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', NULL, NULL),
(2, '2020-03-25', '15:08:08', 1, 4156, 'PENDING', 2, 23, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', NULL, NULL),
(3, '2020-03-26', '14:05:02', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', NULL, NULL),
(4, '2020-03-27', '16:28:16', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'OM LINE', 'OK', 'GOOD', NULL, 'YES', NULL, NULL),
(5, '2020-03-28', '14:01:01', 1, 4144, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', 'CORRECT', 'OK', 'ON LINE', 'ON LINE', 'OK', 'GOOD', NULL, 'YES', NULL, NULL),
(55, '2020-04-17', NULL, NULL, 4156, 'COMPLETED', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', 'YES', '2020-04-18', '18:34:35'),
(58, '2020-04-18', '13:47:38', 1, 4156, 'COMPLETED', 2, -23, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-04-18', '18:33:13'),
(60, '2020-04-19', '23:08:57', 1, 4156, 'COMPLETED', 2, 0, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-04-19', '23:25:51'),
(62, '2020-04-20', '21:38:41', 1, 4156, 'PENDING', 2, 25, 'SVCBL', 'NOT NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'NO', '2020-04-21', '01:32:18'),
(64, '2020-04-21', '22:51:37', 1, 4156, 'COMPLETED WITH ERRORS', 2, 25, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-04-21', '23:34:44'),
(66, '2020-04-22', '17:53:02', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-04-22', '18:03:09'),
(67, '2020-04-23', '20:03:12', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(68, '2020-04-24', '18:43:00', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(69, '2020-04-25', '18:15:03', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(70, '2020-04-26', '01:33:12', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(71, '2020-04-27', '16:39:34', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(72, '2020-04-28', '16:39:34', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(73, '2020-04-29', '14:25:44', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(74, '2020-04-30', '17:34:52', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(75, '2020-05-01', '00:27:17', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(76, '2020-05-02', '16:14:12', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(77, '2020-05-03', '00:56:06', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-05-03', '01:04:15'),
(78, '2020-05-04', '00:38:42', 1, 4156, 'COMPLETED', 2, 24, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(79, '2020-05-05', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(80, '2020-05-06', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(81, '2020-05-07', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(82, '2020-05-08', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(83, '2020-05-09', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(84, '2020-05-10', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(85, '2020-05-11', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(86, '2020-05-12', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(87, '2020-05-13', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(88, '2020-05-14', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(89, '2020-05-15', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(90, '2020-05-16', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(91, '2020-05-17', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(92, '2020-05-18', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(93, '2020-05-19', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(94, '2020-05-20', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(95, '2020-05-21', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(96, '2020-05-22', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(97, '2020-05-23', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(98, '2020-05-24', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(99, '2020-05-25', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(100, '2020-05-26', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(101, '2020-05-27', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(102, '2020-05-28', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(103, '2020-05-29', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(104, '2020-05-30', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(105, '2020-05-31', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(106, '2020-06-01', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(107, '2020-06-02', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(108, '2020-06-03', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(109, '2020-06-04', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(110, '2020-06-05', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(111, '2020-06-06', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(112, '2020-06-07', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(113, '2020-06-08', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(114, '2020-06-09', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(115, '2020-06-10', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(116, '2020-06-11', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(117, '2020-06-12', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(118, '2020-06-13', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(119, '2020-06-14', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(120, '2020-06-15', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(121, '2020-06-16', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(122, '2020-06-17', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(123, '2020-06-18', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(124, '2020-06-19', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(125, '2020-06-20', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(126, '2020-06-21', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(127, '2020-06-22', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(128, '2020-06-23', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(129, '2020-06-24', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(130, '2020-06-25', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(131, '2020-06-26', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(132, '2020-06-27', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(133, '2020-06-28', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(134, '2020-06-29', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(135, '2020-06-30', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(136, '2020-07-01', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(137, '2020-07-02', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(138, '2020-07-03', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(139, '2020-07-04', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(140, '2020-07-05', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(141, '2020-07-06', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(142, '2020-07-07', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(143, '2020-07-08', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(144, '2020-07-09', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(145, '2020-07-10', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(146, '2020-07-11', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(147, '2020-07-12', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(148, '2020-07-13', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(149, '2020-07-14', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(150, '2020-07-15', '12:20:59', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(151, '2020-07-16', '12:21:26', 1, 4156, 'COMPLETED WITH ERRORS', 2, 235, 'SVCBL', 'NORMAL', 'MAINS', 'MAINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(152, '2020-07-17', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(153, '2020-07-18', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(154, '2020-07-19', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(155, '2020-07-20', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(156, '2020-07-21', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(157, '2020-07-22', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(158, '2020-07-23', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(159, '2020-07-24', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(160, '2020-07-25', '15:33:33', 1, 4156, 'PENDING', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(161, '2020-07-26', '15:42:26', 1, 4156, 'PENDING', 2, 25, 'SVCBL', 'NORMAL', 'MAINS', 'STANDBY', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `datisdlogs`
--

DROP TABLE IF EXISTS `datisdlogs`;
CREATE TABLE IF NOT EXISTS `datisdlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `Remarks` varchar(100) NOT NULL,
  `Date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=136 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `datisdlogs`
--

INSERT INTO `datisdlogs` (`log_id`, `emp_id`, `p_id`, `value`, `Remarks`, `Date`, `time`) VALUES
(7, 4156, 3, 'NOT NORMAL', 'Status of ups not NORMAL', '2020-03-26', '11:57:01'),
(8, 4156, 3, 'NOT NORMAL', 'Status of ups not NORMAL(update)', '2020-03-26', '12:26:47'),
(9, 4156, 3, '25', 'Temperature not normal(update)', '2020-03-26', '12:26:57'),
(10, 4156, 3, 'NOT NORMAL', 'Status of ups not NORMAL(update)', '2020-03-26', '12:27:05'),
(11, 4156, 3, 'All parameters NORMAL', 'Parameter/s fixed', '2020-03-26', '12:27:30'),
(90, 4156, 62, 'NOT NORMAL', 'Status of ups not NORMAL', '2020-04-20', '21:38:41'),
(91, 4156, 62, 'MAINS', 'Status of ServerA and serverB is on MAINS', '2020-04-20', '21:38:41'),
(92, 4156, 62, '25', 'Temperature not normal(update)', '2020-04-20', '21:58:42'),
(93, 4156, 62, 'NOT NORMAL', 'Status of ups not NORMAL(update)', '2020-04-20', '21:58:42'),
(94, 4156, 62, 'ok', 'Procedure Followed', '2020-04-20', '21:58:42'),
(95, 4156, 62, 'okk', 'Final submit with errors', '2020-04-20', '21:59:02'),
(102, 4156, 64, '25', 'Temperature exceeds 24 degrees', '2020-04-21', '22:51:37'),
(103, 4156, 64, 'okk', 'All parameters NORMAL', '2020-04-21', '22:52:20'),
(104, 4156, 64, 'okk', 'Final submit with errors', '2020-04-21', '23:24:54'),
(105, 4156, 64, 'kk', 'All parameters NORMAL', '2020-04-21', '23:26:56'),
(106, 4156, 64, 'OK', 'Final submit with errors', '2020-04-21', '23:32:13'),
(107, 4156, 64, 'bye', 'Final submit with errors', '2020-04-21', '23:33:55'),
(118, 4156, 66, 'MAINS', 'Status of ServerA and serverB is on MAINS', '2020-04-22', '17:53:02'),
(119, 4156, 66, 'no', 'Final submit with errors', '2020-04-22', '18:00:06'),
(120, 4156, 66, 'ok', 'All parameters NORMAL', '2020-04-22', '18:02:32'),
(121, 4156, 76, 'All parameters NORMAL', 'Parameters normal at the first submit!', '2020-05-02', '16:14:12'),
(122, 4156, 77, '26', 'Temperature exceeds 24 degrees', '2020-05-03', '00:56:06'),
(123, 4156, 77, 'MAINS', 'Status of ServerA and serverB is on MAINS', '2020-05-03', '00:56:06'),
(124, 4156, 77, 'MAINS', 'Status of ServerA and serverB is on MAINS(update)', '2020-05-03', '00:57:41'),
(125, 4156, 77, 'bye', 'Procedure Followed', '2020-05-03', '00:57:41'),
(126, 4156, 77, 'good', 'Final submit with errors', '2020-05-03', '00:57:48'),
(127, 4156, 77, 'ok', 'All parameters NORMAL', '2020-05-03', '01:03:25'),
(128, 4156, 78, '25', 'Temperature exceeds 24 degrees', '2020-05-04', '00:38:42'),
(129, 4156, 78, 'NON SVCBL', 'Status of ac not correct', '2020-05-04', '00:38:42'),
(130, 4156, 78, 'ok', 'All parameters NORMAL', '2020-05-04', '00:39:04'),
(131, 4156, 151, 'MAINS', 'Status of ServerA and serverB is on MAINS', '2020-07-16', '12:21:26'),
(132, 4156, 151, 'bruh idk\r\n\r\n', 'Final submit with errors', '2020-07-16', '12:21:40'),
(133, 4156, 161, '25', 'Temperature exceeds 24 degrees', '2020-07-26', '15:42:26'),
(134, 4156, 161, 'Done', 'All parameters NORMAL', '2020-07-26', '15:42:36'),
(135, 4156, 161, 'Done', 'All parameters NORMAL', '2020-07-26', '15:44:15');

-- --------------------------------------------------------

--
-- Table structure for table `datisweekly`
--

DROP TABLE IF EXISTS `datisweekly`;
CREATE TABLE IF NOT EXISTS `datisweekly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Status` varchar(40) NOT NULL,
  `serverAorB` varchar(1) DEFAULT NULL,
  `UPS_ip` int(11) DEFAULT NULL,
  `UPS_op` int(11) DEFAULT NULL,
  `Dust_free` varchar(10) DEFAULT NULL,
  `LAN_status` varchar(10) DEFAULT NULL,
  `time_sync` varchar(5) DEFAULT NULL,
  `Audio_quality` varchar(5) DEFAULT NULL,
  `ptt_off_interval_seconds` int(11) DEFAULT NULL,
  `main_to_standby_changeover` varchar(5) DEFAULT NULL,
  `status_of_ROP` varchar(5) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `datisweekly`
--

INSERT INTO `datisweekly` (`p_id`, `date`, `time`, `a_id`, `f_id`, `emp_id`, `Status`, `serverAorB`, `UPS_ip`, `UPS_op`, `Dust_free`, `LAN_status`, `time_sync`, `Audio_quality`, `ptt_off_interval_seconds`, `main_to_standby_changeover`, `status_of_ROP`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-03-11', '11:08:08', 1, 2, 4156, 'PENDING', 'B', 210, 230, 'OK', 'OK', 'OK', 'GOOD', 15, 'OK', 'OK', 'Residual dust was found on the system. Cleaning was performed.', 'YES', NULL, NULL),
(2, '2020-03-18', '10:05:05', 1, 2, 4169, 'COMPLETED', 'A', 230, 230, 'OK', 'OK', 'OK', 'GOOD', 15, 'OK', 'OK', NULL, 'YES', '2020-04-18', '18:34:14'),
(3, '2020-03-25', '15:00:46', 1, 2, 4144, 'COMPLETED', 'A', 200, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'YES', NULL, NULL),
(4, '2020-03-30', '13:13:10', 1, 2, 4144, 'COMPLETED', 'A', 230, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'YES', NULL, NULL),
(10, '2020-04-07', '22:43:40', 1, 2, 4156, 'COMPLETED', 'A', 220, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'YES', NULL, NULL),
(12, '2020-04-08', '17:16:01', 1, 2, 4156, 'PENDING', 'A', 224, 230, 'NOT OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'NO', NULL, NULL),
(20, '2020-04-21', '22:08:19', 1, 2, 4156, 'COMPLETED WITH ERRORS', 'A', 45, 234, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-04-21', '22:17:54'),
(33, '2020-05-01', '17:59:44', 1, 2, 4156, 'COMPLETED WITH ERRORS', 'A', 220, 230, 'NOT OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-05-01', '18:00:12'),
(39, '2020-05-03', '01:07:11', 1, 2, 4144, 'COMPLETED', 'A', 230, 230, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-05-03', '01:10:55'),
(40, '2020-07-16', '12:29:58', 1, 2, 4144, 'COMPLETED WITH ERRORS', 'A', -1, -1, 'OK', 'OK', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `datiswlogs`
--

DROP TABLE IF EXISTS `datiswlogs`;
CREATE TABLE IF NOT EXISTS `datiswlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `Remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=242 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `datiswlogs`
--

INSERT INTO `datiswlogs` (`log_id`, `emp_id`, `p_id`, `Remarks`, `value`, `date`, `time`) VALUES
(1, 4144, 3, 'UPS_ip not in corrent range', '190', '2020-03-25', '15:00:46'),
(2, 4144, 3, 'Not Dustfree', 'NOT OK', '2020-03-25', '15:00:46'),
(3, 4144, 3, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-25', '15:01:04'),
(8, 4144, 4, 'UPS_op value not normal', '220', '2020-04-02', '13:13:10'),
(9, 4144, 4, 'Lan status not OK', 'NOT OK', '2020-04-02', '13:13:10'),
(10, 4144, 4, 'Parameter/s fixed', 'All parameters NORMAL', '2020-04-02', '13:13:18'),
(24, 4156, 10, 'UPS_op value not normal', '220', '2020-04-07', '22:43:40'),
(25, 4156, 10, 'Parameter/s fixed', 'A', '2020-04-07', '22:51:22'),
(29, 4156, 12, 'Not Dustfree', 'NOT OK', '2020-04-08', '17:16:01'),
(30, 4156, 12, 'Not Dustfree(update)', 'A', '2020-04-08', '17:16:13'),
(31, 4156, 12, 'OOPS', 'Final submit with errors', '2020-04-08', '17:16:23'),
(149, 4156, 33, 'Report not submitted', 'No Entry', '2020-04-29', '15:55:22'),
(158, 4156, 33, 'Final submit with errors', 'bye', '2020-05-02', '17:59:44'),
(159, 4144, 39, 'UPS_op value not normal', '190', '2020-05-03', '01:07:11'),
(160, 4144, 39, 'Not Dustfree', 'NOT OK', '2020-05-03', '01:07:11'),
(161, 4144, 39, 'UPS_op value not normal(update)', '220', '2020-05-03', '01:07:28'),
(162, 4144, 39, 'Not Dustfree(update)', 'NOT OK', '2020-05-03', '01:07:28'),
(163, 4144, 39, 'Lan status not OK(update)', 'NOT OK', '2020-05-03', '01:07:28'),
(164, 4144, 39, 'Procedure Followed', 'ok', '2020-05-03', '01:07:28'),
(165, 4144, 39, 'Lan status not OK(update)', 'NOT OK', '2020-05-03', '01:07:46'),
(166, 4144, 39, 'Procedure Followed', 'too good', '2020-05-03', '01:07:46'),
(167, 4144, 39, 'Final submit with errors', 'hello', '2020-05-03', '01:07:52'),
(168, 4144, 39, 'All parameters NORMAL', 'good', '2020-05-03', '01:10:33'),
(169, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-10', '12:20:59'),
(170, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-11', '12:20:59'),
(171, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-12', '12:20:59'),
(172, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-13', '12:20:59'),
(173, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-14', '12:20:59'),
(174, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-15', '12:20:59'),
(175, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-16', '12:20:59'),
(176, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-17', '12:20:59'),
(177, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-18', '12:20:59'),
(178, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-19', '12:20:59'),
(179, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-20', '12:20:59'),
(180, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-21', '12:20:59'),
(181, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-22', '12:20:59'),
(182, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-23', '12:20:59'),
(183, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-24', '12:20:59'),
(184, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-25', '12:20:59'),
(185, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-26', '12:20:59'),
(186, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-27', '12:20:59'),
(187, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-28', '12:20:59'),
(188, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-29', '12:20:59'),
(189, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-30', '12:20:59'),
(190, 4156, 39, 'Report not submitted', 'No Entry', '2020-05-31', '12:20:59'),
(191, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-01', '12:20:59'),
(192, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-02', '12:20:59'),
(193, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-03', '12:20:59'),
(194, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-04', '12:20:59'),
(195, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-05', '12:20:59'),
(196, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-06', '12:20:59'),
(197, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-07', '12:20:59'),
(198, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-08', '12:20:59'),
(199, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-09', '12:20:59'),
(200, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-10', '12:20:59'),
(201, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-11', '12:20:59'),
(202, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-12', '12:20:59'),
(203, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-13', '12:20:59'),
(204, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-14', '12:20:59'),
(205, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-15', '12:20:59'),
(206, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-16', '12:20:59'),
(207, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-17', '12:20:59'),
(208, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-18', '12:20:59'),
(209, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-19', '12:20:59'),
(210, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-20', '12:20:59'),
(211, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-21', '12:20:59'),
(212, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-22', '12:20:59'),
(213, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-23', '12:20:59'),
(214, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-24', '12:20:59'),
(215, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-25', '12:20:59'),
(216, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-26', '12:20:59'),
(217, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-27', '12:20:59'),
(218, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-28', '12:20:59'),
(219, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-29', '12:20:59'),
(220, 4156, 39, 'Report not submitted', 'No Entry', '2020-06-30', '12:20:59'),
(221, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-01', '12:20:59'),
(222, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-02', '12:20:59'),
(223, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-03', '12:20:59'),
(224, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-04', '12:20:59'),
(225, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-05', '12:20:59'),
(226, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-06', '12:20:59'),
(227, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-07', '12:20:59'),
(228, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-08', '12:20:59'),
(229, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-09', '12:20:59'),
(230, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-10', '12:20:59'),
(231, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-11', '12:20:59'),
(232, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-12', '12:20:59'),
(233, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-13', '12:20:59'),
(234, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-14', '12:20:59'),
(235, 4156, 39, 'Report not submitted', 'No Entry', '2020-07-15', '12:20:59'),
(236, 4144, 40, 'UPS_ip not in corrent range', '-1', '2020-07-16', '12:29:58'),
(237, 4144, 40, 'UPS_op value not normal', '-1', '2020-07-16', '12:29:58'),
(238, 4144, 40, 'Final submit with errors', 'um\r\n', '2020-07-16', '12:30:08'),
(239, 4156, 40, 'Report not submitted', 'No Entry', '2020-07-23', '15:33:33'),
(240, 4156, 40, 'Report not submitted', 'No Entry', '2020-07-24', '15:33:33'),
(241, 4156, 40, 'Report not submitted', 'No Entry', '2020-07-25', '15:33:33');

-- --------------------------------------------------------

--
-- Table structure for table `dgm`
--

DROP TABLE IF EXISTS `dgm`;
CREATE TABLE IF NOT EXISTS `dgm` (
  `dgm_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `head_id` int(11) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`dgm_id`),
  KEY `a_id` (`a_id`),
  KEY `head_id` (`head_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dgm`
--

INSERT INTO `dgm` (`dgm_id`, `name`, `designation`, `a_id`, `contact`, `password`, `head_id`, `email`) VALUES
(2102, 'Linus Torvaldas', 'DGM', 1, 904471123, 'pbkdf2_sha256$180000$7LqYYghTlDpY$lXlFwMM4SieeCYZgavDkqEp+I2djxOpf3wqQO8xXC5Q=', 1101, 'yes@gmail.com'),
(2111, 'nisarg', 'DGM', 3, 21423, 'pbkdf2_sha256$180000$09KcfPsyU3Bv$wcFubUhX0ytB2QtXkPMVZLgssg+L/R6zfma1uPcYwow=', 1101, 'asdsad@ymail.com'),
(2121, 'ronaldo', 'DGM', 2, 325234, 'pbkdf2_sha256$180000$UP32hN0mNayv$fa5QGPHN15UN/AdtcfNqA6ALw0vu3m2Uy2IDy7+bv7M=', 1101, 'ok@gmail.com'),
(2131, 'torentino', 'DGM', 4, 4534, 'pbkdf2_sha256$180000$5LSOl4daoaDe$QnS6ZdjAKIdGsI+pRs/aJMLA57+KZ4Kd/PjJ3i2Z/CA=', 1101, 'na@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `dgmreports`
--

DROP TABLE IF EXISTS `dgmreports`;
CREATE TABLE IF NOT EXISTS `dgmreports` (
  `r_id` int(11) NOT NULL AUTO_INCREMENT,
  `r_type` varchar(30) NOT NULL,
  `r_status` varchar(30) NOT NULL,
  `r_count` int(11) NOT NULL,
  PRIMARY KEY (`r_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dgmreports`
--

INSERT INTO `dgmreports` (`r_id`, `r_type`, `r_status`, `r_count`) VALUES
(1, 'datisd', 'PENDING', 83),
(2, 'datisd', 'COMPLETED', 20),
(3, 'datisd', 'COMPLETED WITH ERRORS', 8),
(4, 'dscnd', 'PENDING', 0),
(5, 'dscnd', 'COMPLETED', 0),
(6, 'dscnd', 'COMPLETED WITH ERRORS', 1),
(7, 'cdvord', 'PENDING', 0),
(8, 'cdvord', 'COMPLETED', 0),
(9, 'cdvord', 'COMPLETED WITH ERRORS', 1),
(10, 'scctvd', 'PENDING', 0),
(11, 'scctvd', 'COMPLETED', 0),
(16, 'datisw', 'COMPLETED', 0),
(15, 'datisw', 'PENDING', 0),
(14, 'scctvd', 'COMPLETED WITH ERRORS', 1),
(17, 'datisw', 'COMPLETED WITH ERRORS', 1),
(18, 'cdvorw', 'PENDING', 0),
(19, 'cdvorw', 'COMPLETED', 0),
(20, 'cdvorw', 'COMPLETED WITH ERRORS', 1),
(21, 'scctvw', 'PENDING', 0),
(22, 'scctvw', 'COMPLETED', 0),
(23, 'scctvw', 'COMPLETED WITH ERRORS', 1),
(24, 'cdvorm', 'PENDING', 0),
(25, 'cdvorm', 'COMPLETED', 0),
(26, 'cdvorm', 'COMPLETED WITH ERRORS', 0),
(27, 'scctvm', 'PENDING', 0),
(28, 'scctvm', 'COMPLETED', 0),
(29, 'scctvm', 'COMPLETED WITH ERRORS', 0),
(30, 'dscnm', 'PENDING', 0),
(31, 'dscnm', 'COMPLETED', 0),
(32, 'dscnm', 'COMPLETED WITH ERRORS', 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=63 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'login', 'airport'),
(2, 'login', 'cdvordaily'),
(3, 'login', 'cdvormonthly'),
(4, 'login', 'cdvorweekly'),
(5, 'login', 'communication'),
(6, 'login', 'datisdaily'),
(7, 'login', 'datisweekly'),
(8, 'login', 'dgm'),
(9, 'login', 'dmedaily'),
(10, 'login', 'dmemonthly'),
(11, 'login', 'dmeweekly'),
(12, 'login', 'dscndaily'),
(13, 'login', 'dscnmonthly'),
(14, 'login', 'dscnweekly'),
(15, 'login', 'engineer'),
(16, 'login', 'head'),
(17, 'login', 'issues'),
(18, 'login', 'navigation'),
(19, 'login', 'ndbdaily'),
(20, 'login', 'ndbmonthly'),
(21, 'login', 'ndbweekly'),
(22, 'login', 'scctvdaily'),
(23, 'login', 'scctvmonthly'),
(24, 'login', 'scctvweekly'),
(25, 'login', 'supervisor'),
(26, 'login', 'surveillance'),
(27, 'login', 'vhfdaily'),
(28, 'login', 'vhfmonthly'),
(29, 'login', 'vhfyearly'),
(30, 'admin', 'logentry'),
(31, 'auth', 'permission'),
(32, 'auth', 'group'),
(33, 'auth', 'user'),
(34, 'contenttypes', 'contenttype'),
(35, 'sessions', 'session'),
(36, 'login', 'authgroup'),
(37, 'login', 'authgrouppermissions'),
(38, 'login', 'authpermission'),
(39, 'login', 'authuser'),
(40, 'login', 'authusergroups'),
(41, 'login', 'authuseruserpermissions'),
(42, 'login', 'djangoadminlog'),
(43, 'login', 'djangocontenttype'),
(44, 'login', 'djangomigrations'),
(45, 'login', 'djangosession'),
(46, 'login', 'datisdlogs'),
(47, 'login', 'datiswlogs'),
(48, 'login', 'dscndlogs'),
(49, 'login', 'vhfdlogs'),
(50, 'login', 'vhfmlogs'),
(51, 'login', 'vhfylogs'),
(52, 'login', 'employee'),
(53, 'login', 'mcdo'),
(54, 'login', 'cdvordlogs'),
(55, 'login', 'cdvorwlogs'),
(56, 'login', 'dscnwlogs'),
(57, 'login', 'dscnmlogs'),
(58, 'login', 'cdvormlogs'),
(59, 'login', 'scctvdlogs'),
(60, 'login', 'scctvmlogs'),
(61, 'login', 'scctvwlogs'),
(62, 'login', 'dgmreports');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-03-20 18:42:09.840064'),
(2, 'auth', '0001_initial', '2020-03-20 18:42:10.412917'),
(3, 'admin', '0001_initial', '2020-03-20 18:42:12.079254'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-03-20 18:42:12.386207'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-03-20 18:42:12.408521'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-03-20 18:42:12.577563'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-03-20 18:42:12.703945'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-03-20 18:42:12.785416'),
(9, 'auth', '0004_alter_user_username_opts', '2020-03-20 18:42:12.822220'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-03-20 18:42:12.901993'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-03-20 18:42:12.907018'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-03-20 18:42:12.917989'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-03-20 18:42:13.006949'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-03-20 18:42:13.101602'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-03-20 18:42:13.171220'),
(16, 'auth', '0011_update_proxy_permissions', '2020-03-20 18:42:13.182230'),
(17, 'login', '0001_initial', '2020-03-20 18:42:13.378825'),
(18, 'login', '0002_delete_manors', '2020-03-20 18:42:13.407074'),
(19, 'sessions', '0001_initial', '2020-03-20 18:42:13.839124'),
(20, 'login', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django', '2020-03-20 18:52:30.753958'),
(21, 'login', '0004_datisdlogs_datiswlogs_dscndlogs_employee_mcdo_vhfdlogs_vhfmlogs_vhfylogs', '2020-04-24 14:49:47.418820'),
(22, 'login', '0005_cdvordlogs_cdvorwlogs', '2020-04-24 14:49:47.491848'),
(23, 'login', '0006_dscnwlogs', '2020-04-25 13:28:33.188759'),
(24, 'login', '0007_dscnmlogs', '2020-04-26 06:08:53.455973'),
(25, 'login', '0008_cdvormlogs', '2020-04-26 20:56:17.506680'),
(26, 'login', '0009_scctvdlogs_scctvmlogs_scctvwlogs', '2020-04-28 19:17:22.482070'),
(27, 'login', '0010_dgmreports', '2020-04-30 09:15:37.882617');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('it71ceko34m645tiza9kfdgqof7l6auj', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-05-02 08:31:35.963882'),
('bii06z0wmmubt3005b96nkx0yvbs8gps', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-05-03 18:09:34.053341'),
('k94jx8fbsvr06gqu6i4pkud8s855bbbr', 'Mjc2Nzk0OWZiNzFkZmM4MmI1MzlkMTBjNWUzMDlmZDQzOGQ0MjA1Njp7ImtleSI6Ik5nNFRPVTNOQlJSLS1YLUM3QjVyb0tnNXpwQzg5bHlFNE5sS0NRNVhMbW89IiwiZGVwdCI6Ik4iLCJ0eXBlIjoicyIsInVpZCI6IjMxMTIiLCJwaWQiOiIwIiwibmFtZSI6ImRtZW1vbnRobHkifQ==', '2020-05-01 20:09:07.806931'),
('wtwpg2seq5a1cq62zncine5ntvkcyis9', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-05-06 09:40:34.859926'),
('0xb3e3q04hgnrjy1ummgdija2w95i8xs', 'ZDgxMDRjZDcyYzkwZDkwYzFkNzQxYjg5Mzg1MDY5NDk0Mjg5MDNlZDp7ImtleSI6IkpyTnNESjU2Z0NseEdpVjM5TGpaYkl2dlJ4TVJubDhVak5fNmJOemhPcDA9IiwiZGVwdCI6IkMiLCJ0eXBlIjoicyIsInVpZCI6IjMxOTMiLCJwaWQiOiIzMyIsIm5hbWUiOiJkYXRpc3dlZWtseSJ9', '2020-05-05 18:28:05.119167'),
('g4gslvm74kqtkexn3086jtyr6gu68m9g', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-05-05 19:17:05.743119'),
('281cx89vbwgb14ih73awp6844dv3wf5q', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-05-06 09:48:42.168428'),
('uu2npwzrenssytpylm4yfn3xu5166l50', 'Y2I3ZWY1ZWFhOGY5YmVjY2RjYTdkNzZkYmVlODNiMjkzMjBkNTg2Mjp7InR5cGUiOiJlIiwidWlkIjoiNDEyMyJ9', '2020-05-12 07:21:16.797122'),
('l45d0lz7gxnbhe4b47qi61wx81bjxlhb', 'Y2I3ZWY1ZWFhOGY5YmVjY2RjYTdkNzZkYmVlODNiMjkzMjBkNTg2Mjp7InR5cGUiOiJlIiwidWlkIjoiNDEyMyJ9', '2020-05-08 07:36:07.093745'),
('hdzauvhjgq5w9dessfwg693hfw05n0eq', 'Y2I3ZWY1ZWFhOGY5YmVjY2RjYTdkNzZkYmVlODNiMjkzMjBkNTg2Mjp7InR5cGUiOiJlIiwidWlkIjoiNDEyMyJ9', '2020-05-10 20:59:18.092572'),
('xaf0hf0nqpmlx0v2ry89cpv05f1gaez1', 'MWM1NjA3NWI2ZmM2ZWMzYzhmOGI0MDM1NTdjMGIzNzFhY2FiMDI2YTp7InR5cGUiOiJlIiwidWlkIjoiNDEzMSJ9', '2020-05-12 18:47:44.044217'),
('439r2bscgpyaw276zesl6rosffkmwu7o', 'YmM1MTRlMTRlMmIzMTJkYzM0ZmI0NGE0Mjk0ZDhjYzVjOTM3MThmZjp7InR5cGUiOiJlIiwidWlkIjoiNDE0NCJ9', '2020-05-16 20:02:42.778531'),
('1olcropto0nujcgqkw0grte7m63df0q1', 'ZjZiMjUzODgzMjgwZjRkNDY1YzI2YjkyMTE2NzZmMjExMDExZTE5NDp7InR5cGUiOiJlIiwidWlkIjoiNDE2OSJ9', '2020-05-17 07:26:23.049698'),
('ir5auvf36qeavffshclrrj9ofy5gk7qz', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-05-17 18:46:28.771225'),
('2tffxmeqlo4jqpvrcd5q3w3d3y5rvu5d', 'MzlhZGVmMGJlMWQ0ODE0MDdlNTAyNjA3NTFkZThmZjRkMmNiNjgzNzp7ImtleSI6IkFISm1IYkZOX3k3Tm1IZFdFNG9CM2Y2VzlOQ3U2NnNYd29URjREdmktdjg9IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-05-27 11:51:36.685982'),
('zrhp46xayz3tuvpphkk8u3c3treiw4m2', 'Yjk3ZjlkNWU5YTNiM2U2NDYyYTA0ZjY1YjViODc5ODRhN2IxYTkzYTp7ImtleSI6IlZKVVBGZEhoT1pwMzAxWUxWa1o3d1F5V0k2NHVjT1czYWZaMEdXUGtlcXc9IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-05-28 14:01:45.799160'),
('bdgtzh9q38fymr2aj8ojvdeq5o0hiigl', 'Njc5Y2E0OWNhYjAzOGEzNDI0N2MxNGEyYzY3M2UwYmE0ZDAyOGQyZDp7ImtleSI6IjhZMjRZMWdFOFhjNkk4QkU2OGVmR09TT05jZGhFZFZKY0Z2RVNtRFRuOWs9IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-07-30 13:49:35.732314'),
('qinum45pdk96mgkho0yjo19ix8wwic4n', 'MjdjMzFiMzI0NzgzZTcwYjU2MjdjNDBjY2UxMjcyZTljZGI2ZDkyZjp7ImtleSI6InQ5dW1JUThzLWgzbHJzS1JoNkVrUTZzSmlqWXZjNGxvTTBmQy1qQWx1bE09IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-07-30 16:53:12.246584'),
('4rp2y2z4575bxqq27y4q6nz4h2332p0q', 'YzJiNDQ2NTY1ZjMxMjU5YzY5YzIxMzRmMzQyZmU3NTcwOTBiMzI0ODp7ImtleSI6Im5DR0pPbldDelNYZmhmbUh0cmVyODZlcUI2d3ZWYmFmT0dRVkJPa3FtY1U9IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-07-31 18:26:40.473706'),
('zi2ktxqmhf914ajg3ua7gpwr3vjb10g7', 'ODAyZmRhZmI5ODJiYTFlMzVhOWFiNTVhNjMyNDgyYmZmODg2OTY5NTp7ImtleSI6IlU0M1ZsanRCRTFXNndmZkh2NHBBeF9Kc3lLR21QNDlRelMwUHNhSGxrZE09IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-08-05 19:53:56.234765'),
('jtaea0tkwia0dp20296geka9udetoc9r', 'M2NjMjdhN2JlZmQ5MjU3NDdiY2E4ZTA3ODliMTRiNTVhMGNjZjg3ODp7ImtleSI6IjlRTFdod1ZoSVp1SUc4S0FXUENETE81YldLa2pvR0hyZVI3d1VQeDBxcHc9IiwidHlwZSI6ImQiLCJ1aWQiOiIyMTAyIn0=', '2020-08-06 19:08:00.068553'),
('q7ihrhu9cjltoztbh76s69kir96lnvn8', 'ZjFhNjFkMjEwNGZkMTA4OWIwMTAyZTU3ZjEzYWRhYTIxYWNlMzJjMjp7ImtleSI6InVfMTF1dkVBMmc1MS1JNDRwVXA3S1Z3QnlyNXVIeExKcHRXb3g1ZHVhcm89IiwiZGVwdCI6Ik4iLCJ0eXBlIjoicyIsInVpZCI6IjMxMTIiLCJwaWQiOiI5IiwibmFtZSI6ImNkdm9yZGFpbHkifQ==', '2020-08-09 06:16:11.277897'),
('2kb1zzx6smfvptyeeoxicpjq72gkphas', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-08-09 10:03:35.233576'),
('l6ffggkxkiqw68yxg6jgibt5qsyzmt5z', 'NmE1ZGM2NDBiNTc1MGEwNzJlZTA1MzMwNTU1MTdiMTU0ZTE5NmZjZTp7InR5cGUiOiJlIiwidWlkIjoiNDE1NiJ9', '2020-08-09 13:26:34.131217');

-- --------------------------------------------------------

--
-- Table structure for table `dmedaily`
--

DROP TABLE IF EXISTS `dmedaily`;
CREATE TABLE IF NOT EXISTS `dmedaily` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `eqpt_shelter_cleanliness` varchar(10) DEFAULT NULL,
  `Battery_room_cleanliness` varchar(10) DEFAULT NULL,
  `AC_status` varchar(20) DEFAULT NULL,
  `eqpt_shelter_temperature` float DEFAULT NULL,
  `mains_power_supply` int(11) DEFAULT NULL,
  `stabiliser_output` int(11) DEFAULT NULL,
  `batterybank_voltage` int(11) DEFAULT NULL,
  `status_of_monitor` varchar(10) DEFAULT NULL,
  `unusual_noise` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(30) NOT NULL,
  `s_verify` varchar(11) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  `status` varchar(30) NOT NULL DEFAULT 'PENDING',
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dmedaily`
--

INSERT INTO `dmedaily` (`date`, `a_id`, `emp_id`, `f_id`, `eqpt_shelter_cleanliness`, `Battery_room_cleanliness`, `AC_status`, `eqpt_shelter_temperature`, `mains_power_supply`, `stabiliser_output`, `batterybank_voltage`, `status_of_monitor`, `unusual_noise`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `approval_date`, `approval_time`, `status`) VALUES
('2020-04-12 11:51:12', 1, 4123, '2', 'DUST FREE', 'NOT CLEAN', 'SERVICABLE', 24, 215, 221, 24, 'OK', 'YES', 'Battery room found not clean. Noise was audible from the DME.Issue no. 520', 'NO', 10, NULL, NULL, NULL, 'PENDING'),
('2020-04-12 11:51:27', 1, 4129, '2', 'DUST FREE', 'DUST FREE', 'SERVICABLE', 22, 221, 219, 24, 'OK', 'NO', NULL, 'YES', 11, NULL, NULL, NULL, 'PENDING');

-- --------------------------------------------------------

--
-- Table structure for table `dmemonthly`
--

DROP TABLE IF EXISTS `dmemonthly`;
CREATE TABLE IF NOT EXISTS `dmemonthly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `SGDNF_pulse_width` float DEFAULT NULL,
  `SGDNF_amplitude` float DEFAULT NULL,
  `Squitter_rate_of_inhibit_interrogation` float DEFAULT NULL,
  `max_reply_rate_KHz` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(30) NOT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dmemonthly`
--

INSERT INTO `dmemonthly` (`date`, `a_id`, `emp_id`, `f_id`, `SGDNF_pulse_width`, `SGDNF_amplitude`, `Squitter_rate_of_inhibit_interrogation`, `max_reply_rate_KHz`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`, `approval_date`, `approval_time`) VALUES
('2020-04-12 12:30:49', 1, 4123, '2', 6, 12, 0.94, 2.7, NULL, 'YES', 0, NULL, '', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dmeweekly`
--

DROP TABLE IF EXISTS `dmeweekly`;
CREATE TABLE IF NOT EXISTS `dmeweekly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `test_interrogation_module` int(11) DEFAULT NULL,
  `RX_video_module` int(11) DEFAULT NULL,
  `100W_module` int(11) DEFAULT NULL,
  `Monitor_module` int(11) DEFAULT NULL,
  `AC_regulator_ip` int(11) DEFAULT NULL,
  `AC_regulator_op` int(11) DEFAULT NULL,
  `system_delay` float DEFAULT NULL,
  `pulse_pair_spacing_SEPN` float DEFAULT NULL,
  `reply_efficiency_percent` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(30) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dmeweekly`
--

INSERT INTO `dmeweekly` (`date`, `a_id`, `emp_id`, `f_id`, `test_interrogation_module`, `RX_video_module`, `100W_module`, `Monitor_module`, `AC_regulator_ip`, `AC_regulator_op`, `system_delay`, `pulse_pair_spacing_SEPN`, `reply_efficiency_percent`, `REMARKS`, `Unit_incharge_approval`, `p_id`, `s_verify`, `status`, `approval_date`, `approval_time`) VALUES
('2020-04-12 12:30:06', 1, 4129, '2', 16, 15, 15, 15, 248, 230, 50, 12, 74, NULL, 'YES', 1, NULL, '', NULL, NULL),
('2020-04-12 12:30:20', 1, 4121, '2', 15, 15, 15, 15, 240, 230, 50.8, 12.25, 89, NULL, 'YES', 2, NULL, '', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dscndaily`
--

DROP TABLE IF EXISTS `dscndaily`;
CREATE TABLE IF NOT EXISTS `dscndaily` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `f_id` int(11) NOT NULL DEFAULT '3',
  `emp_id` int(11) DEFAULT NULL,
  `SAT_LED` varchar(30) DEFAULT NULL,
  `ODU_LED` varchar(30) DEFAULT NULL,
  `IO_LED` varchar(30) DEFAULT NULL,
  `Alarm_LED` varchar(30) DEFAULT NULL,
  `Power_LED` varchar(30) DEFAULT NULL,
  `V35_LED` varchar(30) DEFAULT NULL,
  `IP_Voltage` int(11) DEFAULT NULL,
  `OP_voltage` int(11) DEFAULT NULL,
  `Battery_Voltage` int(11) DEFAULT NULL,
  `CorO_function` varchar(20) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `dscndaily_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dscndaily`
--

INSERT INTO `dscndaily` (`p_id`, `status`, `date`, `time`, `a_id`, `f_id`, `emp_id`, `SAT_LED`, `ODU_LED`, `IO_LED`, `Alarm_LED`, `Power_LED`, `V35_LED`, `IP_Voltage`, `OP_voltage`, `Battery_Voltage`, `CorO_function`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '', '2020-03-30', '13:14:06', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 220, 210, 'OK', NULL, 'YES', NULL, NULL),
(2, '', '2020-03-31', '16:05:04', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 190, 'OK', 'Alarm LED found ON.\r\nLess voltage generated at the output side of the UPS. This giving rise to even lesser and insufficient battery voltage of 170V.\r\nIssue no 518. Issue was solved on the same day.', 'YES', NULL, NULL),
(3, '', '2020-04-01', '23:50:12', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 195, 'OK', 'UPS I/P,O/P very low. ', 'YES', NULL, NULL),
(4, '', '2020-04-02', '01:13:31', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 200, 'OK', 'Alarm LED is ON. it was tuned off successfully', 'YES', NULL, NULL),
(5, 'COMPLETED', '2020-04-23', '17:29:54', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 220, 210, 'OK', 'Every parameters are normal', 'YES', '2020-04-23', '16:07:10'),
(8, 'COMPLETED WITH ERRORS', '2020-04-25', '22:18:56', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'ON', 'STEADY ON', 'RX/TX BLINKING', 220, 220, 220, 'OK', NULL, NULL, NULL, NULL),
(9, 'COMPLETED', '2020-04-26', '22:51:57', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 220, 220, 220, 'OK', NULL, NULL, NULL, NULL),
(10, 'PENDING', '2020-04-27', '16:39:34', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(11, 'PENDING', '2020-04-28', '16:39:34', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(12, 'PENDING', '2020-04-29', '14:25:48', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(13, 'COMPLETED', '2020-04-30', '16:59:26', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 220, 220, 220, 'OK', NULL, 'YES', '2020-04-30', '17:25:48'),
(16, 'COMPLETED', '2020-05-01', '17:59:29', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 230, 'OK', NULL, 'YES', '2020-05-01', '18:13:45'),
(20, 'COMPLETED WITH ERRORS', '2020-05-02', '21:26:25', 1, 3, 4156, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'ON', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 230, 'NOT OK', NULL, NULL, NULL, NULL),
(22, 'COMPLETED', '2020-05-03', '12:33:37', 1, 3, 4169, 'STEADY ON', 'STEADY ON', 'STEADY ON', 'OFF', 'STEADY ON', 'RX/TX BLINKING', 230, 230, 230, 'OK', NULL, NULL, NULL, NULL),
(23, 'PENDING', '2020-05-04', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(24, 'PENDING', '2020-05-05', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(25, 'PENDING', '2020-05-06', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(26, 'PENDING', '2020-05-07', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(27, 'PENDING', '2020-05-08', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(28, 'PENDING', '2020-05-09', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(29, 'PENDING', '2020-05-10', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(30, 'PENDING', '2020-05-11', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(31, 'PENDING', '2020-05-12', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(32, 'PENDING', '2020-05-13', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(33, 'PENDING', '2020-05-14', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(34, 'PENDING', '2020-05-15', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(35, 'PENDING', '2020-05-16', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(36, 'PENDING', '2020-05-17', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(37, 'PENDING', '2020-05-18', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(38, 'PENDING', '2020-05-19', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(39, 'PENDING', '2020-05-20', '12:21:05', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(40, 'PENDING', '2020-05-21', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(42, 'PENDING', '2020-05-22', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(43, 'PENDING', '2020-05-23', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(44, 'PENDING', '2020-05-24', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(45, 'PENDING', '2020-05-25', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(46, 'PENDING', '2020-05-26', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(47, 'PENDING', '2020-05-27', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(48, 'PENDING', '2020-05-28', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(49, 'PENDING', '2020-05-29', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(50, 'PENDING', '2020-05-30', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(51, 'PENDING', '2020-05-31', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(52, 'PENDING', '2020-06-01', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(53, 'PENDING', '2020-06-02', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(54, 'PENDING', '2020-06-03', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(55, 'PENDING', '2020-06-04', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(56, 'PENDING', '2020-06-05', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(57, 'PENDING', '2020-06-06', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(58, 'PENDING', '2020-06-07', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(59, 'PENDING', '2020-06-08', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(60, 'PENDING', '2020-06-09', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(61, 'PENDING', '2020-06-10', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(62, 'PENDING', '2020-06-11', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(63, 'PENDING', '2020-06-12', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(64, 'PENDING', '2020-06-13', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(65, 'PENDING', '2020-06-14', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(66, 'PENDING', '2020-06-15', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(67, 'PENDING', '2020-06-16', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(68, 'PENDING', '2020-06-17', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(69, 'PENDING', '2020-06-18', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(70, 'PENDING', '2020-06-19', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(71, 'PENDING', '2020-06-20', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(72, 'PENDING', '2020-06-21', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(73, 'PENDING', '2020-06-22', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(74, 'PENDING', '2020-06-23', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(75, 'PENDING', '2020-06-24', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(76, 'PENDING', '2020-06-25', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(77, 'PENDING', '2020-06-26', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(78, 'PENDING', '2020-06-27', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(79, 'PENDING', '2020-06-28', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(80, 'PENDING', '2020-06-29', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(81, 'PENDING', '2020-06-30', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(82, 'PENDING', '2020-07-01', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(83, 'PENDING', '2020-07-02', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(84, 'PENDING', '2020-07-03', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(85, 'PENDING', '2020-07-04', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(86, 'PENDING', '2020-07-05', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(87, 'PENDING', '2020-07-06', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(88, 'PENDING', '2020-07-07', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(89, 'PENDING', '2020-07-08', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(90, 'PENDING', '2020-07-09', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(91, 'PENDING', '2020-07-10', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(92, 'PENDING', '2020-07-11', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(93, 'PENDING', '2020-07-12', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(94, 'PENDING', '2020-07-13', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(95, 'PENDING', '2020-07-14', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(96, 'PENDING', '2020-07-15', '12:21:06', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(97, 'COMPLETED WITH ERRORS', '2020-07-16', '12:22:02', 1, 3, 4156, 'NOT STEADY ON', 'STEADY ON', 'STEADY ON', 'ON', 'STEADY ON', 'RX/TX BLINKING', -1, 23, -1, 'OK', NULL, NULL, NULL, NULL),
(98, 'PENDING', '2020-07-17', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(99, 'PENDING', '2020-07-18', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(100, 'PENDING', '2020-07-19', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(101, 'PENDING', '2020-07-20', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(102, 'PENDING', '2020-07-21', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(103, 'PENDING', '2020-07-22', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(104, 'PENDING', '2020-07-23', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(105, 'PENDING', '2020-07-24', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(106, 'PENDING', '2020-07-25', '15:33:33', 1, 3, 4156, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dscndlogs`
--

DROP TABLE IF EXISTS `dscndlogs`;
CREATE TABLE IF NOT EXISTS `dscndlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `p_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `dscndlogs_ibfk_2` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=137 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dscndlogs`
--

INSERT INTO `dscndlogs` (`log_id`, `emp_id`, `remarks`, `value`, `date`, `time`, `p_id`) VALUES
(1, 4144, 'Alarm LED was turned ON', 'ON', '2020-03-28', '23:50:12', 4),
(2, 4144, 'UPS I/P Voltage exceeding normal voltage', '210', '2020-03-28', '23:50:12', 4),
(3, 4144, 'UPS O/P Voltage exceeding normal voltage', '210', '2020-03-28', '23:50:12', 1),
(4, 4144, 'UPS Battery Voltage exceeding normal voltage', '170', '2020-03-28', '23:50:12', 1),
(5, 4144, 'Alarm LED was turned ON(update)', 'ON', '2020-03-28', '23:51:19', 1),
(6, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '23:52:09', 2),
(7, 4169, 'Alarm LED was turned ON', 'ON', '2020-03-29', '01:13:31', 1),
(8, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-29', '01:13:51', 1),
(11, 4156, 'Alarm LED was turned ON', 'STEADY ON', '2020-04-25', '22:18:56', 8),
(12, 4156, 'Rx/Tx -not Blinking(update)', 'RX/TX NOT BLINKING', '2020-04-25', '00:49:34', 8),
(13, 4156, 'Alarm LED was turned ON(update)', 'ON', '2020-04-25', '00:49:34', 8),
(14, 4156, 'Procedure Followed', 'okkk', '2020-04-25', '00:49:34', 8),
(15, 4156, 'Rx/Tx -not Blinking(update)', 'RX/TX NOT BLINKING', '2020-04-25', '00:50:00', 8),
(16, 4156, 'Alarm LED was turned ON(update)', 'ON', '2020-04-25', '00:50:00', 8),
(17, 4156, 'Procedure Followed', 'okkk', '2020-04-25', '00:50:00', 8),
(61, 4156, 'Rx/Tx -not Blinking(update)', 'RX/TX NOT BLINKING', '2020-05-01', '18:08:44', 16),
(62, 4156, 'Alarm LED was turned ON(update)', 'ON', '2020-05-01', '18:08:44', 16),
(63, 4156, 'UPS I/P Voltage exceeding normal voltage(update)', '210', '2020-05-01', '18:08:44', 16),
(115, 4169, 'SAT LED not steady on', 'NOT STEADY ON', '2020-05-03', '12:33:37', 22),
(116, 4169, 'I/O LED not steady on', 'NOT STEADY ON', '2020-05-03', '12:33:37', 22),
(117, 4169, 'UPS I/P Voltage exceeding normal voltage', '170', '2020-05-03', '12:33:37', 22),
(118, 4169, 'UPS O/P Voltage exceeding normal voltage', '170', '2020-05-03', '12:33:37', 22),
(119, 4169, 'SAT LED not steady on(update)', 'NOT STEADY ON', '2020-05-03', '12:35:20', 22),
(120, 4169, 'IO LED not steady on(update)', 'NOT STEADY ON', '2020-05-03', '12:35:20', 22),
(121, 4169, 'UPS O/P Voltage exceeding normal voltage(update)', '170', '2020-05-03', '12:35:20', 22),
(122, 4169, 'Procedure Followed', 'hi', '2020-05-03', '12:35:20', 22),
(123, 4169, 'SAT LED not steady on(update)', 'NOT STEADY ON', '2020-05-03', '12:37:40', 22),
(124, 4169, 'IO LED not steady on(update)', 'NOT STEADY ON', '2020-05-03', '12:37:40', 22),
(125, 4169, 'UPS I/P Voltage exceeding normal voltage(update)', '170', '2020-05-03', '12:37:40', 22),
(126, 4169, 'UPS O/P Voltage exceeding normal voltage(update)', '170', '2020-05-03', '12:37:40', 22),
(127, 4169, 'UPS Battery Voltage exceeding normal voltage(update)', '170', '2020-05-03', '12:37:40', 22),
(128, 4169, 'C/O Function not OK(update)', 'NOT OK', '2020-05-03', '12:37:40', 22),
(129, 4169, 'Procedure Followed', 'good', '2020-05-03', '12:37:40', 22),
(130, 4169, 'All parameters NORMAL', 'fixed', '2020-05-03', '12:47:28', 22),
(131, 4156, 'SAT LED not steady on', 'NOT STEADY ON', '2020-07-16', '12:22:02', 97),
(132, 4156, 'Alarm LED was turned ON', 'ON', '2020-07-16', '12:22:02', 97),
(133, 4156, 'UPS I/P Voltage exceeding normal voltage', '-1', '2020-07-16', '12:22:02', 97),
(134, 4156, 'UPS O/P Voltage exceeding normal voltage', '23', '2020-07-16', '12:22:02', 97),
(135, 4156, 'UPS Battery Voltage exceeding normal voltage', '-1', '2020-07-16', '12:22:02', 97),
(136, 4156, 'Final submit with errors', 'sup\r\n', '2020-07-16', '12:22:11', 97);

-- --------------------------------------------------------

--
-- Table structure for table `dscnmlogs`
--

DROP TABLE IF EXISTS `dscnmlogs`;
CREATE TABLE IF NOT EXISTS `dscnmlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(50) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `dscnmlogs_ibfk_1` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dscnmlogs`
--

INSERT INTO `dscnmlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(1, 4156, 5, 'Parameters as submitted in the report', 'Parameters submitted to the supervisor', '2020-04-27', '12:29:55'),
(2, 4156, 5, 'ok', 'Parameters submitted to the supervisor after rectification', '2020-04-27', '18:51:43'),
(4, 4169, 7, 'Parameters as submitted in the report', 'Parameters submitted to the supervisor', '2020-05-03', '12:52:57'),
(5, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-02', '12:21:06'),
(6, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-03', '12:21:06'),
(7, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-04', '12:21:06'),
(8, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-05', '12:21:06'),
(9, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-06', '12:21:06'),
(10, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-07', '12:21:06'),
(11, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-08', '12:21:06'),
(12, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-09', '12:21:06'),
(13, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-10', '12:21:06'),
(14, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-11', '12:21:06'),
(15, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-12', '12:21:06'),
(16, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-13', '12:21:06'),
(17, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-14', '12:21:06'),
(18, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-15', '12:21:06'),
(19, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-16', '12:21:06'),
(20, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-17', '12:21:06'),
(21, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-18', '12:21:06'),
(22, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-19', '12:21:06'),
(23, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-20', '12:21:06'),
(24, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-21', '12:21:06'),
(25, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-22', '12:21:06'),
(26, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-23', '12:21:06'),
(27, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-24', '12:21:06'),
(28, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-25', '12:21:06'),
(29, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-26', '12:21:06'),
(30, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-27', '12:21:06'),
(31, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-28', '12:21:06'),
(32, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-29', '12:21:06'),
(33, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-30', '12:21:06'),
(34, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-01', '12:21:06'),
(35, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-02', '12:21:06'),
(36, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-03', '12:21:06'),
(37, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-04', '12:21:06'),
(38, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-05', '12:21:06'),
(39, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-06', '12:21:06'),
(40, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-07', '12:21:06'),
(41, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-08', '12:21:06'),
(42, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-09', '12:21:06'),
(43, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-10', '12:21:06'),
(44, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-11', '12:21:06'),
(45, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-12', '12:21:06'),
(46, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-13', '12:21:06'),
(47, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-14', '12:21:06'),
(48, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-15', '12:21:06'),
(49, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-02', '12:29:21'),
(50, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-03', '12:29:21'),
(51, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-04', '12:29:21'),
(52, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-05', '12:29:21'),
(53, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-06', '12:29:21'),
(54, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-07', '12:29:21'),
(55, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-08', '12:29:21'),
(56, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-09', '12:29:21'),
(57, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-10', '12:29:21'),
(58, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-11', '12:29:21'),
(59, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-12', '12:29:21'),
(60, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-13', '12:29:21'),
(61, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-14', '12:29:21'),
(62, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-15', '12:29:21'),
(63, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-16', '12:29:21'),
(64, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-17', '12:29:21'),
(65, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-18', '12:29:21'),
(66, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-19', '12:29:21'),
(67, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-20', '12:29:21'),
(68, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-21', '12:29:21'),
(69, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-22', '12:29:21'),
(70, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-23', '12:29:21'),
(71, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-24', '12:29:21'),
(72, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-25', '12:29:21'),
(73, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-26', '12:29:21'),
(74, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-27', '12:29:21'),
(75, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-28', '12:29:21'),
(76, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-29', '12:29:21'),
(77, 4144, 7, 'No Entry', 'Report not submitted', '2020-06-30', '12:29:21'),
(78, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-01', '12:29:21'),
(79, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-02', '12:29:21'),
(80, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-03', '12:29:21'),
(81, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-04', '12:29:21'),
(82, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-05', '12:29:21'),
(83, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-06', '12:29:21'),
(84, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-07', '12:29:21'),
(85, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-08', '12:29:21'),
(86, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-09', '12:29:21'),
(87, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-10', '12:29:21'),
(88, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-11', '12:29:21'),
(89, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-12', '12:29:21'),
(90, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-13', '12:29:21'),
(91, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-14', '12:29:21'),
(92, 4144, 7, 'No Entry', 'Report not submitted', '2020-07-15', '12:29:21'),
(93, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-02', '15:33:33'),
(94, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-03', '15:33:33'),
(95, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-04', '15:33:33'),
(96, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-05', '15:33:33'),
(97, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-06', '15:33:33'),
(98, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-07', '15:33:33'),
(99, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-08', '15:33:33'),
(100, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-09', '15:33:33'),
(101, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-10', '15:33:33'),
(102, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-11', '15:33:33'),
(103, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-12', '15:33:33'),
(104, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-13', '15:33:33'),
(105, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-14', '15:33:33'),
(106, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-15', '15:33:33'),
(107, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-16', '15:33:33'),
(108, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-17', '15:33:33'),
(109, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-18', '15:33:33'),
(110, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-19', '15:33:33'),
(111, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-20', '15:33:33'),
(112, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-21', '15:33:33'),
(113, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-22', '15:33:33'),
(114, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-23', '15:33:33'),
(115, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-24', '15:33:33'),
(116, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-25', '15:33:33'),
(117, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-26', '15:33:33'),
(118, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-27', '15:33:33'),
(119, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-28', '15:33:33'),
(120, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-29', '15:33:33'),
(121, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-30', '15:33:33'),
(122, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-01', '15:33:33'),
(123, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-02', '15:33:33'),
(124, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-03', '15:33:33'),
(125, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-04', '15:33:33'),
(126, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-05', '15:33:33'),
(127, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-06', '15:33:33'),
(128, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-07', '15:33:33'),
(129, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-08', '15:33:33'),
(130, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-09', '15:33:33'),
(131, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-10', '15:33:33'),
(132, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-11', '15:33:33'),
(133, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-12', '15:33:33'),
(134, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-13', '15:33:33'),
(135, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-14', '15:33:33'),
(136, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-15', '15:33:33'),
(137, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-16', '15:33:33'),
(138, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-17', '15:33:33'),
(139, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-18', '15:33:33'),
(140, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-19', '15:33:33'),
(141, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-20', '15:33:33'),
(142, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-21', '15:33:33'),
(143, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-22', '15:33:33'),
(144, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-23', '15:33:33'),
(145, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-24', '15:33:33'),
(146, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-25', '15:33:33'),
(147, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-02', '18:56:32'),
(148, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-03', '18:56:32'),
(149, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-04', '18:56:32'),
(150, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-05', '18:56:32'),
(151, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-06', '18:56:32'),
(152, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-07', '18:56:32'),
(153, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-08', '18:56:32'),
(154, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-09', '18:56:32'),
(155, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-10', '18:56:32'),
(156, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-11', '18:56:32'),
(157, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-12', '18:56:32'),
(158, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-13', '18:56:32'),
(159, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-14', '18:56:32'),
(160, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-15', '18:56:32'),
(161, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-16', '18:56:32'),
(162, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-17', '18:56:32'),
(163, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-18', '18:56:32'),
(164, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-19', '18:56:32'),
(165, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-20', '18:56:32'),
(166, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-21', '18:56:32'),
(167, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-22', '18:56:32'),
(168, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-23', '18:56:32'),
(169, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-24', '18:56:32'),
(170, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-25', '18:56:32'),
(171, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-26', '18:56:32'),
(172, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-27', '18:56:32'),
(173, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-28', '18:56:32'),
(174, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-29', '18:56:32'),
(175, 4156, 7, 'No Entry', 'Report not submitted', '2020-06-30', '18:56:32'),
(176, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-01', '18:56:32'),
(177, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-02', '18:56:32'),
(178, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-03', '18:56:32'),
(179, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-04', '18:56:32'),
(180, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-05', '18:56:32'),
(181, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-06', '18:56:32'),
(182, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-07', '18:56:32'),
(183, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-08', '18:56:32'),
(184, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-09', '18:56:32'),
(185, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-10', '18:56:32'),
(186, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-11', '18:56:32'),
(187, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-12', '18:56:32'),
(188, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-13', '18:56:32'),
(189, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-14', '18:56:32'),
(190, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-15', '18:56:32'),
(191, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-16', '18:56:32'),
(192, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-17', '18:56:32'),
(193, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-18', '18:56:32'),
(194, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-19', '18:56:32'),
(195, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-20', '18:56:32'),
(196, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-21', '18:56:32'),
(197, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-22', '18:56:32'),
(198, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-23', '18:56:32'),
(199, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-24', '18:56:32'),
(200, 4156, 7, 'No Entry', 'Report not submitted', '2020-07-25', '18:56:32');

-- --------------------------------------------------------

--
-- Table structure for table `dscnmonthly`
--

DROP TABLE IF EXISTS `dscnmonthly`;
CREATE TABLE IF NOT EXISTS `dscnmonthly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `status` varchar(40) NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) DEFAULT NULL,
  `Cleaning_DSCN_associated_eqpt` tinytext,
  `Battery_backup_time_of_UPS1nUPS2` tinytext,
  `UPS_battery_voltage_on_load` tinytext,
  `Antenna_n_cable_check` tinytext,
  `Earth_resistance` tinytext,
  `EorN_voltage` int(11) DEFAULT NULL,
  `eqpt_status_after_check` varchar(5) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `dscnmonthly_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dscnmonthly`
--

INSERT INTO `dscnmonthly` (`p_id`, `date`, `time`, `status`, `a_id`, `emp_id`, `f_id`, `Cleaning_DSCN_associated_eqpt`, `Battery_backup_time_of_UPS1nUPS2`, `UPS_battery_voltage_on_load`, `Antenna_n_cable_check`, `Earth_resistance`, `EorN_voltage`, `eqpt_status_after_check`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-02-27', '10:05:06', 'COMPLETED', 1, 4156, 3, 'Cleaning performed.', '15hrs ', 'Can withstand load ', 'All antennas and cables properly connected.', 'All connections are maintained.', 25, 'GOOD', NULL, 'YES', '2020-02-27', '13:07:05'),
(2, '2020-03-27', '11:06:04', 'COMPLETED', 1, 4156, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'YES', '2020-03-27', '14:11:06'),
(5, '2020-04-27', '12:29:55', 'COMPLETED WITH ERRORS', 1, 4169, 3, 'cleaning performed ', '15 hrs', 'can withstamd', 'xs', 'ok', 25, 'ok', NULL, 'NO', '2020-05-01', '18:15:07'),
(7, '2020-05-03', '12:52:57', 'PENDING', 1, 4169, 3, 'hi', 'bye', 'die', 'my', 'foo', 3, 'to', NULL, 'NO', '2020-05-03', '19:02:02');

-- --------------------------------------------------------

--
-- Table structure for table `dscnweekly`
--

DROP TABLE IF EXISTS `dscnweekly`;
CREATE TABLE IF NOT EXISTS `dscnweekly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `status` varchar(30) NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `Air_conditioning_check` tinytext,
  `Cleaning_DSCN_associated_eqpt` tinytext,
  `UPS1_UPS2_battery_backup` tinytext,
  `UPS_battery_voltage_on_load` tinytext,
  `Antenna_n_Cable_check` tinytext,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dscnweekly`
--

INSERT INTO `dscnweekly` (`p_id`, `date`, `time`, `status`, `a_id`, `emp_id`, `f_id`, `Air_conditioning_check`, `Cleaning_DSCN_associated_eqpt`, `UPS1_UPS2_battery_backup`, `UPS_battery_voltage_on_load`, `Antenna_n_Cable_check`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-04-17', '14:06:03', 'COMPLETED', 1, 4156, 3, 'ALL installed AC\'s working.', 'ALL DSCN related equipments were cleaned.', 'UPS1 & UPS2 battery backup maintained.', 'Can withstand load', 'All cables and Antenna properly connected', NULL, 'YES', '2020-04-17', '13:06:04'),
(4, '2020-04-24', '09:09:00', '', 1, 4144, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `dscnwlogs`
--

DROP TABLE IF EXISTS `dscnwlogs`;
CREATE TABLE IF NOT EXISTS `dscnwlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `emp_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `designation` varchar(10) NOT NULL,
  `a_id` int(11) NOT NULL,
  PRIMARY KEY (`emp_id`) USING BTREE,
  KEY `a_id` (`a_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `name`, `designation`, `a_id`) VALUES
(1101, 'Hannibal Lecter', 'ED CNS', 1),
(2102, 'Linus Torvaldas', 'DGM', 1),
(3112, 'BP Singh', 'AGM CT', 1),
(3181, 'Mahesh Gotawandi', 'AGM SR', 1),
(3193, 'Corey Schrafer', 'AGM CE', 1),
(4121, 'Umesh Yadav', 'MGR CT', 1),
(4123, 'Ketan Hackerman', 'AM', 1),
(4129, 'Ramesh Sharma', 'JET', 1),
(4131, 'Chandresh Reddy', 'MGR SR', 1),
(4132, 'Suresh Kelkar', 'AM', 1),
(4133, 'Thon Thangal', 'JET', 1),
(4144, 'Hudson Odoi', 'AM', 1),
(4156, 'Mason Mount', 'JET', 1),
(4169, 'Varun Naik', 'MGR CE', 1);

-- --------------------------------------------------------

--
-- Table structure for table `engineer`
--

DROP TABLE IF EXISTS `engineer`;
CREATE TABLE IF NOT EXISTS `engineer` (
  `emp_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `dept` varchar(1) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT NULL,
  `email` varchar(30) NOT NULL DEFAULT 'bro@gmail.com',
  PRIMARY KEY (`emp_id`),
  KEY `a_id` (`a_id`),
  KEY `supervisor_id` (`supervisor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `engineer`
--

INSERT INTO `engineer` (`emp_id`, `name`, `designation`, `a_id`, `dept`, `contact`, `password`, `supervisor_id`, `email`) VALUES
(4121, 'Umesh Yadav', 'MGR CT', 1, 'N', 213112, 'pbkdf2_sha256$180000$Kj8R19kacWs5$72QHE97Jv6lEBHE7+BTdxvvSq3F9Wde8dA5lzwbGDqY=', 3112, 'bro@gmail.com'),
(4123, 'Ketan Hackerman', 'AM', 1, 'N', 21343, 'pbkdf2_sha256$180000$JAMo3q70IL9k$IpOIzvv+SQgd8ZQG2rzmkWDBfJTJGudEfmxj1sV4YQc=', 3112, 'bro@gmail.com'),
(4129, 'Ramesh Sharma', 'JET', 1, 'N', 32412, 'pbkdf2_sha256$180000$diZOk8Rzg1jx$hs/Io2JxPemTz/XiP1p/1ZNseMjMDi87l8hmWF/nmcI=', 3112, 'bro@gmail.com'),
(4131, 'Chandresh Reddy', 'MGR SR', 1, 'S', 21315, 'pbkdf2_sha256$180000$KqlhlXzv8Mjd$Jz3b0MbUJiah//q+7bR17PzYMZarf0/bjtSY2m3Im5E=', 3181, 'bro@gmail.com'),
(4132, 'Suresh Kelkar', 'AM', 1, 'S', 12312, 'pbkdf2_sha256$180000$TyI6a1BHImPz$T138jiTOLZO5K4cIoLP4HTS/Ips0oyFJX4XmF/rvp6Y=', 3181, 'bro@gmail.com'),
(4133, 'bobby', 'JET', 1, 'S', 44499, 'pbkdf2_sha256$180000$3mDUpcCefGhT$ISSBIRA6W4A34bfUm/5Q36geKPDs5LhGl5decyPhLTA=', 3181, 'bro@gmail.com'),
(4144, 'Hudson Odoi', 'AM', 1, 'C', 23231, 'pbkdf2_sha256$180000$0gx6UouLSNhm$reJqcqeiPkGZncq2y/Xbw/BdkhnaQoA08Lo7AepAEJE=', 3193, 'bro@gmail.com'),
(4156, 'Mason Mount', 'JET', 1, 'C', 231123, 'pbkdf2_sha256$180000$jSyJMRXoC0OR$WRh6O+2VZnlicZqvopk6Iz6NPzj1tcv+OrkGa71r/bA=', 3193, 'bro@gmail.com'),
(4169, 'Varun Naik', 'MGR CE', 1, 'C', 866651, 'pbkdf2_sha256$180000$u14lkS5xAW9g$N4A5ZRz8byVghDGCYfIfZKi8mbd2+oS45clKoeOKHJQ=', 3193, 'bro123@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `head`
--

DROP TABLE IF EXISTS `head`;
CREATE TABLE IF NOT EXISTS `head` (
  `head_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  PRIMARY KEY (`head_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `head`
--

INSERT INTO `head` (`head_id`, `name`, `designation`, `contact`, `password`) VALUES
(1101, 'Hannibal Lecter', 'ED CNS', 95187238, 'pbkdf2_sha256$180000$Q6fOe3VyK5li$36zjcFXU8UGpx3Q16ozZ4kB/e12+8P2Og0USItJkPZo=');

-- --------------------------------------------------------

--
-- Table structure for table `issues`
--

DROP TABLE IF EXISTS `issues`;
CREATE TABLE IF NOT EXISTS `issues` (
  `issue_no` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `Topic` varchar(30) NOT NULL,
  `desgn` varchar(10) DEFAULT NULL,
  `dept` varchar(1) DEFAULT NULL,
  `facility_affected` varchar(20) DEFAULT NULL,
  `observations` tinytext,
  `actions_taken` tinytext,
  `approved_by` int(11) DEFAULT NULL,
  PRIMARY KEY (`issue_no`,`date`,`a_id`),
  UNIQUE KEY `issue_no` (`issue_no`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `approved_by` (`approved_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issues`
--

INSERT INTO `issues` (`issue_no`, `date`, `a_id`, `emp_id`, `Topic`, `desgn`, `dept`, `facility_affected`, `observations`, `actions_taken`, `approved_by`) VALUES
(503, '2020-03-24 10:48:19', 1, 4144, 'BIT TEST FAILURE', 'AM', 'C', 'VHF RX (PAE)', 'Bit test failure was observed. This lead to non availability of the instrument.', 'Switched to standby receiver from VCS operator position for tower main frequency i.e. 118.65 MHz.', 3193),
(504, '2020-03-24 10:48:35', 1, 4156, 'SQUELCH DEFEAT', 'JET', 'C', 'VHF RX (PAE)', 'Ready signal not found to be Standard. Squelch defeat was observed to be ON. Squelch threshold varying more than usual. ', 'ATCO switched to alternate frequency', 3193),
(517, '2020-03-24 10:48:55', 1, 4169, 'BIT TEST FAILURE', 'MGR CE', 'C', 'VHF RX (PAE)', 'Bit test failure and abnormal AC to DC changeover observed. Referred to AGM-CE.\r\n', 'Emergency frequency utilised as per standard operating procedure from standard transmitter at EMERGENCY frequency of 121.5 MHz.', 2102),
(518, '2020-03-24 10:49:12', 1, 4169, 'UPS FAULTS', 'MGR CE', 'C', 'DSCN', 'Less voltage generated at the output side of the UPS. This giving rise to even lesser and insufficient battery voltage of 170V.\r\n', 'Class B surge diverter was found producing anomalies. Standby replacement was used on MGR CE\'s recommendation.', 3193),
(519, '2020-03-24 10:49:41', 1, 4129, 'SURGE DIVERTER FAULTS', 'JET', 'N', 'DVOR', 'PS 5V,PS 12V,PS -12V, reading deviating too much. This caused temperature to rise beyond the threshold of 70 degrees, recording 79 degrees.\r\nClass C surge diverter found faulty.', 'Class C surge diverter sent for repairing. Facility suspended till further notice.', 3112),
(520, '2020-03-24 10:49:56', 1, 4123, 'CLEANLINESS', 'AM', 'N', 'DME (HP)', 'Battery room not clean. This led to less voltage generation as per recommendation. This further lead to the sound produced by the DME due to low power supply.', 'Room was cleaned and the connections were thoroughly checked.', 3112),
(521, '2020-03-24 10:50:10', 1, 4129, 'UPS FAULTS', 'JET', 'N', 'NDB', 'Forward power observed to be very less (80W) as compared to (100W). This has led to decrease in reflected power.\r\n', 'Fault in UPS 1(Master) power supply. No spares available. This particular NDB is suspended until further notice. Spare NDB from Udaipur station has been called out. ', 2102);

-- --------------------------------------------------------

--
-- Table structure for table `mcdo`
--

DROP TABLE IF EXISTS `mcdo`;
CREATE TABLE IF NOT EXISTS `mcdo` (
  `emp_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `topic` varchar(50) NOT NULL,
  `DOP` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `content` tinytext NOT NULL,
  `DOA` timestamp NULL DEFAULT NULL,
  `approved_by` int(11) DEFAULT NULL,
  PRIMARY KEY (`emp_id`,`a_id`),
  KEY `a_id` (`a_id`),
  KEY `approved_by` (`approved_by`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mcdo`
--

INSERT INTO `mcdo` (`emp_id`, `a_id`, `topic`, `DOP`, `content`, `DOA`, `approved_by`) VALUES
(4131, 1, 'Enhancement of Surveillance Facilities', '2020-03-30 11:06:33', '1. Drone based surveillance pioneer.\r\n2. Zero faults return in scheduled maintenance for a period of 2 months.', '2020-04-02 11:06:33', 3181);

-- --------------------------------------------------------

--
-- Table structure for table `navigation`
--

DROP TABLE IF EXISTS `navigation`;
CREATE TABLE IF NOT EXISTS `navigation` (
  `f_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `facility` varchar(20) DEFAULT NULL,
  `frequency` int(11) DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `IDNT` varchar(10) DEFAULT NULL,
  `coordinateN` varchar(11) DEFAULT NULL,
  `coordinateE` varchar(11) DEFAULT NULL,
  `eqpt` varchar(20) DEFAULT NULL,
  `DOI` date DEFAULT NULL,
  `DOC` date DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT '3112',
  PRIMARY KEY (`f_id`,`a_id`),
  UNIQUE KEY `f_id` (`f_id`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`supervisor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `navigation`
--

INSERT INTO `navigation` (`f_id`, `a_id`, `facility`, `frequency`, `power`, `IDNT`, `coordinateN`, `coordinateE`, `eqpt`, `DOI`, `DOC`, `supervisor_id`) VALUES
(1, 1, 'DVOR', 117, 100, 'QQZ', '22 19\'58.2', '73 13\'30.5', 'AMS 1150', '2001-09-11', '2001-09-18', 3181),
(2, 1, 'DME (HP)', 1144, 1000, 'QQZ', '22 19\'58.2', '73 13\'30.5', 'GCEL 753', '2001-10-19', '2001-10-28', 3181),
(3, 1, 'NDB', 0, 100, 'QZ', '22 20\'5.2', '73 12\'33.6', 'SAC-100', '2019-07-22', '2019-11-07', 3181);

-- --------------------------------------------------------

--
-- Table structure for table `ndbdaily`
--

DROP TABLE IF EXISTS `ndbdaily`;
CREATE TABLE IF NOT EXISTS `ndbdaily` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `room_temp` int(11) DEFAULT NULL,
  `ac_mains_voltage_50Hz` int(11) DEFAULT NULL,
  `battery_voltage` int(11) DEFAULT NULL,
  `reflected_power` int(11) DEFAULT NULL,
  `forward_power` int(11) DEFAULT NULL,
  `modulation` int(11) DEFAULT NULL,
  `system_status_LED` varchar(3) DEFAULT NULL,
  `Primary_TX_LED` varchar(3) DEFAULT NULL,
  `TX_power_ON_LED` varchar(3) DEFAULT NULL,
  `remote_ctrl_link_LED` varchar(20) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ndbdaily`
--

INSERT INTO `ndbdaily` (`date`, `a_id`, `emp_id`, `f_id`, `room_temp`, `ac_mains_voltage_50Hz`, `battery_voltage`, `reflected_power`, `forward_power`, `modulation`, `system_status_LED`, `Primary_TX_LED`, `TX_power_ON_LED`, `remote_ctrl_link_LED`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:37:54', 1, 4121, '3', 20, 230, 21, 18, 100, 90, 'ON', 'ON', 'ON', 'BLINKING', NULL, 'YES', NULL, NULL, 1, NULL, ''),
('2020-03-24 10:37:57', 1, 4121, '3', 20, 225, 24, 18, 100, 87, 'ON', 'ON', 'ON', 'BLINKING', NULL, 'YES', NULL, NULL, 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `ndbmonthly`
--

DROP TABLE IF EXISTS `ndbmonthly`;
CREATE TABLE IF NOT EXISTS `ndbmonthly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `frwd_power_modulation_OFF` int(11) DEFAULT NULL,
  `reflected_power` int(11) DEFAULT NULL,
  `modulation_depth_check` int(11) DEFAULT NULL,
  `ident_code_check` varchar(10) DEFAULT NULL,
  `antenna_n_ACU_check` varchar(20) DEFAULT NULL,
  `NDB_eqpt_n_ACU_cleaning` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ndbmonthly`
--

INSERT INTO `ndbmonthly` (`date`, `a_id`, `emp_id`, `f_id`, `frwd_power_modulation_OFF`, `reflected_power`, `modulation_depth_check`, `ident_code_check`, `antenna_n_ACU_check`, `NDB_eqpt_n_ACU_cleaning`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:38:26', 1, 4121, '3', 100, 15, 92, 'VALID', 'GOOD', 'DONE', NULL, 'YES', NULL, NULL, 1, NULL, ''),
('2020-03-24 10:38:29', 1, 4129, '3', 80, 10, 82, 'VALID', 'GOOD', 'DONE', 'Forward power observed to be very less (80W) as compared to (100W). This has led to decrease in reflected power.\r\nReferred to AGM-CT. Issue no. 521.', 'NO', NULL, NULL, 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `ndbweekly`
--

DROP TABLE IF EXISTS `ndbweekly`;
CREATE TABLE IF NOT EXISTS `ndbweekly` (
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` varchar(10) NOT NULL,
  `mains_pwr_supply_check` tinytext,
  `battery_terminals_check` tinytext,
  `battery_sealed` varchar(3) DEFAULT NULL,
  `specific_gravity` float DEFAULT NULL,
  `antenna_site_condition` tinytext,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ndbweekly`
--

INSERT INTO `ndbweekly` (`date`, `a_id`, `emp_id`, `f_id`, `mains_pwr_supply_check`, `battery_terminals_check`, `battery_sealed`, `specific_gravity`, `antenna_site_condition`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`, `p_id`, `s_verify`, `status`) VALUES
('2020-03-24 10:38:48', 1, 4123, '3', 'OK', 'OK', 'YES', 12.3, 'OK', NULL, 'YES', NULL, NULL, 1, NULL, ''),
('2020-03-24 10:38:51', 1, 4129, '3', 'OK', 'OK', 'NO', 12, 'OK', NULL, 'YES', NULL, NULL, 2, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `scctvdaily`
--

DROP TABLE IF EXISTS `scctvdaily`;
CREATE TABLE IF NOT EXISTS `scctvdaily` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `status` varchar(30) NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `UPS_battery_indication` varchar(20) DEFAULT NULL,
  `Servers_ON_condition` varchar(10) DEFAULT NULL,
  `NAS_status_in_VMSorVRM` varchar(10) DEFAULT NULL,
  `recording_active_status_VRS_server` varchar(30) DEFAULT NULL,
  `recording_active_status_RRS_server` varchar(20) DEFAULT NULL,
  `database_status_VMS` varchar(10) DEFAULT NULL,
  `cameras_IVMS` varchar(10) DEFAULT NULL,
  `eqpt_cleaning` varchar(20) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `scctvdaily_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=114 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scctvdaily`
--

INSERT INTO `scctvdaily` (`p_id`, `date`, `time`, `status`, `a_id`, `emp_id`, `f_id`, `UPS_battery_indication`, `Servers_ON_condition`, `NAS_status_in_VMSorVRM`, `recording_active_status_VRS_server`, `recording_active_status_RRS_server`, `database_status_VMS`, `cameras_IVMS`, `eqpt_cleaning`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-04-25', '09:04:06', 'COMPLETED', 1, 4132, 3, 'FULL', 'OK', 'OK', '32', 'PAUSE', 'OK', 'OK', 'OK', NULL, 'YES', '2020-04-26', '13:07:06'),
(2, '2020-04-27', '07:06:06', 'COMPLETED', 1, 4133, 3, 'FULL', 'OK', 'OK', '32', 'PAUSE', 'OK', 'OK', 'CARRIED OUT', NULL, 'YES', '2020-04-27', '10:07:00'),
(3, '2020-04-28', '07:11:08', 'COMPLETED', 1, 4131, 3, 'FULL', 'OK', 'OK', '32', 'PAUSE', 'OK', 'OK', 'OK', NULL, 'YES', '2020-04-28', '19:10:05'),
(35, '2020-04-29', '17:37:15', 'COMPLETED WITH ERRORS', 1, 4131, 2, 'FULL', 'OK', 'OK', 'EQUALS TO TOTAL CAMERA', 'ON', 'OK', 'OK', 'CARRIED OUT', NULL, NULL, NULL, NULL),
(36, '2020-04-30', '22:41:20', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(37, '2020-05-01', '22:41:20', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(38, '2020-05-02', '22:29:19', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(39, '2020-05-03', '22:37:24', 'COMPLETED', 1, 4131, 2, 'FULL', 'OK', 'OK', 'EQUALS TO TOTAL CAMERA', 'PAUSE', 'OK', 'OK', 'CARRIED OUT', NULL, NULL, NULL, NULL),
(40, '2020-05-04', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(41, '2020-05-05', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(42, '2020-05-06', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(43, '2020-05-07', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(44, '2020-05-08', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(45, '2020-05-09', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(46, '2020-05-10', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(47, '2020-05-11', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(48, '2020-05-12', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(49, '2020-05-13', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(50, '2020-05-14', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(51, '2020-05-15', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(52, '2020-05-16', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(53, '2020-05-17', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(54, '2020-05-18', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(55, '2020-05-19', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(56, '2020-05-20', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(57, '2020-05-21', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(58, '2020-05-22', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(59, '2020-05-23', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(60, '2020-05-24', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(61, '2020-05-25', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(62, '2020-05-26', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(63, '2020-05-27', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(64, '2020-05-28', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(65, '2020-05-29', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(66, '2020-05-30', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(67, '2020-05-31', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(68, '2020-06-01', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(69, '2020-06-02', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(70, '2020-06-03', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(71, '2020-06-04', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(72, '2020-06-05', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(73, '2020-06-06', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(74, '2020-06-07', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(75, '2020-06-08', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(76, '2020-06-09', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(77, '2020-06-10', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(78, '2020-06-11', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(79, '2020-06-12', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(80, '2020-06-13', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(81, '2020-06-14', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(82, '2020-06-15', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(83, '2020-06-16', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(84, '2020-06-17', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(85, '2020-06-18', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(86, '2020-06-19', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(87, '2020-06-20', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(88, '2020-06-21', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(89, '2020-06-22', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(90, '2020-06-23', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(91, '2020-06-24', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(92, '2020-06-25', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(93, '2020-06-26', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(94, '2020-06-27', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(95, '2020-06-28', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(96, '2020-06-29', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(97, '2020-06-30', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(98, '2020-07-01', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(99, '2020-07-02', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(100, '2020-07-03', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(101, '2020-07-04', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(102, '2020-07-05', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(103, '2020-07-06', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(104, '2020-07-07', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(105, '2020-07-08', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(106, '2020-07-09', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(107, '2020-07-10', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(108, '2020-07-11', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(109, '2020-07-12', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(110, '2020-07-13', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(111, '2020-07-14', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(112, '2020-07-15', '12:22:38', 'PENDING', 1, 4131, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(113, '2020-07-16', '12:28:08', 'COMPLETED WITH ERRORS', 1, 4131, 2, 'FULL', 'OK', 'OK', 'EQUALS TO TOTAL CAMERA', 'ON', 'OK', 'OK', 'CARRIED OUT', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `scctvdlogs`
--

DROP TABLE IF EXISTS `scctvdlogs`;
CREATE TABLE IF NOT EXISTS `scctvdlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(40) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scctvdlogs`
--

INSERT INTO `scctvdlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(1, 4131, 35, 'NOT OK', 'NAS status in VMS/VRM is NOT OK ', '2020-07-07', '00:34:13'),
(2, 4131, 35, 'ON', 'Status of RRS camera is ON', '2020-04-29', '00:34:13'),
(3, 4131, 35, 'ON', 'Status of RRS camera is ON', '2020-04-29', '01:04:54'),
(4, 4131, 35, 'ON', 'Status of RRS camera is ON', '2020-04-29', '01:08:07'),
(5, 4131, 35, 'ON', 'Status of RRS camera is ON', '2020-04-29', '01:09:48'),
(6, 4131, 35, 'ON', 'Status of RRS camera is ON', '2020-04-29', '17:33:53'),
(7, 4131, 35, 'NOT OK', 'Status of ivms server is NOT OK', '2020-04-29', '17:33:53'),
(8, 4131, 35, 'ON', 'Status of RRS camera is ON', '2020-04-29', '17:37:15'),
(9, 4131, 35, 'bye', 'Final submit with errors', '2020-04-29', '17:38:29'),
(10, 4131, 39, 'ON', 'Status of RRS camera is ON', '2020-05-03', '22:36:02'),
(11, 4131, 39, 'NOT CARRIED OUT', 'Cleaning of equipments not carried out', '2020-05-03', '22:36:02'),
(12, 4131, 39, 'bye', 'Procedure Followed', '2020-05-03', '22:36:23'),
(13, 4131, 39, 'DISCHARGED', 'UPS Battery Indication is \'DISCHARGED\' ', '2020-05-03', '22:36:23'),
(14, 4131, 39, 'NOT OK', 'ALL SERVERS NOT IN ON STATE', '2020-05-03', '22:36:23'),
(15, 4131, 39, 'NOT OK', 'NAS status in VMS/VRM is NOT OK ', '2020-05-03', '22:36:23'),
(16, 4131, 39, 'ON', 'Status of RRS camera is ON', '2020-05-03', '22:36:23'),
(17, 4131, 39, 'NOT CARRIED OUT', 'Cleaning of equipments not carried out', '2020-05-03', '22:36:23'),
(18, 4131, 39, 'hello', 'Procedure Followed', '2020-05-03', '22:37:06'),
(19, 4131, 39, 'ON', 'Status of RRS camera is ON', '2020-05-03', '22:37:06'),
(20, 4131, 39, 'All parameters NORMAL', 'done', '2020-05-03', '22:37:24'),
(21, 4131, 113, 'ON', 'Status of RRS camera is ON', '2020-07-16', '12:27:53'),
(22, 4131, 113, 'kaai na re', 'Procedure Followed', '2020-07-16', '12:28:08'),
(23, 4131, 113, 'ON', 'Status of RRS camera is ON', '2020-07-16', '12:28:08'),
(24, 4131, 113, 'lol\r\n', 'Final submit with errors', '2020-07-16', '12:28:18');

-- --------------------------------------------------------

--
-- Table structure for table `scctvmlogs`
--

DROP TABLE IF EXISTS `scctvmlogs`;
CREATE TABLE IF NOT EXISTS `scctvmlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(40) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `scctvmlogs_ibfk_1` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scctvmlogs`
--

INSERT INTO `scctvmlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(23, 4169, 1, '12', 'Parameters normal at the first submit!', '2020-07-07', '00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `scctvmonthly`
--

DROP TABLE IF EXISTS `scctvmonthly`;
CREATE TABLE IF NOT EXISTS `scctvmonthly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `status` varchar(30) NOT NULL,
  `ups_ip_voltage` int(11) DEFAULT NULL,
  `ups_op_voltage` int(11) DEFAULT NULL,
  `ups_battery_op_voltage_ACpwrON` int(11) DEFAULT NULL,
  `ups_battery_op_voltage_ACpwrOFF` int(11) DEFAULT NULL,
  `ups_battery_op_voltage_after15min_ACpwrOFF` int(11) DEFAULT NULL,
  `server_status` varchar(5) DEFAULT NULL,
  `cameras_in_VRS_server` varchar(20) DEFAULT NULL,
  `NAS_free_capacity` float DEFAULT NULL,
  `OFClinkto_L2L3_switches` varchar(20) DEFAULT NULL,
  `cleaning_camera_eqpt` varchar(20) DEFAULT NULL,
  `user_rights_check` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `scctvmonthly_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scctvmonthly`
--

INSERT INTO `scctvmonthly` (`p_id`, `date`, `time`, `a_id`, `emp_id`, `f_id`, `status`, `ups_ip_voltage`, `ups_op_voltage`, `ups_battery_op_voltage_ACpwrON`, `ups_battery_op_voltage_ACpwrOFF`, `ups_battery_op_voltage_after15min_ACpwrOFF`, `server_status`, `cameras_in_VRS_server`, `NAS_free_capacity`, `OFClinkto_L2L3_switches`, `cleaning_camera_eqpt`, `user_rights_check`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-07-01', '09:04:02', 1, 4131, 3, 'COMPLETED', 235, 225, 203, 191, 176, 'ON', 'ACCESSIBLE', 1.24, 'BLINKING GREEN', 'CARRIED OUT', 'OK', NULL, 'YES', '2020-03-24', '14:04:11'),
(2, '2020-04-24', '09:06:04', 1, 4131, 3, 'COMPLETED', 230, 225, 208, 186, 176, 'ON', 'OK', 9.2, 'BLINKING GREEN', 'CARRIED OUT', 'OK', NULL, 'YES', '2020-04-24', '17:12:04'),
(6, '2020-04-29', '20:59:00', 1, 4131, 3, 'COMPLETED WITH ERRORS', 237, 230, 207, 185, 179, 'ON', 'OK', 1, 'BLINKING GREEN', 'CARRIED OUT', 'OK', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `scctvweekly`
--

DROP TABLE IF EXISTS `scctvweekly`;
CREATE TABLE IF NOT EXISTS `scctvweekly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `status` varchar(30) NOT NULL,
  `a_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL,
  `ups_ip_voltage` int(11) DEFAULT NULL,
  `ups_op_voltage` int(11) DEFAULT NULL,
  `ups_battery_status` varchar(10) DEFAULT NULL,
  `server_status` varchar(5) DEFAULT NULL,
  `camera_NAS_status_in_VRS` varchar(10) DEFAULT NULL,
  `workstns_n_client_softw_check` varchar(10) DEFAULT NULL,
  `cameras_client_IVMS_softw` varchar(10) DEFAULT NULL,
  `NAS_free_capacity` float DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `SCCTVWeekly_ibfk_3` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scctvweekly`
--

INSERT INTO `scctvweekly` (`p_id`, `date`, `time`, `status`, `a_id`, `emp_id`, `f_id`, `ups_ip_voltage`, `ups_op_voltage`, `ups_battery_status`, `server_status`, `camera_NAS_status_in_VRS`, `workstns_n_client_softw_check`, `cameras_client_IVMS_softw`, `NAS_free_capacity`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`) VALUES
(1, '2020-07-07', '09:05:04', 'COMPLETED', 1, 4131, 3, 230, 225, 'FULL', 'OK', 'OK', 'OK', 'OK', 1.23, 'NAS_free_capacity not to be equal to 0.', 'YES', '2020-04-15', '08:04:04'),
(2, '2020-04-22', '09:05:05', 'COMPLETED', 1, 4132, 3, 225, 220, 'FULL', 'OK', 'OK', 'OK', 'OK', 1.34, NULL, 'YES', '2020-04-22', '16:05:04'),
(3, '2020-04-29', '17:51:03', 'COMPLETED WITH ERRORS', 1, 4131, 3, 230, 231, 'FULL', 'ON', 'OK', 'OK', 'OK', 0, NULL, NULL, NULL, NULL),
(4, '2020-07-16', '12:28:30', 'COMPLETED WITH ERRORS', 1, 4131, 3, 23, 12, 'FULL', 'ON', 'OK', 'OK', 'OK', 12, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `scctvwlogs`
--

DROP TABLE IF EXISTS `scctvwlogs`;
CREATE TABLE IF NOT EXISTS `scctvwlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `value` varchar(40) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `scctvwlogs`
--

INSERT INTO `scctvwlogs` (`log_id`, `emp_id`, `p_id`, `value`, `remarks`, `date`, `time`) VALUES
(1, 4131, 3, '231', 'UPS_op not in corrent range', '2020-07-07', '17:42:47'),
(2, 4131, 3, 'DISCHARGED', 'UPS battery not full', '2020-04-29', '17:42:47'),
(3, 4131, 3, '0', 'NAS_free_capacity not OK', '2020-04-29', '17:42:47'),
(4, 4131, 3, '231', 'UPS_op not in corrent range', '2020-04-29', '17:51:03'),
(5, 4131, 3, '0', 'NAS_free_capacity not OK', '2020-04-29', '17:51:03'),
(6, 4131, 3, 'bye', 'Final submit with errors', '2020-04-29', '17:54:32'),
(7, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-06', '12:22:38'),
(8, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-07', '12:22:38'),
(9, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-08', '12:22:38'),
(10, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-09', '12:22:38'),
(11, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-10', '12:22:38'),
(12, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-11', '12:22:38'),
(13, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-12', '12:22:38'),
(14, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-13', '12:22:38'),
(15, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-14', '12:22:38'),
(16, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-15', '12:22:38'),
(17, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-16', '12:22:38'),
(18, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-17', '12:22:38'),
(19, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-18', '12:22:38'),
(20, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-19', '12:22:38'),
(21, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-20', '12:22:38'),
(22, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-21', '12:22:38'),
(23, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-22', '12:22:38'),
(24, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-23', '12:22:38'),
(25, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-24', '12:22:38'),
(26, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-25', '12:22:38'),
(27, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-26', '12:22:38'),
(28, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-27', '12:22:38'),
(29, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-28', '12:22:38'),
(30, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-29', '12:22:38'),
(31, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-30', '12:22:38'),
(32, 4131, 3, 'No Entry', 'Report not submitted', '2020-05-31', '12:22:38'),
(33, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-01', '12:22:38'),
(34, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-02', '12:22:38'),
(35, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-03', '12:22:38'),
(36, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-04', '12:22:38'),
(37, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-05', '12:22:38'),
(38, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-06', '12:22:38'),
(39, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-07', '12:22:38'),
(40, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-08', '12:22:38'),
(41, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-09', '12:22:38'),
(42, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-10', '12:22:38'),
(43, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-11', '12:22:38'),
(44, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-12', '12:22:38'),
(45, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-13', '12:22:38'),
(46, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-14', '12:22:38'),
(47, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-15', '12:22:38'),
(48, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-16', '12:22:38'),
(49, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-17', '12:22:38'),
(50, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-18', '12:22:38'),
(51, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-19', '12:22:38'),
(52, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-20', '12:22:38'),
(53, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-21', '12:22:38'),
(54, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-22', '12:22:38'),
(55, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-23', '12:22:38'),
(56, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-24', '12:22:38'),
(57, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-25', '12:22:38'),
(58, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-26', '12:22:38'),
(59, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-27', '12:22:38'),
(60, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-28', '12:22:38'),
(61, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-29', '12:22:38'),
(62, 4131, 3, 'No Entry', 'Report not submitted', '2020-06-30', '12:22:38'),
(63, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-01', '12:22:38'),
(64, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-02', '12:22:38'),
(65, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-03', '12:22:38'),
(66, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-04', '12:22:38'),
(67, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-05', '12:22:38'),
(68, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-06', '12:22:38'),
(69, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-07', '12:22:38'),
(70, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-08', '12:22:38'),
(71, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-09', '12:22:38'),
(72, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-10', '12:22:38'),
(73, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-11', '12:22:38'),
(74, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-12', '12:22:38'),
(75, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-13', '12:22:38'),
(76, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-14', '12:22:38'),
(77, 4131, 3, 'No Entry', 'Report not submitted', '2020-07-15', '12:22:38'),
(78, 4131, 4, '23', 'UPS ip not in range', '2020-07-16', '12:28:30'),
(79, 4131, 4, '12', 'UPS_op not in corrent range', '2020-07-16', '12:28:30'),
(80, 4131, 4, 'bye\r\n', 'Final submit with errors', '2020-07-16', '12:28:38');

-- --------------------------------------------------------

--
-- Table structure for table `supervisor`
--

DROP TABLE IF EXISTS `supervisor`;
CREATE TABLE IF NOT EXISTS `supervisor` (
  `supervisor_id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `designation` varchar(10) DEFAULT NULL,
  `a_id` int(11) DEFAULT NULL,
  `dept` varchar(1) DEFAULT NULL,
  `contact` int(11) DEFAULT NULL,
  `password` varchar(128) CHARACTER SET latin1 DEFAULT NULL,
  `dgm_id` int(11) DEFAULT NULL,
  `email` varchar(30) NOT NULL DEFAULT 'hello@gmail.com',
  PRIMARY KEY (`supervisor_id`),
  KEY `a_id` (`a_id`),
  KEY `dgm_id` (`dgm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `supervisor`
--

INSERT INTO `supervisor` (`supervisor_id`, `name`, `designation`, `a_id`, `dept`, `contact`, `password`, `dgm_id`, `email`) VALUES
(3112, 'BP Singh', 'AGM CT', 1, 'N', 1122121, 'pbkdf2_sha256$180000$olWqd4mSQKuK$vfdND+Nh6wKyerQ5VnlHKd3F/qw4z23QnDULN52vxn0=', 2102, 'hello@gmail.com'),
(3181, 'Mahesh Gotawandi', 'AGM SR', 1, 'S', 3211122, 'pbkdf2_sha256$180000$emnVA6NyWm1x$wpwILWSGgc2CLasfATRPm0vYinsPg4LWpdQvlIJBv0M=', 2102, 'hello@gmail.com'),
(3193, 'Corey Schrafer', 'AGM CE', 1, 'C', 121212, 'pbkdf2_sha256$180000$IcWsycUfGh6U$pAnm3Se2RLkiSCnsM4xV/NAqYDMB58sPxshHXSS40ro=', 2102, 'hello@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `surveillance`
--

DROP TABLE IF EXISTS `surveillance`;
CREATE TABLE IF NOT EXISTS `surveillance` (
  `f_id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `facility` varchar(20) DEFAULT NULL,
  `eqpt` varchar(20) DEFAULT NULL,
  `DOI` date DEFAULT NULL,
  `DOC` date DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT '3181',
  PRIMARY KEY (`f_id`,`a_id`),
  UNIQUE KEY `f_id` (`f_id`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`supervisor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `surveillance`
--

INSERT INTO `surveillance` (`f_id`, `a_id`, `facility`, `eqpt`, `DOI`, `DOC`, `supervisor_id`) VALUES
(1, 1, 'X-BIS', 'H.S.6040i', '2007-12-10', '2008-01-19', 3181),
(2, 1, 'ETD', '500 T', '2000-08-09', '0200-08-18', 3181),
(3, 1, 'SCCTV', 'INFINOVA', '1999-09-08', '1999-10-11', 3181);

-- --------------------------------------------------------

--
-- Table structure for table `vhfdaily`
--

DROP TABLE IF EXISTS `vhfdaily`;
CREATE TABLE IF NOT EXISTS `vhfdaily` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_verify` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `status` varchar(40) NOT NULL,
  `f_id` int(11) NOT NULL DEFAULT '1',
  `a_id` int(11) NOT NULL,
  `RX_no` int(11) DEFAULT NULL,
  `frequency_MHz` int(11) DEFAULT NULL,
  `bit_test` varchar(10) DEFAULT NULL,
  `vstatus` varchar(10) DEFAULT NULL,
  `RXN_check` varchar(10) DEFAULT NULL,
  `ACorDC_CorO` varchar(10) DEFAULT NULL,
  `SQ_threshold` int(11) DEFAULT NULL,
  `Remarks` tinytext,
  `Unit_Incharge_Approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vhfdaily`
--

INSERT INTO `vhfdaily` (`p_id`, `s_verify`, `date`, `time`, `emp_id`, `status`, `f_id`, `a_id`, `RX_no`, `frequency_MHz`, `bit_test`, `vstatus`, `RXN_check`, `ACorDC_CorO`, `SQ_threshold`, `Remarks`, `Unit_Incharge_Approval`, `approval_date`, `approval_time`) VALUES
(1, NULL, '2020-03-27', '11:04:05', 4144, '', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', 'C/O NORMAL', -85, 'SQ threshold < -80 DBm as expected.\r\nMaintenance carried out for VHF RX for model type of PAE.', 'YES', NULL, NULL),
(2, NULL, '2020-03-28', '12:04:07', 4144, '', 1, 1, 1, 122, 'PASS', 'READY', 'RXN NORMAL', 'C/O NORMAL', -81, 'Pass', 'YES', NULL, NULL),
(3, NULL, '2020-03-29', '15:06:06', 4156, '', 1, 1, 1, 119, 'PASS', 'READY', 'RXN NORMAL', 'C/O NORMAL', -82, NULL, 'YES', NULL, NULL),
(4, NULL, '2020-03-30', '22:37:04', 4144, '', 1, 1, 1, 123, 'PASS', 'READY', 'RXN NORMAL', NULL, -82, NULL, 'YES', NULL, NULL),
(5, NULL, '2020-03-31', '11:02:13', 4169, '', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', NULL, -83, NULL, 'YES', NULL, NULL),
(6, NULL, '2020-04-01', '12:40:49', 4156, '', 1, 1, 1, 123, 'PASS', 'READY', 'RXN NORMAL', NULL, -83, NULL, 'YES', NULL, NULL),
(7, NULL, '2020-04-02', '13:12:52', 4144, '', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', NULL, -82, NULL, 'YES', NULL, NULL),
(8, NULL, '2020-04-07', '17:28:28', 4156, 'COMPLETED', 1, 1, 1, 120, 'PASS', 'READY', 'RXN NORMAL', NULL, -82, NULL, 'YES', '2020-04-18', '21:46:46'),
(9, NULL, '2020-04-14', '21:40:49', 4156, 'COMPLETED', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(10, NULL, '2020-04-15', '00:24:04', 4156, '', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(11, NULL, '2020-04-16', '16:51:37', 4156, '', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(12, NULL, '2020-04-17', '13:41:02', 4156, '', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', 'YES', '2020-04-18', '22:29:49'),
(13, NULL, '2020-04-18', '16:40:35', 4156, '', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL),
(14, NULL, '2020-04-19', '19:49:03', 4156, 'COMPLETED WITH ERRORS', 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '---Report not submitted---', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vhfdlogs`
--

DROP TABLE IF EXISTS `vhfdlogs`;
CREATE TABLE IF NOT EXISTS `vhfdlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `p_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`),
  KEY `p_id` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vhfdlogs`
--

INSERT INTO `vhfdlogs` (`log_id`, `emp_id`, `remarks`, `value`, `date`, `time`, `p_id`) VALUES
(1, 4144, 'Bit test failed', 'FAIL', '2020-03-27', '22:37:04', NULL),
(2, 4144, 'Not Ready', 'NOT READY', '2020-03-27', '22:37:04', NULL),
(3, 4144, 'SQ Threshold above -80 Db', '-82', '2020-03-27', '22:37:04', NULL),
(4, 4144, 'Not Ready(update)', 'NOT READY', '2020-03-27', '22:37:39', NULL),
(5, 4144, 'SQ Threshold above -80 Db(update)', '-82', '2020-03-27', '22:37:39', NULL),
(6, 4144, 'SQ Threshold above -80 Db(update)', '-82', '2020-03-27', '22:37:57', NULL),
(7, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-27', '22:37:57', NULL),
(8, 4144, 'Bit test failed', 'READY', '2020-03-28', '11:02:13', NULL),
(9, 4144, 'Not Ready', 'OK', '2020-03-28', '11:02:13', NULL),
(10, 4144, 'SQ Threshold above -80 Db', '-83', '2020-03-28', '11:02:13', NULL),
(11, 4144, 'SQ Threshold above -80 Db(update)', '-83', '2020-03-28', '11:02:29', NULL),
(12, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '11:02:29', NULL),
(13, 4156, 'SQ Threshold above -80 Db', '-83', '2020-04-01', '12:40:49', NULL),
(14, 4144, 'SQ Threshold above -80 Db', '-82', '2020-04-02', '13:12:52', NULL),
(15, 4156, 'SQ Threshold above -80 Db', '-82', '2020-04-03', '17:28:28', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vhfmlogs`
--

DROP TABLE IF EXISTS `vhfmlogs`;
CREATE TABLE IF NOT EXISTS `vhfmlogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `value` varchar(30) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vhfmlogs`
--

INSERT INTO `vhfmlogs` (`log_id`, `emp_id`, `value`, `remarks`, `date`, `time`) VALUES
(1, 4144, '-116', 'Squelch Threshold not normal ', '2020-03-28', '01:32:06'),
(2, 4144, 'ON', 'Squelch carrier Override is not off', '2020-03-28', '01:32:06'),
(3, 4144, 'ST', 'SQUELCH O/P FACILITIES not standard', '2020-03-28', '01:32:06'),
(4, 4144, 'ON', 'Squelch carrier Override is not off(update)', '2020-03-28', '01:32:11'),
(5, 4144, 'ST', 'SQUELCH O/P FACILITIES not standard(update)', '2020-03-28', '01:32:11'),
(6, 4144, 'All parameters NORMAL', 'Parameter/s fixed', '2020-03-28', '01:32:19');

-- --------------------------------------------------------

--
-- Table structure for table `vhfmonthly`
--

DROP TABLE IF EXISTS `vhfmonthly`;
CREATE TABLE IF NOT EXISTS `vhfmonthly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL DEFAULT '1',
  `a_id` int(11) NOT NULL,
  `modulation_mode` varchar(10) DEFAULT NULL,
  `line_op` int(11) DEFAULT NULL,
  `squelch_defeat` varchar(3) DEFAULT NULL,
  `squelch_threshold` int(11) DEFAULT NULL,
  `squelch_carrier_override` varchar(3) DEFAULT NULL,
  `RF_pre_ATTN` varchar(3) DEFAULT NULL,
  `AGC` varchar(3) DEFAULT NULL,
  `Ready_signal` varchar(5) DEFAULT NULL,
  `Squelch_op_marc` varchar(5) DEFAULT NULL,
  `Squelch_op_facilities` varchar(5) DEFAULT NULL,
  `Squelch_op_phantom` varchar(5) DEFAULT NULL,
  `Squelch_defeat_ip` varchar(5) DEFAULT NULL,
  `bit_test` varchar(10) DEFAULT NULL,
  `REMARKS` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  UNIQUE KEY `date_2` (`date`),
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vhfmonthly`
--

INSERT INTO `vhfmonthly` (`p_id`, `date`, `time`, `emp_id`, `f_id`, `a_id`, `modulation_mode`, `line_op`, `squelch_defeat`, `squelch_threshold`, `squelch_carrier_override`, `RF_pre_ATTN`, `AGC`, `Ready_signal`, `Squelch_op_marc`, `Squelch_op_facilities`, `Squelch_op_phantom`, `Squelch_defeat_ip`, `bit_test`, `REMARKS`, `Unit_incharge_approval`, `approval_date`, `approval_time`, `s_verify`, `status`) VALUES
(1, '2020-01-27', '11:24:47', 4169, 1, 1, 'AM-Voice', 12, 'OFF', -107, 'OFF', 'OFF', 'ON', 'STD', 'STD', 'STD', 'STD', 'STD', 'OK', NULL, 'YES', NULL, NULL, NULL, ''),
(2, '2020-02-26', '11:24:57', 4156, 1, 1, 'AM-Voice', 11, 'OFF', -103, 'OFF', 'OFF', 'ON', 'STD', 'STD', 'STD', 'STD', 'STD', 'OK', '', 'YES', NULL, NULL, NULL, ''),
(3, '2020-03-28', '01:32:06', 4144, 1, 1, 'AM-Voice', 11, 'OFF', -113, 'OFF', 'OFF', 'ON', 'STD', 'STD', 'STD', 'STD', 'STD', 'OK', NULL, 'YES', NULL, NULL, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `vhfyearly`
--

DROP TABLE IF EXISTS `vhfyearly`;
CREATE TABLE IF NOT EXISTS `vhfyearly` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `f_id` int(11) NOT NULL DEFAULT '1',
  `a_id` int(11) NOT NULL,
  `RX_no` int(11) DEFAULT '1',
  `frequency_MHz` float DEFAULT NULL,
  `reference_freq` float DEFAULT NULL,
  `power` int(11) DEFAULT NULL,
  `bit_test` varchar(5) DEFAULT NULL,
  `AC_DC_changeover` varchar(20) DEFAULT NULL,
  `Remarks` tinytext,
  `Unit_incharge_approval` varchar(3) DEFAULT NULL,
  `approval_date` date DEFAULT NULL,
  `approval_time` time DEFAULT NULL,
  `s_verify` int(11) DEFAULT NULL,
  `status` varchar(30) NOT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE KEY `date` (`date`,`a_id`) USING BTREE,
  KEY `a_id` (`a_id`),
  KEY `emp_id` (`emp_id`),
  KEY `f_id` (`f_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vhfyearly`
--

INSERT INTO `vhfyearly` (`p_id`, `date`, `time`, `emp_id`, `f_id`, `a_id`, `RX_no`, `frequency_MHz`, `reference_freq`, `power`, `bit_test`, `AC_DC_changeover`, `Remarks`, `Unit_incharge_approval`, `approval_date`, `approval_time`, `s_verify`, `status`) VALUES
(1, '2018-03-29', '15:20:34', 4156, 1, 1, 1, 119, 20.95, 43, 'PASS', 'NORMAL(DC)', 'Every parameter was observed to be normal.', 'YES', NULL, NULL, NULL, ''),
(2, '2019-03-29', '11:40:12', 4169, 1, 1, 1, 120, 20.95, 26, 'PASS', 'NORMAL(DC)', NULL, 'YES', NULL, NULL, NULL, ''),
(3, '2020-03-28', '13:56:08', 4144, 1, 1, 1, 120, 20.95, 39, 'PASS', 'NORMAL(DC)', 'Parameter/s fixed', 'YES', NULL, NULL, NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `vhfylogs`
--

DROP TABLE IF EXISTS `vhfylogs`;
CREATE TABLE IF NOT EXISTS `vhfylogs` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `emp_id` int(11) NOT NULL,
  `remarks` varchar(100) NOT NULL,
  `value` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vhfylogs`
--

INSERT INTO `vhfylogs` (`log_id`, `emp_id`, `remarks`, `value`, `date`, `time`) VALUES
(1, 4144, 'Bit Test failed', 'FAIL', '2020-03-28', '13:56:08'),
(2, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '13:58:27'),
(3, 4144, 'Parameter/s fixed', 'All parameters NORMAL', '2020-03-28', '13:59:04');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `airport`
--
ALTER TABLE `airport`
  ADD CONSTRAINT `airport_ibfk_1` FOREIGN KEY (`dgm_id`) REFERENCES `dgm` (`dgm_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD CONSTRAINT `auth_user_ibfk_1` FOREIGN KEY (`username`) REFERENCES `dgm` (`dgm_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auth_user_ibfk_2` FOREIGN KEY (`username`) REFERENCES `engineer` (`emp_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auth_user_ibfk_3` FOREIGN KEY (`username`) REFERENCES `head` (`head_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auth_user_ibfk_4` FOREIGN KEY (`username`) REFERENCES `supervisor` (`supervisor_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `cdvordaily`
--
ALTER TABLE `cdvordaily`
  ADD CONSTRAINT `CDVORDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvordaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvordaily_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `navigation` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvordlogs`
--
ALTER TABLE `cdvordlogs`
  ADD CONSTRAINT `cdvordlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvordlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `cdvordaily` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvormlogs`
--
ALTER TABLE `cdvormlogs`
  ADD CONSTRAINT `cdvormlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvormlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `cdvormonthly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvormonthly`
--
ALTER TABLE `cdvormonthly`
  ADD CONSTRAINT `cdvormonthly_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvormonthly_ibfk_2` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvormonthly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `navigation` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvorweekly`
--
ALTER TABLE `cdvorweekly`
  ADD CONSTRAINT `CDVORWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvorweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvorweekly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `navigation` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `cdvorwlogs`
--
ALTER TABLE `cdvorwlogs`
  ADD CONSTRAINT `cdvorwlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `cdvorwlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `cdvorweekly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `communication`
--
ALTER TABLE `communication`
  ADD CONSTRAINT `communication_ibfk_2` FOREIGN KEY (`supervisor_id`) REFERENCES `supervisor` (`supervisor_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `communication_ibfk_3` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datisdaily`
--
ALTER TABLE `datisdaily`
  ADD CONSTRAINT `datisdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisdaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisdaily_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datisdlogs`
--
ALTER TABLE `datisdlogs`
  ADD CONSTRAINT `datisdlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisdlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `datisdaily` (`p_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `datisweekly`
--
ALTER TABLE `datisweekly`
  ADD CONSTRAINT `datisweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisweekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datisweekly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `datiswlogs`
--
ALTER TABLE `datiswlogs`
  ADD CONSTRAINT `datiswlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `datiswlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `datisweekly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dgm`
--
ALTER TABLE `dgm`
  ADD CONSTRAINT `dgm_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dgm_ibfk_2` FOREIGN KEY (`head_id`) REFERENCES `head` (`head_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `dmedaily`
--
ALTER TABLE `dmedaily`
  ADD CONSTRAINT `DMEDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dmedaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dmemonthly`
--
ALTER TABLE `dmemonthly`
  ADD CONSTRAINT `DMEMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dmemonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dmeweekly`
--
ALTER TABLE `dmeweekly`
  ADD CONSTRAINT `DMEWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dmeweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscndaily`
--
ALTER TABLE `dscndaily`
  ADD CONSTRAINT `DSCNDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscndaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscndaily_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscndlogs`
--
ALTER TABLE `dscndlogs`
  ADD CONSTRAINT `dscndlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscndlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `dscndaily` (`p_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `dscnmlogs`
--
ALTER TABLE `dscnmlogs`
  ADD CONSTRAINT `dscnmlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnmlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `dscnmonthly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscnmonthly`
--
ALTER TABLE `dscnmonthly`
  ADD CONSTRAINT `DSCNMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnmonthly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscnweekly`
--
ALTER TABLE `dscnweekly`
  ADD CONSTRAINT `DSCNWeekly_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnweekly_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `dscnwlogs`
--
ALTER TABLE `dscnwlogs`
  ADD CONSTRAINT `dscnwlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `dscnwlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `dscnweekly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `engineer`
--
ALTER TABLE `engineer`
  ADD CONSTRAINT `engineer_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `engineer_ibfk_2` FOREIGN KEY (`supervisor_id`) REFERENCES `supervisor` (`supervisor_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `issues`
--
ALTER TABLE `issues`
  ADD CONSTRAINT `Issues_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `gaand_karta_chedeycha` FOREIGN KEY (`approved_by`) REFERENCES `employee` (`emp_id`),
  ADD CONSTRAINT `issues_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `mcdo`
--
ALTER TABLE `mcdo`
  ADD CONSTRAINT `mcdo_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mcdo_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `mcdo_ibfk_3` FOREIGN KEY (`approved_by`) REFERENCES `employee` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `navigation`
--
ALTER TABLE `navigation`
  ADD CONSTRAINT `navigation_ibfk_3` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `navigation_ibfk_4` FOREIGN KEY (`supervisor_id`) REFERENCES `supervisor` (`supervisor_id`) ON UPDATE CASCADE;

--
-- Constraints for table `ndbdaily`
--
ALTER TABLE `ndbdaily`
  ADD CONSTRAINT `NDBDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ndbdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `ndbmonthly`
--
ALTER TABLE `ndbmonthly`
  ADD CONSTRAINT `NDBMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ndbmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `ndbweekly`
--
ALTER TABLE `ndbweekly`
  ADD CONSTRAINT `NDBWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `ndbweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvdaily`
--
ALTER TABLE `scctvdaily`
  ADD CONSTRAINT `SCCTVDaily_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvdaily_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `surveillance` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvdlogs`
--
ALTER TABLE `scctvdlogs`
  ADD CONSTRAINT `scctvdlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvdlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `scctvdaily` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvmlogs`
--
ALTER TABLE `scctvmlogs`
  ADD CONSTRAINT `scctvmlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvmlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `scctvmonthly` (`p_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvmonthly`
--
ALTER TABLE `scctvmonthly`
  ADD CONSTRAINT `SCCTVMonthly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvmonthly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `surveillance` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvweekly`
--
ALTER TABLE `scctvweekly`
  ADD CONSTRAINT `SCCTVWeekly_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `SCCTVWeekly_ibfk_3` FOREIGN KEY (`f_id`) REFERENCES `surveillance` (`f_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvweekly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scctvwlogs`
--
ALTER TABLE `scctvwlogs`
  ADD CONSTRAINT `scctvwlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `scctvwlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `scctvweekly` (`p_id`);

--
-- Constraints for table `supervisor`
--
ALTER TABLE `supervisor`
  ADD CONSTRAINT `supervisor_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `supervisor_ibfk_2` FOREIGN KEY (`dgm_id`) REFERENCES `dgm` (`dgm_id`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Constraints for table `surveillance`
--
ALTER TABLE `surveillance`
  ADD CONSTRAINT `surveillance_ibfk_3` FOREIGN KEY (`supervisor_id`) REFERENCES `supervisor` (`supervisor_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `surveillance_ibfk_4` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfdaily`
--
ALTER TABLE `vhfdaily`
  ADD CONSTRAINT `VHFDaily_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfdaily_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfdaily_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfdlogs`
--
ALTER TABLE `vhfdlogs`
  ADD CONSTRAINT `vhfdlogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfdlogs_ibfk_2` FOREIGN KEY (`p_id`) REFERENCES `vhfdaily` (`p_id`);

--
-- Constraints for table `vhfmonthly`
--
ALTER TABLE `vhfmonthly`
  ADD CONSTRAINT `VHFMonthly_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfmonthly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfmonthly_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfyearly`
--
ALTER TABLE `vhfyearly`
  ADD CONSTRAINT `VHFYearly_ibfk_3` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfyearly_ibfk_1` FOREIGN KEY (`a_id`) REFERENCES `airport` (`a_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `vhfyearly_ibfk_2` FOREIGN KEY (`f_id`) REFERENCES `communication` (`f_id`) ON UPDATE CASCADE;

--
-- Constraints for table `vhfylogs`
--
ALTER TABLE `vhfylogs`
  ADD CONSTRAINT `vhfylogs_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `engineer` (`emp_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
