
DROP TABLE IF EXISTS `Currencies`;
CREATE TABLE IF NOT EXISTS `Currencies` (
  `CurrencyId` int(11) NOT NULL AUTO_INCREMENT,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `Code` varchar(100) CHARACTER SET utf8 NOT NULL,
  `Symbol` varchar(100) CHARACTER SET utf8 NOT NULL,
  `CurrenciesImage` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`CurrencyId`),
  UNIQUE KEY `IX_Currencies_Code` (`Code`),
  UNIQUE KEY `IX_Currencies_Symbol` (`Symbol`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
