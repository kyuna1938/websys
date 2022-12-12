-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- ホスト: db
-- 生成日時: 2022 年 12 月 12 日 14:43
-- サーバのバージョン： 8.0.29
-- PHP のバージョン: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `a3_db`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- テーブルのデータのダンプ `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('03af7f9b67b2');

-- --------------------------------------------------------

--
-- テーブルの構造 `books`
--

CREATE TABLE `books` (
  `id` int NOT NULL,
  `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
  `price` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- テーブルのデータのダンプ `books`
--

INSERT INTO `books` (`id`, `name`, `price`) VALUES
(1, '本1', 1000),
(2, '本2', 1200),
(3, '本3', 100),
(4, '本4', 10000),
(5, '本5', 10000),
(6, '本6', 10000),
(7, '本7', 10000),
(8, '本8', 10000);

-- --------------------------------------------------------

--
-- テーブルの構造 `sales`
--

CREATE TABLE `sales` (
  `id` int NOT NULL,
  `book_id` int DEFAULT NULL,
  `quantity` int NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sex` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- テーブルのデータのダンプ `sales`
--

INSERT INTO `sales` (`id`, `book_id`, `quantity`, `date`, `sex`) VALUES
(1, 1, 1, '2022-12-06 09:22:29', 0),
(2, 1, 3, '2022-12-06 09:22:29', 0),
(3, 2, 5, '2022-12-06 09:22:29', 0),
(4, 1, 1, '2022-12-13 14:22:20', 0),
(5, 1, 2, '2022-12-13 14:22:20', 1),
(6, 1, 2, '2022-12-13 14:22:20', 2),
(7, 1, 1, '2022-12-13 14:22:20', 0),
(8, 1, 1, '2022-12-12 14:22:20', 0),
(9, 1, 5, '2022-12-10 14:22:20', 1),
(10, 1, 3, '2022-12-09 14:22:20', 2),
(11, 1, 2, '2022-12-09 14:22:20', 0),
(12, 2, 2, '2022-12-13 14:22:20', 0),
(13, 2, 1, '2022-12-13 14:22:20', 1),
(14, 3, 1, '2022-12-13 14:22:20', 1),
(15, 4, 1, '2022-12-13 14:22:20', 1),
(16, 5, 1, '2022-12-13 14:22:20', 1),
(17, 6, 1, '2022-12-13 14:22:20', 1),
(18, 7, 3, '2022-12-13 14:22:20', 1),
(19, 7, 4, '2022-12-13 14:22:20', 0),
(20, 8, 2, '2022-12-13 14:22:20', 2),
(21, 2, 5, '2022-12-12 14:22:20', 0),
(22, 4, 2, '2022-12-11 14:22:20', 1),
(23, 4, 1, '2022-12-11 14:22:20', 0),
(24, 4, 2, '2022-12-09 14:22:20', 2),
(25, 5, 1, '2022-12-11 14:22:20', 2),
(26, 5, 1, '2022-12-11 14:22:20', 0),
(27, 6, 2, '2022-12-12 14:22:20', 0),
(28, 7, 1, '2022-12-08 14:22:20', 1),
(29, 8, 2, '2022-12-13 14:22:20', 0),
(30, 8, 1, '2022-12-11 14:22:20', 1);

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- テーブルのインデックス `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_books_id` (`id`),
  ADD KEY `ix_books_name` (`name`);

--
-- テーブルのインデックス `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `book_id` (`book_id`),
  ADD KEY `ix_sales_id` (`id`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `books`
--
ALTER TABLE `books`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- テーブルの AUTO_INCREMENT `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
