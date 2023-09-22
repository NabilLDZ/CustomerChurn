-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 01 Des 2022 pada 13.40
-- Versi server: 10.4.20-MariaDB
-- Versi PHP: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `telekom`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelanggan`
--

CREATE TABLE `pelanggan` (
  `UpdatedAt` date NOT NULL DEFAULT current_timestamp(),
  `CustomerID` bigint(11) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Gender` varchar(6) NOT NULL,
  `SeniorCitizen` varchar(3) NOT NULL,
  `Partner` varchar(3) NOT NULL,
  `Tenure` int(11) NOT NULL,
  `PhoneService` varchar(3) NOT NULL,
  `StreamingTV` varchar(3) NOT NULL,
  `InternetService` varchar(3) NOT NULL,
  `PaperlessBilling` varchar(3) NOT NULL,
  `MonthlyCharges` float NOT NULL,
  `TotalCharges` float NOT NULL,
  `Churn` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `pelanggan`
--

INSERT INTO `pelanggan` (`UpdatedAt`, `CustomerID`, `Name`, `Gender`, `SeniorCitizen`, `Partner`, `Tenure`, `PhoneService`, `StreamingTV`, `InternetService`, `PaperlessBilling`, `MonthlyCharges`, `TotalCharges`, `Churn`) VALUES
('2022-11-28', 54419550, 'Santoso', 'Female', 'Yes', 'Yes', 3, 'No', 'No', 'Yes', 'No', 23, 69, 'Yes'),
('2022-11-28', 54419551, 'Nabil', 'Female', 'Yes', 'Yes', 1, 'No', 'Yes', 'No', 'No', 33.41, 33.41, 'No'),
('2022-11-29', 54419552, 'Ucup', 'Male', 'Yes', 'Yes', 1, 'Yes', 'Yes', 'Yes', 'Yes', 33.1, 33.1, 'No'),
('2022-11-29', 54419553, 'Danantya', 'Male', 'No', 'Yes', 45, 'Yes', 'Yes', 'Yes', 'Yes', 34.9, 1570.5, 'No'),
('2022-11-29', 54419554, 'Messi', 'Male', 'Yes', 'Yes', 2, 'No', 'No', 'Yes', 'No', 94, 188, 'Yes'),
('2022-11-29', 54419557, 'Patrick', 'Male', 'Yes', 'Yes', 2, 'Yes', 'Yes', 'Yes', 'Yes', 32.34, 64.68, 'No'),
('2022-11-29', 54419559, 'Udin', 'Male', 'No', 'Yes', 2, 'Yes', 'No', 'Yes', 'Yes', 32.34, 64.68, 'Yes'),
('2022-12-01', 54419561, 'Budi', 'Female', 'Yes', 'Yes', 6, 'Yes', 'Yes', 'Yes', 'Yes', 34, 204, 'Yes'),
('2022-12-01', 54419562, 'Handi', 'Male', 'Yes', 'Yes', 1, 'No', 'No', 'No', 'No', 32, 32, 'No');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  ADD PRIMARY KEY (`CustomerID`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `pelanggan`
--
ALTER TABLE `pelanggan`
  MODIFY `CustomerID` bigint(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54419563;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
