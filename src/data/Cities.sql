DROP TABLE IF EXISTS `Cities`;
CREATE TABLE IF NOT EXISTS `Cities` (
  `CityId` int(11) NOT NULL,
  `StateId` int(11) NOT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`CityId`),
  KEY `FK_Cities_StateId` (`StateId`),
  CONSTRAINT `FK_Cities_StateId` FOREIGN KEY (`StateId`) REFERENCES `States` (`StateId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
