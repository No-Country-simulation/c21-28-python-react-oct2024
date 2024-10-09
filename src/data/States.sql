DROP TABLE IF EXISTS `States`;
CREATE TABLE IF NOT EXISTS `States` (
  `StateId` int(11) NOT NULL,
  `CountryId` int(11) NOT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `Iso_3166_numeric_1` varchar(3) CHARACTER SET utf8 NOT NULL,
  `Iso_3166_alpha_2` varchar(3) CHARACTER SET utf8 NOT NULL,
  `Iso_3166_alpha_3` varchar(5) CHARACTER SET utf8 NOT NULL,
  `StatesImage` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`StateId`),
  UNIQUE KEY `IX_States_Iso_1` (`Iso_3166_numeric_1`),
  UNIQUE KEY `IX_States_Iso_2` (`Iso_3166_alpha_2`),
  UNIQUE KEY `IX_States_Iso_3` (`Iso_3166_alpha_3`),
  KEY `FK_States_CountryId` (`CountryId`),
  CONSTRAINT `FK_States_CountryId` FOREIGN KEY (`CountryId`) REFERENCES `Countries` (`CountryId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
