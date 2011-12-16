-- phpMyAdmin SQL Dump
-- version 3.3.9.2
-- http://www.phpmyadmin.net
--
-- Host: mysql
-- Generation Time: Dec 16, 2011 at 02:48 AM
-- Server version: 5.1.39
-- PHP Version: 5.3.6-11

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `justdothat_bdd`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_message`
--

CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_message`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=68 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add message', 4, 'add_message'),
(11, 'Can change message', 4, 'change_message'),
(12, 'Can delete message', 4, 'delete_message'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add site', 7, 'add_site'),
(20, 'Can change site', 7, 'change_site'),
(21, 'Can delete site', 7, 'delete_site'),
(22, 'Can add log entry', 8, 'add_logentry'),
(23, 'Can change log entry', 8, 'change_logentry'),
(24, 'Can delete log entry', 8, 'delete_logentry'),
(25, 'Can add defi', 9, 'add_defi'),
(26, 'Can change defi', 9, 'change_defi'),
(27, 'Can delete defi', 9, 'delete_defi'),
(28, 'Can add categorie', 10, 'add_categorie'),
(29, 'Can change categorie', 10, 'change_categorie'),
(30, 'Can delete categorie', 10, 'delete_categorie'),
(31, 'Can add relever', 11, 'add_relever'),
(32, 'Can change relever', 11, 'change_relever'),
(33, 'Can delete relever', 11, 'delete_relever'),
(34, 'Can add utilisateur', 12, 'add_utilisateur'),
(35, 'Can change utilisateur', 12, 'change_utilisateur'),
(36, 'Can delete utilisateur', 12, 'delete_utilisateur'),
(37, 'Can add message prive', 13, 'add_messageprive'),
(38, 'Can change message prive', 13, 'change_messageprive'),
(39, 'Can delete message prive', 13, 'delete_messageprive'),
(40, 'Can add badge', 14, 'add_badge'),
(41, 'Can change badge', 14, 'change_badge'),
(42, 'Can delete badge', 14, 'delete_badge'),
(43, 'Can add gagner', 15, 'add_gagner'),
(44, 'Can change gagner', 15, 'change_gagner'),
(45, 'Can delete gagner', 15, 'delete_gagner'),
(46, 'Can add reponse', 16, 'add_reponse'),
(47, 'Can change reponse', 16, 'change_reponse'),
(48, 'Can delete reponse', 16, 'delete_reponse'),
(49, 'Can add commentaire', 17, 'add_commentaire'),
(50, 'Can change commentaire', 17, 'change_commentaire'),
(51, 'Can delete commentaire', 17, 'delete_commentaire'),
(52, 'Can add noter', 18, 'add_noter'),
(53, 'Can change noter', 18, 'change_noter'),
(54, 'Can delete noter', 18, 'delete_noter'),
(55, 'Can add source', 19, 'add_source'),
(56, 'Can change source', 19, 'change_source'),
(57, 'Can delete source', 19, 'delete_source'),
(58, 'Can add thumbnail', 20, 'add_thumbnail'),
(59, 'Can change thumbnail', 20, 'change_thumbnail'),
(60, 'Can delete thumbnail', 20, 'delete_thumbnail'),
(61, 'Can add comment', 21, 'add_comment'),
(62, 'Can change comment', 21, 'change_comment'),
(63, 'Can delete comment', 21, 'delete_comment'),
(64, 'Can moderate comments', 21, 'can_moderate'),
(65, 'Can add comment flag', 22, 'add_commentflag'),
(66, 'Can change comment flag', 22, 'change_commentflag'),
(67, 'Can delete comment flag', 22, 'delete_commentflag');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(3, 'Vince', '', '', 'vincentjubault@gmail.com', 'sha1$b9d6d$d067adeeceebdc5242867c455dcac6c0d495809e', 0, 1, 0, '2011-12-16 01:58:57', '2011-12-16 00:50:04'),
(4, 'marlene', '', '', 'marlene-10@hotmail.fr', 'sha1$13aa4$e214dbdf1ed781448981fb4d72025a2144749596', 1, 1, 1, '2011-12-16 02:23:02', '2011-12-16 00:55:50'),
(5, 'babar', '', '', 'babar@hotmail.com', 'sha1$cc7f5$e007406287cdd277ea9f86c0c0b447270c54f22e', 0, 1, 0, '2011-12-16 01:06:06', '2011-12-16 00:59:47'),
(6, 'Stryder', '', '', 'florian.lamy@gmail.com', 'sha1$49d78$e7bbaed71bae3b25c46938e1df3e26e285f876fb', 0, 1, 0, '2011-12-16 01:24:13', '2011-12-16 01:16:43'),
(7, 'Choupette', '', '', 'chou@free.fr', 'sha1$312c3$6074285fe2949536850129eb36130a30c243ff92', 0, 1, 0, '2011-12-16 02:04:26', '2011-12-16 01:42:37'),
(8, 'CrazyDude', '', '', 'crazy@dude.fr', 'sha1$3ee8e$a3867b63cfb07d0555e0cedfda5c8504c9fe5c9e', 0, 1, 0, '2011-12-16 02:08:48', '2011-12-16 01:53:41'),
(9, 'PinkMan', '', '', 'pink@man.fr', 'sha1$e7784$4acc9bb409d604712737552235b9d0e15b3285fe', 0, 1, 0, '2011-12-16 02:33:16', '2011-12-16 02:02:13'),
(11, 'winnielepunk', '', '', 'roldao.timothee@neuf.fr', 'sha1$08259$fdf295efca4b7a470eebebfc087718a2ea7789a1', 1, 1, 1, '2011-12-16 02:30:28', '2011-12-16 02:29:58'),
(12, 'jeff', '', '', 'jeff_biondi@msn.com', 'sha1$1a1b0$19c1d89e54a389f8da13e6fbd9f33ab0067f8557', 0, 1, 0, '2011-12-16 02:33:49', '2011-12-16 02:30:53');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `defi_categorie`
--

CREATE TABLE IF NOT EXISTS `defi_categorie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(100) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `defi_categorie_a951d5d6` (`slug`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `defi_categorie`
--

INSERT INTO `defi_categorie` (`id`, `slug`, `nom`, `description`) VALUES
(1, 'poney', 'poney', 'poney'),
(2, 'Food', 'Food', 'Food'),
(3, 'Sport', 'Sport', 'Sport'),
(4, 'Family', 'Family', 'Family'),
(5, 'BadAss', 'Bad Ass', 'Bad Ass'),
(6, 'Art', 'Art', 'Art'),
(7, 'Adventure', 'Adventure', 'Adventure'),
(8, 'Style', 'Style', 'Style');

-- --------------------------------------------------------

--
-- Table structure for table `defi_defi`
--

CREATE TABLE IF NOT EXISTS `defi_defi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(100) NOT NULL,
  `titre` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `debut` date NOT NULL,
  `fin` date NOT NULL,
  `photo` varchar(100) NOT NULL,
  `difficulte` int(11) NOT NULL,
  `categorie_id` int(11) NOT NULL,
  `createur_id` int(11) NOT NULL,
  `fini` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `defi_defi_a951d5d6` (`slug`),
  KEY `defi_defi_15ce544c` (`categorie_id`),
  KEY `defi_defi_7cd86c5` (`createur_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `defi_defi`
--

INSERT INTO `defi_defi` (`id`, `slug`, `titre`, `description`, `debut`, `fin`, `photo`, `difficulte`, `categorie_id`, `createur_id`, `fini`) VALUES
(2, 'put-a-lime-in-a-coconut', 'put a lime in a coconut', 'put a lime in a coconut and drink ''em both up.', '2011-12-16', '2012-01-01', 'challenge_pics/default.png', 1, 1, 3, 0),
(3, 'eat-the-biggest-sandwich', 'Eat the biggest sandwich!', 'Will you dare eating the biggest sandwich of the world ?', '2011-12-16', '2011-12-29', 'challenge_pics/almuerzo-hamburguesas-comida-los-tomates_370920.jpg', 2, 2, 4, 0),
(4, 'se-jeter-du-toit', 'Se jeter du toit', 'Le but du défi est de sauter d''un toit, le plus haut possible bien sur ', '2011-12-16', '2011-12-21', 'challenge_pics/jump-off-roof.jpg', 3, 5, 5, 0),
(5, 'carry-on-a-fake-baby', 'Carry on a fake baby', 'Carry on a fake baby during an entire week!!', '2011-12-16', '2012-01-10', 'challenge_pics/baby.jpg', 2, 4, 4, 0),
(6, 'crazy-hair-cut', 'Crazy hair cut', 'Get the craziest hair cut ever seen!', '2011-12-16', '2011-12-21', 'challenge_pics/hai.jpg', 3, 8, 4, 0),
(7, 'with-a-bike', 'With a bike', 'Cross the Sahara desert with a Bike in less than 1 week!', '2011-12-16', '2012-02-01', 'challenge_pics/bike.jpg', 4, 3, 4, 0),
(8, 'salsa', 'Salsa!', 'Make the perfect move!', '2011-12-16', '2011-12-18', 'challenge_pics/salsa.jpg', 2, 6, 4, 0),
(9, 'sing-sing-sing', 'Sing sing sing', 'Sing "Le petit bonhomme en mousse" in front of at leat 200 people.', '2011-12-16', '2012-01-05', 'challenge_pics/sing.jpg', 2, 6, 4, 0),
(10, 'kill-your-dog', 'kill your dog', 'kill your dog in a creative way and show us a nice pic !', '2011-12-16', '2012-05-10', 'challenge_pics/kawaii-baby-dog-vol6-stickers-deco-blanc-grand-format_1.jpg', 1, 6, 3, 0),
(11, 'jump-high', 'Jump High !', 'Jump the highest possible without springboard !', '2011-12-16', '2011-12-30', 'challenge_pics/jump3.jpg', 3, 3, 9, 0);

-- --------------------------------------------------------

--
-- Table structure for table `defi_relever`
--

CREATE TABLE IF NOT EXISTS `defi_relever` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `defi_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `defi_relever_23b2b636` (`defi_id`),
  KEY `defi_relever_5f9483ee` (`utilisateur_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `defi_relever`
--

INSERT INTO `defi_relever` (`id`, `defi_id`, `utilisateur_id`) VALUES
(6, 3, 3),
(7, 2, 4),
(8, 2, 4),
(9, 4, 6),
(10, 6, 3),
(11, 4, 3),
(12, 3, 3),
(13, 6, 7),
(14, 9, 3),
(15, 8, 7),
(16, 11, 7),
(17, 3, 7),
(18, 6, 3),
(19, 11, 4),
(20, 11, 8),
(21, 4, 12),
(22, 10, 12);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=17 ;

--
-- Dumping data for table `django_admin_log`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_comments`
--

CREATE TABLE IF NOT EXISTS `django_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_type_id` int(11) NOT NULL,
  `object_pk` longtext NOT NULL,
  `site_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(75) NOT NULL,
  `user_url` varchar(200) NOT NULL,
  `comment` longtext NOT NULL,
  `submit_date` datetime NOT NULL,
  `ip_address` char(15) DEFAULT NULL,
  `is_public` tinyint(1) NOT NULL,
  `is_removed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_comments_e4470c6e` (`content_type_id`),
  KEY `django_comments_6223029` (`site_id`),
  KEY `django_comments_fbfc09f1` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `django_comments`
--

INSERT INTO `django_comments` (`id`, `content_type_id`, `object_pk`, `site_id`, `user_id`, `user_name`, `user_email`, `user_url`, `comment`, `submit_date`, `ip_address`, `is_public`, `is_removed`) VALUES
(1, 16, '9', 1, 5, 'babar', 'babar@hotmail.com', '', 'Trop chaud le mec !', '2011-12-16 01:20:40', '77.201.40.99', 1, 0),
(2, 16, '9', 1, 6, 'Stryder', 'florian.lamy@gmail.com', '', 't''as vu TMTC cousin', '2011-12-16 01:22:02', '89.83.15.14', 1, 0),
(3, 16, '9', 1, 3, 'Vince', 'vincentjubault@gmail.com', '', 'lol ptdr', '2011-12-16 01:30:17', '84.101.25.48', 1, 0),
(4, 16, '7', 1, 3, 'Vince', 'vincentjubault@gmail.com', '', 'not bad, do it again !', '2011-12-16 01:35:36', '84.101.25.48', 1, 0),
(5, 16, '6', 1, 4, 'marlene', 'marlene-10@hotmail.fr', '', 'Yeah Effectively !', '2011-12-16 01:40:10', '81.57.96.61', 1, 0),
(6, 16, '9', 1, 6, 'Stryder', 'florian.lamy@gmail.com', '', 'lui c''était mon pote et il a pas survécu xD', '2011-12-16 01:52:02', '89.83.15.14', 1, 0),
(7, 16, '14', 1, 6, 'Stryder', 'florian.lamy@gmail.com', '', 'you are my hero. When is the concert ?!!', '2011-12-16 01:58:28', '89.83.15.14', 1, 0),
(8, 16, '11', 1, 5, 'babar', 'babar@hotmail.com', '', 'Classe la combi\r\n', '2011-12-16 02:00:53', '77.201.40.99', 1, 0),
(9, 16, '10', 1, 7, 'Choupette', 'chou@free.fr', '', 'You will never win !', '2011-12-16 02:07:10', '81.57.96.61', 1, 0),
(10, 16, '16', 1, 7, 'Choupette', 'chou@free.fr', '', 'Great!', '2011-12-16 02:07:24', '81.57.96.61', 1, 0),
(11, 16, '16', 1, 4, 'marlene', 'marlene-10@hotmail.fr', '', 'I will win !', '2011-12-16 02:08:07', '81.57.96.61', 1, 0),
(12, 16, '13', 1, 3, 'Vince', 'vincentjubault@gmail.com', '', 'you will see what crazy really means', '2011-12-16 02:08:23', '84.101.25.48', 1, 0),
(13, 16, '20', 1, 8, 'CrazyDude', 'crazy@dude.fr', '', 'I''am the strongest!', '2011-12-16 02:09:19', '81.57.96.61', 1, 0),
(14, 16, '9', 1, 12, 'jeff', 'jeff_biondi@msn.com', '', 'xpldr', '2011-12-16 02:34:07', '83.114.53.178', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `django_comment_flags`
--

CREATE TABLE IF NOT EXISTS `django_comment_flags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `flag` varchar(30) NOT NULL,
  `flag_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`comment_id`,`flag`),
  KEY `django_comment_flags_fbfc09f1` (`user_id`),
  KEY `django_comment_flags_9b3dc754` (`comment_id`),
  KEY `django_comment_flags_111c90f9` (`flag`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `django_comment_flags`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'message', 'auth', 'message'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'site', 'sites', 'site'),
(8, 'log entry', 'admin', 'logentry'),
(9, 'defi', 'defi', 'defi'),
(10, 'categorie', 'defi', 'categorie'),
(11, 'relever', 'defi', 'relever'),
(12, 'utilisateur', 'utilisateur', 'utilisateur'),
(13, 'message prive', 'utilisateur', 'messageprive'),
(14, 'badge', 'utilisateur', 'badge'),
(15, 'gagner', 'utilisateur', 'gagner'),
(16, 'reponse', 'reponse', 'reponse'),
(17, 'commentaire', 'reponse', 'commentaire'),
(18, 'noter', 'reponse', 'noter'),
(19, 'source', 'easy_thumbnails', 'source'),
(20, 'thumbnail', 'easy_thumbnails', 'thumbnail'),
(21, 'comment', 'comments', 'comment'),
(22, 'comment flag', 'comments', 'commentflag');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0941bb33a9f10786eac55623bbe6d79a', 'Njg1NWJjNzU1MGIyMmQ2NzIxYWNiMzk5MzU4OTI4NWU2OGU5NzQxMjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2011-12-29 23:27:32'),
('0bdc15d37fc2ec5c2de60f3f15bd5d63', 'OGI2YjBiNDZkMjZkMmMzNjU0MDcyM2MzZmZiYzM3OGZlOGZjODY5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg==\n', '2011-12-30 00:50:19'),
('12ed2c10c5d08485cd31a1af1faa641d', 'YTFkMWNhOTJiMTYxMzIxMDM2ZTA5NzJiODhjMWM1NDczNDBkODA2NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQR1Lg==\n', '2011-12-30 02:18:26'),
('40755863e3165329a98aee2d24f19fcc', 'OGRmMzY0OGY5M2I2ZGEwNjhlZDE0ZWIxNTVhZWFlMWJlODVkZjQ0MjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2011-12-30 02:36:19'),
('4c7b645e47ffb0e2c6e2ec257d75c719', 'OGRmMzY0OGY5M2I2ZGEwNjhlZDE0ZWIxNTVhZWFlMWJlODVkZjQ0MjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2011-12-29 19:38:02'),
('5503dba276e969383a475fc2f1d8b4cb', 'OGI2YjBiNDZkMjZkMmMzNjU0MDcyM2MzZmZiYzM3OGZlOGZjODY5ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg==\n', '2011-12-30 01:58:57'),
('95397ad3e31159584d273ce93a44b540', 'OGFjZTNkMjA3NmViZGNhNjU4MzBjN2RjYWY3OWMzZTU2YmZlOGJiMzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQV1Lg==\n', '2011-12-30 01:06:06'),
('b2244ca2aa3efe13a48aa59a60490332', 'YjkzOTA0NjMxNDViMTUxZTM0YjBkZDc5ZjE5YmEwYTc3YTgzMmNlNjqAAn1xAS4=\n', '2011-12-30 02:35:31'),
('b8b91b908b10345e1191d34af00aaccf', 'MjVkMTg1OWY0ZDA2OTQ4MzEyMTZmMTY3NjFmZGMzZjJlZmQ4YTc1ZjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQZ1Lg==\n', '2011-12-30 01:24:13'),
('fe9182dcf5c422c13a7b9304526c5dac', 'MGNiNzRiMzc2NTdlMzdhZjM2OTU5MTdjYzY3NTM2N2IwMjg3ZGY4YTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQx1Lg==\n', '2011-12-30 02:33:49');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_source`
--

CREATE TABLE IF NOT EXISTS `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storage_hash` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_3a997c55` (`storage_hash`),
  KEY `easy_thumbnails_source_52094d6e` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=44 ;

--
-- Dumping data for table `easy_thumbnails_source`
--

INSERT INTO `easy_thumbnails_source` (`id`, `storage_hash`, `name`, `modified`) VALUES
(1, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/logo.png', '2011-12-15 19:39:02'),
(2, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/logo.png', '2011-12-15 19:44:17'),
(3, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/logo.png', '2011-12-15 19:45:04'),
(4, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/logo_1.png', '2011-12-15 19:45:37'),
(5, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/logo_2.png', '2011-12-15 19:46:06'),
(6, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/logo_3.png', '2011-12-15 21:30:10'),
(7, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/logo_4.png', '2011-12-15 21:30:43'),
(8, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/logo_1.png', '2011-12-15 21:31:47'),
(9, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/IMG_09152.jpg', '2011-12-16 00:50:04'),
(10, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/photo.png', '2011-12-16 00:55:50'),
(11, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/babar.jpg', '2011-12-16 00:59:47'),
(12, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/almuerzo-hamburguesas-comida-los-tomates_370920.jpg', '2011-12-16 01:07:28'),
(13, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/default.png', '2011-12-16 01:08:50'),
(14, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/stock-photo-big-hamburger-isolated-on-white-65852539.jpg', '2011-12-16 01:10:16'),
(15, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/jump-off-roof.jpg', '2011-12-16 01:12:06'),
(16, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/70357_742139914_8383416_n.jpg', '2011-12-16 01:16:43'),
(17, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/coconut.jpg', '2011-12-16 01:17:00'),
(18, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/chine-gratte-ciel.jpg', '2011-12-16 01:18:37'),
(19, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/baby.jpg', '2011-12-16 01:22:02'),
(20, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/hai.jpg', '2011-12-16 01:27:03'),
(21, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/IMG_09152.jpg', '2011-12-16 01:28:24'),
(22, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/bike.jpg', '2011-12-16 01:30:58'),
(23, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/images.jpg', '2011-12-16 01:32:31'),
(24, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/salsa.jpg', '2011-12-16 01:34:02'),
(25, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/sing.jpg', '2011-12-16 01:38:51'),
(26, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/kawaii-baby-dog-vol6-stickers-deco-blanc-grand-format_1.jpg', '2011-12-16 01:40:29'),
(27, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/choupette.jpg', '2011-12-16 01:42:37'),
(28, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/choupette.jpg', '2011-12-16 01:43:13'),
(29, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/concert-a-lyon.jpg', '2011-12-16 01:44:40'),
(30, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/salsa2.jpg', '2011-12-16 01:45:44'),
(31, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/man3.jpg', '2011-12-16 01:53:41'),
(32, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/man2.jpg', '2011-12-16 02:02:13'),
(33, 'f9bde26a1556cd667f742bd34ec7c55e', 'challenge_pics/jump3.jpg', '2011-12-16 02:04:04'),
(34, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/jump2.jpg', '2011-12-16 02:04:50'),
(35, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/lunch.jpg', '2011-12-16 02:06:37'),
(36, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/crazy.jpg', '2011-12-16 02:07:31'),
(37, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/jump.jpg', '2011-12-16 02:07:55'),
(38, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/jump4.jpg', '2011-12-16 02:09:08'),
(39, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/default.png', '2011-12-16 01:09:01'),
(40, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/poney.jpg', '2011-12-16 02:29:58'),
(41, 'f9bde26a1556cd667f742bd34ec7c55e', 'profile_pics/jeff.jpg', '2011-12-16 02:30:53'),
(42, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/moutarde-me-monte-au-nez-01-g.jpg', '2011-12-16 02:37:47'),
(43, 'f9bde26a1556cd667f742bd34ec7c55e', 'reponse_pics/Capture_décran_2011-12-16_à_02.41.02.png', '2011-12-16 02:41:44');

-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

CREATE TABLE IF NOT EXISTS `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storage_hash` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thumbnails_thumbnail_3a997c55` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_52094d6e` (`name`),
  KEY `easy_thumbnails_thumbnail_89f89e85` (`source_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=77 ;

--
-- Dumping data for table `easy_thumbnails_thumbnail`
--

INSERT INTO `easy_thumbnails_thumbnail` (`id`, `storage_hash`, `name`, `modified`, `source_id`) VALUES
(1, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/logo.png.120x120_q85_crop.jpg', '2011-12-15 19:42:04', 1),
(2, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/logo.png.30x30_q85_crop.jpg', '2011-12-15 19:42:28', 1),
(3, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/logo.png.200x140_q85_crop.jpg', '2011-12-15 19:44:17', 2),
(4, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/logo.png.145x145_q85_crop.jpg', '2011-12-15 19:44:44', 2),
(5, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/logo.png.145x145_q85_crop.jpg', '2011-12-15 19:45:04', 3),
(6, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/logo_1.png.145x145_q85_crop.jpg', '2011-12-15 19:45:37', 4),
(7, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/logo_2.png.145x145_q85_crop.jpg', '2011-12-15 19:46:06', 5),
(8, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/logo_3.png.145x145_q85_crop.jpg', '2011-12-15 21:30:10', 6),
(9, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/logo_4.png.145x145_q85_crop.jpg', '2011-12-15 21:30:44', 7),
(10, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/logo_1.png.120x120_q85_crop.jpg', '2011-12-15 21:31:47', 8),
(11, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/logo_1.png.30x30_q85_crop.jpg', '2011-12-15 21:31:57', 8),
(12, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/IMG_09152.jpg.120x120_q85_crop.jpg', '2011-12-16 00:50:04', 9),
(13, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/IMG_09152.jpg.30x30_q85_crop.jpg', '2011-12-16 00:50:19', 9),
(14, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/IMG_09152.jpg.145x145_q85_crop.jpg', '2011-12-16 00:50:27', 9),
(15, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/photo.png.120x120_q85_crop.jpg', '2011-12-16 00:55:50', 10),
(16, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/photo.png.30x30_q85_crop.jpg', '2011-12-16 00:55:57', 10),
(17, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/photo.png.145x145_q85_crop.jpg', '2011-12-16 00:56:03', 10),
(18, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/babar.jpg.120x120_q85_crop.jpg', '2011-12-16 00:59:47', 11),
(19, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/babar.jpg.30x30_q85_crop.jpg', '2011-12-16 01:06:07', 11),
(20, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/babar.jpg.145x145_q85_crop.jpg', '2011-12-16 01:06:19', 11),
(21, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/almuerzo-hamburguesas-comida-los-tomates_370920.jpg.200x140_q85_crop.jpg', '2011-12-16 01:07:28', 12),
(22, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/almuerzo-hamburguesas-comida-los-tomates_370920.jpg.145x100_q85_crop.jpg', '2011-12-16 01:08:31', 12),
(23, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/default.png.200x140_q85_crop.png', '2011-12-16 01:09:20', 13),
(24, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/stock-photo-big-hamburger-isolated-on-white-65852539.jpg.145x145_q85_crop.jpg', '2011-12-16 01:10:16', 14),
(25, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/default.png.145x100_q85_crop.png', '2011-12-16 01:10:32', 13),
(26, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/jump-off-roof.jpg.200x140_q85_crop.jpg', '2011-12-16 01:12:07', 15),
(27, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/jump-off-roof.jpg.145x100_q85_crop.jpg', '2011-12-16 01:12:50', 15),
(28, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/70357_742139914_8383416_n.jpg.120x120_q85_crop.jpg', '2011-12-16 01:16:44', 16),
(29, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/70357_742139914_8383416_n.jpg.30x30_q85_crop.jpg', '2011-12-16 01:16:53', 16),
(30, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/coconut.jpg.145x145_q85_crop.jpg', '2011-12-16 01:17:00', 17),
(31, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/70357_742139914_8383416_n.jpg.145x145_q85_crop.jpg', '2011-12-16 01:18:29', 16),
(32, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/chine-gratte-ciel.jpg.145x145_q85_crop.jpg', '2011-12-16 01:18:37', 18),
(33, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/baby.jpg.200x140_q85_crop.jpg', '2011-12-16 01:22:02', 19),
(34, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/baby.jpg.145x100_q85_crop.jpg', '2011-12-16 01:22:19', 19),
(35, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/hai.jpg.200x140_q85_crop.jpg', '2011-12-16 01:27:03', 20),
(36, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/hai.jpg.145x100_q85_crop.jpg', '2011-12-16 01:27:09', 20),
(37, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/IMG_09152.jpg.145x145_q85_crop.jpg', '2011-12-16 01:28:24', 21),
(38, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/bike.jpg.200x140_q85_crop.jpg', '2011-12-16 01:30:58', 22),
(39, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/bike.jpg.145x100_q85_crop.jpg', '2011-12-16 01:31:02', 22),
(40, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/images.jpg.145x145_q85_crop.jpg', '2011-12-16 01:32:31', 23),
(41, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/salsa.jpg.200x140_q85_crop.jpg', '2011-12-16 01:34:02', 24),
(42, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/salsa.jpg.145x100_q85_crop.jpg', '2011-12-16 01:36:04', 24),
(43, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/sing.jpg.200x140_q85_crop.jpg', '2011-12-16 01:38:51', 25),
(44, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/sing.jpg.145x100_q85_crop.jpg', '2011-12-16 01:38:56', 25),
(45, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/kawaii-baby-dog-vol6-stickers-deco-blanc-grand-format_1.jpg.200x140_q85_crop.jpg', '2011-12-16 01:40:29', 26),
(46, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/kawaii-baby-dog-vol6-stickers-deco-blanc-grand-format_1.jpg.145x100_q85_crop.jpg', '2011-12-16 01:40:38', 26),
(47, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/choupette.jpg.120x120_q85_crop.jpg', '2011-12-16 01:42:37', 27),
(48, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/choupette.jpg.30x30_q85_crop.jpg', '2011-12-16 01:42:52', 27),
(49, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/choupette.jpg.145x145_q85_crop.jpg', '2011-12-16 01:43:14', 27),
(50, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/choupette.jpg.145x145_q85_crop.jpg', '2011-12-16 01:43:14', 28),
(51, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/concert-a-lyon.jpg.145x145_q85_crop.jpg', '2011-12-16 01:44:40', 29),
(52, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/salsa2.jpg.145x145_q85_crop.jpg', '2011-12-16 01:45:44', 30),
(53, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/man3.jpg.120x120_q85_crop.jpg', '2011-12-16 01:53:41', 31),
(54, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/man3.jpg.145x145_q85_crop.jpg', '2011-12-16 01:58:39', 31),
(55, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/man2.jpg.120x120_q85_crop.jpg', '2011-12-16 02:02:13', 32),
(56, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/man2.jpg.30x30_q85_crop.jpg', '2011-12-16 02:02:56', 32),
(57, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/jump3.jpg.200x140_q85_crop.jpg', '2011-12-16 02:04:04', 33),
(58, 'd26becbf46ac48eda79c7a39a13a02dd', 'challenge_pics/jump3.jpg.145x100_q85_crop.jpg', '2011-12-16 02:04:35', 33),
(59, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/jump2.jpg.145x145_q85_crop.jpg', '2011-12-16 02:04:50', 34),
(60, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/lunch.jpg.145x145_q85_crop.jpg', '2011-12-16 02:06:37', 35),
(61, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/crazy.jpg.145x145_q85_crop.jpg', '2011-12-16 02:07:31', 36),
(62, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/jump.jpg.145x145_q85_crop.jpg', '2011-12-16 02:07:55', 37),
(63, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/man3.jpg.30x30_q85_crop.jpg', '2011-12-16 02:08:48', 31),
(64, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/jump4.jpg.145x145_q85_crop.jpg', '2011-12-16 02:09:08', 38),
(65, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/man2.jpg.145x145_q85_crop.jpg', '2011-12-16 02:18:25', 32),
(66, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/default.png.120x120_q85_crop.png', '2011-12-16 02:27:59', 39),
(67, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/poney.jpg.120x120_q85_crop.jpg', '2011-12-16 02:29:58', 40),
(68, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/default.png.145x145_q85_crop.png', '2011-12-16 02:30:04', 39),
(69, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/poney.jpg.30x30_q85_crop.jpg', '2011-12-16 02:30:28', 40),
(70, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/default.png.30x30_q85_crop.png', '2011-12-16 02:30:38', 39),
(71, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/poney.jpg.145x145_q85_crop.jpg', '2011-12-16 02:30:41', 40),
(72, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/jeff.jpg.120x120_q85_crop.jpg', '2011-12-16 02:30:54', 41),
(73, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/jeff.jpg.145x145_q85_crop.jpg', '2011-12-16 02:31:40', 41),
(74, 'd26becbf46ac48eda79c7a39a13a02dd', 'profile_pics/jeff.jpg.30x30_q85_crop.jpg', '2011-12-16 02:33:49', 41),
(75, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/moutarde-me-monte-au-nez-01-g.jpg.145x145_q85_crop.jpg', '2011-12-16 02:37:48', 42),
(76, 'd26becbf46ac48eda79c7a39a13a02dd', 'reponse_pics/Capture_décran_2011-12-16_à_02.41.02.png.145x145_q85_crop.jpg', '2011-12-16 02:41:44', 43);

-- --------------------------------------------------------

--
-- Table structure for table `reponse_commentaire`
--

CREATE TABLE IF NOT EXISTS `reponse_commentaire` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `date_commentaire` date NOT NULL,
  `moderation` tinyint(1) NOT NULL,
  `notification` tinyint(1) NOT NULL,
  `reponse_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reponse_commentaire_36647aed` (`reponse_id`),
  KEY `reponse_commentaire_5f9483ee` (`utilisateur_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `reponse_commentaire`
--


-- --------------------------------------------------------

--
-- Table structure for table `reponse_noter`
--

CREATE TABLE IF NOT EXISTS `reponse_noter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `note` tinyint(1) NOT NULL,
  `reponse_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reponse_noter_36647aed` (`reponse_id`),
  KEY `reponse_noter_5f9483ee` (`utilisateur_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=18 ;

--
-- Dumping data for table `reponse_noter`
--

INSERT INTO `reponse_noter` (`id`, `note`, `reponse_id`, `utilisateur_id`) VALUES
(6, 1, 6, 3),
(7, 1, 7, 4),
(8, 1, 9, 5),
(9, 1, 10, 3),
(10, 1, 8, 3),
(11, 1, 6, 4),
(12, 1, 13, 7),
(13, 1, 15, 7),
(15, 1, 18, 3),
(16, 1, 11, 5),
(17, 1, 21, 12);

-- --------------------------------------------------------

--
-- Table structure for table `reponse_reponse`
--

CREATE TABLE IF NOT EXISTS `reponse_reponse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `slug` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `date_reponse` date NOT NULL,
  `photo` varchar(100) NOT NULL,
  `notification` tinyint(1) NOT NULL,
  `defi_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  `classement` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reponse_reponse_a951d5d6` (`slug`),
  KEY `reponse_reponse_23b2b636` (`defi_id`),
  KEY `reponse_reponse_5f9483ee` (`utilisateur_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `reponse_reponse`
--

INSERT INTO `reponse_reponse` (`id`, `slug`, `message`, `date_reponse`, `photo`, `notification`, `defi_id`, `utilisateur_id`, `classement`) VALUES
(6, '', 'I was hungry', '2011-12-16', 'reponse_pics/stock-photo-big-hamburger-isolated-on-white-65852539.jpg', 1, 3, 3, 4),
(7, '', 'Haha I succeed !', '2011-12-16', 'reponse_pics/coconut.jpg', 1, 2, 4, 4),
(8, '', 'Haha I succeeded !', '2011-12-16', 'reponse_pics/defaut.jpg', 1, 2, 4, 4),
(9, '', 'Ouais regarde j''ai pris cette photo en sautant', '2011-12-16', 'reponse_pics/chine-gratte-ciel.jpg', 1, 4, 6, 4),
(10, '', 'my usual is CRAZY !', '2011-12-16', 'reponse_pics/IMG_09152.jpg', 1, 6, 3, 4),
(11, '', 'oooops got a little too far away', '2011-12-16', 'reponse_pics/images.jpg', 1, 4, 3, 4),
(12, '', 'I was hungry', '2011-12-16', 'reponse_pics/defaut.jpg', 1, 3, 3, 4),
(13, '', 'Look mine is the best !', '2011-12-16', 'reponse_pics/choupette.jpg', 1, 6, 7, 4),
(14, '', 'I did it ! everyone loved it ! it was amazing !!', '2011-12-16', 'reponse_pics/concert-a-lyon.jpg', 1, 9, 3, 4),
(15, '', 'I love Salsa !', '2011-12-16', 'reponse_pics/salsa2.jpg', 1, 8, 7, 4),
(16, '', 'So high !', '2011-12-16', 'reponse_pics/jump2.jpg', 1, 11, 7, 4),
(17, '', 'Mine is bigger !', '2011-12-16', 'reponse_pics/lunch.jpg', 1, 3, 7, 4),
(18, '', 'CRAZY !!!!!!', '2011-12-16', 'reponse_pics/crazy.jpg', 1, 6, 3, 4),
(19, '', 'Who is the greatest ?', '2011-12-16', 'reponse_pics/jump.jpg', 1, 11, 4, 4),
(20, '', 'Jump', '2011-12-16', 'reponse_pics/jump4.jpg', 1, 11, 8, 4),
(21, '', 'j''espère que j''ai gagné.', '2011-12-16', 'reponse_pics/moutarde-me-monte-au-nez-01-g.jpg', 1, 4, 12, 4),
(22, '', 'nice shirt', '2011-12-16', 'reponse_pics/Capture_décran_2011-12-16_à_02.41.02.png', 1, 10, 12, 4);

-- --------------------------------------------------------

--
-- Table structure for table `utilisateur_badge`
--

CREATE TABLE IF NOT EXISTS `utilisateur_badge` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(45) NOT NULL,
  `description` longtext NOT NULL,
  `photo` varchar(200) NOT NULL,
  `dateBadge` date NOT NULL,
  `notification` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `utilisateur_badge`
--


-- --------------------------------------------------------

--
-- Table structure for table `utilisateur_gagner`
--

CREATE TABLE IF NOT EXISTS `utilisateur_gagner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `badge_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `utilisateur_gagner_80db5b24` (`badge_id`),
  KEY `utilisateur_gagner_5f9483ee` (`utilisateur_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `utilisateur_gagner`
--


-- --------------------------------------------------------

--
-- Table structure for table `utilisateur_messageprive`
--

CREATE TABLE IF NOT EXISTS `utilisateur_messageprive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dateMessage` datetime NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `emeteur_id` int(11) NOT NULL,
  `destinataire_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `utilisateur_messageprive_ffbe48e8` (`emeteur_id`),
  KEY `utilisateur_messageprive_d7c911b5` (`destinataire_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `utilisateur_messageprive`
--

INSERT INTO `utilisateur_messageprive` (`id`, `dateMessage`, `lu`, `emeteur_id`, `destinataire_id`, `message`) VALUES
(1, '2011-12-16 00:44:56', 1, 5, 6, 'Coquin !'),
(2, '2011-12-16 00:44:56', 1, 4, 6, 'Genre tu te jettes du toit quoi !!'),
(3, '2011-12-16 00:44:56', 1, 4, 5, 'Who are you ??'),
(4, '2011-12-16 00:44:49', 1, 6, 4, 'et oui je suis un ouf t''as vu'),
(5, '2011-12-16 00:44:49', 1, 6, 5, 'coquin toi même'),
(6, '2011-12-16 00:44:56', 1, 6, 4, 'ben jsuis moi'),
(7, '2011-12-16 00:44:49', 1, 4, 6, 'Baba c''est toi ?'),
(8, '2011-12-16 00:44:49', 0, 6, 4, 'non ça c''est pas moi'),
(9, '2011-12-16 00:44:49', 1, 5, 6, 'un nouveau message baby'),
(10, '2011-12-16 00:44:49', 0, 5, 4, 'I''m babar'),
(11, '2011-12-16 00:44:49', 1, 6, 5, 'ah ouais ben ça marche, tu vois bien cette réponse ?'),
(12, '2011-12-16 00:44:56', 1, 5, 6, 'oui je te vois');

-- --------------------------------------------------------

--
-- Table structure for table `utilisateur_utilisateur`
--

CREATE TABLE IF NOT EXISTS `utilisateur_utilisateur` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `points` int(11) DEFAULT NULL,
  `dateNaissance` date NOT NULL,
  `pays` varchar(45) NOT NULL,
  `sexeM` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `utilisateur_utilisateur`
--

INSERT INTO `utilisateur_utilisateur` (`id`, `user_id`, `avatar`, `points`, `dateNaissance`, `pays`, `sexeM`) VALUES
(3, 3, 'profile_pics/IMG_09152.jpg', 0, '1989-05-22', 'France', 1),
(4, 4, 'profile_pics/photo.png', 0, '1989-06-10', 'France', 1),
(5, 5, 'profile_pics/babar.jpg', 0, '1995-01-01', 'suisse', 1),
(6, 6, 'profile_pics/70357_742139914_8383416_n.jpg', 0, '1989-04-17', 'France', 1),
(7, 7, 'profile_pics/choupette.jpg', 0, '1986-04-04', 'U.K.', 1),
(8, 8, 'profile_pics/man3.jpg', 0, '1983-09-05', 'Italy', 1),
(9, 9, 'profile_pics/man2.jpg', 0, '1986-12-01', 'France', 1),
(11, 11, 'profile_pics/poney.jpg', 0, '1988-12-17', 'FRANCE', 1),
(12, 12, 'profile_pics/jeff.jpg', 0, '1989-07-15', 'france', 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_message`
--
ALTER TABLE `auth_message`
  ADD CONSTRAINT `user_id_refs_id_9af0b65a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `defi_defi`
--
ALTER TABLE `defi_defi`
  ADD CONSTRAINT `categorie_id_refs_id_99b3e9e3` FOREIGN KEY (`categorie_id`) REFERENCES `defi_categorie` (`id`),
  ADD CONSTRAINT `createur_id_refs_id_e5defdda` FOREIGN KEY (`createur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `defi_relever`
--
ALTER TABLE `defi_relever`
  ADD CONSTRAINT `defi_id_refs_id_168ded77` FOREIGN KEY (`defi_id`) REFERENCES `defi_defi` (`id`),
  ADD CONSTRAINT `utilisateur_id_refs_id_772d0d9a` FOREIGN KEY (`utilisateur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_comments`
--
ALTER TABLE `django_comments`
  ADD CONSTRAINT `user_id_refs_id_81622011` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_f2a7975b` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `site_id_refs_id_8db720f8` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`);

--
-- Constraints for table `django_comment_flags`
--
ALTER TABLE `django_comment_flags`
  ADD CONSTRAINT `comment_id_refs_id_373a05f7` FOREIGN KEY (`comment_id`) REFERENCES `django_comments` (`id`),
  ADD CONSTRAINT `user_id_refs_id_603c4dcb` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `easy_thumbnails_thumbnail`
--
ALTER TABLE `easy_thumbnails_thumbnail`
  ADD CONSTRAINT `source_id_refs_id_5bffe8f5` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`);

--
-- Constraints for table `reponse_commentaire`
--
ALTER TABLE `reponse_commentaire`
  ADD CONSTRAINT `reponse_id_refs_id_f7c4711f` FOREIGN KEY (`reponse_id`) REFERENCES `reponse_reponse` (`id`),
  ADD CONSTRAINT `utilisateur_id_refs_id_da7ecda2` FOREIGN KEY (`utilisateur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `reponse_noter`
--
ALTER TABLE `reponse_noter`
  ADD CONSTRAINT `reponse_id_refs_id_7c071b9b` FOREIGN KEY (`reponse_id`) REFERENCES `reponse_reponse` (`id`),
  ADD CONSTRAINT `utilisateur_id_refs_id_97a76b5c` FOREIGN KEY (`utilisateur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `reponse_reponse`
--
ALTER TABLE `reponse_reponse`
  ADD CONSTRAINT `defi_id_refs_id_69ee0657` FOREIGN KEY (`defi_id`) REFERENCES `defi_defi` (`id`),
  ADD CONSTRAINT `utilisateur_id_refs_id_2e7d137a` FOREIGN KEY (`utilisateur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `utilisateur_gagner`
--
ALTER TABLE `utilisateur_gagner`
  ADD CONSTRAINT `badge_id_refs_id_4467917b` FOREIGN KEY (`badge_id`) REFERENCES `utilisateur_badge` (`id`),
  ADD CONSTRAINT `utilisateur_id_refs_id_d291644` FOREIGN KEY (`utilisateur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `utilisateur_messageprive`
--
ALTER TABLE `utilisateur_messageprive`
  ADD CONSTRAINT `destinataire_id_refs_id_eac1ec97` FOREIGN KEY (`destinataire_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `emeteur_id_refs_id_eac1ec97` FOREIGN KEY (`emeteur_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `utilisateur_utilisateur`
--
ALTER TABLE `utilisateur_utilisateur`
  ADD CONSTRAINT `user_id_refs_id_3734d86a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
