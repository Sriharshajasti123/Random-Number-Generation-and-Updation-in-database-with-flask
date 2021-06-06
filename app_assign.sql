-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 06, 2021 at 08:32 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `app_assign`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Sno` int(22) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `student_id` int(255) NOT NULL,
  `id_tag` int(255) NOT NULL,
  `Dob` varchar(25) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Username` varchar(24) NOT NULL,
  `Password` varchar(33) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Sno`, `Name`, `student_id`, `id_tag`, `Dob`, `Email`, `Username`, `Password`) VALUES
(1, 'Ram', 10, 838, '1999/02/03', 'Ram@gmail.com', 'Ram12', '1111'),
(14, 'sri', 1000, 627, '2021-06-05', 'sri814823@gmail.com', 'sri111', 'sri111'),
(15, 'rishi', 100, 742, '2021-06-01', 'rishi@gmail.com', 'rishi47', 'rishi47'),
(18, 'chandu', 234, 292, '2021-06-02', 'chandu@gmail.com', 'chandu123', 'chandu123'),
(19, 'sunny', 600, 582, '2021-06-03', 'sunny@gmail.com', 'sunny456', 'sunny456');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`Sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `Sno` int(22) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
